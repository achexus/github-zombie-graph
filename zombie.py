import os
import requests
import random
import time
import sys
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("GITHUB_TOKEN")
USERNAME = os.getenv("GITHUB_USERNAME", "SURVIVOR")
GAME_START_DATE = "2026-08-15"

MSG_OVERKILL = [
    "TARGET PRACTICE AT SECTOR {date}. OVERWHELMING FIREPOWER USED.",
    "THREAT NEUTRALIZED ON {date}. NO CASUALTIES REPORTED.",
    "CLEAN SWEEP. {commits} HITS CONFIRMED ON {date}.",
    "ZOMBIE HORDE OBLITERATED AT {date}. EXCELLENT WORK COMMANDER.",
    "RADAR CLEAR AT {date}. ENEMY STRENGTH WAS PATHETIC."
]
MSG_CLEARED = [
    "CLOSE CALL ON {date}. PERIMETER BARELY SECURED.",
    "HAND-TO-HAND COMBAT ON {date}. WE HOLD THE LINE.",
    "SECTOR {date} CLEAR BUT AMMO IS RUNNING DANGEROUSLY LOW.",
    "DEFENSES HELD ON {date}. REINFORCING GATES NOW.",
    "NARROW ESCAPE AT {date}. NO ROOM FOR ERROR."
]
MSG_FAILED = [
    "MAYDAY! BARRICADES BREACHED ON {date}!",
    "SECTOR {date} OVERRUN. WE TOOK DOWN {commits} BUT IT WAS NOT ENOUGH.",
    "DEFENSE FAILED AT {date}. FALLING BACK TO INNER SECTOR.",
    "TOO MANY OF THEM ON {date}! REQUESTING IMMEDIATE BACKUP!",
    "CASUALTIES REPORTED ON {date}. UNABLE TO HOLD PERIMETER."
]
MSG_ZERO = [
    "RADIO SILENCE ON {date}. SECTOR ASSUMED LOST.",
    "NO DEFENSIVE ACTION TAKEN ON {date}. WALKERS ROAM FREE.",
    "CAMERAS SHOW HEAVY INFESTATION AT {date}. NO RESISTANCE.",
    "GHOST TOWN AT SECTOR {date}. WHERE IS EVERYONE?",
    "ZERO COMMITS ON {date}. SEVERE VULNERABILITY DETECTED."
]
MSG_GENERIC = [
    "STATIC... ADJUSTING FREQUENCY...",
    "OUTPOST ALPHA REPORTING ALL CLEAR...",
    "HEARING MOANS FROM THE EASTERN WOODS...",
    "SUPPLY DROP COORDINATES UPDATED...",
    "CHECKING GEIGER COUNTERS. RADIATION NORMAL..."
]

query = f"""
query {{
  user(login: "{USERNAME}") {{
    contributionsCollection {{
      contributionCalendar {{
        totalContributions
        weeks {{
          contributionDays {{
            contributionCount
            date
          }}
        }}
      }}
    }}
  }}
}}
"""

def get_contribution_data():
    url = 'https://api.github.com/graphql'
    headers = {
        'Authorization': f'Bearer {TOKEN}',
        'Content-Type': 'application/json'
    }
    response = requests.post(url, json={'query': query}, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if 'errors' in data: return None
        weeks = data['data']['user']['contributionsCollection']['contributionCalendar']['weeks']
        days = []
        for week in weeks:
            for day in week['contributionDays']:
                days.append(day)
        return days
    return None

def generate_pipboy_svg(days, streak, rank, survived, invaded, active_day_count):
    svg_width = 850
    svg_height = 380
    
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{svg_width}" height="{svg_height}">
    <style>
        .bg {{ fill: #050a05; }}
        .scanline {{ stroke: rgba(57, 255, 20, 0.10); stroke-width: 1; }}
        .text-neon {{ fill: #39ff14; font-family: 'Courier New', Courier, monospace; font-weight: bold; }}
        .text-dim {{ fill: #1a4d1a; font-family: 'Courier New', Courier, monospace; font-weight: bold; }}
        .text-title {{ font-size: 22px; }}
        .text-info {{ font-size: 14px; }}
        .text-medal {{ font-size: 12px; }}
        
        .box-medal-earned {{ fill: rgba(57, 255, 20, 0.05); stroke: #39ff14; stroke-width: 1; }}
        .box-medal-locked {{ fill: transparent; stroke: #1a4d1a; stroke-width: 1; stroke-dasharray: 4; }}
        
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
    svg_content += f'<text x="25" y="75" class="text-neon text-info">SURVIVAL DAY : {active_day_count}</text>\n'
    svg_content += f'<text x="25" y="95" class="text-neon text-info">RANK         : {rank.upper()}</text>\n'
    svg_content += f'<text x="400" y="75" class="text-neon text-info">STREAK       : {streak} DAYS</text>\n'
    svg_content += f'<text x="400" y="95" class="text-neon text-info">STATUS       : {survived} CLEARED / {invaded} INVADED</text>\n'
    
    box_size = 12
    gap = 3
    start_x = 25
    start_y = 130
    
    ticker_logs = [random.choice(MSG_GENERIC), random.choice(MSG_GENERIC)]
    
    for i, day in enumerate(days):
        col = i // 7  
        row = i % 7   
        x = start_x + (col * (box_size + gap))
        y = start_y + (row * (box_size + gap))
        
        date = day['date']
        commits = day['contributionCount']
        
        if date < GAME_START_DATE:
            if commits == 0: color_class = "past-0"
            elif commits <= 2: color_class = "past-1"
            elif commits <= 4: color_class = "past-2"
            elif commits <= 6: color_class = "past-3"
            else: color_class = "past-4"
        else:
            random.seed(date)
            zombies = random.randint(1, 4)
            if commits >= zombies:
                fark = commits - zombies
                if fark == 0: 
                    color_class = "game-survived-1"
                    ticker_logs.append(random.choice(MSG_CLEARED).format(date=date, commits=commits))
                elif fark <= 2: 
                    color_class = "game-survived-2"
                    ticker_logs.append(random.choice(MSG_CLEARED).format(date=date, commits=commits))
                else: 
                    color_class = "game-survived-3"
                    ticker_logs.append(random.choice(MSG_OVERKILL).format(date=date, commits=commits))
            else:
                if commits > 0: 
                    color_class = "game-invaded-1"
                    ticker_logs.append(random.choice(MSG_FAILED).format(date=date, commits=commits))
                else: 
                    color_class = "game-invaded-2"
                    ticker_logs.append(random.choice(MSG_ZERO).format(date=date, commits=commits))
                
        svg_content += f'<rect x="{x}" y="{y}" width="{box_size}" height="{box_size}" class="{color_class}" />\n'
        
    medal_y = 260
    ranks_data = [
        {"name": "ROOKIE", "req": 1, "icon": "◆"},
        {"name": "SERGEANT", "req": 30, "icon": "▲▲▲"},
        {"name": "COMMANDER", "req": 100, "icon": "★"},
        {"name": "WAR HERO", "req": 365, "icon": "❂"}
    ]
    medal_box_width = 185
    medal_gap = 20
    start_medal_x = 25
    
    svg_content += f'<text x="25" y="245" class="text-neon text-medal">ACHIEVEMENTS &amp; MEDALS</text>\n'

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
        <text y="350" class="text-neon text-info">
            <animate attributeName="x" from="{svg_width}" to="{to_x_coord}" dur="{animation_duration}s" repeatCount="indefinite" />
            {ticker_text}
        </text>
    </g>
    </svg>
    """
    
    # Dosyayı zombi-grafik.svg olarak kaydediyoruz
    with open("zombi-grafik.svg", "w", encoding="utf-8") as file:
        file.write(svg_content)

def simulate_zombie_survival(days):
    active_days = [day for day in days if day['date'] >= GAME_START_DATE]
    if not active_days: return

    streak = 0
    for i, day in enumerate(reversed(active_days)):
        if day['contributionCount'] > 0: streak += 1
        elif i == 0 and day['contributionCount'] == 0: continue
        else: break
            
    if streak >= 365: rank = "WAR HERO"
    elif streak >= 100: rank = "COMMANDER"
    elif streak >= 30: rank = "SERGEANT"
    elif streak > 0: rank = "ROOKIE"
    else: rank = "LOST CIVILIAN"
    
    total_survived = sum(1 for d in active_days if d['contributionCount'] >= (random.seed(d['date']) or random.randint(1,4)))
    total_invaded = len(active_days) - total_survived
    
    generate_pipboy_svg(days, streak, rank, total_survived, total_invaded, len(active_days))

if __name__ == "__main__":
    github_data = get_contribution_data()
    if github_data:
        simulate_zombie_survival(github_data)