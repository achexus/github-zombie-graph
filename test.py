import random
from datetime import datetime, date, timedelta
import sys

USERNAME = "ACHEXUS"
GAME_START_DATE = date.today().strftime("%Y-%m-%d")

MSG_OVERKILL = ["TARGET PRACTICE AT SECTOR {date}. OVERWHELMING FIREPOWER USED.", "THREAT NEUTRALIZED ON {date}. NO CASUALTIES REPORTED.", "CLEAN SWEEP. {commits} HITS CONFIRMED ON {date}."]
MSG_CLEARED = ["CLOSE CALL ON {date}. PERIMETER BARELY SECURED.", "HAND-TO-HAND COMBAT ON {date}. WE HOLD THE LINE.", "SECTOR {date} CLEAR BUT AMMO IS RUNNING DANGEROUSLY LOW."]
MSG_FAILED = ["MAYDAY! BARRICADES BREACHED ON {date}!", "SECTOR {date} OVERRUN. WE TOOK DOWN {commits} BUT IT WAS NOT ENOUGH.", "DEFENSE FAILED AT {date}. FALLING BACK TO INNER SECTOR."]
MSG_ZERO = ["RADIO SILENCE ON {date}. SECTOR ASSUMED LOST.", "NO DEFENSIVE ACTION TAKEN ON {date}. WALKERS ROAM FREE.", "CAMERAS SHOW HEAVY INFESTATION AT {date}. NO RESISTANCE."]
MSG_GENERIC = ["STATIC... ADJUSTING FREQUENCY...", "OUTPOST ALPHA REPORTING ALL CLEAR...", "HEARING MOANS FROM THE EASTERN WOODS..."]

def generate_mock_data():
    days = []
    base_date = date.today() - timedelta(days=371)
    for i in range(371):
        current = base_date + timedelta(days=i)
        commits = random.choices([0, 1, 3, 6, 10], weights=[50, 20, 15, 10, 5])[0]
        days.append({
            "date": current.strftime("%Y-%m-%d"), 
            "contributionCount": commits
        })
    return days

# --- ANİMASYON MODÜLLERİ ---
def get_radar_svg(x, y):
    cx = x + 120
    cy = y + 90
    return f"""
    <rect x="{x}" y="{y}" width="240" height="175" class="intel-panel" />
    <text x="{x+10}" y="{y+20}" class="text-neon text-medal">LOCAL RADAR [50M RADIUS]</text>
    <circle cx="{cx}" cy="{cy}" r="65" stroke="#1a4d1a" stroke-width="1" fill="none" />
    <circle cx="{cx}" cy="{cy}" r="45" stroke="#1a4d1a" stroke-width="1" fill="none" />
    <circle cx="{cx}" cy="{cy}" r="25" stroke="#1a4d1a" stroke-width="1" fill="none" />
    <line x1="{cx}" y1="{cy-65}" x2="{cx}" y2="{cy+65}" stroke="#1a4d1a" stroke-width="1" />
    <line x1="{cx-65}" y1="{cy}" x2="{cx+65}" y2="{cy}" stroke="#1a4d1a" stroke-width="1" />
    
    <g>
        <path d="M {cx} {cy} L {cx} {cy-65} A 65 65 0 0 1 {cx+65} {cy} Z" fill="rgba(57, 255, 20, 0.15)" />
        <animateTransform attributeName="transform" type="rotate" from="0 {cx} {cy}" to="360 {cx} {cy}" dur="4s" repeatCount="indefinite" />
    </g>
    
    <circle cx="{cx-30}" cy="{cy-40}" r="3" fill="#ff003c">
        <animate attributeName="opacity" values="0;1;0" dur="4s" begin="1s" repeatCount="indefinite" />
    </circle>
    <circle cx="{cx+40}" cy="{cy+20}" r="3" fill="#ff003c">
        <animate attributeName="opacity" values="0;1;0" dur="4s" begin="2.5s" repeatCount="indefinite" />
    </circle>
    <circle cx="{cx-15}" cy="{cy+50}" r="3" fill="#ff003c">
        <animate attributeName="opacity" values="0;1;0" dur="4s" begin="3.5s" repeatCount="indefinite" />
    </circle>
    """

def get_live_cam_svg(state, x, y):
    bg = f'<rect x="{x}" y="{y}" width="240" height="140" class="intel-panel" />'
    
    if state == "en_route":
        content = f"""
        <text x="{x+10}" y="{y+20}" class="text-neon text-medal">LIVE CAM: SQUAD EN ROUTE</text>
        <line x1="{x+20}" y1="{y+70}" x2="{x+200}" y2="{y+70}" stroke="#1a4d1a" stroke-dasharray="5,5" stroke-width="2" />
        <circle cx="{x+20}" cy="{y+70}" r="6" fill="#39ff14">
            <animate attributeName="cx" values="{x+20};{x+200};{x+20}" dur="6s" repeatCount="indefinite" />
        </circle>
        <rect x="{x+195}" y="{y+65}" width="10" height="10" fill="#ff003c" opacity="0.7" />
        <text x="{x+180}" y="{y+95}" class="text-neon" font-size="10">TARGET</text>
        """
    elif state == "combat":
        content = f"""
        <text x="{x+10}" y="{y+20}" class="text-neon text-medal">LIVE CAM: ENGAGING HORDE</text>
        <!-- Barricade -->
        <rect x="{x+40}" y="{y+50}" width="15" height="60" fill="#285473" />
        <!-- Muzzle Flashes -->
        <line x1="{x+55}" y1="{y+60}" x2="{x+220}" y2="{y+60}" stroke="#39ff14" stroke-width="2" opacity="0">
            <animate attributeName="opacity" values="0;1;0;0" dur="0.2s" repeatCount="indefinite" />
        </line>
        <line x1="{x+55}" y1="{y+90}" x2="{x+220}" y2="{y+90}" stroke="#39ff14" stroke-width="2" opacity="0">
            <animate attributeName="opacity" values="0;0;0;1;0" dur="0.35s" repeatCount="indefinite" />
        </line>
        <!-- Zombies Approaching -->
        <circle cx="{x+230}" cy="{y+60}" r="5" fill="#ff003c">
             <animate attributeName="cx" values="{x+230};{x+60}" dur="1.5s" repeatCount="indefinite" />
        </circle>
        <circle cx="{x+200}" cy="{y+90}" r="5" fill="#ff003c">
             <animate attributeName="cx" values="{x+200};{x+60}" dur="2.1s" repeatCount="indefinite" />
        </circle>
        """
    elif state == "secure":
        content = f"""
        <text x="{x+10}" y="{y+20}" class="text-neon text-medal">LIVE CAM: SECTOR SECURE</text>
        <text x="{x+120}" y="{y+115}" class="text-neon" font-size="14" text-anchor="middle">
            <animate attributeName="opacity" values="1;0.3;1" dur="2s" repeatCount="indefinite" />
            CAMP ESTABLISHED
        </text>
        <!-- Campfire -->
        <polygon points="{x+110},{y+90} {x+120},{y+60} {x+130},{y+90}" fill="#ff8c00">
            <animate attributeName="points" values="{x+110},{y+90} {x+120},{y+60} {x+130},{y+90}; {x+110},{y+90} {x+120},{y+75} {x+130},{y+90}; {x+110},{y+90} {x+120},{y+60} {x+130},{y+90}" dur="0.6s" repeatCount="indefinite" />
        </polygon>
        <rect x="{x+105}" y="{y+90}" width="30" height="6" fill="#4a3b2c" />
        """
    return bg + content


def generate_pipboy_svg(days, streak, rank, survived, invaded, survival_day_count):
    svg_width = 900
    svg_height = 680
    
    today_data = days[-1]
    today_date = today_data['date']
    today_commits = today_data['contributionCount']
    random.seed(today_date)
    today_zombies = random.randint(1, 4)
    
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
        
        .past-0 {{ fill: #0d1117; stroke: #1a2332; stroke-width: 1; rx: 2; ry: 2; }}
        .past-1 {{ fill: #1c3242; rx: 2; ry: 2; }}
        .past-2 {{ fill: #285473; rx: 2; ry: 2; }}
        .past-3 {{ fill: #3679a6; rx: 2; ry: 2; }}
        .past-4 {{ fill: #459fdb; rx: 2; ry: 2; }}

        .game-survived-1 {{ fill: #1f6b11; rx: 2; ry: 2; }} 
        .game-survived-2 {{ fill: #2c9e17; rx: 2; ry: 2; }} 
        .game-survived-3 {{ fill: #39ff14; rx: 2; ry: 2; }} 
        
        .game-invaded-1 {{ fill: #8a0020; rx: 2; ry: 2; }}  
        .game-invaded-2 {{ fill: #ff003c; rx: 2; ry: 2; }}  

        @keyframes pulse-beacon {{
            0% {{ fill-opacity: 1; stroke: #ffffff; stroke-width: 1px; }}
            50% {{ fill-opacity: 0.4; stroke: #39ff14; stroke-width: 3px; }}
            100% {{ fill-opacity: 1; stroke: #ffffff; stroke-width: 1px; }}
        }}
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
    svg_content += f'<text x="25" y="95" class="text-neon text-info">RANK         : {rank.upper()}</text>\n'
    svg_content += f'<text x="400" y="75" class="text-neon text-info">STREAK       : {streak} DAYS</text>\n'
    svg_content += f'<text x="400" y="95" class="text-neon text-info">STATUS       : {survived} CLEARED / {invaded} INVADED</text>\n'
    
    svg_content += f'<rect x="25" y="115" width="850" height="30" class="intel-panel" />\n'
    svg_content += f'<text x="35" y="135" class="text-neon text-info">TODAY INTEL | INCOMING ZOMBIES: {today_zombies} | ELIMINATED: {today_commits} | STATUS: <tspan class="text-status">{today_status}</tspan></text>\n'

    box_size = 18 
    gap = 4
    start_x = 25
    start_y = 165 
    
    ticker_logs = [random.choice(MSG_GENERIC), random.choice(MSG_GENERIC)]
    
    for i, day in enumerate(days):
        week_idx = i // 7  
        day_idx = i % 7   
        
        if week_idx < 27:
            col = week_idx
            row = day_idx
        else:
            col = week_idx - 27
            row = day_idx + 7
        
        x = start_x + (col * (box_size + gap))
        y = start_y + (row * (box_size + gap))
        
        date_str = day['date']
        commits = day['contributionCount']
        
        if date_str < GAME_START_DATE:
            if commits == 0: color_class = "past-0"
            elif commits <= 2: color_class = "past-1"
            elif commits <= 4: color_class = "past-2"
            elif commits <= 6: color_class = "past-3"
            else: color_class = "past-4"
        else:
            random.seed(date_str)
            zombies = random.randint(1, 4)
            if commits >= zombies:
                fark = commits - zombies
                if fark == 0: 
                    color_class = "game-survived-1"
                    ticker_logs.append(random.choice(MSG_CLEARED).format(date=date_str, commits=commits))
                elif fark <= 2: 
                    color_class = "game-survived-2"
                    ticker_logs.append(random.choice(MSG_CLEARED).format(date=date_str, commits=commits))
                else: 
                    color_class = "game-survived-3"
                    ticker_logs.append(random.choice(MSG_OVERKILL).format(date=date_str, commits=commits))
            else:
                if commits > 0: 
                    color_class = "game-invaded-1"
                    ticker_logs.append(random.choice(MSG_FAILED).format(date=date_str, commits=commits))
                else: 
                    color_class = "game-invaded-2"
                    ticker_logs.append(random.choice(MSG_ZERO).format(date=date_str, commits=commits))
                
        extra_class = " current-day" if i == len(days) - 1 else ""
        svg_content += f'<rect x="{x}" y="{y}" width="{box_size}" height="{box_size}" class="{color_class}{extra_class}" />\n'
        
    # --- YENİ EKLENEN ANİMASYON PANELLERİ (SAĞ TARAF) ---
    # Map genişliği yaklaşık 600px tutuyor. Sağdaki 300px'lik alanı panellere ayırdık.
    live_cam_x = 635
    svg_content += get_live_cam_svg(cam_state, live_cam_x, 165)
    svg_content += get_radar_svg(live_cam_x, 315)


    medal_y = 510
    ranks_data = [
        {"name": "ROOKIE", "req": 1, "icon": "◆"},
        {"name": "SERGEANT", "req": 30, "icon": "▲▲▲"},
        {"name": "COMMANDER", "req": 100, "icon": "★"},
        {"name": "WAR HERO", "req": 365, "icon": "❂"}
    ]
    medal_box_width = 185
    medal_gap = 20
    start_medal_x = 25
    
    svg_content += f'<text x="25" y="495" class="text-neon text-medal">ACHIEVEMENTS &amp; MEDALS</text>\n'

    for idx, r_data in enumerate(ranks_data):
        m_x = start_medal_x + (idx * (medal_box_width + medal_gap))
        is_earned = streak >= r_data["req"]
        box_class = "box-medal-earned" if is_earned else "box-medal-locked"
        text_class = "text-neon" if is_earned else "text-dim"
        status_text = "[UNLOCKED]" if is_earned else f"[LOCKED: {r_data['req']} DAYS]"
        
        svg_content += f'<rect x="{m_x}" y="{medal_y}" width="{medal_box_width}" height="45" rx="3" ry="3" class="{box_class}" />\n'
        svg_content += f'<text x="{m_x + 10}" y="{medal_y + 18}" class="{text_class} text-medal">{r_data["icon"]} {r_data["name"]}</text>\n'
        svg_content += f'<text x="{m_x + 10}" y="{medal_y + 35}" class="{text_class} text-medal">{status_text}</text>\n'

    ticker_logs.append(random.choice(MSG_GENERIC))
    ticker_text = " /// ".join(ticker_logs) + " ///"
    text_width_px = len(ticker_text) * 8
    to_x_coord = -(text_width_px)
    animation_duration = max(30, int(len(ticker_text) * 0.05))
    
    svg_content += f"""
        <text y="610" class="text-neon text-info">
            <animate attributeName="x" from="{svg_width}" to="{to_x_coord}" dur="{animation_duration}s" repeatCount="indefinite" />
            {ticker_text}
        </text>
    </g>
    </svg>
    """
    
    with open("test_v2_graph.svg", "w", encoding="utf-8") as file:
        file.write(svg_content)
    print("[SUCCESS] Ana harita oluşturuldu: 'test_v2_graph.svg'")

def generate_animations_test():
    """Tüm animasyonları aynı anda görebilmen için özel şov dosyası"""
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" width="600" height="400">
    <style>
        .bg {{ fill: #050a05; }}
        .text-neon {{ fill: #39ff14; font-family: 'Courier New', Courier, monospace; font-weight: bold; font-size: 14px;}}
        .text-medal {{ font-size: 12px; }}
        .intel-panel {{ fill: rgba(13, 17, 23, 0.8); stroke: #1a4d1a; stroke-width: 1; rx: 4; ry: 4; }}
    </style>
    <rect width="100%" height="100%" class="bg" />
    <text x="20" y="30" class="text-neon">ANIMATION SHOWCASE ROOM</text>
    
    {get_live_cam_svg("en_route", 20, 50)}
    {get_live_cam_svg("combat", 280, 50)}
    {get_live_cam_svg("secure", 20, 210)}
    {get_radar_svg(280, 210)}
    </svg>
    """
    with open("test_animasyonlar.svg", "w", encoding="utf-8") as file:
        file.write(svg_content)
    print("[SUCCESS] Tüm animasyonları içeren şov dosyası oluşturuldu: 'test_animasyonlar.svg'")

if __name__ == "__main__":
    mock_days = generate_mock_data()
    start_date_obj = datetime.strptime(GAME_START_DATE, "%Y-%m-%d").date()
    latest_date_obj = datetime.strptime(mock_days[-1]['date'], "%Y-%m-%d").date()
    survival_day = max(0, (latest_date_obj - start_date_obj).days)

    generate_pipboy_svg(mock_days, streak=12, rank="ROOKIE", survived=0, invaded=0, survival_day_count=survival_day)
    
    # Yeni Animasyon Test Dosyasını Çalıştır
    generate_animations_test()