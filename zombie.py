import os
import requests
import random
import math
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("GITHUB_TOKEN")
USERNAME = os.getenv("GITHUB_USERNAME", os.getenv("GITHUB_REPOSITORY_OWNER", "achexus"))
DIFFICULTY = os.getenv("GITHUB_DIFFICULTY", "normal").lower().strip()
# Varsayılan ana tema 'classic' olarak ayarlandı
THEME_NAME = os.getenv("GITHUB_THEME", "classic").lower().strip()

# --- THEME PALETTES ---
THEMES = {
    "cyberpunk": {
        "bg_color":        "#0a0010",
        "panel_color":     "rgba(10, 0, 20, 0.85)",
        "panel_stroke":    "#6a0080",
        "panel_dark":      "#050008",
        "primary_text":    "#ff00ff",
        "dim_text":        "#4a0060",
        "secure_color":    "#ff00ff",
        "danger_color":    "#ff0066",
        "danger_dark":     "#990040",
        "warning_color":   "#ff66ff",
        "radar_ring":      "#6a0080",
        "radar_sweep":     "rgba(255, 0, 255, 0.15)",
        "scanline":        "rgba(255, 0, 255, 0.08)",
        "crosshair":       "#ff00ff",
        "crosshair_bg":    "rgba(255,0,255,0.05)",
        "secure_bg":       "rgba(255, 0, 255, 0.15)",
        "cam_bg":          "#080010",
        "cam_secure_bg":   "#0a0010",
        "grid_stroke":     "#1a0030",
        "tire_stripe":     "#6a0080",
        "tire_hub":        "#2a0040",
        "tire_hub2":       "#0a0010",
        "bar_fill":        "#ff00ff",
        "past_0":          "#050008",
        "past_1":          "#130020",
        "past_2":          "#220033",
        "past_3":          "#30004d",
        "past_4":          "#3f0066",
        "surv_1":          "#660066",
        "surv_2":          "#990099",
        "surv_3":          "#cc00cc",
        "surv_4":          "#ff00ff",
        "inv_1":           "#5e0020",
        "inv_1_stroke":    "#990040",
        "inv_2":           "#20000a",
    },
    "fallout": {
        "bg_color":        "#0a0800",
        "panel_color":     "rgba(10, 8, 0, 0.85)",
        "panel_stroke":    "#4d3800",
        "panel_dark":      "#070600",
        "primary_text":    "#ffa500",
        "dim_text":        "#4d3800",
        "secure_color":    "#ffa500",
        "danger_color":    "#cc4400",
        "danger_dark":     "#992200",
        "warning_color":   "#ff6600",
        "radar_ring":      "#4d3800",
        "radar_sweep":     "rgba(255, 165, 0, 0.15)",
        "scanline":        "rgba(255, 165, 0, 0.08)",
        "crosshair":       "#ffa500",
        "crosshair_bg":    "rgba(255,165,0,0.05)",
        "secure_bg":       "rgba(255, 165, 0, 0.15)",
        "cam_bg":          "#0d0900",
        "cam_secure_bg":   "#0a0800",
        "grid_stroke":     "#261900",
        "tire_stripe":     "#4d3800",
        "tire_hub":        "#261900",
        "tire_hub2":       "#0a0800",
        "bar_fill":        "#ffa500",
        "past_0":          "#0a0800",
        "past_1":          "#1a1400",
        "past_2":          "#332800",
        "past_3":          "#4d3c00",
        "past_4":          "#665000",
        "surv_1":          "#664400",
        "surv_2":          "#996600",
        "surv_3":          "#cc8800",
        "surv_4":          "#ffa500",
        "inv_1":           "#4a1111",
        "inv_1_stroke":    "#8a2222",
        "inv_2":           "#1a0505",
    },
    "resident_evil": {
        "bg_color":        "#0a0a0a",
        "panel_color":     "rgba(10, 10, 10, 0.9)",
        "panel_stroke":    "#4a0000",
        "panel_dark":      "#050505",
        "primary_text":    "#e8e8e8",
        "dim_text":        "#4a0000",
        "secure_color":    "#e8e8e8",
        "danger_color":    "#cc0000",
        "danger_dark":     "#880000",
        "warning_color":   "#ff4400",
        "radar_ring":      "#4a0000",
        "radar_sweep":     "rgba(200, 0, 0, 0.15)",
        "scanline":        "rgba(232, 232, 232, 0.06)",
        "crosshair":       "#e8e8e8",
        "crosshair_bg":    "rgba(200,200,200,0.05)",
        "secure_bg":       "rgba(232, 232, 232, 0.12)",
        "cam_bg":          "#0d0000",
        "cam_secure_bg":   "#0a0a0a",
        "grid_stroke":     "#1a0000",
        "tire_stripe":     "#4a0000",
        "tire_hub":        "#1a0000",
        "tire_hub2":       "#0a0a0a",
        "bar_fill":        "#e8e8e8",
        "past_0":          "#0a0a0a",
        "past_1":          "#1a1a1a",
        "past_2":          "#2a2a2a",
        "past_3":          "#3a3a3a",
        "past_4":          "#4a4a4a",
        "surv_1":          "#555555",
        "surv_2":          "#888888",
        "surv_3":          "#bbbbbb",
        "surv_4":          "#e8e8e8",
        "inv_1":           "#660000",
        "inv_1_stroke":    "#aa0000",
        "inv_2":           "#220000",
    },
    "classic": {
        "bg_color":        "#0d1117",
        "panel_color":     "rgba(13, 17, 23, 0.8)",
        "panel_stroke":    "#1a4d1a",
        "panel_dark":      "#0a0a0f",
        "primary_text":    "#39ff14",
        "dim_text":        "#1a4d1a",
        "secure_color":    "#39ff14",
        "danger_color":    "#d92525",
        "danger_dark":     "#a11b1b",
        "warning_color":   "#ff8c00",
        "radar_ring":      "#1a4d1a",
        "radar_sweep":     "rgba(57, 255, 20, 0.15)",
        "scanline":        "rgba(57, 255, 20, 0.10)",
        "crosshair":       "#39ff14",
        "crosshair_bg":    "rgba(57,255,20,0.05)",
        "secure_bg":       "rgba(57, 255, 20, 0.15)",
        "cam_bg":          "#050510",
        "cam_secure_bg":   "#0d1117",
        "grid_stroke":     "#1a2332",
        "tire_stripe":     "#1a4d1a",
        "tire_hub":        "#1c3242",
        "tire_hub2":       "#0d1117",
        "bar_fill":        "#39ff14",
        "past_0":          "#0d1117",
        "past_1":          "#1c3242",
        "past_2":          "#285473",
        "past_3":          "#3679a6",
        "past_4":          "#459fdb",
        "surv_1":          "#1f6b11",
        "surv_2":          "#2c9e17",
        "surv_3":          "#39ff14",
        "surv_4":          "#a3ff00",
        "inv_1":           "#8a0020",
        "inv_1_stroke":    "#ff003c",
        "inv_2":           "#3a000d",
    }
}

THEME = THEMES.get(THEME_NAME, THEMES["classic"])

# --- SABİT MESAJLAR VE RÜTBELER ---
MSG_OVERKILL = ["TARGET PRACTICE AT SECTOR {date}. OVERWHELMING FIREPOWER USED.", "THREAT NEUTRALIZED ON {date}. NO CASUALTIES REPORTED."]
MSG_CLEARED = ["CLOSE CALL ON {date}. PERIMETER BARELY SECURED.", "HAND-TO-HAND COMBAT ON {date}. WE HOLD THE LINE."]
MSG_FAILED = ["MAYDAY! BARRICADES BREACHED ON {date}!", "SECTOR {date} OVERRUN. WE TOOK DOWN {commits} BUT IT WAS NOT ENOUGH."]
MSG_ZERO = ["RADIO SILENCE ON {date}. SECTOR ASSUMED LOST.", "NO DEFENSIVE ACTION TAKEN ON {date}. WALKERS ROAM FREE."]
MSG_GENERIC = ["STATIC... ADJUSTING FREQUENCY...", "OUTPOST ALPHA REPORTING ALL CLEAR...", "HEARING MOANS FROM THE EASTERN WOODS..."]

MSG_EN_ROUTE = ["RADAR CONTACT ON THE MOVE. WE NEED BACKUP AT THE NEXT CROSSROAD.", "SQUAD EN ROUTE. MULTIPLE BOGEYS DETECTED ON SCANNERS."]
MSG_COMBAT = ["HOT DROP! WE HAVE ENGAGED THE ENEMY! FIRE AT WILL!", "DO NOT LET THEM CROSS THE PERIMETER! HOLD THE LINE!"]
MSG_SECURE = ["SECTOR CLEAR. REBUILDING BARRICADES AND RESTOCKING SUPPLIES.", "ALL HOSTILES NEUTRALIZED. PATROLLING THE BORDERS."]

ORDERED_RANKS = [
    (10, "SCAVENGER", "▲"), (25, "SURVIVOR", "★"), (50, "SCOUT", "❂"),
    (75, "VANGUARD", "🛡️"), (100, "DEFENDER", "⚔️"), (125, "GUARDIAN", "🏰"),
    (150, "VETERAN", "👑"), (175, "SHARPSHOOTER", "🎯"), (200, "TACTICIAN", "🧠"),
    (225, "COMMANDER", "⭐"), (250, "ZOMBIE HUNTER", "🩸"), (275, "SLAYER", "💀"),
    (300, "LIVING LEGEND", "🌌")
]

_DIFFICULTY_RANGES = {
    "easy":      (1, 2),
    "normal":    (1, 4),
    "hard":      (3, 6),
    "nightmare": (5, 10),
}

def get_zombie_count_for_date(date_str, difficulty=None):
    if not date_str: return 0
    if difficulty is None: difficulty = DIFFICULTY
    lo, hi = _DIFFICULTY_RANGES.get(difficulty, _DIFFICULTY_RANGES["normal"])
    
    try:
        r = random.Random(date_str)
        return r.randint(lo, hi)
    except Exception:
        return 0

def calculate_level_info(total_commits):
    if total_commits == 0: return 0, 0, 1
    level = int((math.sqrt(8 * total_commits + 1) - 1) / 2)
    current_level_base_xp = (level * (level + 1)) // 2
    next_level_base_xp = ((level + 1) * (level + 2)) // 2
    
    current_xp_in_level = total_commits - current_level_base_xp
    xp_needed_for_next = next_level_base_xp - current_level_base_xp
    return level, current_xp_in_level, xp_needed_for_next

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

def get_radar_svg(remaining_zombies, x, y, width, height, t):
    cx = x + (width / 2)
    cy = y + 95
    dots = ""
    coords = [(-40, -35), (35, 20), (-15, 45), (45, -25)]
    for idx in range(min(remaining_zombies, 4)):
        dx, dy = coords[idx]
        dots += f"""
        <circle cx="{cx+dx}" cy="{cy+dy}" r="4" fill="{t['danger_color']}">
            <animate attributeName="opacity" values="0;1;0" dur="3s" begin="{idx * 0.7}s" repeatCount="indefinite" />
        </circle>
        """
    return f"""
    <rect x="{x}" y="{y}" width="{width}" height="{height}" class="intel-panel" />
    <text x="{x+15}" y="{y+25}" class="text-neon text-medal">LOCAL RADAR [50M RADIUS]</text>
    <circle cx="{cx}" cy="{cy}" r="55" stroke="{t['radar_ring']}" stroke-width="1" fill="none" />
    <circle cx="{cx}" cy="{cy}" r="35" stroke="{t['radar_ring']}" stroke-width="1" fill="none" />
    <circle cx="{cx}" cy="{cy}" r="15" stroke="{t['radar_ring']}" stroke-width="1" fill="none" />
    <line x1="{cx}" y1="{cy-55}" x2="{cx}" y2="{cy+55}" stroke="{t['radar_ring']}" stroke-width="1" />
    <line x1="{cx-55}" y1="{cy}" x2="{cx+55}" y2="{cy}" stroke="{t['radar_ring']}" stroke-width="1" />
    <g>
        <path d="M {cx} {cy} L {cx} {cy-55} A 55 55 0 0 1 {cx+55} {cy} Z" fill="{t['radar_sweep']}" />
        <animateTransform attributeName="transform" type="rotate" from="0 {cx} {cy}" to="360 {cx} {cy}" dur="3.5s" repeatCount="indefinite" />
    </g>
    {dots}
    """

def get_live_cam_svg(state, x, y, width, height, t, is_easter_egg=False):
    bg = f'<rect x="{x}" y="{y}" width="{width}" height="{height}" class="intel-panel" />'
    blink_dur = "0.2s" if is_easter_egg else "1.5s"
    live_header = f"""
    <circle cx="{x+18}" cy="{y+20}" r="4" fill="{t['danger_color']}">
        <animate attributeName="opacity" values="1;0;1" dur="{blink_dur}" repeatCount="indefinite" />
    </circle>
    <text x="{x+28}" y="{y+24}" class="text-neon text-medal">LIVE</text>
    """
    
    if state == "en_route":
        content = live_header + f"""
        <clipPath id="tire_clip_cam">
            <rect x="{x+10}" y="{y+40}" width="{width-20}" height="{height-50}" rx="4" />
        </clipPath>
        <g clip-path="url(#tire_clip_cam)">
            <rect x="{x+10}" y="{y+40}" width="{width-20}" height="{height-50}" fill="{t['panel_dark']}" />
            <line x1="{x+10}" y1="{y+145}" x2="{x+width-10}" y2="{y+145}" stroke="{t['tire_stripe']}" stroke-dasharray="35, 25" stroke-width="4">
                <animate attributeName="stroke-dashoffset" from="60" to="0" dur="0.15s" repeatCount="indefinite" />
            </line>
            <g>
                <animateTransform attributeName="transform" type="translate" values="0,0; 0,4; 0,0" dur="0.25s" repeatCount="indefinite" />
                <g>
                    <animateTransform attributeName="transform" type="rotate" from="0 {x+(width/2)} {y+40}" to="360 {x+(width/2)} {y+40}" dur="0.8s" repeatCount="indefinite" />
                    <circle cx="{x+(width/2)}" cy="{y+40}" r="105" fill="{t['panel_dark']}" stroke="{t['grid_stroke']}" stroke-width="8" />
                    <circle cx="{x+(width/2)}" cy="{y+40}" r="100" fill="none" stroke="#000000" stroke-width="10" stroke-dasharray="18, 15" />
                    <circle cx="{x+(width/2)}" cy="{y+40}" r="65" fill="{t['tire_hub']}" stroke="{t['bg_color']}" stroke-width="4" />
                    <line x1="{x+(width/2)}" y1="{y+40-65}" x2="{x+(width/2)}" y2="{y+40+65}" stroke="{t['tire_hub2']}" stroke-width="8" />
                    <line x1="{x+(width/2)-65}" y1="{y+40}" x2="{x+(width/2)+65}" y2="{y+40}" stroke="{t['tire_hub2']}" stroke-width="8" />
                    <line x1="{x+(width/2)-45}" y1="{y+40-45}" x2="{x+(width/2)+45}" y2="{y+40+45}" stroke="{t['tire_hub2']}" stroke-width="8" />
                    <line x1="{x+(width/2)-45}" y1="{y+40+45}" x2="{x+(width/2)+45}" y2="{y+40-45}" stroke="{t['tire_hub2']}" stroke-width="8" />
                    <circle cx="{x+(width/2)}" cy="{y+40}" r="18" fill="{t['tire_hub2']}" />
                </g>
            </g>
        </g>
        <rect x="{x+10}" y="{y+40}" width="{width-20}" height="{height-50}" fill="none" stroke="{t['tire_stripe']}" stroke-width="1" rx="4" />
        """
    elif state == "combat":
        content = live_header + f"""
        <rect x="{x+10}" y="{y+40}" width="{width-20}" height="{height-50}" fill="{t['cam_bg']}" rx="4" ry="4" />
        <g>
            <animateTransform attributeName="transform" type="translate" values="0,0; 0,-12; 0,0" dur="1.5s" repeatCount="indefinite" />
            <animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.7;0.8;1" dur="4s" repeatCount="indefinite" />
            <circle cx="{x+240}" cy="{y+100}" r="15" fill="{t['danger_dark']}" opacity="0.6">
                 <animate attributeName="cx" values="{x+240};{x+40}" dur="4s" repeatCount="indefinite" />
            </circle>
            <circle cx="{x+240}" cy="{y+100}" r="9" fill="{t['danger_color']}" opacity="0.9">
                 <animate attributeName="cx" values="{x+240};{x+40}" dur="4s" repeatCount="indefinite" />
            </circle>
        </g>
        <g>
            <animateTransform attributeName="transform" type="translate" values="0,0; 0,-8; 0,0" dur="1.2s" repeatCount="indefinite" />
            <animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.8;0.9;1" dur="5s" repeatCount="indefinite" />
            <circle cx="{x+220}" cy="{y+130}" r="18" fill="{t['danger_dark']}" opacity="0.5">
                 <animate attributeName="cx" values="{x+220};{x+40}" dur="5s" repeatCount="indefinite" />
            </circle>
            <circle cx="{x+220}" cy="{y+130}" r="11" fill="{t['danger_color']}" opacity="0.8">
                 <animate attributeName="cx" values="{x+220};{x+40}" dur="5s" repeatCount="indefinite" />
            </circle>
        </g>
        <g stroke="{t['crosshair']}" stroke-width="1.5">
            <animateTransform attributeName="transform" type="translate" values="0,0; 30,8; -20,-10; 0,0" dur="4s" repeatCount="indefinite" />
            <circle cx="{x+(width/2)}" cy="{y+95}" r="45" fill="{t['crosshair_bg']}" />
            <line x1="{x+(width/2)-60}" y1="{y+95}" x2="{x+(width/2)+60}" y2="{y+95}" />
            <line x1="{x+(width/2)}" y1="{y+35}" x2="{x+(width/2)}" y2="{y+155}" />
            <circle cx="{x+(width/2)}" cy="{y+95}" r="2" fill="{t['crosshair']}" stroke="none">
                <animate attributeName="opacity" values="1;0;1" dur="0.8s" repeatCount="indefinite" />
            </circle>
        </g>
        """
    else:
        content = live_header + f"""
        <rect x="{x+10}" y="{y+40}" width="{width-20}" height="{height-50}" fill="{t['cam_secure_bg']}" rx="4" ry="4" />
        <path d="M {x+10} {y+70} L {x+width-10} {y+70} M {x+10} {y+105} L {x+width-10} {y+105} M {x+10} {y+140} L {x+width-10} {y+140}" stroke="{t['grid_stroke']}" stroke-width="4" />
        <path d="M {x+60} {y+40} L {x+60} {y+height-10} M {x+130} {y+40} L {x+130} {y+height-10} M {x+200} {y+40} L {x+200} {y+height-10}" stroke="{t['grid_stroke']}" stroke-width="4" />
        
        <rect x="{x+20}" y="{y+45}" width="30" height="20" fill="{t['tire_hub']}" />
        <rect x="{x+70}" y="{y+45}" width="50" height="20" fill="{t['cam_bg']}" />
        <rect x="{x+140}" y="{y+45}" width="50" height="20" fill="{t['tire_hub']}" />
        <rect x="{x+210}" y="{y+45}" width="40" height="20" fill="{t['cam_bg']}" />
        
        <rect x="{x+20}" y="{y+75}" width="30" height="25" fill="{t['cam_bg']}" />
        <rect x="{x+70}" y="{y+75}" width="50" height="25" fill="{t['tire_hub']}" />
        <rect x="{x+140}" y="{y+75}" width="50" height="25" fill="{t['tire_hub']}" />
        <rect x="{x+210}" y="{y+75}" width="40" height="25" fill="{t['cam_bg']}" />
        
        <rect x="{x+20}" y="{y+110}" width="30" height="25" fill="{t['tire_hub']}" />
        <rect x="{x+70}" y="{y+110}" width="50" height="25" fill="{t['cam_bg']}" />
        
        <rect x="{x+135}" y="{y+110}" width="115" height="25" fill="{t['secure_bg']}" stroke="{t['secure_color']}" stroke-width="1" />
        <circle cx="{x+150}" cy="{y+122}" r="3" fill="{t['secure_color']}">
            <animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite" />
        </circle>
        <text x="{x+195}" y="{y+126}" class="text-neon" font-size="11" text-anchor="middle">SAFE ZONE</text>
        
        <line x1="{x+10}" y1="{y+40}" x2="{x+10}" y2="{y+height-10}" stroke="{t['secure_color']}" stroke-width="2" opacity="0.5">
            <animate attributeName="x1" values="{x+10};{x+width-10};{x+10}" dur="5s" repeatCount="indefinite" />
            <animate attributeName="x2" values="{x+10};{x+width-10};{x+10}" dur="5s" repeatCount="indefinite" />
        </line>
        """
    return bg + content

def generate_pipboy_svg(days, level, xp_current, xp_needed, survived, invaded, survival_day, total_commits, first_active_date, t, theme_name):
    svg_width = 980
    svg_height = 740
    is_easter_egg = (total_commits == 100)
    
    day_map = {d['date']: d['contributionCount'] for d in days}
    today_str = days[-1]['date']
    
    today_commits = day_map.get(today_str, 0)
    today_zombies = get_zombie_count_for_date(today_str) if today_str >= first_active_date else 0
    remaining_zombies = max(0, today_zombies - today_commits)
    
    if today_str < first_active_date:
        cam_state = "secure"
        today_status = "SYSTEM STANDBY (PRE-INVASION)"
        status_color = t['secure_color']
        remaining_zombies = 0
    else:
        if today_commits == 0:
            cam_state = "en_route"
            today_status = "CRITICAL (EN ROUTE)"
            status_color = t['danger_color']
        elif today_commits < today_zombies:
            cam_state = "combat"
            today_status = "BREACHED (ENGAGING)"
            status_color = t['warning_color']
        else:
            cam_state = "secure"
            today_status = "SECURE (CLEARED)"
            status_color = t['secure_color']

    if cam_state == "en_route": current_msgs = MSG_EN_ROUTE
    elif cam_state == "combat": current_msgs = MSG_COMBAT
    else: current_msgs = MSG_SECURE
    
    if is_easter_egg:
        today_status = "FATAL EXCEPTION 0x00000064"
        status_color = "#ff00ff"
        current_msgs = ["SYSTEM FAILURE", "CORRUPTED DATA", "WHO ARE WE?", "LOST IN THE GRID"]

    current_rank_idx = -1
    for i, (req, name, icon) in enumerate(ORDERED_RANKS):
        if level >= req:
            current_rank_idx = i
            
    active_rank_name = "UNRANKED" if current_rank_idx == -1 else ORDERED_RANKS[current_rank_idx][1]
    if is_easter_egg: active_rank_name = "KAYBOLMUŞ"

    screen_class = "screen easter-egg" if is_easter_egg else "screen"

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{svg_width}" height="{svg_height}">
    <style>
        .bg {{ fill: transparent; }}
        .scanline {{ stroke: {t['scanline']}; stroke-width: 1; }}
        .text-neon {{ fill: {t['primary_text']}; font-family: 'Courier New', Courier, monospace; font-weight: bold; }}
        .text-dim {{ fill: {t['dim_text']}; font-family: 'Courier New', Courier, monospace; font-weight: bold; }}
        .text-title {{ font-size: 22px; }}
        .text-info {{ font-size: 14px; }}
        .text-medal {{ font-size: 12px; }}
        .text-status {{ fill: {status_color}; font-family: 'Courier New', Courier, monospace; font-weight: bold; font-size: 14px; }}
        .box-medal-earned {{ fill: {t['secure_bg']}; stroke: {t['primary_text']}; stroke-width: 1; }}
        .box-medal-locked {{ fill: transparent; stroke: {t['dim_text']}; stroke-width: 1; stroke-dasharray: 4; }}
        .intel-panel {{ fill: {t['panel_color']}; stroke: {t['panel_stroke']}; stroke-width: 1; rx: 4; ry: 4; }}
        .fog-of-war {{ fill: {t['panel_color']}; stroke: {t['panel_stroke']}; stroke-width: 1; stroke-dasharray: 2; opacity: 0.8; }}
        
        .past-0 {{ fill: {t['past_0']}; stroke: {t['grid_stroke']}; stroke-width: 1; rx: 2; ry: 2; }}
        .past-1 {{ fill: {t['past_1']}; rx: 2; ry: 2; }}
        .past-2 {{ fill: {t['past_2']}; rx: 2; ry: 2; }}
        .past-3 {{ fill: {t['past_3']}; rx: 2; ry: 2; }}
        .past-4 {{ fill: {t['past_4']}; rx: 2; ry: 2; }}
        .game-survived-1 {{ fill: {t['surv_1']}; rx: 2; ry: 2; }} 
        .game-survived-2 {{ fill: {t['surv_2']}; rx: 2; ry: 2; }} 
        .game-survived-3 {{ fill: {t['surv_3']}; rx: 2; ry: 2; }} 
        .game-survived-4 {{ fill: {t['surv_4']}; rx: 2; ry: 2; }} 
        
        .game-invaded-1 {{ fill: {t['inv_1']}; stroke: {t['inv_1_stroke']}; stroke-width: 1; rx: 2; ry: 2; }}  
        .game-invaded-2 {{ fill: {t['inv_2']}; rx: 2; ry: 2; }}  
        
        @keyframes pulse-beacon {{ 0% {{ fill-opacity: 1; stroke: #ffffff; stroke-width: 1px; }} 50% {{ fill-opacity: 0.4; stroke: {t['secure_color']}; stroke-width: 3px; }} 100% {{ fill-opacity: 1; stroke: #ffffff; stroke-width: 1px; }} }}
        .current-day {{ animation: pulse-beacon 1.5s infinite; rx: 3; ry: 3; }}
        
        @keyframes crt-flicker {{ 0% {{ opacity: 0.95; }} 5% {{ opacity: 0.85; }} 10% {{ opacity: 0.95; }} 15% {{ opacity: 1.0; }} 50% {{ opacity: 0.98; }} 100% {{ opacity: 0.95; }} }}
        @keyframes system-glitch {{ 0% {{ transform: translate(0, 0); }} 2% {{ transform: translate(1px, -1px); }} 4% {{ transform: translate(-1px, 1px); }} 6% {{ transform: translate(0, 0); }} 100% {{ transform: translate(0, 0); }} }}
        .screen {{ animation: crt-flicker 0.15s infinite, system-glitch 4s infinite; }}
    </style>
    <rect width="{svg_width}" height="{svg_height}" class="bg" />
    <g class="{screen_class}">
    """
    
    for y in range(0, svg_height, 4):
        svg_content += f'<line x1="0" y1="{y}" x2="{svg_width}" y2="{y}" class="scanline" />\n'
        
    svg_content += f'<text x="25" y="40" class="text-neon text-title">{USERNAME.upper()} SURVIVAL SYSTEM [{theme_name.upper()}]</text>\n'
    svg_content += f'<text x="25" y="75" class="text-neon text-info">SURVIVAL DAY : {survival_day}</text>\n'
    svg_content += f'<text x="25" y="95" class="text-neon text-info">RANK         : {active_rank_name.upper()} (LVL {level})</text>\n'
    svg_content += f'<text x="450" y="75" class="text-neon text-info">TOTAL XP     : {total_commits} XP</text>\n'
    svg_content += f'<text x="450" y="95" class="text-neon text-info">STATUS       : {survived} CLEARED / {invaded} INVADED</text>\n'
    
    display_zombies = 0 if today_str < first_active_date else today_zombies
    display_commits = 0 if today_str < first_active_date else today_commits

    svg_content += f'<rect x="25" y="115" width="930" height="30" class="intel-panel" />\n'
    svg_content += f'<text x="35" y="135" class="text-neon text-info">TODAY INTEL | INCOMING ZOMBIES: {display_zombies} | ELIMINATED: {display_commits} | STATUS: <tspan class="text-status">{today_status}</tspan></text>\n'

    box_size, gap, start_x, start_y = 20, 4, 25, 165 
    ticker_logs = [random.choice(current_msgs), random.choice(MSG_GENERIC)]
    
    for i in range(378):
        week_idx, day_idx = i // 7, i % 7   
        col = week_idx if week_idx < 27 else week_idx - 27
        row = day_idx if week_idx < 27 else day_idx + 7
        x, y = start_x + (col * (box_size + gap)), start_y + (row * (box_size + gap))
        
        if i < len(days):
            day = days[i]
            date_str, commits = day['date'], day['contributionCount']
            extra_class = " current-day" if i == len(days) - 1 else ""
            
            if date_str < first_active_date:
                if commits == 0: color_class = "past-0"
                elif commits <= 2: color_class = "past-1"
                elif commits <= 4: color_class = "past-2"
                elif commits <= 6: color_class = "past-3"
                else: color_class = "past-4"
            else:
                zombies = get_zombie_count_for_date(date_str)
                if commits >= zombies:
                    fark = commits - zombies
                    if fark == 0: color_class = "game-survived-1"
                    elif fark == 1: color_class = "game-survived-2"
                    else: color_class = "game-survived-3" if fark == 2 else "game-survived-4"
                    
                    if date_str < today_str:
                        msg = random.choice(MSG_OVERKILL) if fark >= 2 else random.choice(MSG_CLEARED)
                        ticker_logs.append(msg.format(date=date_str, commits=commits))
                else:
                    if commits > 0: 
                        color_class = "game-invaded-1"
                        if date_str < today_str:
                            ticker_logs.append(random.choice(MSG_FAILED).format(date=date_str, commits=commits))
                    else: 
                        color_class = "game-invaded-2"
                        if date_str < today_str:
                            ticker_logs.append(random.choice(MSG_ZERO).format(date=date_str, commits=commits))
            
            svg_content += f'<rect x="{x}" y="{y}" width="{box_size}" height="{box_size}" class="{color_class}{extra_class}" />\n'
        else:
            svg_content += f'<rect x="{x}" y="{y}" width="{box_size}" height="{box_size}" class="fog-of-war" />\n'
        
    panel_x, panel_width, panel_height = 690, 265, 164
    svg_content += get_live_cam_svg(cam_state, panel_x, 165, panel_width, panel_height, t, is_easter_egg)
    svg_content += get_radar_svg(remaining_zombies, panel_x, 337, panel_width, panel_height, t)

    medal_y, medal_box_width, medal_gap, start_medal_x = 540, 200, 25, 25
    start_idx = max(0, min(current_rank_idx, len(ORDERED_RANKS) - 4))
    
    slots = []
    for i in range(4):
        target_idx = start_idx + i
        if target_idx < len(ORDERED_RANKS):
            req, name, icon = ORDERED_RANKS[target_idx]
            slots.append({"name": name, "req": req, "icon": icon, "unlocked": level >= req})
    
    svg_content += f'<text x="25" y="525" class="text-neon text-medal">RANK PROGRESSION [ACTIVE &amp; UPCOMING]</text>\n'
    for idx, slot in enumerate(slots):
        m_x = start_medal_x + (idx * (medal_box_width + medal_gap))
        box_class = "box-medal-earned" if slot["unlocked"] else "box-medal-locked"
        text_class = "text-neon" if slot["unlocked"] else "text-dim"
        status_text = "[UNLOCKED]" if slot["unlocked"] else f"[LOCKED: LVL {slot['req']}]"
        
        svg_content += f'<rect x="{m_x}" y="{medal_y}" width="{medal_box_width}" height="45" rx="3" ry="3" class="{box_class}" />\n'
        svg_content += f'<text x="{m_x + 10}" y="{medal_y + 18}" class="{text_class} text-medal">{slot["icon"]} {slot["name"]}</text>\n'
        svg_content += f'<text x="{m_x + 10}" y="{medal_y + 35}" class="{text_class} text-medal">{status_text}</text>\n'

    if not is_easter_egg:
        xp_bar_y = 615
        total_blocks = 77
        block_width = 10
        block_gap = 2
        bar_x = 25
        bar_width = (total_blocks * (block_width + block_gap)) + 2
        
        svg_content += f'<text x="25" y="{xp_bar_y + 10}" class="text-neon text-info">SYSTEM UPGRADE PROGRESS</text>\n'
        svg_content += f'<text x="{bar_x + bar_width}" y="{xp_bar_y + 10}" class="text-neon text-info" text-anchor="end">{xp_current} / {xp_needed} XP TO LVL {level + 1}</text>\n'
        
        svg_content += f'<rect x="{bar_x}" y="{xp_bar_y + 17}" width="{bar_width}" height="20" fill="none" stroke="{t["panel_stroke"]}" stroke-width="1.5" />\n'
        
        if xp_needed > 0: fill_count = int(round((xp_current / xp_needed) * total_blocks))
        else: fill_count = 0
            
        for i in range(total_blocks):
            b_x = bar_x + 2 + i * (block_width + block_gap)
            b_y = xp_bar_y + 20
            
            if i < fill_count:
                if i == fill_count - 1:
                    svg_content += f'<rect x="{b_x}" y="{b_y}" width="{block_width}" height="14" fill="{t["bar_fill"]}">\n'
                    svg_content += f'    <animate attributeName="opacity" values="1;0.2;1" dur="0.8s" repeatCount="indefinite" />\n'
                    svg_content += f'</rect>\n'
                else:
                    svg_content += f'<rect x="{b_x}" y="{b_y}" width="{block_width}" height="14" fill="{t["bar_fill"]}" />\n'
    else:
        svg_content += f'<text x="490" y="640" class="text-status" text-anchor="middle" font-size="20">ERROR 404: LEVEL PROGRESSION NOT FOUND</text>\n'

    ticker_logs = ticker_logs[-15:]
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
    
    # Sadece seçilen (THEME_NAME) temayı 'zombie-graph.svg' olarak dışarı aktarıyoruz
    if theme_name == THEME_NAME:
        filename = "zombie-graph.svg"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(svg_content)
        print(f"[SUCCESS] Ana grafik oluşturuldu: '{filename}' ({theme_name.capitalize()})")
    else:
        filename = f"zombie-graph-{theme_name}.svg"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(svg_content)
        print(f"[SUCCESS] Alternatif tema oluşturuldu: '{filename}'")

def simulate_zombie_survival(days):
    today_str = days[-1]['date']
    today_obj = datetime.strptime(today_str, "%Y-%m-%d").date()
    
    cutoff_date_str = (today_obj - timedelta(days=30)).strftime("%Y-%m-%d")
    first_active_date = None
    
    for d in days:
        if d['date'] >= cutoff_date_str and d['contributionCount'] > 0:
            first_active_date = d['date']
            break
            
    if not first_active_date: 
        first_active_date = today_str 

    survival_day = 0
    for d in days:
        if d['date'] > today_str:
            break
        if d['contributionCount'] > 0:
            survival_day += 1
        elif d['date'] < today_str:
            survival_day = 0 

    total_survived = 0
    total_invaded = 0
    total_commits = 0
    
    active_days = [day for day in days if day['date'] >= first_active_date]
    
    for d in active_days:
        date_str = d['date']
        if date_str >= today_str: continue 
        
        commits = d['contributionCount']
        total_commits += commits
        
        zombies = get_zombie_count_for_date(date_str)
        if commits >= zombies: total_survived += 1
        else: total_invaded += 1 

    today_commits = next((d['contributionCount'] for d in days if d['date'] == today_str), 0)
    total_commits += today_commits

    level, xp_current, xp_needed = calculate_level_info(total_commits)
    
    # Tüm temalar için ayrı ayrı SVG üretimi
    for theme_key, theme_data in THEMES.items():
        generate_pipboy_svg(
            days, level, xp_current, xp_needed, total_survived, total_invaded, 
            survival_day, total_commits, first_active_date, 
            t=theme_data, theme_name=theme_key
        )

if __name__ == "__main__":
    real_github_data = get_contribution_data()
    if real_github_data: simulate_zombie_survival(real_github_data)
    else: print("[ERROR] Veri çekilemedi.")