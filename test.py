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

def generate_pipboy_svg(days, streak, rank, survived, invaded, survival_day_count):
    svg_width = 850
    svg_height = 650 # YENİ: Arayüz aşağıya doğru devasa genişletildi
    
    # --- YENİ: Bugünün Aksiyon ve Zombi Verileri (Intel) ---
    today_data = days[-1]
    today_date = today_data['date']
    today_commits = today_data['contributionCount']
    random.seed(today_date)
    today_zombies = random.randint(1, 4)
    
    if today_commits >= today_zombies:
        today_status = "SECURE (CLEARED)"
        status_color = "#39ff14" # Yeşil
    elif today_commits > 0:
        today_status = "BREACHED (HEAVY DAMAGE)"
        status_color = "#ff003c" # Kırmızı
    else:
        today_status = "CRITICAL (OVERRUN)"
        status_color = "#ff003c"

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
        .intel-panel {{ fill: rgba(13, 17, 23, 0.7); stroke: #1a4d1a; stroke-width: 1; rx: 4; ry: 4; }}
        
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

        /* YENİ: Bugünün yanıp sönen radarı */
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
    
    # --- YENİ: Taktiksel Günlük İstihbarat Paneli ---
    svg_content += f'<rect x="25" y="115" width="800" height="30" class="intel-panel" />\n'
    svg_content += f'<text x="35" y="135" class="text-neon text-info">TODAY INTEL | INCOMING ZOMBIES: {today_zombies} | ELIMINATED: {today_commits} | STATUS: <tspan class="text-status">{today_status}</tspan></text>\n'

    # --- YENİ: İkiye Bölünmüş, Büyütülmüş Harita (Radar) ---
    box_size = 14 # Kutular 12'den 14'e büyütüldü
    gap = 4
    start_x = 25
    
    start_y_alpha = 195 # İlk harita konumu
    start_y_omega = 355 # İkinci harita konumu
    
    svg_content += f'<text x="25" y="180" class="text-neon text-medal">SECTOR ALPHA (FIRST 6 MONTHS)</text>\n'
    svg_content += f'<text x="25" y="340" class="text-neon text-medal">SECTOR OMEGA (RECENT 6 MONTHS)</text>\n'

    ticker_logs = [random.choice(MSG_GENERIC), random.choice(MSG_GENERIC)]
    
    for i, day in enumerate(days):
        week_idx = i // 7  
        day_idx = i % 7   
        
        # Haritayı 27. Haftadan itibaren alt bloka taşıyoruz
        if week_idx < 27:
            x = start_x + (week_idx * (box_size + gap))
            y = start_y_alpha + (day_idx * (box_size + gap))
        else:
            x = start_x + ((week_idx - 27) * (box_size + gap))
            y = start_y_omega + (day_idx * (box_size + gap))
        
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
                
        # Eğer bu çizilen kutu SON GÜN ise ona 'current-day' animasyon class'ını ekliyoruz
        extra_class = " current-day" if i == len(days) - 1 else ""
        svg_content += f'<rect x="{x}" y="{y}" width="{box_size}" height="{box_size}" class="{color_class}{extra_class}" />\n'
        
    # --- YENİ: Genişletilmiş Badgeler ---
    medal_y = 520
    ranks_data = [
        {"name": "ROOKIE", "req": 1, "icon": "◆"},
        {"name": "SERGEANT", "req": 30, "icon": "▲▲▲"},
        {"name": "COMMANDER", "req": 100, "icon": "★"},
        {"name": "SHARPSHOOTER", "req": 180, "icon": "⌖"}, # YENİ RÜTBE EKLENDİ
        {"name": "WAR HERO", "req": 365, "icon": "❂"}
    ]
    
    # 5 Madalya sığması için ölçüleri güncelledik
    medal_box_width = 150
    medal_gap = 12
    start_medal_x = 25
    
    svg_content += f'<text x="25" y="505" class="text-neon text-medal">ACHIEVEMENTS &amp; MEDALS</text>\n'

    for idx, r_data in enumerate(ranks_data):
        m_x = start_medal_x + (idx * (medal_box_width + medal_gap))
        is_earned = streak >= r_data["req"]
        box_class = "box-medal-earned" if is_earned else "box-medal-locked"
        text_class = "text-neon" if is_earned else "text-dim"
        status_text = "[UNLOCKED]" if is_earned else f"[LOCKED: {r_data['req']}D]"
        
        svg_content += f'<rect x="{m_x}" y="{medal_y}" width="{medal_box_width}" height="45" rx="3" ry="3" class="{box_class}" />\n'
        svg_content += f'<text x="{m_x + 10}" y="{medal_y + 18}" class="{text_class} text-medal">{r_data["icon"]} {r_data["name"]}</text>\n'
        svg_content += f'<text x="{m_x + 10}" y="{medal_y + 35}" class="{text_class} text-medal">{status_text}</text>\n'

    ticker_logs.append(random.choice(MSG_GENERIC))
    ticker_text = " /// ".join(ticker_logs) + " ///"
    text_width_px = len(ticker_text) * 8
    to_x_coord = -(text_width_px)
    animation_duration = max(30, int(len(ticker_text) * 0.05))
    
    svg_content += f"""
        <text y="620" class="text-neon text-info">
            <animate attributeName="x" from="{svg_width}" to="{to_x_coord}" dur="{animation_duration}s" repeatCount="indefinite" />
            {ticker_text}
        </text>
    </g>
    </svg>
    """
    
    with open("test_v2_graph.svg", "w", encoding="utf-8") as file:
        file.write(svg_content)
    print("\n[SUCCESS] v0.2.0 UI Genişletme Testi tamamlandı: 'test_v2_graph.svg'")

if __name__ == "__main__":
    mock_days = generate_mock_data()
    
    start_date_obj = datetime.strptime(GAME_START_DATE, "%Y-%m-%d").date()
    latest_date_obj = datetime.strptime(mock_days[-1]['date'], "%Y-%m-%d").date()
    survival_day = max(0, (latest_date_obj - start_date_obj).days)

    generate_pipboy_svg(mock_days, streak=12, rank="ROOKIE", survived=0, invaded=0, survival_day_count=survival_day)