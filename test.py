import random
from datetime import datetime, date, timedelta
import sys

USERNAME = "ACHEXUS"
GAME_START_DATE = date.today().strftime("%Y-%m-%d")

MSG_OVERKILL = ["TARGET PRACTICE AT SECTOR {date}. OVERWHELMING FIREPOWER USED.", "THREAT NEUTRALIZED ON {date}. NO CASUALTIES REPORTED."]
MSG_CLEARED = ["CLOSE CALL ON {date}. PERIMETER BARELY SECURED.", "HAND-TO-HAND COMBAT ON {date}. WE HOLD THE LINE."]
MSG_FAILED = ["MAYDAY! BARRICADES BREACHED ON {date}!", "SECTOR {date} OVERRUN. WE TOOK DOWN {commits} BUT IT WAS NOT ENOUGH."]
MSG_ZERO = ["RADIO SILENCE ON {date}. SECTOR ASSUMED LOST.", "NO DEFENSIVE ACTION TAKEN ON {date}. WALKERS ROAM FREE."]
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

# --- GELİŞMİŞ ANİMASYON MODÜLLERİ ---
def get_radar_svg(remaining_zombies, x, y, width, height):
    cx = x + (width / 2)
    cy = y + 95 # Radarı biraz daha aşağı aldık
    
    # Sadece HAYATTA KALAN (vurulmamış) zombiler kadar nokta çiz
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
    
    if state == "en_route":
        content = f"""
        <text x="{x+15}" y="{y+25}" class="text-neon text-medal">LIVE CAM: SQUAD EN ROUTE</text>
        <!-- Kayan Yol (Hareket Hissi) -->
        <line x1="{x+10}" y1="{y+130}" x2="{x+width-10}" y2="{y+130}" stroke="#39ff14" stroke-dasharray="15, 10" stroke-width="2">
            <animate attributeName="stroke-dashoffset" from="25" to="0" dur="0.4s" repeatCount="indefinite" />
        </line>
        <!-- Zırhlı Araç -->
        <g>
            <animate attributeName="transform" type="translate" values="0,0; 0,2; 0,0" dur="0.2s" repeatCount="indefinite" />
            <path d="M {x+50} {y+110} L {x+70} {y+80} L {x+130} {y+80} L {x+150} {y+110} L {x+170} {y+110} L {x+170} {y+125} L {x+50} {y+125} Z" fill="#285473" />
            <rect x="{x+80}" y="{y+85}" width="20" height="15" fill="#0d1117" />
            <rect x="{x+110}" y="{y+85}" width="20" height="15" fill="#0d1117" />
            <!-- Tekerlekler -->
            <circle cx="{x+80}" cy="{y+125}" r="10" fill="#0d1117" stroke="#39ff14" stroke-width="2" />
            <circle cx="{x+140}" cy="{y+125}" r="10" fill="#0d1117" stroke="#39ff14" stroke-width="2" />
        </g>
        """
    elif state == "combat":
        content = f"""
        <text x="{x+15}" y="{y+25}" class="text-neon text-medal">LIVE CAM: THERMAL SCOPE (ENGAGING)</text>
        <!-- Termal Arka Plan -->
        <rect x="{x+10}" y="{y+40}" width="{width-20}" height="{height-50}" fill="#0a0a2a" rx="4" ry="4" />
        
        <!-- Termal Zombiler (Isı İmzası) -->
        <circle cx="{x+230}" cy="{y+100}" r="8" fill="#ff8c00" opacity="0.8">
             <animate attributeName="cx" values="{x+250};{x+40}" dur="4s" repeatCount="indefinite" />
             <animate attributeName="cy" values="{y+100};{y+95};{y+100}" dur="0.5s" repeatCount="indefinite" />
        </circle>
        <circle cx="{x+180}" cy="{y+120}" r="10" fill="#ff003c" opacity="0.9">
             <animate attributeName="cx" values="{x+250};{x+40}" dur="5s" repeatCount="indefinite" />
             <animate attributeName="cy" values="{y+120};{y+115};{y+120}" dur="0.7s" repeatCount="indefinite" />
        </circle>
        
        <!-- Sniper Dürbünü (Crosshair) & Geri Tepme (Recoil) -->
        <g stroke="#39ff14" stroke-width="1.5">
            <animate attributeName="transform" type="translate" values="0,0; -8,-8; 0,0; 0,0" dur="2.5s" keyTimes="0; 0.05; 0.15; 1" repeatCount="indefinite" />
            <circle cx="{x+(width/2)}" cy="{y+95}" r="45" fill="rgba(57,255,20,0.05)" />
            <line x1="{x+(width/2)-60}" y1="{y+95}" x2="{x+(width/2)+60}" y2="{y+95}" />
            <line x1="{x+(width/2)}" y1="{y+35}" x2="{x+(width/2)}" y2="{y+155}" />
            <!-- Merkez Lazer Noktası -->
            <circle cx="{x+(width/2)}" cy="{y+95}" r="2" fill="#ff003c" stroke="none">
                <animate attributeName="opacity" values="1;0;1" dur="2.5s" repeatCount="indefinite" />
            </circle>
        </g>
        """
    elif state == "secure":
        content = f"""
        <text x="{x+15}" y="{y+25}" class="text-neon text-medal">LIVE CAM: SECTOR SECURE (CITY)</text>
        
        <!-- Şehir Silüeti (Skyline) -->
        <path d="M {x+20} {y+145} L {x+20} {y+80} L {x+40} {y+80} L {x+40} {y+60} L {x+70} {y+60} L {x+70} {y+90} L {x+100} {y+90} L {x+100} {y+50} L {x+140} {y+50} L {x+140} {y+100} L {x+170} {y+100} L {x+170} {y+70} L {x+210} {y+70} L {x+210} {y+145} Z" fill="#1c3242" />
        
        <!-- Binalardaki Tek Tük Işıklar -->
        <rect x="{x+30}" y="{y+90}" width="4" height="4" fill="#39ff14" opacity="0.6" />
        <rect x="{x+80}" y="{y+100}" width="4" height="4" fill="#39ff14" opacity="0.6" />
        <rect x="{x+150}" y="{y+80}" width="4" height="4" fill="#39ff14" opacity="0.6" />
        
        <!-- Dönen Arama/Kurtarma Projektörü -->
        <polygon points="{x+120},{y+145} {x+40},{y+40} {x+200},{y+40}" fill="rgba(57, 255, 20, 0.15)">
            <animate attributeName="points" values="{x+120},{y+145} {x+40},{y+40} {x+200},{y+40}; {x+120},{y+145} {x+100},{y+30} {x+260},{y+30}; {x+120},{y+145} {x+40},{y+40} {x+200},{y+40}" dur="6s" repeatCount="indefinite" />
        </polygon>
        <text x="{x+132}" y="{y+130}" class="text-neon" font-size="12" text-anchor="middle">SAFE ZONE</text>
        """
    return bg + content


def generate_pipboy_svg(days, streak, rank, survived, invaded, survival_day_count):
    # --- YENİ: GENİŞLETİLMİŞ VE EŞİTLENMİŞ BOYUTLAR ---
    svg_width = 980
    svg_height = 740
    
    today_data = days[-1]
    today_date = today_data['date']
    today_commits = today_data['contributionCount']
    random.seed(today_date)
    today_zombies = random.randint(1, 4)
    
    remaining_zombies = max(0, today_zombies - today_commits)
    
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
    svg_content += f'<text x="450" y="75" class="text-neon text-info">STREAK       : {streak} DAYS</text>\n'
    svg_content += f'<text x="450" y="95" class="text-neon text-info">STATUS       : {survived} CLEARED / {invaded} INVADED</text>\n'
    
    svg_content += f'<rect x="25" y="115" width="930" height="30" class="intel-panel" />\n'
    svg_content += f'<text x="35" y="135" class="text-neon text-info">TODAY INTEL | INCOMING ZOMBIES: {today_zombies} | ELIMINATED: {today_commits} | STATUS: <tspan class="text-status">{today_status}</tspan></text>\n'

    # --- MATEMATİKSEL KUSURSUZ HARİTA HİZALAMASI ---
    box_size = 20 # Büyütüldü
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
        
    # --- YAN PANELLER (Alt Sınırları Harita ile Eşitlendi: 497. Pixel) ---
    panel_x = 690
    panel_width = 265
    panel_height = 164
    
    svg_content += get_live_cam_svg(cam_state, panel_x, 165, panel_width, panel_height)
    svg_content += get_radar_svg(remaining_zombies, panel_x, 337, panel_width, panel_height)


    # --- MADALYALAR AŞAĞI KAYDIRILDI ---
    medal_y = 540
    ranks_data = [
        {"name": "ROOKIE", "req": 1, "icon": "◆"},
        {"name": "SERGEANT", "req": 30, "icon": "▲▲▲"},
        {"name": "COMMANDER", "req": 100, "icon": "★"},
        {"name": "WAR HERO", "req": 365, "icon": "❂"}
    ]
    medal_box_width = 200
    medal_gap = 25
    start_medal_x = 25
    
    svg_content += f'<text x="25" y="525" class="text-neon text-medal">ACHIEVEMENTS &amp; MEDALS</text>\n'

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
        <text y="640" class="text-neon text-info">
            <animate attributeName="x" from="{svg_width}" to="{to_x_coord}" dur="{animation_duration}s" repeatCount="indefinite" />
            {ticker_text}
        </text>
    </g>
    </svg>
    """
    
    with open("test_v2_graph.svg", "w", encoding="utf-8") as file:
        file.write(svg_content)
    print("[SUCCESS] Hizalanmış Ana Harita oluşturuldu: 'test_v2_graph.svg'")

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
    
    {get_live_cam_svg("en_route", 20, 50, 265, 164)}
    {get_live_cam_svg("combat", 300, 50, 265, 164)}
    {get_live_cam_svg("secure", 20, 230, 265, 164)}
    {get_radar_svg(4, 300, 230, 265, 164)} 
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