import os
import requests
import random
import json
import math
from datetime import datetime, date, timedelta
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("GITHUB_TOKEN")
USERNAME = os.getenv("GITHUB_USERNAME", os.getenv("GITHUB_REPOSITORY_OWNER", "achexus"))
STATE_FILE = "zombie-state.json"

MSG_OVERKILL = ["TARGET PRACTICE AT SECTOR {date}. OVERWHELMING FIREPOWER USED.", "THREAT NEUTRALIZED ON {date}. NO CASUALTIES REPORTED."]
MSG_CLEARED = ["CLOSE CALL ON {date}. PERIMETER BARELY SECURED.", "HAND-TO-HAND COMBAT ON {date}. WE HOLD THE LINE."]
MSG_FAILED = ["MAYDAY! BARRICADES BREACHED ON {date}!", "SECTOR {date} OVERRUN. WE TOOK DOWN {commits} BUT IT WAS NOT ENOUGH."]
MSG_ZERO = ["RADIO SILENCE ON {date}. SECTOR ASSUMED LOST.", "NO DEFENSIVE ACTION TAKEN ON {date}. WALKERS ROAM FREE."]
MSG_GENERIC = ["STATIC... ADJUSTING FREQUENCY...", "OUTPOST ALPHA REPORTING ALL CLEAR...", "HEARING MOANS FROM THE EASTERN WOODS..."]

MSG_EN_ROUTE = [
    "RADAR CONTACT ON THE MOVE. WE NEED BACKUP AT THE NEXT CROSSROAD.",
    "SQUAD EN ROUTE. MULTIPLE BOGEYS DETECTED ON SCANNERS.",
    "ETA 5 MINUTES. KEEP WEAPONS HOT AND EYES PEELED.",
    "MOVEMENT IN THE SHADOWS AHEAD. PROCEED WITH CAUTION.",
    "VEHICLE SYSTEMS NOMINAL. CLOSING IN ON THE TARGET ZONE."
]

MSG_COMBAT = [
    "HOT DROP! WE HAVE ENGAGED THE ENEMY! FIRE AT WILL!",
    "DO NOT LET THEM CROSS THE PERIMETER! HOLD THE LINE!",
    "RELOADING! COVERING FIRE NEEDED AT THE FLANK!",
    "THEY ARE BREAKING THROUGH THE WIRE! FALL BACK TO SECONDARY POSITIONS!",
    "MULTIPLE HOSTILES DOWN, BUT MORE ARE COMING FROM THE WOODS!"
]

MSG_SECURE = [
    "SECTOR CLEAR. REBUILDING BARRICADES AND RESTOCKING SUPPLIES.",
    "HQ, BE ADVISED: WE HEAR SCREAMS FROM GRID C-7. BE CAREFUL OUT THERE.",
    "ALL HOSTILES NEUTRALIZED. PATROLLING THE BORDERS FOR STRAGGLERS.",
    "WARNING: OUTPOST DELTA WENT SILENT. STAY ALERT IN SECURE ZONES.",
    "GATHERING SUPPLIES. NO SIGN OF THE UNDEAD IN THIS SECTOR TODAY."
]

DEFENSE_BADGES = [
    {"name": "IRON SENTRY", "req": 50, "icon": "[D]", "desc": "Demir Muhafız"},
    {"name": "IMPENETRABLE", "req": 100, "icon": "[D]", "desc": "Aşılmaz Surlar"},
    {"name": "SIEGE BREAKER", "req": 500, "icon": "[D]", "desc": "Kuşatma Kıran"},
    {"name": "TITAN BULWARK", "req": 1500, "icon": "[D]", "desc": "Titan Kalkanı"},
    {"name": "ETERNAL HAVEN", "req": 3000, "icon": "[D]", "desc": "Ebedi Sığınak"},
    {"name": "WORLD CITADEL", "req": 5000, "icon": "[D]", "desc": "Dünyanın Sonu Kalesi"}
]

COMMIT_BADGES = [
    {"name": "FLESH RIPPER", "req": 100, "icon": "[C]", "desc": "Et Parçalayan"},
    {"name": "APEX PREDATOR", "req": 500, "icon": "[C]", "desc": "Zirve Avcısı"},
    {"name": "SOUL HARVESTER", "req": 1000, "icon": "[C]", "desc": "Can Söken"},
    {"name": "PURE CARNAGE", "req": 2500, "icon": "[C]", "desc": "Saf Kıyım"},
    {"name": "APOCALYPSE ENG", "req": 5000, "icon": "[C]", "desc": "Kıyamet Çarkı"},
    {"name": "WALKING CALAMITY", "req": 10000, "icon": "[C]", "desc": "Yürüyen Felaket"},
    {"name": "ABS EXTINCTION", "req": 50000, "icon": "[C]", "desc": "Mutlak Yok Oluş"}
]

def calculate_level_info(total_commits):
    if total_commits == 0:
        return 0, 0, 1
    # 1+2+3+... = n(n+1)/2 matematik formülünden seviye bulma
    level = int((math.sqrt(8 * total_commits + 1) - 1) / 2)
    current_level_base_xp = (level * (level + 1)) // 2
    next_level_base_xp = ((level + 1) * (level + 2)) // 2
    
    current_xp_in_level = total_commits - current_level_base_xp
    xp_needed_for_next = next_level_base_xp - current_level_base_xp
    
    return level, current_xp_in_level, xp_needed_for_next

def get_rank(level):
    # Yeni yapı: Max 300 seviye, her 25 seviyede bir atlayan rütbeler
    RANKS = [
        (300, "LIVING LEGEND"), (275, "ZOMBIE HUNTER"), (250, "COMMANDER"),
        (225, "TACTICIAN"), (200, "SHARPSHOOTER"), (175, "VETERAN"),
        (150, "GUARDIAN"), (125, "DEFENDER"), (100, "VANGUARD"),
        (75, "SCOUT"), (50, "SURVIVOR"), (25, "SCAVENGER")
    ]
    for req_level, name in RANKS:
        if level >= req_level:
            return name, req_level
            
    return "LONE WANDERER", 25

def get_current_epic_badge(value, badges_list):
    earned = [b for b in badges_list if value >= b['req']]
    unearned = [b for b in badges_list if value < b['req']]
    if not earned: return badges_list[0], False
    elif unearned: return unearned[0], False
    else: return earned[-1], True

query = f"""
query {{ user(login: "{USERNAME}") {{ contributionsCollection {{ contributionCalendar {{
        totalContributions weeks {{ contributionDays {{ contributionCount date }} }}
}} }} }} }}
"""

def get_contribution_data():
    print(f"[INTEL] {USERNAME} için GitHub'dan canlı veriler çekiliyor...")
    url = 'https://api.github.com/graphql'
    headers = {'Authorization': f'Bearer {TOKEN}', 'Content-Type': 'application/json'}
    response = requests.post(url, json={'query': query}, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if 'errors' in data: return None
        weeks = data['data']['user']['contributionsCollection']['contributionCalendar']['weeks']
        days = []
        for week in weeks:
            for day in week['contributionDays']: days.append(day)
        return days
    return None

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    return {"start_date": "", "history": {}}

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=4)

def get_radar_svg(remaining_zombies, x, y, width, height):
    cx = x + (width / 2)
    cy = y + 95
    dots = ""
    coords = [(-40, -35), (35, 20), (-15, 45), (45, -25)]
    for idx in range(min(remaining_zombies, 4)):
        dx, dy = coords[idx]
        dots += f"""
        <circle cx="{cx+dx}" cy="{cy+dy}" r="4" fill="#ff003c">
            <animate attributeName="opacity" values="0;1;0" dur="3s" begin="{idx * 0.7}s" repeatCount="indefinite" />
        </circle>
        """
    return f"""
    <rect x="{x}" y="{y}" width="{width}" height="{height}" class="intel-panel" />
    <text x="{x+15}" y="{y+25}" class="text-neon text-medal">LOCAL RADAR [50M RADIUS]</text>
    <circle cx="{cx}" cy="{cy}" r="55" stroke="#1a4d1a" stroke-width="1" fill="none" />
    <circle cx="{cx}" cy="{cy}" r="35" stroke="#1a4d1a" stroke-width="1" fill="none" />
    <circle cx="{cx}" cy="{cy}" r="15" stroke="#1a4d1a" stroke-width="1" fill="none" />
    <line x1="{cx}" y1="{cy-55}" x2="{cx}" y2="{cy+55}" stroke="#1a4d1a" stroke-width="1" />
    <line x1="{cx-55}" y1="{cy}" x2="{cx+55}" y2="{cy}" stroke="#1a4d1a" stroke-width="1" />
    <g>
        <path d="M {cx} {cy} L {cx} {cy-55} A 55 55 0 0 1 {cx+55} {cy} Z" fill="rgba(57, 255, 20, 0.15)" />
        <animateTransform attributeName="transform" type="rotate" from="0 {cx} {cy}" to="360 {cx} {cy}" dur="3.5s" repeatCount="indefinite" />
    </g>
    {dots}
    """

def get_live_cam_svg(state, x, y, width, height):
    bg = f'<rect x="{x}" y="{y}" width="{width}" height="{height}" class="intel-panel" />'
    
    live_header = f"""
    <circle cx="{x+18}" cy="{y+20}" r="4" fill="#ff003c">
        <animate attributeName="opacity" values="1;0;1" dur="1.5s" repeatCount="indefinite" />
    </circle>
    <text x="{x+28}" y="{y+24}" class="text-neon text-medal">LIVE</text>
    """
    
    if state == "en_route":
        content = live_header + f"""
        <clipPath id="tire_clip_cam">
            <rect x="{x+10}" y="{y+40}" width="{width-20}" height="{height-50}" rx="4" />
        </clipPath>
        
        <g clip-path="url(#tire_clip_cam)">
            <rect x="{x+10}" y="{y+40}" width="{width-20}" height="{height-50}" fill="#0a0a0f" />
            <line x1="{x+10}" y1="{y+145}" x2="{x+width-10}" y2="{y+145}" stroke="#1a4d1a" stroke-dasharray="35, 25" stroke-width="4">
                <animate attributeName="stroke-dashoffset" from="60" to="0" dur="0.15s" repeatCount="indefinite" />
            </line>
            <g>
                <animateTransform attributeName="transform" type="translate" values="0,0; 0,4; 0,0" dur="0.25s" repeatCount="indefinite" />
                <g>
                    <animateTransform attributeName="transform" type="rotate" from="0 {x+(width/2)} {y+40}" to="360 {x+(width/2)} {y+40}" dur="0.8s" repeatCount="indefinite" />
                    <circle cx="{x+(width/2)}" cy="{y+40}" r="105" fill="#050a05" stroke="#1a2332" stroke-width="8" />
                    <circle cx="{x+(width/2)}" cy="{y+40}" r="100" fill="none" stroke="#000000" stroke-width="10" stroke-dasharray="18, 15" />
                    <circle cx="{x+(width/2)}" cy="{y+40}" r="65" fill="#1c3242" stroke="#0d1117" stroke-width="4" />
                    <line x1="{x+(width/2)}" y1="{y+40-65}" x2="{x+(width/2)}" y2="{y+40+65}" stroke="#0d1117" stroke-width="8" />
                    <line x1="{x+(width/2)-65}" y1="{y+40}" x2="{x+(width/2)+65}" y2="{y+40}" stroke="#0d1117" stroke-width="8" />
                    <line x1="{x+(width/2)-45}" y1="{y+40-45}" x2="{x+(width/2)+45}" y2="{y+40+45}" stroke="#0d1117" stroke-width="8" />
                    <line x1="{x+(width/2)-45}" y1="{y+40+45}" x2="{x+(width/2)+45}" y2="{y+40-45}" stroke="#0d1117" stroke-width="8" />
                    <circle cx="{x+(width/2)}" cy="{y+40}" r="18" fill="#0d1117" />
                </g>
            </g>
        </g>
        <rect x="{x+10}" y="{y+40}" width="{width-20}" height="{height-50}" fill="none" stroke="#1a4d1a" stroke-width="1" rx="4" />
        """
    elif state == "combat":
        content = live_header + f"""
        <rect x="{x+10}" y="{y+40}" width="{width-20}" height="{height-50}" fill="#050510" rx="4" ry="4" />
        <g>
            <animateTransform attributeName="transform" type="translate" values="0,0; 0,-12; 0,0" dur="1.5s" repeatCount="indefinite" />
            <animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.7;0.8;1" dur="4s" repeatCount="indefinite" />
            <circle cx="{x+240}" cy="{y+100}" r="15" fill="#FF0000" opacity="0.6">
                 <animate attributeName="cx" values="{x+240};{x+40}" dur="4s" repeatCount="indefinite" />
            </circle>
            <circle cx="{x+240}" cy="{y+100}" r="9" fill="#FF8C00" opacity="0.9">
                 <animate attributeName="cx" values="{x+240};{x+40}" dur="4s" repeatCount="indefinite" />
            </circle>
            <circle cx="{x+240}" cy="{y+100}" r="4" fill="#FFFFFF" opacity="1">
                 <animate attributeName="cx" values="{x+240};{x+40}" dur="4s" repeatCount="indefinite" />
            </circle>
        </g>
        <g>
            <animateTransform attributeName="transform" type="translate" values="0,0; 0,-8; 0,0" dur="1.2s" repeatCount="indefinite" />
            <animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.8;0.9;1" dur="5s" repeatCount="indefinite" />
            <circle cx="{x+220}" cy="{y+130}" r="18" fill="#FF0000" opacity="0.5">
                 <animate attributeName="cx" values="{x+220};{x+40}" dur="5s" repeatCount="indefinite" />
            </circle>
            <circle cx="{x+220}" cy="{y+130}" r="11" fill="#FFD700" opacity="0.8">
                 <animate attributeName="cx" values="{x+220};{x+40}" dur="5s" repeatCount="indefinite" />
            </circle>
            <circle cx="{x+220}" cy="{y+130}" r="5" fill="#FFFFFF" opacity="1">
                 <animate attributeName="cx" values="{x+220};{x+40}" dur="5s" repeatCount="indefinite" />
            </circle>
        </g>
        <g stroke="#39ff14" stroke-width="1.5">
            <animateTransform attributeName="transform" type="translate" values="0,0; 30,8; -20,-10; 0,0" dur="4s" repeatCount="indefinite" />
            <circle cx="{x+(width/2)}" cy="{y+95}" r="45" fill="rgba(57,255,20,0.05)" />
            <line x1="{x+(width/2)-60}" y1="{y+95}" x2="{x+(width/2)+60}" y2="{y+95}" />
            <line x1="{x+(width/2)}" y1="{y+35}" x2="{x+(width/2)}" y2="{y+155}" />
            <circle cx="{x+(width/2)}" cy="{y+95}" r="2" fill="#39ff14" stroke="none">
                <animate attributeName="opacity" values="1;0;1" dur="0.8s" repeatCount="indefinite" />
            </circle>
        </g>
        """
    elif state == "secure":
        content = live_header + f"""
        <rect x="{x+10}" y="{y+40}" width="{width-20}" height="{height-50}" fill="#0d1117" rx="4" ry="4" />
        <path d="M {x+10} {y+70} L {x+width-10} {y+70} M {x+10} {y+105} L {x+width-10} {y+105} M {x+10} {y+140} L {x+width-10} {y+140}" stroke="#1a2332" stroke-width="4" />
        <path d="M {x+60} {y+40} L {x+60} {y+height-10} M {x+130} {y+40} L {x+130} {y+height-10} M {x+200} {y+40} L {x+200} {y+height-10}" stroke="#1a2332" stroke-width="4" />
        
        <rect x="{x+20}" y="{y+45}" width="30" height="20" fill="#1c3242" />
        <rect x="{x+70}" y="{y+45}" width="50" height="20" fill="#285473" />
        <rect x="{x+140}" y="{y+45}" width="50" height="20" fill="#1c3242" />
        <rect x="{x+210}" y="{y+45}" width="40" height="20" fill="#285473" />
        
        <rect x="{x+20}" y="{y+75}" width="30" height="25" fill="#285473" />
        <rect x="{x+70}" y="{y+75}" width="50" height="25" fill="#1c3242" />
        <rect x="{x+140}" y="{y+75}" width="50" height="25" fill="#1c3242" />
        <rect x="{x+210}" y="{y+75}" width="40" height="25" fill="#285473" />
        
        <rect x="{x+20}" y="{y+110}" width="30" height="25" fill="#1c3242" />
        <rect x="{x+70}" y="{y+110}" width="50" height="25" fill="#285473" />
        
        <rect x="{x+135}" y="{y+110}" width="115" height="25" fill="rgba(57, 255, 20, 0.15)" stroke="#39ff14" stroke-width="1" />
        <circle cx="{x+150}" cy="{y+122}" r="3" fill="#39ff14">
            <animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite" />
        </circle>
        <text x="{x+195}" y="{y+126}" class="text-neon" font-size="11" text-anchor="middle">SAFE ZONE</text>
        
        <line x1="{x+10}" y1="{y+40}" x2="{x+10}" y2="{y+height-10}" stroke="rgba(57, 255, 20, 0.5)" stroke-width="2">
            <animate attributeName="x1" values="{x+10};{x+width-10};{x+10}" dur="5s" repeatCount="indefinite" />
            <animate attributeName="x2" values="{x+10};{x+width-10};{x+10}" dur="5s" repeatCount="indefinite" />
        </line>
        """
    return bg + content

def generate_pipboy_svg(days, level, xp_current, xp_needed, rank_name, next_rank_req, survived, invaded, survival_day_count, total_commits, game_start_date, history):
    svg_width = 980
    svg_height = 740
    
    day_map = {d['date']: d['contributionCount'] for d in days}
    today_date_obj = date.today()
    today_str = today_date_obj.strftime("%Y-%m-%d")
    
    gh_weekday = (today_date_obj.weekday() + 1) % 7 
    grid_end_date = today_date_obj + timedelta(days=(6 - gh_weekday))
    grid_start_date = grid_end_date - timedelta(days=377)
    
    today_commits = day_map.get(today_str, 0)
    today_zombies = history.get(today_str, 0)
    remaining_zombies = max(0, today_zombies - today_commits)
    
    if today_str < game_start_date:
        cam_state = "secure"
        today_status = "SYSTEM STANDBY (PRE-INVASION)"
        status_color = "#39ff14"
        remaining_zombies = 0
    else:
        if today_commits == 0:
            cam_state = "en_route"
            today_status = "CRITICAL (EN ROUTE)"
            status_color = "#ff003c"
        elif today_commits < today_zombies:
            cam_state = "combat"
            today_status = "BREACHED (ENGAGING)"
            status_color = "#ff8c00"
        else:
            cam_state = "secure"
            today_status = "SECURE (CLEARED)"
            status_color = "#39ff14"

    if cam_state == "en_route": current_msgs = MSG_EN_ROUTE
    elif cam_state == "combat": current_msgs = MSG_COMBAT
    else: current_msgs = MSG_SECURE

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{svg_width}" height="{svg_height}">
    <style>
        .bg {{ fill: transparent; }}
        .scanline {{ stroke: rgba(57, 255, 20, 0.10); stroke-width: 1; }}
        .text-neon {{ fill: #39ff14; font-family: 'Courier New', Courier, monospace; font-weight: bold; }}
        .text-dim {{ fill: #1a4d1a; font-family: 'Courier New', Courier, monospace; font-weight: bold; }}
        .text-title {{ font-size: 22px; }}
        .text-info {{ font-size: 14px; }}
        .text-medal {{ font-size: 12px; }}
        .text-status {{ fill: {status_color}; font-family: 'Courier New', Courier, monospace; font-weight: bold; font-size: 14px; }}
        .box-medal-earned {{ fill: rgba(57, 255, 20, 0.05); stroke: #39ff14; stroke-width: 1; }}
        .box-medal-locked {{ fill: transparent; stroke: #1a4d1a; stroke-width: 1; stroke-dasharray: 4; }}
        .intel-panel {{ fill: rgba(13, 17, 23, 0.8); stroke: #1a4d1a; stroke-width: 1; rx: 4; ry: 4; }}
        .fog-of-war {{ fill: rgba(13, 17, 23, 0.3); stroke: #1a4d1a; stroke-width: 1; stroke-dasharray: 2; opacity: 0.8; }}
        .past-0 {{ fill: #0d1117; stroke: #1a2332; stroke-width: 1; rx: 2; ry: 2; }}
        .past-1 {{ fill: #1c3242; rx: 2; ry: 2; }}
        .past-2 {{ fill: #285473; rx: 2; ry: 2; }}
        .past-3 {{ fill: #3679a6; rx: 2; ry: 2; }}
        .past-4 {{ fill: #459fdb; rx: 2; ry: 2; }}
        .game-survived-1 {{ fill: #1f6b11; rx: 2; ry: 2; }} 
        .game-survived-2 {{ fill: #2c9e17; rx: 2; ry: 2; }} 
        .game-survived-3 {{ fill: #39ff14; rx: 2; ry: 2; }} 
        .game-survived-4 {{ fill: #a3ff00; rx: 2; ry: 2; }} 
        .game-invaded-1 {{ fill: #8a0020; stroke: #ff003c; stroke-width: 1; rx: 2; ry: 2; }}  
        .game-invaded-2 {{ fill: #ff003c; rx: 2; ry: 2; }}  
        @keyframes pulse-beacon {{ 0% {{ fill-opacity: 1; stroke: #ffffff; stroke-width: 1px; }} 50% {{ fill-opacity: 0.4; stroke: #39ff14; stroke-width: 3px; }} 100% {{ fill-opacity: 1; stroke: #ffffff; stroke-width: 1px; }} }}
        .current-day {{ animation: pulse-beacon 1.5s infinite; rx: 3; ry: 3; }}
        @keyframes crt-flicker {{ 0% {{ opacity: 0.95; }} 5% {{ opacity: 0.85; }} 10% {{ opacity: 0.95; }} 15% {{ opacity: 1.0; }} 50% {{ opacity: 0.98; }} 100% {{ opacity: 0.95; }} }}
        @keyframes system-glitch {{ 0% {{ transform: translate(0, 0); }} 2% {{ transform: translate(1px, -1px); }} 4% {{ transform: translate(-1px, 1px); }} 6% {{ transform: translate(0, 0); }} 100% {{ transform: translate(0, 0); }} }}
        .screen {{ animation: crt-flicker 0.15s infinite, system-glitch 4s infinite; }}
    </style>
    <rect width="{svg_width}" height="{svg_height}" class="bg" />
    <g class="screen">
    """
    
    for y in range(0, svg_height, 4):
        svg_content += f'<line x1="0" y1="{y}" x2="{svg_width}" y2="{y}" class="scanline" />\n'
        
    svg_content += f'<text x="25" y="40" class="text-neon text-title">{USERNAME.upper()} SURVIVAL SYSTEM</text>\n'
    svg_content += f'<text x="25" y="75" class="text-neon text-info">SURVIVAL DAY : {survival_day_count}</text>\n'
    svg_content += f'<text x="25" y="95" class="text-neon text-info">RANK         : {rank_name.upper()} (LVL {level})</text>\n'
    svg_content += f'<text x="450" y="75" class="text-neon text-info">TOTAL XP     : {total_commits} XP</text>\n'
    svg_content += f'<text x="450" y="95" class="text-neon text-info">STATUS       : {survived} CLEARED / {invaded} INVADED</text>\n'
    
    display_zombies = 0 if today_str < game_start_date else today_zombies
    display_commits = 0 if today_str < game_start_date else today_commits

    svg_content += f'<rect x="25" y="115" width="930" height="30" class="intel-panel" />\n'
    svg_content += f'<text x="35" y="135" class="text-neon text-info">TODAY INTEL | INCOMING ZOMBIES: {display_zombies} | ELIMINATED: {display_commits} | STATUS: <tspan class="text-status">{today_status}</tspan></text>\n'

    box_size, gap, start_x, start_y = 20, 4, 25, 165 
    ticker_logs = [random.choice(current_msgs), random.choice(current_msgs)]
    
    for i in range(378):
        week_idx, day_idx = i // 7, i % 7   
        col = week_idx if week_idx < 27 else week_idx - 27
        row = day_idx if week_idx < 27 else day_idx + 7
        x, y = start_x + (col * (box_size + gap)), start_y + (row * (box_size + gap))
        
        if i < len(days):
            day = days[i]
            date_str, commits = day['date'], day['contributionCount']
            extra_class = " current-day" if i == len(days) - 1 else ""
            
            if date_str < game_start_date:
                if commits == 0: color_class = "past-0"
                elif commits <= 2: color_class = "past-1"
                elif commits <= 4: color_class = "past-2"
                elif commits <= 6: color_class = "past-3"
                else: color_class = "past-4"
            else:
                zombies = history.get(date_str, 0)
                if commits >= zombies:
                    fark = commits - zombies
                    if fark == 0: color_class = "game-survived-1"
                    elif fark == 1: color_class = "game-survived-2"
                    elif fark == 2: color_class = "game-survived-3"
                    else: color_class = "game-survived-4"
                    ticker_logs.append(random.choice(MSG_CLEARED).format(date=date_str, commits=commits))
                else:
                    if commits > 0: 
                        color_class = "game-invaded-1"
                        ticker_logs.append(random.choice(MSG_FAILED).format(date=date_str, commits=commits))
                    else: 
                        color_class = "game-invaded-2"
                        ticker_logs.append(random.choice(MSG_ZERO).format(date=date_str, commits=commits))
            svg_content += f'<rect x="{x}" y="{y}" width="{box_size}" height="{box_size}" class="{color_class}{extra_class}" />\n'
        else:
            svg_content += f'<rect x="{x}" y="{y}" width="{box_size}" height="{box_size}" class="fog-of-war" />\n'
        
    panel_x, panel_width, panel_height = 690, 265, 164
    svg_content += get_live_cam_svg(cam_state, panel_x, 165, panel_width, panel_height)
    svg_content += get_radar_svg(remaining_zombies, panel_x, 337, panel_width, panel_height)

    medal_y, medal_box_width, medal_gap, start_medal_x = 540, 200, 25, 25
    
    def_badge, def_unlocked = get_current_epic_badge(survived, DEFENSE_BADGES)
    commit_badge, commit_unlocked = get_current_epic_badge(total_commits, COMMIT_BADGES)

    slots = [
        {"name": rank_name, "req": level, "icon": "[R]", "unlocked": True, "type": "RANK"},
        {"name": "NEXT RANK", "req": next_rank_req, "icon": "[R]", "unlocked": False, "type": "GOAL"},
        {"name": def_badge["name"], "req": def_badge["req"], "icon": def_badge["icon"], "unlocked": def_unlocked, "type": "DEFENSE"},
        {"name": commit_badge["name"], "req": commit_badge["req"], "icon": commit_badge["icon"], "unlocked": commit_unlocked, "type": "COMMIT"}
    ]
    
    svg_content += f'<text x="25" y="525" class="text-neon text-medal">ACHIEVEMENTS &amp; MEDALS [TACTICAL SLOTS]</text>\n'
    for idx, slot in enumerate(slots):
        m_x = start_medal_x + (idx * (medal_box_width + medal_gap))
        box_class = "box-medal-earned" if slot["unlocked"] else "box-medal-locked"
        text_class = "text-neon" if slot["unlocked"] else "text-dim"
        status_text = "[UNLOCKED]" if slot["unlocked"] else f"[LOCKED: {slot['req']}]"
        if slot["type"] == "GOAL": status_text = f"[UNLOCKS AT LVL {slot['req']}]"
        
        svg_content += f'<rect x="{m_x}" y="{medal_y}" width="{medal_box_width}" height="45" rx="3" ry="3" class="{box_class}" />\n'
        svg_content += f'<text x="{m_x + 10}" y="{medal_y + 18}" class="{text_class} text-medal">{slot["icon"]} {slot["name"]}</text>\n'
        svg_content += f'<text x="{m_x + 10}" y="{medal_y + 35}" class="{text_class} text-medal">{status_text}</text>\n'

    # XP BAR
    xp_bar_y = 615
    xp_width = 930
    fill_width = int((xp_current / xp_needed) * xp_width) if xp_needed > 0 else 0
    
    svg_content += f'<text x="25" y="{xp_bar_y + 10}" class="text-neon text-info">LEVEL PROGRESS</text>\n'
    svg_content += f'<text x="955" y="{xp_bar_y + 10}" class="text-neon text-info" text-anchor="end">{xp_current} / {xp_needed} XP TO LVL {level + 1}</text>\n'
    svg_content += f'<rect x="25" y="{xp_bar_y + 20}" width="{xp_width}" height="14" class="intel-panel" />\n'
    svg_content += f'<rect x="25" y="{xp_bar_y + 20}" width="{fill_width}" height="14" fill="#39ff14" rx="2" ry="2" />\n'

    # AKAN YAZI
    ticker_logs.append(random.choice(current_msgs))
    ticker_text = " /// ".join(ticker_logs) + " ///"
    text_width_px = len(ticker_text) * 8
    to_x_coord = -(text_width_px)
    animation_duration = max(30, int(len(ticker_text) * 0.05))
    
    svg_content += f"""
        <text y="685" class="text-neon text-info">
            <animate attributeName="x" from="{svg_width}" to="{to_x_coord}" dur="{animation_duration}s" repeatCount="indefinite" />
            {ticker_text}
        </text>
    </g>
    </svg>
    """
    
    with open("zombie-graph.svg", "w", encoding="utf-8") as file:
        file.write(svg_content)
    print(f"[SUCCESS] Test Action Zombie Graph oluşturuldu: 'zombie-graph.svg'")

def simulate_zombie_survival(days):
    state = load_state()
    today_str = date.today().strftime("%Y-%m-%d")

    if not state.get("start_date"):
        state["start_date"] = today_str
        save_state(state)

    game_start_date = state["start_date"]
    history = state.get("history", {})

    active_days = [day for day in days if day['date'] >= game_start_date]
    if not active_days: 
        generate_pipboy_svg(days, level=0, xp_current=0, xp_needed=1, rank_name="LONE WANDERER", next_rank_req=25, survived=0, invaded=0, survival_day_count=0, total_commits=0, game_start_date=game_start_date, history=history)
        return

    start_date_obj = datetime.strptime(game_start_date, "%Y-%m-%d").date()
    latest_date_obj = datetime.strptime(active_days[-1]['date'], "%Y-%m-%d").date()
    survival_day = max(0, (latest_date_obj - start_date_obj).days)

    state_updated = False
    for d in active_days:
        date_str = d['date']
        if date_str not in history and date_str <= today_str:
            history[date_str] = random.randint(1, 4)
            state_updated = True

    if state_updated:
        state["history"] = history
        save_state(state)

    total_survived = 0
    total_invaded = 0
    total_commits = sum(d['contributionCount'] for d in active_days)
    
    for d in active_days:
        date_str = d['date']
        if date_str >= today_str: continue
        commits = d['contributionCount']
        zombies = history.get(date_str, 0)
        
        if commits >= zombies: total_survived += 1
        else: total_invaded += 1 

    # GERÇEK HESAPLAMALAR
    level, xp_current, xp_needed = calculate_level_info(total_commits)
    rank_name, current_rank_req = get_rank(level)
    
    next_rank_req = 25
    if level >= 25:
        next_rank_req = ((level // 25) + 1) * 25
        if next_rank_req > 300: next_rank_req = 300

    # =========================================================================
    # TEST GÖRÜNÜMÜ İÇİN MOCK DEĞERLER 
    # (Level 2 ve Yarı Dolu Bar görünümünü test etmek için bunları ezdiriyoruz)
    # Tasarımı gördükten sonra bu bloğu silebilirsiniz.
    level = 2
    xp_current = 1  
    xp_needed = 2   
    total_commits = 4 
    rank_name, _ = get_rank(level)
    next_rank_req = 25
    # =========================================================================
    
    generate_pipboy_svg(days, level, xp_current, xp_needed, rank_name, next_rank_req, total_survived, total_invaded, survival_day, total_commits, game_start_date, history)

if __name__ == "__main__":
    real_github_data = get_contribution_data()
    if real_github_data: simulate_zombie_survival(real_github_data)
    else: print("[ERROR] Veri çekilemedi.")