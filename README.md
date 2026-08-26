
Gemini

Chat

Spark
beta
New chat
Search chats
Images
Videos
Library
Gems
New notebook
Numerical Methods for Computer Engineering: Introduction and Applications
Lojik Devreler
1.0.0 Versiyonu Güncellemeleri ve Rütbe Mantığı
Diferansiyel Denklemlerde Temel Kavramlar
Eylül 2026 - Haziran 2027 Excel Takvimi
Etkinlik Takvimi Chatbot Projesi
GitHub Trafiğinde Cloners Anlamı
Yönetim Kurulu İçin Kurumsal Unvan Önerileri
Erciyes Çip Topluluğu Uygulama Önerisi
Kenar Alma Aleti Kullanımı
Deri İşleme Seti Aletleri Tanıtımı
Komik ve Ağırbaşlı Animasyon Karakterleri
Kült Fantastik ve Animasyon Yapımları
Professional Engineering Bio Translation
LinkedIn Özet Taslağı ve Rehberi
Göz Reçetesi Yorumu: Hipermetropi ve Astigmatizma
Port Trafiğini Kopyalama ve Analiz
GitHub Actions Commit Veri Çekmeme Sorunu
Günün Sonu ve Comm Beklentisi
SVG Görselinin Neden Görüntülenmediği
GitHub Kod Kullanımını İzleme Yöntemleri
GitHub Actions ile Zombie Grafiği
Çok Dilli README Dosyası Oluşturma
README Dil Seçenekleri İçin Çözümler
Kablosuz Kulaklık Karşılaştırması ve Seçim Rehberi
GitHub Profil Özelleştirme Araçları Listesi
GitHub Profil Tasarımı İçin Fikirler
Türkiye'de Gamepad Üretimi Durumu
Yükseklik Haritası Veri Yaratıcılığı
LinkedIn İş İlanları Otomasyonu Geliştirme
Topluluk Projeleri İçin Entegre Tasarım
Conversation with Gemini
bunun için ne demem lazım git kodu olarak terminale

Terminaldeki hata mesajı yine senin için hayat kurtarmış! Git, tam olarak şunu söylüyor: "Şu an main dalındasın ama henüz kaydetmediğin bazı çalışmaların var (zombie-graph.svg değiştirilmiş ve test.py isimli yeni bir dosya oluşturulmuş). Eğer seni test dalına geçirirsem bu dosyaları ezmek ve silmek zorunda kalırım, o yüzden işlemi iptal ediyorum."

Git, senin yazdığın o güzelim simülasyon kodlarını kazara kaybetmemen için sistemi kilitliyor. Bu değişiklikleri silmeden, güvenli bir şekilde test branch'ine taşımak için Git'in "Stash" (Geçici Zula) özelliğini kullanacağız.

VS Code terminaline sırasıyla şu komutları gir:

1. Çalışmalarını (yeni eklenen dosyalar dahil) geçici bir hafızaya al:

Bash
git stash -u
2. Artık ortalık temizlendiğine göre güvenle test branch'ine geçiş yap:

Bash
git switch test
3. Hafızaya aldığımız o güncel çalışmaları test branch'ine geri dök:

Bash
git stash pop
(Ufak bir not: 3. komutu çalıştırdığında test.py dosyası için bir çakışma (conflict) uyarısı alabilirsin çünkü eski test branch'inde de bir test.py vardı. Eğer ekranında garip yazılar çıkarsa hiç dert etme; test.py dosyasının içini tamamen silip, bir önceki mesajımda verdiğim o "TEST ORTAMI" simülasyon kodunu tekrar yapıştırman ve kaydetmen yeterli olacaktır.)

Bu adımları uyguladıktan sonra tamamen test dalında ve kaldığımız yerde olacaksın!

direktmen başlama günü muhabbetini kaldıralım. çekilen verilere göre kişinin statları yazsın. 0 commit günlerde survival day sıfırlansın şeklinde test1 test 2 test 3 şeklinde de 3 tane farklı veriseti ile 3 farklı dosyla oluştur nasıl görünüyor test edelim.

Bu gerçekten muazzam bir fikir! Başlangıç tarihi (start date) ve JSON state dosyasını tamamen ortadan kaldırmak, bu projeyi teknik olarak bir başyapıta dönüştürür. GitHub Actions'ın "Stateless" (durumsuz/geçici) doğasına %100 uyan, kurşun geçirmez bir sisteme geçmiş olacağız.

Senin fikrinden yola çıkarak algoritmayı şu şekilde harika bir yapıya büründürdüm:

Hayatta Kalma Serisi (Streak Sistemi): Artık "Survival Day" bir sayaç değil, senin aktif serin (streak) olacak. Her commit attığında seri uzayacak, 0 commit attığın an seri sıfırlanacak (Streak Broken). Bu, kullanıcıları her gün kod yazmaya (hayatta kalmaya) çok daha fazla teşvik edecek!

Kıpkırmızı Ekran Kâbusunu Çözdüm: Eğer tüm geçmişi zombi oyunu sayarsak, çok sık kod yazmayan birinin ekranı 300 tane kırmızı (İstila) kutuyla dolar ve çok çirkin görünürdü. Bunun yerine kod, çekilen veri içerisindeki "İlk Commit Attığın Günü" zombi istilasının başlangıcı olarak kabul edecek. O günden öncesi klasik GitHub grisi, o günden sonrası ise kıyasıya hayatta kalma mücadelesi olacak!

Aşağıdaki test.py kodunu çalıştırdığında sana tam 3 farklı senaryoya ait 3 farklı SVG dosyası üretecek.

Lütfen şu anki test.py dosyanın içini tamamen sil ve bu kodu yapıştırıp çalıştır:

Python
import random
import math
from datetime import datetime, timedelta

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

def get_zombie_count_for_date(date_str):
    r = random.Random(date_str)
    return r.randint(1, 4)

def calculate_level_info(total_commits):
    if total_commits == 0:
        return 0, 0, 1
    level = int((math.sqrt(8 * total_commits + 1) - 1) / 2)
    current_level_base_xp = (level * (level + 1)) // 2
    next_level_base_xp = ((level + 1) * (level + 2)) // 2
    
    current_xp_in_level = total_commits - current_level_base_xp
    xp_needed_for_next = next_level_base_xp - current_level_base_xp
    return level, current_xp_in_level, xp_needed_for_next

# ==========================================
# TEST VERİSETİ OLUŞTURUCULAR
# ==========================================
def generate_mock_days(scenario_type):
    days = []
    end_date = datetime.strptime("2026-08-24", "%Y-%m-%d")
    start_date = end_date - timedelta(days=377)
    
    current_date = start_date
    while current_date <= end_date:
        date_str = current_date.strftime("%Y-%m-%d")
        commits = 0
        
        days_from_end = (end_date - current_date).days
        
        if scenario_type == 1:
            # TEST 1: VETERAN SURVIVOR (Son 30 gündür hiç kaçırmamış, harika bir seri)
            if days_from_end < 30:
                commits = random.randint(2, 6)
            elif days_from_end % 3 == 0 and days_from_end < 150:
                commits = random.randint(1, 3)
                
        elif scenario_type == 2:
            # TEST 2: FALLEN HERO (Geçmişi çok iyi ama dün commit atmamış, serisi DÜN SIFIRLANMIŞ)
            if days_from_end > 2 and days_from_end < 60:
                commits = random.randint(1, 5)
            elif days_from_end == 1: # Dün
                commits = 0
            elif days_from_end == 0: # Bugün
                commits = 2
                
        elif scenario_type == 3:
            # TEST 3: ROOKIE / GHOST (Neredeyse 1 yıldır yok, sadece son 3 gündür kod yazıyor)
            if days_from_end <= 3:
                commits = random.randint(1, 3)
            else:
                commits = 0

        days.append({"date": date_str, "contributionCount": commits})
        current_date += timedelta(days=1)
        
    return days

# ==========================================
# SVG BİLEŞENLERİ
# ==========================================
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
    else:
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

# ==========================================
# ANA ÇİZİM FONKSİYONU
# ==========================================
def generate_pipboy_svg(days, level, xp_current, xp_needed, survived, invaded, current_streak, total_commits, first_active_date, output_filename, scenario_name):
    svg_width = 980
    svg_height = 740
    
    day_map = {d['date']: d['contributionCount'] for d in days}
    today_str = days[-1]['date']
    
    today_commits = day_map.get(today_str, 0)
    today_zombies = get_zombie_count_for_date(today_str) if today_str >= first_active_date else 0
    remaining_zombies = max(0, today_zombies - today_commits)
    
    if today_str < first_active_date:
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

    current_msgs = MSG_SECURE if cam_state == "secure" else (MSG_COMBAT if cam_state == "combat" else MSG_EN_ROUTE)
    
    current_rank_idx = -1
    for i, (req, name, icon) in enumerate(ORDERED_RANKS):
        if level >= req:
            current_rank_idx = i
            
    active_rank_name = "UNRANKED" if current_rank_idx == -1 else ORDERED_RANKS[current_rank_idx][1]

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
        
    svg_content += f'<text x="25" y="40" class="text-neon text-title">ACHEXUS SURVIVAL SYSTEM [{scenario_name}]</text>\n'
    svg_content += f'<text x="25" y="75" class="text-neon text-info">ACTIVE STREAK: {current_streak} DAYS</text>\n'
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
            
            # YENİ MANTIK: Sadece ilk aktif günden sonrakiler zombi istilası sayılır.
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
    svg_content += get_live_cam_svg(cam_state, panel_x, 165, panel_width, panel_height)
    svg_content += get_radar_svg(remaining_zombies, panel_x, 337, panel_width, panel_height)

    # -------------------------------------------------------------
    # KAYAN RÜTBE SİSTEMİ
    # -------------------------------------------------------------
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

    # -------------------------------------------------------------
    # TERMINAL STYLE LOADING (XP) BAR
    # -------------------------------------------------------------
    xp_bar_y = 615
    total_blocks = 77
    block_width = 10
    block_gap = 2
    bar_x = 25
    bar_width = (total_blocks * (block_width + block_gap)) + 2
    
    svg_content += f'<text x="25" y="{xp_bar_y + 10}" class="text-neon text-info">SYSTEM UPGRADE PROGRESS</text>\n'
    svg_content += f'<text x="{bar_x + bar_width}" y="{xp_bar_y + 10}" class="text-neon text-info" text-anchor="end">{xp_current} / {xp_needed} XP TO LVL {level + 1}</text>\n'
    
    svg_content += f'<rect x="{bar_x}" y="{xp_bar_y + 17}" width="{bar_width}" height="20" fill="none" stroke="#1a4d1a" stroke-width="1.5" />\n'
    
    if xp_needed > 0: fill_count = int(round((xp_current / xp_needed) * total_blocks))
    else: fill_count = 0
        
    for i in range(total_blocks):
        b_x = bar_x + 2 + i * (block_width + block_gap)
        b_y = xp_bar_y + 20
        
        if i < fill_count:
            if i == fill_count - 1:
                svg_content += f'<rect x="{b_x}" y="{b_y}" width="{block_width}" height="14" fill="#39ff14">\n'
                svg_content += f'    <animate attributeName="opacity" values="1;0.2;1" dur="0.8s" repeatCount="indefinite" />\n'
                svg_content += f'</rect>\n'
            else:
                svg_content += f'<rect x="{b_x}" y="{b_y}" width="{block_width}" height="14" fill="#39ff14" />\n'

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
    
    with open(output_filename, "w", encoding="utf-8") as file:
        file.write(svg_content)
    print(f"[SUCCESS] Grafik oluşturuldu: '{output_filename}' ({scenario_name})")

def run_simulation(scenario_type, filename, scenario_name):
    days = generate_mock_days(scenario_type)
    today_str = days[-1]['date']
    
    # 1. YENİ MANTIK: Kullanıcının grafikteki İLK aktif olduğu günü bul (Start date gerektirmez!)
    first_active_date = None
    for d in days:
        if d['contributionCount'] > 0:
            first_active_date = d['date']
            break
            
    if not first_active_date: 
        first_active_date = today_str # Eğer hayatı boyunca hiç commit atmadıysa
        
    # 2. YENİ MANTIK: Hayatta Kalma Serisi (Streak) - Sıfırlanan Sayaç
    current_streak = 0
    for d in days:
        if d['date'] > today_str:
            break
        if d['contributionCount'] > 0:
            current_streak += 1
        else:
            current_streak = 0 # 0 COMMIT GÜNÜNDE SERİ SIFIRLANIR!

    # İstatistikleri hesapla
    total_survived = 0
    total_invaded = 0
    total_commits = 0
    
    active_days = [day for day in days if day['date'] >= first_active_date]
    
    for d in active_days:
        date_str = d['date']
        if date_str >= today_str: continue # Bugünün sonucu henüz belli değil
        
        commits = d['contributionCount']
        total_commits += commits
        
        zombies = get_zombie_count_for_date(date_str)
        if commits >= zombies: total_survived += 1
        else: total_invaded += 1 

    # Bugünün commitlerini de XP'ye dahil et
    today_commits = next((d['contributionCount'] for d in days if d['date'] == today_str), 0)
    total_commits += today_commits

    level, xp_current, xp_needed = calculate_level_info(total_commits)
    
    generate_pipboy_svg(days, level, xp_current, xp_needed, total_survived, total_invaded, current_streak, total_commits, first_active_date, filename, scenario_name)

if __name__ == "__main__":
    print(f"\n--- 3 FARKLI SENARYO TESTİ BAŞLIYOR ---\n")
    
    run_simulation(1, "test1_veteran.svg", "TEST 1: VETERAN (30 Days Active)")
    run_simulation(2, "test2_fallen_hero.svg", "TEST 2: FALLEN HERO (Streak Broken Yesterday)")
    run_simulation(3, "test3_rookie.svg", "TEST 3: ROOKIE / GHOST (Just Started 3 Days Ago)")
    
    print(f"\n--- TEST TAMAMLANDI. Dosyaları VS Code üzerinden inceleyebilirsin! ---")
Bu kodu çalıştırdığında VS Code dizininde 3 adet yeni SVG belirecek:

test1_veteran.svg: 30 gündür aralıksız kod yazan birinin 30 günlük serisini (Streak) ve yemyeşil haritasını göreceksin.

test2_fallen_hero.svg: Daha önce çok iyi commitler atmış ama dün commit atmadığı için serisi 0'lanmış birinin acı tablosunu göreceksin (Streak: 1 olacak, çünkü sadece bugün commit atmış).

test3_rookie.svg: Koskoca bir yıl boyunca hiç kod yazmamış, sadece son 3 gündür kod yazan birinin haritası. Eski günler saçma sapan kırmızı zombi istilası yerine temiz gri renkte (Standby) görünecek.

Senaryoları incele, eğer bu yeni ve devrimsel algoritma (Streak + İlk Aktif Gün) içine sinerse bunu direkt ana sürüme entegre edeceğiz!

arayüzde aktive streak yazmasın survival day olarak kalmasını isterim. gereksiz hataları da ayıkla

Testlerdeki mantığın hoşuna gitmesine sevindim! O "ACTIVE STREAK" yazısını hemen orijinal ruhuna sadık kalarak "SURVIVAL DAY" olarak geri değiştirdim.

Ayrıca kodda gizlenen çok kritik bir "Sabah Sıfırlanması" (Morning Reset) hatasını da ayıkladım:
Eski mantıkta eğer sabah kalkıp GitHub'a baksaydın ve henüz o gün commit atmadıysan, kod dünü unutup "Bugün 0 commit, seriyi sıfırla!" diyordu. Bunu düzelttim! Artık seri (Survival Day) sadece geçmiş günlerde commit atmazsan sıfırlanıyor. Bugün henüz bitmediği için, bugün 0 commit olsan bile dünkü serin ekranda korunmaya devam edecek.

Artık JSON dosyasına, state tutmaya veya karmaşık veritabanlarına ihtiyacımız yok. Bu, projenin en kusursuz, hatasız ve nihai ana kodudur.

Aşağıdaki kodu doğrudan ana projedeki zombie.py dosyana yapıştırabilirsin:

Python
import os
import requests
import random
import math
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("GITHUB_TOKEN")
USERNAME = os.getenv("GITHUB_USERNAME", os.getenv("GITHUB_REPOSITORY_OWNER", "achexus"))

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

def get_zombie_count_for_date(date_str):
    # Zombiler artık tarihe göre matematiksel olarak hesaplanır (JSON state'e gerek kalmadı)
    r = random.Random(date_str)
    return r.randint(1, 4)

def calculate_level_info(total_commits):
    if total_commits == 0:
        return 0, 0, 1
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

def get_live_cam_svg(state, x, y, width, height, is_easter_egg=False):
    bg = f'<rect x="{x}" y="{y}" width="{width}" height="{height}" class="intel-panel" />'
    
    blink_dur = "0.2s" if is_easter_egg else "1.5s"
    
    live_header = f"""
    <circle cx="{x+18}" cy="{y+20}" r="4" fill="#ff003c">
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
    else:
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

def generate_pipboy_svg(days, level, xp_current, xp_needed, survived, invaded, survival_day, total_commits, first_active_date):
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
    
    if is_easter_egg:
        today_status = "FATAL EXCEPTION 0x00000064"
        status_color = "#ff00ff"
        current_msgs = ["SYSTEM FAILURE", "CORRUPTED DATA", "WHO ARE WE?", "LOST IN THE GRID"]

    current_rank_idx = -1
    for i, (req, name, icon) in enumerate(ORDERED_RANKS):
        if level >= req:
            current_rank_idx = i
            
    if current_rank_idx == -1:
        active_rank_name = "UNRANKED"
    else:
        active_rank_name = ORDERED_RANKS[current_rank_idx][1]
        
    if is_easter_egg:
        active_rank_name = "KAYBOLMUŞ"

    screen_class = "screen easter-egg" if is_easter_egg else "screen"

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
        
        @keyframes extreme-glitch {{
            0%   {{ transform: translate(0, 0); opacity: 0.9; }}
            10%  {{ transform: translate(-5px, 5px); opacity: 0.5; filter: hue-rotate(90deg); }}
            20%  {{ transform: translate(5px, -5px); opacity: 1.0; }}
            30%  {{ transform: translate(-5px, -5px); opacity: 0.4; filter: hue-rotate(-90deg); }}
            40%  {{ transform: translate(5px, 5px); opacity: 0.9; }}
            50%  {{ transform: translate(-2px, 2px); opacity: 0.6; filter: hue-rotate(180deg); }}
            60%  {{ transform: translate(2px, -2px); opacity: 1.0; }}
            70%  {{ transform: translate(-2px, -2px); opacity: 0.5; filter: hue-rotate(-180deg); }}
            80%  {{ transform: translate(2px, 2px); opacity: 0.9; }}
            90%  {{ transform: translate(0, 0); opacity: 0.7; filter: hue-rotate(45deg); }}
            100% {{ transform: translate(0, 0); opacity: 0.9; }}
        }}
        .easter-egg {{ animation: extreme-glitch 0.15s infinite !important; }}
    </style>
    <rect width="{svg_width}" height="{svg_height}" class="bg" />
    <g class="{screen_class}">
    """
    
    for y in range(0, svg_height, 4):
        svg_content += f'<line x1="0" y1="{y}" x2="{svg_width}" y2="{y}" class="scanline" />\n'
        
    svg_content += f'<text x="25" y="40" class="text-neon text-title">{USERNAME.upper()} SURVIVAL SYSTEM</text>\n'
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
            
            # Sadece ilk commit gününden sonrakiler zombi istilası sayılır
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
            
            if is_easter_egg:
                dur = round(random.uniform(0.1, 0.4), 2)
                anim = f'<animate attributeName="fill" values="#ff003c;#39ff14;#ff8c00;#0d1117;#00ffff;#ff00ff" dur="{dur}s" repeatCount="indefinite" />'
                svg_content += f'<rect x="{x}" y="{y}" width="{box_size}" height="{box_size}" class="{color_class}{extra_class}">{anim}</rect>\n'
            else:
                svg_content += f'<rect x="{x}" y="{y}" width="{box_size}" height="{box_size}" class="{color_class}{extra_class}" />\n'
        else:
            svg_content += f'<rect x="{x}" y="{y}" width="{box_size}" height="{box_size}" class="fog-of-war" />\n'
        
    panel_x, panel_width, panel_height = 690, 265, 164
    svg_content += get_live_cam_svg(cam_state, panel_x, 165, panel_width, panel_height, is_easter_egg)
    svg_content += get_radar_svg(remaining_zombies, panel_x, 337, panel_width, panel_height)

    # -------------------------------------------------------------
    # KAYAN RÜTBE SİSTEMİ
    # -------------------------------------------------------------
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

    # -------------------------------------------------------------
    # TERMINAL STYLE LOADING (XP) BAR
    # -------------------------------------------------------------
    if not is_easter_egg:
        xp_bar_y = 615
        total_blocks = 77
        block_width = 10
        block_gap = 2
        bar_x = 25
        bar_width = (total_blocks * (block_width + block_gap)) + 2
        
        svg_content += f'<text x="25" y="{xp_bar_y + 10}" class="text-neon text-info">SYSTEM UPGRADE PROGRESS</text>\n'
        svg_content += f'<text x="{bar_x + bar_width}" y="{xp_bar_y + 10}" class="text-neon text-info" text-anchor="end">{xp_current} / {xp_needed} XP TO LVL {level + 1}</text>\n'
        
        svg_content += f'<rect x="{bar_x}" y="{xp_bar_y + 17}" width="{bar_width}" height="20" fill="none" stroke="#1a4d1a" stroke-width="1.5" />\n'
        
        if xp_needed > 0: fill_count = int(round((xp_current / xp_needed) * total_blocks))
        else: fill_count = 0
            
        for i in range(total_blocks):
            b_x = bar_x + 2 + i * (block_width + block_gap)
            b_y = xp_bar_y + 20
            
            if i < fill_count:
                if i == fill_count - 1:
                    svg_content += f'<rect x="{b_x}" y="{b_y}" width="{block_width}" height="14" fill="#39ff14">\n'
                    svg_content += f'    <animate attributeName="opacity" values="1;0.2;1" dur="0.8s" repeatCount="indefinite" />\n'
                    svg_content += f'</rect>\n'
                else:
                    svg_content += f'<rect x="{b_x}" y="{b_y}" width="{block_width}" height="14" fill="#39ff14" />\n'
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
    
    with open("zombie-graph.svg", "w", encoding="utf-8") as file:
        file.write(svg_content)
    print(f"[SUCCESS] Zombie Graph oluşturuldu: 'zombie-graph.svg'")

def simulate_zombie_survival(days):
    today_str = days[-1]['date']
    
    # 1. Kullanıcının İLK aktif olduğu günü bul
    first_active_date = None
    for d in days:
        if d['contributionCount'] > 0:
            first_active_date = d['date']
            break
            
    if not first_active_date: 
        first_active_date = today_str # Hiç commit atmamışsa
        
    # 2. Hayatta Kalma Serisi (BUG FIX: Bugün 0 commit olsa bile dünkü seriyi bozmaz)
    survival_day = 0
    for d in days:
        if d['date'] > today_str:
            break
        if d['contributionCount'] > 0:
            survival_day += 1
        elif d['date'] < today_str:
            survival_day = 0 # Sadece GEÇMİŞ günlerde 0 commit atıldıysa seriyi sıfırla

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

    # Bugünün commitlerini XP'ye dahil et
    today_commits = next((d['contributionCount'] for d in days if d['date'] == today_str), 0)
    total_commits += today_commits

    level, xp_current, xp_needed = calculate_level_info(total_commits)
    
    generate_pipboy_svg(days, level, xp_current, xp_needed, total_survived, total_invaded, survival_day, total_commits, first_active_date)

if __name__ == "__main__":
    real_github_data = get_contribution_data()
    if real_github_data: simulate_zombie_survival(real_github_data)
    else: print("[ERROR] Veri çekilemedi.")
Ana Dala (Main) Göndermek İçin Komutlar:

Kodunu yapıştırıp kaydettikten sonra terminaline sırasıyla şu İngilizce commit komutlarını girerek depoyu uçuşa hazır hale getirebilirsin:

Bash
git switch main
git add zombie.py
git commit -m "feat: migrate to stateless architecture and dynamic streak system"
git push origin main
önce test e push yapmak istiyorum switch yapamadım sanki neden

Görseli incelediğimde hatanın tam olarak ne olduğunu ve neden kaynaklandığını buldum! Aslında ortada iki durum var:

1. Zaten test Branch'indesin:
VS Code'un sol alt köşesindeki mavi çubuğa dikkatli bakarsan test* yazdığını göreceksin. Yani daha önceki adımlarda test dalına başarıyla geçmişsin. git switch test yazdığında Git'in hata vermesinin bir sebebi de zaten o dalda olman, ama asıl sebep ikinci madde.

2. Çakışma (Conflict) Kilidi:
Terminalde zombie-graph.svg: needs merge ve error: you need to resolve your current index first hatası var. Bu, daha önce kodları zuladan geri çıkardığımızda (git stash pop) Git'in zombie-graph.svg dosyasında bir çakışma yaşadığını ve senin bunu onaylamanı beklediğini gösteriyor. Git, "Bu çakışmayı çözmeden sana hiçbir işlem yaptırmam" diyerek sistemi kilitlemiş.

zombie-graph.svg zaten kodumuzun otomatik ürettiği bir çıktı dosyası olduğu için satır satır çakışma çözmemize hiç gerek yok. Git'e sadece "Bu güncel halini kabul et" deyip kilidi açacağız.

Bu kilidi açıp kodları doğrudan test branch'ine pushlamak için terminale sırasıyla şu komutları girmen yeterli:

1. Çakışmayı çöz ve tüm dosyaları (test senaryoları dahil) ekle:

Bash
git add .
2. Test ortamı için commit at:

Bash
git commit -m "test: apply stateless streak algorithm and new test scenarios"
3. Test branch'ine (uzak sunucuya) pushla:

Bash
git push origin test
Bu adımları yaptıktan sonra Git'in üzerindeki kilit kalkacak ve kodların GitHub'daki test branch'ine başarıyla yüklenmiş olacak! Sonrasında GitHub arayüzünden test branch'ini kontrol edebilirsin.

burada hangilerini silmem lazım sence

Harika bir tespit daha! Yeni "Stateless" (durumsuz) algoritmaya geçtiğimiz için o listede artık tamamen çöp haline gelen ve silmen gereken tek bir dosya var:

🗑️ zombie-state.json

Neden siliyoruz?
Çünkü yeni yazdığımız muazzam algoritmada artık başlangıç tarihini veya geçmiş günleri bir yere kaydetmemize gerek kalmadı. Sistem tamamen senin GitHub commit geçmişine bakarak ilk başladığın günü dinamik olarak kendi buluyor. Bu dosya artık hiçbir işe yaramıyor ve repoda boşuna kalabalık yapıyor.

(Not: zombie-graph.svg dosyası profilinde görselin görünmesi için repoda kalmalı, onu silmiyoruz.)

Bu gereksiz dosyayı ana dalından (main) temizlemek için VS Code terminaline sırasıyla şu komutları girebilirsin:

Bash
git switch main
git rm zombie-state.json
git commit -m "chore: remove obsolete zombie-state.json file"
git push origin main
Bu işlemi yaptıktan sonra depon tamamen yeni mimariye uygun, pırıl pırıl ve fazlalıklardan arınmış olacak!

name: 'GitHub Zombie Survival Graph'

description: 'Transform your standard GitHub contribution graph into a post-apocalyptic tactical survival system.'

branding:

  icon: 'activity'

  color: 'green'



inputs:

  github_token:

    description: 'Verileri çekmek için gerekli GitHub Token (secrets.GITHUB_TOKEN)'

    required: true

  github_username:

    description: 'GitHub kullanıcı adı (Opsiyonel, otomatik bulunur)'

    required: false

    default: ${{ github.repository_owner }}

  game_start_date:

    description: 'Zombi istilasının başlama tarihi (YYYY-MM-DD)'

    required: false

    default: '2026-08-15'



runs:

  using: "composite"

  steps:

    - name: Set up Python

      uses: actions/setup-python@v4

      with:

        python-version: '3.10'

        

    - name: Install dependencies

      shell: bash

      run: pip install requests python-dotenv

        

    - name: Run Zombie Script

      shell: bash

      env:

        GITHUB_TOKEN: ${{ inputs.github_token }}

        GITHUB_USERNAME: ${{ inputs.github_username }}

        GAME_START_DATE: ${{ inputs.game_start_date }}

      # python dosyasını action'ın kendi klasöründen bulup çalıştırır

      run: python ${{ github.action_path }}/zombie.py

action kodları doğrumu daha iyi hale getirileilir mi. push sayısına göre güncellenmesini istiyorum arayüzün

Gönderdiğin action.yml kodunu inceledim. Kodun temel yapısı doğru ancak daha önce yazdığımız yeni "Stateless" (durumsuz) algoritmaya uyum sağlaması için bir temizlik yapmamız gerekiyor.

Ayrıca "push sayısına göre güncellenmesini istiyorum" talebin için önemli bir detayı netleştirmeliyiz. action.yml dosyası sadece eklentinin ne yapacağını tanımlar. Eklentinin ne zaman çalışacağını (örneğin her push işleminde) belirleyen yer, bu action'ı kullandığın deponun içindeki .github/workflows/ klasöründe bulunan iş akışı (workflow) dosyasıdır.

Aşağıda her iki dosya için de yapman gereken düzenlemeleri profesyonel ve sade bir şekilde listeledim.

1. action.yml Dosyasının Güncellenmesi
Yeni algoritmamızda başlangıç tarihini dinamik olarak GitHub commit geçmişinden bulduğumuz için game_start_date girdisine artık ihtiyacımız yok. Bu girdiyi dosyadan tamamen kaldırmalıyız.

action.yml dosyanı şu şekilde güncelle:

YAML
name: 'GitHub Zombie Survival Graph'
description: 'Transform your standard GitHub contribution graph into a post-apocalyptic tactical survival system.'
branding:
  icon: 'activity'
  color: 'green'

inputs:
  github_token:
    description: 'Verileri cekmek icin gerekli GitHub Token (secrets.GITHUB_TOKEN)'
    required: true
  github_username:
    description: 'GitHub kullanici adi (Opsiyonel, otomatik bulunur)'
    required: false
    default: ${{ github.repository_owner }}

runs:
  using: "composite"
  steps:
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
        
    - name: Install dependencies
      shell: bash
      run: pip install requests python-dotenv
        
    - name: Run Zombie Script
      shell: bash
      env:
        GITHUB_TOKEN: ${{ inputs.github_token }}
        GITHUB_USERNAME: ${{ inputs.github_username }}
      run: python ${{ github.action_path }}/zombie.py
2. İş Akışı (Workflow) Dosyasının Güncellenmesi
Grafiğin her kod gönderdiğinde (push) otomatik olarak güncellenmesini sağlamak için, profil depondaki (büyük ihtimalle achexus/achexus deposu) .github/workflows/ klasörü altındaki yml dosyanı düzenlemelisin.

Tetikleyici (trigger) kısmına push komutunu eklemen yeterlidir. Aşağıdaki örnek şablonu kendi dosyana entegre edebilirsin:

YAML
name: Update Zombie Survival Graph

on:
  push:
    branches:
      - main
  schedule:
    - cron: "0 0 * * *" # Push atilmasa bile her gece 00:00'da kontrol eder
  workflow_dispatch: # Manuel tetikleme butonu ekler

jobs:
  update-graph:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v3

      - name: Generate Zombie Graph
        uses: achexus/github-zombie-graph@v1.1.1 # Guncel versiyon etiketini kullan
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}

      - name: Commit and Push changes
        run: |
          git config --global user.name "github-actions[bot]"
          git config --global user.email "github-actions[bot]@users.noreply.github.com"
          git add zombie-graph.svg
          git commit -m "chore: update zombie survival graph" || exit 0
          git push
Bu değişiklikleri uyguladıktan sonra sistem, main dalına yaptığın her kod gönderimini algılayacak ve arka planda action'ı çalıştırarak görseli tazeleyecektir.

İş akışı dosyanın mevcut yapısında yukarıdaki örneğe uymayan veya çakışan bir tetikleyici bloğu bulunuyor mu?

bunun sonucu neye göre bu olarak çıktı tam olarak. başlangıç gününü ne sayıyor açık kırmızı koyu kırmızıyı neye göre seçiyor

Harika bir soru. Grafiğin neredeyse tamamen kırmızı bir kan gölüne dönmesinin ve renklerin farklılaşmasının ardında yatan tam matematiksel sebep şu:

1. Başlangıç Günü Neden Böyle Hesaplandı? (Neden Her Yer Kırmızı?)
Son yazdığımız "Stateless" algoritmada, sistemin başlangıç gününü bulması için ona şu kuralı verdik: "Son 1 yıl (378 gün) içindeki atılmış İLK commiti bul ve istilayı o gün başlat."

Senin orijinal GitHub grafiğine baktığımızda, asıl yoğun tempon Ağustos ayında olsa da, taa Ekim (October) aylarında atılmış 1-2 tane ufak commitin var. Sistem o Ekim ayındaki commiti görüp "Oyun Ekim ayında başladı!" diyor. Ekim'den Ağustos'a kadar kod yazmadığın o devasa ayları da oyunun içi saydığı için, aradaki o boş yüzlerce günü zombi istilası olarak işaretliyor (Zaten istatistiklerdeki 310 INVADED koca bir senenin boş geçtiğini gösteriyor).

2. Kırmızı Renklerin Anlamı Ne?
Kodumuzda yenilgi durumları için iki farklı CSS sınıfı belirledik. Kırmızının tonu, senin o günkü direnişine göre değişiyor:

Açık/Parlak Kırmızı (Neon Red): O gün 0 commit attın demektir. Zombiler hiçbir direnişle (savunmayla) karşılaşmadan bölgeyi tamamen işgal etti. Haritandaki devasa parlak kırmızı alanlar, aylarca hiç kod yazmadığın günleri temsil ediyor.

Koyu Kırmızı / Bordo (Dark Crimson): O gün kod yazdın (commit > 0) ama yazdığın kod sayısı, o gün gelen zombi sayısından azdı. Yani silahını çektin, direndin ama cephanen yetmedi. Haritanda nadiren görünen o koyu kırmızı kutular, savaşıp kaybettiğin günleri gösteriyor.

Bu Kötü Görüntüyü Nasıl Çözeriz?
Taa 10 ay önceki tek bir commit yüzünden bütün yılın kırmızı olması arayüzü çok çirkinleştirmiş. Bu "ilk aktif gün" mantığı eski hesaplarda pek işe yaramıyor.

Bunu çözmek için koda ufak bir limit koyabiliriz: "Sadece son 60 gün (veya 30 gün) içindeki ilk commiti başlangıç say." Böylece o eski aylardaki tek tük commitler görmezden gelinir, geçmiş günlerin hepsi "Standby" (Güvenli Gri) modunda kalır ve sadece asıl aktif olduğun son aylar mücadele alanına dönüşür.

Eğer mantıklı geldiyse bu kısıtlamayı içeren güncel kodu hemen verebilirim.

evet son 30 gündeki ilk committen başlasın kodlar. kırmızı renk tonlar biraz oyunun renk şemasına uymuyor renk şemasına uyan bir renk seçiminde bulun

Harika bir dokunuş. O devasa parlak kırmızı bloklar terminalin şık ve karanlık siberpunk yapısını gerçekten bozuyordu. İki sorunu da tek seferde çözdüm:

30 Günlük Başlangıç Sınırı: Kod artık tüm 1 yıla bakmak yerine sadece son 30 gün içindeki ilk commitini buluyor. Böylece aylar önceki tek bir commit yüzünden grafiğin başı sonu kıpkırmızı olmayacak. Eğer son 30 günde hiç commit yoksa, istilayı doğrudan bugün başlatacak.

Koyu Siberpunk Renk Paleti: Parlak "hata" kırmızısı yerine, terminal stiline uyan "Corrupted System" (Bozulmuş Sistem) renklerine geçtim:

0 commit atılan boş günlerde göz yormayan, arka planla bütünleşen çok koyu kan kırmızısı (#20080a).

Direnip kaybedilen günlerde ise biraz daha belirgin, kirli bir bordo/kızıl (#5e1111).
Böylece ekran kan gölüne dönmek yerine, şık bir yeşil terminalde bozulmuş/enfekte olmuş sektörler gibi görünecek.

İşte güncellenmiş nihai zombie.py kodun:

Python
import os
import requests
import random
import math
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("GITHUB_TOKEN")
USERNAME = os.getenv("GITHUB_USERNAME", os.getenv("GITHUB_REPOSITORY_OWNER", "achexus"))

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

def get_zombie_count_for_date(date_str):
    r = random.Random(date_str)
    return r.randint(1, 4)

def calculate_level_info(total_commits):
    if total_commits == 0:
        return 0, 0, 1
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

def get_radar_svg(remaining_zombies, x, y, width, height):
    cx = x + (width / 2)
    cy = y + 95
    dots = ""
    coords = [(-40, -35), (35, 20), (-15, 45), (45, -25)]
    for idx in range(min(remaining_zombies, 4)):
        dx, dy = coords[idx]
        dots += f"""
        <circle cx="{cx+dx}" cy="{cy+dy}" r="4" fill="#d92525">
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

def get_live_cam_svg(state, x, y, width, height, is_easter_egg=False):
    bg = f'<rect x="{x}" y="{y}" width="{width}" height="{height}" class="intel-panel" />'
    
    blink_dur = "0.2s" if is_easter_egg else "1.5s"
    
    live_header = f"""
    <circle cx="{x+18}" cy="{y+20}" r="4" fill="#d92525">
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
            <circle cx="{x+240}" cy="{y+100}" r="15" fill="#a11b1b" opacity="0.6">
                 <animate attributeName="cx" values="{x+240};{x+40}" dur="4s" repeatCount="indefinite" />
            </circle>
            <circle cx="{x+240}" cy="{y+100}" r="9" fill="#d92525" opacity="0.9">
                 <animate attributeName="cx" values="{x+240};{x+40}" dur="4s" repeatCount="indefinite" />
            </circle>
        </g>
        <g>
            <animateTransform attributeName="transform" type="translate" values="0,0; 0,-8; 0,0" dur="1.2s" repeatCount="indefinite" />
            <animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.8;0.9;1" dur="5s" repeatCount="indefinite" />
            <circle cx="{x+220}" cy="{y+130}" r="18" fill="#a11b1b" opacity="0.5">
                 <animate attributeName="cx" values="{x+220};{x+40}" dur="5s" repeatCount="indefinite" />
            </circle>
            <circle cx="{x+220}" cy="{y+130}" r="11" fill="#d92525" opacity="0.8">
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
    else:
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

def generate_pipboy_svg(days, level, xp_current, xp_needed, survived, invaded, survival_day, total_commits, first_active_date):
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
        status_color = "#39ff14"
        remaining_zombies = 0
    else:
        if today_commits == 0:
            cam_state = "en_route"
            today_status = "CRITICAL (EN ROUTE)"
            status_color = "#d92525"
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
    
    if is_easter_egg:
        today_status = "FATAL EXCEPTION 0x00000064"
        status_color = "#ff00ff"
        current_msgs = ["SYSTEM FAILURE", "CORRUPTED DATA", "WHO ARE WE?", "LOST IN THE GRID"]

    current_rank_idx = -1
    for i, (req, name, icon) in enumerate(ORDERED_RANKS):
        if level >= req:
            current_rank_idx = i
            
    if current_rank_idx == -1:
        active_rank_name = "UNRANKED"
    else:
        active_rank_name = ORDERED_RANKS[current_rank_idx][1]
        
    if is_easter_egg:
        active_rank_name = "KAYBOLMUŞ"

    screen_class = "screen easter-egg" if is_easter_egg else "screen"

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
        
        /* GÜNCELLENEN SİBERPUNK KORUPTE RENKLER */
        .game-invaded-1 {{ fill: #5e1111; stroke: #a11b1b; stroke-width: 1; rx: 2; ry: 2; }}  
        .game-invaded-2 {{ fill: #20080a; rx: 2; ry: 2; }}  
        
        @keyframes pulse-beacon {{ 0% {{ fill-opacity: 1; stroke: #ffffff; stroke-width: 1px; }} 50% {{ fill-opacity: 0.4; stroke: #39ff14; stroke-width: 3px; }} 100% {{ fill-opacity: 1; stroke: #ffffff; stroke-width: 1px; }} }}
        .current-day {{ animation: pulse-beacon 1.5s infinite; rx: 3; ry: 3; }}
        
        @keyframes crt-flicker {{ 0% {{ opacity: 0.95; }} 5% {{ opacity: 0.85; }} 10% {{ opacity: 0.95; }} 15% {{ opacity: 1.0; }} 50% {{ opacity: 0.98; }} 100% {{ opacity: 0.95; }} }}
        @keyframes system-glitch {{ 0% {{ transform: translate(0, 0); }} 2% {{ transform: translate(1px, -1px); }} 4% {{ transform: translate(-1px, 1px); }} 6% {{ transform: translate(0, 0); }} 100% {{ transform: translate(0, 0); }} }}
        .screen {{ animation: crt-flicker 0.15s infinite, system-glitch 4s infinite; }}
        
        @keyframes extreme-glitch {{
            0%   {{ transform: translate(0, 0); opacity: 0.9; }}
            10%  {{ transform: translate(-5px, 5px); opacity: 0.5; filter: hue-rotate(90deg); }}
            20%  {{ transform: translate(5px, -5px); opacity: 1.0; }}
            30%  {{ transform: translate(-5px, -5px); opacity: 0.4; filter: hue-rotate(-90deg); }}
            40%  {{ transform: translate(5px, 5px); opacity: 0.9; }}
            50%  {{ transform: translate(-2px, 2px); opacity: 0.6; filter: hue-rotate(180deg); }}
            60%  {{ transform: translate(2px, -2px); opacity: 1.0; }}
            70%  {{ transform: translate(-2px, -2px); opacity: 0.5; filter: hue-rotate(-180deg); }}
            80%  {{ transform: translate(2px, 2px); opacity: 0.9; }}
            90%  {{ transform: translate(0, 0); opacity: 0.7; filter: hue-rotate(45deg); }}
            100% {{ transform: translate(0, 0); opacity: 0.9; }}
        }}
        .easter-egg {{ animation: extreme-glitch 0.15s infinite !important; }}
    </style>
    <rect width="{svg_width}" height="{svg_height}" class="bg" />
    <g class="{screen_class}">
    """
    
    for y in range(0, svg_height, 4):
        svg_content += f'<line x1="0" y1="{y}" x2="{svg_width}" y2="{y}" class="scanline" />\n'
        
    svg_content += f'<text x="25" y="40" class="text-neon text-title">{USERNAME.upper()} SURVIVAL SYSTEM</text>\n'
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
            
            if is_easter_egg:
                dur = round(random.uniform(0.1, 0.4), 2)
                anim = f'<animate attributeName="fill" values="#ff003c;#39ff14;#ff8c00;#0d1117;#00ffff;#ff00ff" dur="{dur}s" repeatCount="indefinite" />'
                svg_content += f'<rect x="{x}" y="{y}" width="{box_size}" height="{box_size}" class="{color_class}{extra_class}">{anim}</rect>\n'
            else:
                svg_content += f'<rect x="{x}" y="{y}" width="{box_size}" height="{box_size}" class="{color_class}{extra_class}" />\n'
        else:
            svg_content += f'<rect x="{x}" y="{y}" width="{box_size}" height="{box_size}" class="fog-of-war" />\n'
        
    panel_x, panel_width, panel_height = 690, 265, 164
    svg_content += get_live_cam_svg(cam_state, panel_x, 165, panel_width, panel_height, is_easter_egg)
    svg_content += get_radar_svg(remaining_zombies, panel_x, 337, panel_width, panel_height)

    # -------------------------------------------------------------
    # KAYAN RÜTBE SİSTEMİ
    # -------------------------------------------------------------
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

    # -------------------------------------------------------------
    # TERMINAL STYLE LOADING (XP) BAR
    # -------------------------------------------------------------
    if not is_easter_egg:
        xp_bar_y = 615
        total_blocks = 77
        block_width = 10
        block_gap = 2
        bar_x = 25
        bar_width = (total_blocks * (block_width + block_gap)) + 2
        
        svg_content += f'<text x="25" y="{xp_bar_y + 10}" class="text-neon text-info">SYSTEM UPGRADE PROGRESS</text>\n'
        svg_content += f'<text x="{bar_x + bar_width}" y="{xp_bar_y + 10}" class="text-neon text-info" text-anchor="end">{xp_current} / {xp_needed} XP TO LVL {level + 1}</text>\n'
        
        svg_content += f'<rect x="{bar_x}" y="{xp_bar_y + 17}" width="{bar_width}" height="20" fill="none" stroke="#1a4d1a" stroke-width="1.5" />\n'
        
        if xp_needed > 0: fill_count = int(round((xp_current / xp_needed) * total_blocks))
        else: fill_count = 0
            
        for i in range(total_blocks):
            b_x = bar_x + 2 + i * (block_width + block_gap)
            b_y = xp_bar_y + 20
            
            if i < fill_count:
                if i == fill_count - 1:
                    svg_content += f'<rect x="{b_x}" y="{b_y}" width="{block_width}" height="14" fill="#39ff14">\n'
                    svg_content += f'    <animate attributeName="opacity" values="1;0.2;1" dur="0.8s" repeatCount="indefinite" />\n'
                    svg_content += f'</rect>\n'
                else:
                    svg_content += f'<rect x="{b_x}" y="{b_y}" width="{block_width}" height="14" fill="#39ff14" />\n'
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
    
    with open("zombie-graph.svg", "w", encoding="utf-8") as file:
        file.write(svg_content)
    print(f"[SUCCESS] Zombie Graph oluşturuldu: 'zombie-graph.svg'")

def simulate_zombie_survival(days):
    today_str = days[-1]['date']
    today_obj = datetime.strptime(today_str, "%Y-%m-%d").date()
    
    # 1. Sadece SON 30 GÜN içindeki İLK aktif günü bul
    cutoff_date_str = (today_obj - timedelta(days=30)).strftime("%Y-%m-%d")
    first_active_date = None
    
    for d in days:
        if d['date'] >= cutoff_date_str and d['contributionCount'] > 0:
            first_active_date = d['date']
            break
            
    if not first_active_date: 
        first_active_date = today_str 

    # 2. Hayatta Kalma Serisi
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
    
    generate_pipboy_svg(days, level, xp_current, xp_needed, total_survived, total_invaded, survival_day, total_commits, first_active_date)

if __name__ == "__main__":
    real_github_data = get_contribution_data()
    if real_github_data: simulate_zombie_survival(real_github_data)
    else: print("[ERROR] Veri çekilemedi.")
Değişiklikleri Git'e yollamak için terminale sırasıyla bunları girebilirsin:

Bash
git switch main
git add zombie.py
git commit -m "fix: constrain start date to last 30 days and refine cyberpunk error colors"
git push origin main
1.1.2 versiyonu için düzenlemelerimizi yapalım hadi

Bu devasa altyapı değişikliğini (Stateless mimari, renk düzenlemeleri ve 30 gün sınırı) taçlandırmanın vakti geldi. Daha önceki talebine uygun olarak, yapay zeka tarafından yazılmış gibi durmayan, emojilerden arındırılmış ve son derece profesyonel bir yama notu (Release Notes) hazırladım.

Görseldeki ekranda doldurman gereken alanlar şu şekilde:

Tag: v1.1.2 yazıp "Create new tag" seçeneğine tıkla.

Target: main

Release title: v1.1.2 - Stateless Engine & UI Polish

Aşağıdaki metni kopyalayıp doğrudan "Describe this release" yazan büyük metin kutusuna yapıştırabilirsin:

v1.1.2 - Stateless Engine & UI Polish
System Engineering Update

The core architecture of the survival graph has been overhauled. Local state dependencies have been eliminated, transitioning the system to a fully dynamic, real-time calculation engine directly integrated with GitHub contribution data.

Architectural Updates
Stateless Execution: Removed the dependency on the local state file. The system now dynamically calculates the active commit streak and invasion start date on the fly, preventing data corruption and reset loops on GitHub Actions runners.

Action Configurations: Cleaned action.yml by removing the obsolete game_start_date input variable. The action is now entirely plug-and-play.

Critical Fixes
Dynamic Start Date Limitation: Addressed a visual anomaly where a single legacy commit would render the entire year as an active invasion zone. The algorithm now isolates the invasion start date to the first active commit within the last 30 days.

Streak Reset Logic: Fixed a synchronization issue where the survival day streak would falsely reset to zero if the workflow was triggered early in the day before a commit was made.

Interface Enhancements
Corrupted System Color Palette: Replaced the high-contrast red indicator blocks with a darker, desaturated crimson palette. This adjustment provides a cleaner integration with the dark cyberpunk terminal aesthetic for days categorized as invaded or inactive.

HUD Terminology: Standardized the interface text to display "SURVIVAL DAY", strictly representing the user's current unbroken contribution streak.

Bu notları ekleyip "Publish release" butonuna bastığında, projenin bu en hatasız ve profesyonel sürümü tüm GitHub topluluğuna sunulmuş olacak. Eline sağlık!

açıklamayı önceki verdiğin gibi sanki zombi telsizi ayarında verir misin

İşte atmosferi koruyan, ancak çok daha ciddi, askeri bir telsiz kaydı formatında hazırlanmış sürüm notları:

v1.1.2 - OPERATION: GHOST PROTOCOL (Stateless Engine & UI Polish)
Transmission Status: SECURE

Sender: System Engineering Command

Subject: Core Architecture Overhaul & Tactical Calibration

Command has authorized a complete architectural rewrite of the survival tracking system. All local state dependencies have been severed. The tracking engine is now fully autonomous, operating directly on live grid intel. Update your local defense nodes to v1.1.2 immediately to ensure operational accuracy.

[ARCHITECTURAL UPDATES]
Autonomous Stateless Execution: Local state files have been purged. The engine now dynamically calculates active survival streaks and initial invasion dates in real-time, eliminating data corruption across ephemeral servers.

Streamlined Deployment: Obsolete start-date configurations have been stripped from the deployment protocols. The defense action is now fully plug-and-play.

[CRITICAL FIXES]
Threat Zone Containment: The system will no longer flag the entire annual grid as a compromised zone due to isolated legacy activity. Invasion parameters are now strictly confined to the first active signature detected within the last 30 days.

Morning Reset Override: Patched a synchronization vulnerability where early morning radar sweeps falsely reported a broken survival streak before daily defenses could be established.

[INTERFACE ENHANCEMENTS]
Corrupted Sector Signatures: High-visibility neon red indicators have been decommissioned. Invaded and offline sectors now emit a darkened, desaturated crimson signature, optimizing the tactical HUD visibility.

HUD Terminology: Interface readouts have been recalibrated. The system now strictly displays "SURVIVAL DAY", accurately tracking the operator's unbroken chain of defensive actions.

End of transmission. Hold the line.

— SYSTEM COMMAND —

# 🧟‍♂️ GitHub Zombie Survival Graph



<div align="center">

  <table>

    <tr>

      <td align="center"><a href="#english">🇬🇧 English</a></td>

      <td align="center"><a href="#turkce">🇹🇷 Türkçe</a></td>

      <td align="center"><a href="#espanol">🇪🇸 Español</a></td>

      <td align="center"><a href="#deutsch">🇩🇪 Deutsch</a></td>

      <td align="center"><a href="#francais">🇫🇷 Français</a></td>

    </tr>

    <tr>

      <td align="center"><a href="#italiano">🇮🇹 Italiano</a></td>

      <td align="center"><a href="#portugues">🇵🇹 Português</a></td>

      <td align="center"><a href="#русский">🇷🇺 Русский</a></td>

      <td align="center"><a href="#nederlands">🇳🇱 Nederlands</a></td>

      <td align="center"><a href="#polski">🇵🇱 Polski</a></td>

    </tr>

  </table>

</div>



<br>



<div align="center">

  <img src="zombie-graph.svg" alt="GitHub Zombie Survival Graph" />

</div>



---



<h2 id="english">🇬🇧 English</h2>



Transform your standard GitHub contribution graph into a post-apocalyptic tactical survival system! This GitHub Action generates a dynamic SVG showing your survival streak, eliminated zombies (commits), and tactical rank based on your daily GitHub activity.



### 🚀 How to Use



**1. Create the Workflow**

Create a new file in your repository at `.github/workflows/zombie-graph.yml` and add the following code:



```yaml

name: GitHub Zombie Survival Graph



on:

  schedule:

    - cron: "0 0 * * *" # Runs automatically every midnight

  workflow_dispatch: # Allows manual trigger



jobs:

  build:

    runs-on: ubuntu-latest

    permissions:

      contents: write



    steps:

      - name: Checkout Repository

        uses: actions/checkout@v4



      - name: Generate Zombie Survival Graph

        uses: achexus/github-zombie-graph@main

        with:

          github_token: ${{ secrets.GITHUB_TOKEN }}



      - name: Commit and Push the generated SVG

        uses: stefanzweifel/git-auto-commit-action@v5

        with:

          commit_message: "Update GitHub Zombie Survival Graph"

          file_pattern: zombie-graph.svg

```



> **⚠️ Important Note:** Ensure your repository allows Actions to read and write. Go to **Settings > Actions > General**, scroll down to **Workflow permissions**, and select **"Read and write permissions"**.



**2. Update your README**

Add the generated SVG to your profile's `README.md`:



```html

<div align="center">

  <img src="zombie-graph.svg" alt="My Zombie Survival Status" />

</div>

```



---



<h2 id="turkce">🇹🇷 Türkçe</h2>



Klasik GitHub katkı grafiğinizi kıyamet sonrası taktiksel bir hayatta kalma sistemine dönüştürün! Bu GitHub Action, günlük GitHub aktivitenize dayanarak hayatta kalma serinizi, yok edilen zombileri (commit'ler) ve taktiksel rütbenizi gösteren dinamik bir SVG oluşturur.



### 🚀 Nasıl Kullanılır?



**1. Workflow Dosyasını Oluşturun**

Deponuzda `.github/workflows/zombie-graph.yml` yolunda yeni bir dosya oluşturun ve aşağıdaki kodu ekleyin:



```yaml

name: GitHub Zombie Survival Graph



on:

  schedule:

    - cron: "0 0 * * *" # Her gece yarısı otomatik çalışır

  workflow_dispatch: # Manuel tetiklemeye izin verir



jobs:

  build:

    runs-on: ubuntu-latest

    permissions:

      contents: write



    steps:

      - name: Checkout Repository

        uses: actions/checkout@v4



      - name: Generate Zombie Survival Graph

        uses: achexus/github-zombie-graph@main

        with:

          github_token: ${{ secrets.GITHUB_TOKEN }}



      - name: Commit and Push the generated SVG

        uses: stefanzweifel/git-auto-commit-action@v5

        with:

          commit_message: "Update GitHub Zombie Survival Graph"

          file_pattern: zombie-graph.svg

```



> **⚠️ Önemli Not:** Deponuzun Action'lar için okuma ve yazma iznine sahip olduğundan emin olun. **Settings > Actions > General** sekmesine gidin, en alttaki **Workflow permissions** kısmından **"Read and write permissions"** seçeneğini işaretleyip kaydedin.



**2. README Dosyanızı Güncelleyin**

Oluşturulan SVG dosyasını profilinizin `README.md` dosyasına ekleyin:



```html

<div align="center">

  <img src="zombie-graph.svg" alt="My Zombie Survival Status" />

</div>

```



---



<h2 id="espanol">🇪🇸 Español</h2>



¡Transforma tu gráfico de contribuciones de GitHub estándar en un sistema táctico de supervivencia post-apocalíptico! Esta GitHub Action genera un SVG dinámico que muestra tu racha de supervivencia, zombis eliminados (commits) y rango táctico.



### 🚀 Cómo Utilizar



**1. Crear el Flujo de Trabajo (Workflow)**

Crea un nuevo archivo en tu repositorio en `.github/workflows/zombie-graph.yml` y añade el siguiente código:



```yaml

name: GitHub Zombie Survival Graph



on:

  schedule:

    - cron: "0 0 * * *"

  workflow_dispatch: 



jobs:

  build:

    runs-on: ubuntu-latest

    permissions:

      contents: write



    steps:

      - name: Checkout Repository

        uses: actions/checkout@v4



      - name: Generate Zombie Survival Graph

        uses: achexus/github-zombie-graph@main

        with:

          github_token: ${{ secrets.GITHUB_TOKEN }}



      - name: Commit and Push the generated SVG

        uses: stefanzweifel/git-auto-commit-action@v5

        with:

          commit_message: "Update GitHub Zombie Survival Graph"

          file_pattern: zombie-graph.svg

```



> **⚠️ Nota Importante:** Asegúrate de que tu repositorio permite a las Actions leer y escribir. Ve a **Settings > Actions > General**, desplázate hasta **Workflow permissions** y selecciona **"Read and write permissions"**.



**2. Actualizar el README**

Añade el SVG generado al `README.md` de tu perfil:



```html

<div align="center">

  <img src="zombie-graph.svg" alt="My Zombie Survival Status" />

</div>

```



---



<h2 id="deutsch">🇩🇪 Deutsch</h2>



Verwandle dein standardmäßiges GitHub-Beitragsdiagramm in ein postapokalyptisches taktisches Überlebenssystem! Diese GitHub Action generiert eine dynamische SVG, die deine Überlebenssträhne, eliminierte Zombies (Commits) und deinen taktischen Rang anzeigt.



### 🚀 Verwendung



**1. Workflow Erstellen**

Erstelle eine neue Datei in deinem Repository unter `.github/workflows/zombie-graph.yml` und füge den folgenden Code hinzu:



```yaml

name: GitHub Zombie Survival Graph



on:

  schedule:

    - cron: "0 0 * * *"

  workflow_dispatch: 



jobs:

  build:

    runs-on: ubuntu-latest

    permissions:

      contents: write



    steps:

      - name: Checkout Repository

        uses: actions/checkout@v4



      - name: Generate Zombie Survival Graph

        uses: achexus/github-zombie-graph@main

        with:

          github_token: ${{ secrets.GITHUB_TOKEN }}



      - name: Commit and Push the generated SVG

        uses: stefanzweifel/git-auto-commit-action@v5

        with:

          commit_message: "Update GitHub Zombie Survival Graph"

          file_pattern: zombie-graph.svg

```



> **⚠️ Wichtiger Hinweis:** Stelle sicher, dass dein Repository Lese- und Schreibrechte für Actions erlaubt. Gehe zu **Settings > Actions > General**, scrolle zu **Workflow permissions** und wähle **"Read and write permissions"**.



**2. README Aktualisieren**

Füge die generierte SVG-Datei zur `README.md` deines Profils hinzu:



```html

<div align="center">

  <img src="zombie-graph.svg" alt="My Zombie Survival Status" />

</div>

```



---



<h2 id="francais">🇫🇷 Français</h2>



Transformez votre graphique de contributions GitHub standard en un système de survie tactique post-apocalyptique ! Cette GitHub Action génère un SVG dynamique affichant votre série de survie, les zombies éliminés (commits) et votre rang tactique.



### 🚀 Comment l'utiliser



**1. Créer le Workflow**

Créez un nouveau fichier dans votre dépôt à l'emplacement `.github/workflows/zombie-graph.yml` et ajoutez le code suivant :



```yaml

name: GitHub Zombie Survival Graph



on:

  schedule:

    - cron: "0 0 * * *"

  workflow_dispatch: 



jobs:

  build:

    runs-on: ubuntu-latest

    permissions:

      contents: write



    steps:

      - name: Checkout Repository

        uses: actions/checkout@v4



      - name: Generate Zombie Survival Graph

        uses: achexus/github-zombie-graph@main

        with:

          github_token: ${{ secrets.GITHUB_TOKEN }}



      - name: Commit and Push the generated SVG

        uses: stefanzweifel/git-auto-commit-action@v5

        with:

          commit_message: "Update GitHub Zombie Survival Graph"

          file_pattern: zombie-graph.svg

```



> **⚠️ Remarque Importante :** Assurez-vous que votre dépôt autorise les Actions à lire et écrire. Allez dans **Settings > Actions > General**, descendez jusqu'à **Workflow permissions**, et sélectionnez **"Read and write permissions"**.



**2. Mettre à jour votre README**

Ajoutez le SVG généré au `README.md` de votre profil :



```html

<div align="center">

  <img src="zombie-graph.svg" alt="My Zombie Survival Status" />

</div>

```



---



<h2 id="italiano">🇮🇹 Italiano</h2>



Trasforma il tuo grafico standard dei contributi di GitHub in un sistema tattico di sopravvivenza post-apocalittico! Questa GitHub Action genera un SVG dinamico che mostra la tua serie di sopravvivenza, gli zombie eliminati (commit) e il tuo grado tattico.



### 🚀 Come Usarlo



**1. Creare il Workflow**

Crea un nuovo file nel tuo repository in `.github/workflows/zombie-graph.yml` e aggiungi il seguente codice:



```yaml

name: GitHub Zombie Survival Graph



on:

  schedule:

    - cron: "0 0 * * *"

  workflow_dispatch: 



jobs:

  build:

    runs-on: ubuntu-latest

    permissions:

      contents: write



    steps:

      - name: Checkout Repository

        uses: actions/checkout@v4



      - name: Generate Zombie Survival Graph

        uses: achexus/github-zombie-graph@main

        with:

          github_token: ${{ secrets.GITHUB_TOKEN }}



      - name: Commit and Push the generated SVG

        uses: stefanzweifel/git-auto-commit-action@v5

        with:

          commit_message: "Update GitHub Zombie Survival Graph"

          file_pattern: zombie-graph.svg

```



> **⚠️ Nota Importante:** Assicurati che il tuo repository consenta alle Action di leggere e scrivere. Vai su **Settings > Actions > General**, scorri fino a **Workflow permissions** e seleziona **"Read and write permissions"**.



**2. Aggiornare il README**

Aggiungi l'SVG generato al `README.md` del tuo profilo:



```html

<div align="center">

  <img src="zombie-graph.svg" alt="My Zombie Survival Status" />

</div>

```



---



<h2 id="portugues">🇵🇹 Português</h2>



Transforme seu gráfico de contribuições padrão do GitHub em um sistema tático de sobrevivência pós-apocalíptico! Esta GitHub Action gera um SVG dinâmico mostrando sua sequência de sobrevivência, zumbis eliminados (commits) e rank tático.



### 🚀 Como Usar



**1. Criar o Workflow**

Crie um novo arquivo no seu repositório em `.github/workflows/zombie-graph.yml` e adicione o seguinte código:



```yaml

name: GitHub Zombie Survival Graph



on:

  schedule:

    - cron: "0 0 * * *"

  workflow_dispatch: 



jobs:

  build:

    runs-on: ubuntu-latest

    permissions:

      contents: write



    steps:

      - name: Checkout Repository

        uses: actions/checkout@v4



      - name: Generate Zombie Survival Graph

        uses: achexus/github-zombie-graph@main

        with:

          github_token: ${{ secrets.GITHUB_TOKEN }}



      - name: Commit and Push the generated SVG

        uses: stefanzweifel/git-auto-commit-action@v5

        with:

          commit_message: "Update GitHub Zombie Survival Graph"

          file_pattern: zombie-graph.svg

```



> **⚠️ Nota Importante:** Certifique-se de que seu repositório permite que as Actions leiam e escrevam. Vá para **Settings > Actions > General**, role até **Workflow permissions** e selecione **"Read and write permissions"**.



**2. Atualizar o README**

Adicione o SVG gerado ao `README.md` do seu perfil:



```html

<div align="center">

  <img src="zombie-graph.svg" alt="My Zombie Survival Status" />

</div>

```



---



<h2 id="русский">🇷🇺 Русский</h2>



Превратите ваш стандартный график активности GitHub в постапокалиптическую тактическую систему выживания! Этот GitHub Action создает динамический SVG, показывающий вашу серию выживания, уничтоженных зомби (коммиты) и тактический ранг.



### 🚀 Как Использовать



**1. Создайте рабочий процесс (Workflow)**

Создайте новый файл в вашем репозитории по пути `.github/workflows/zombie-graph.yml` и добавьте следующий код:



```yaml

name: GitHub Zombie Survival Graph



on:

  schedule:

    - cron: "0 0 * * *"

  workflow_dispatch: 



jobs:

  build:

    runs-on: ubuntu-latest

    permissions:

      contents: write



    steps:

      - name: Checkout Repository

        uses: actions/checkout@v4



      - name: Generate Zombie Survival Graph

        uses: achexus/github-zombie-graph@main

        with:

          github_token: ${{ secrets.GITHUB_TOKEN }}



      - name: Commit and Push the generated SVG

        uses: stefanzweifel/git-auto-commit-action@v5

        with:

          commit_message: "Update GitHub Zombie Survival Graph"

          file_pattern: zombie-graph.svg

```



> **⚠️ Важное Примечание:** Убедитесь, что ваш репозиторий разрешает Actions чтение и запись. Перейдите в **Settings > Actions > General**, прокрутите до **Workflow permissions** и выберите **"Read and write permissions"**.



**2. Обновите ваш README**

Добавьте сгенерированный SVG в `README.md` вашего профиля:



```html

<div align="center">

  <img src="zombie-graph.svg" alt="My Zombie Survival Status" />

</div>

```



---



<h2 id="nederlands">🇳🇱 Nederlands</h2>



Transformeer je standaard GitHub bijdragegrafiek in een post-apocalyptisch tactisch overlevingssysteem! Deze GitHub Action genereert een dynamische SVG die je overlevingsreeks, geëlimineerde zombies (commits) en tactische rang toont.



### 🚀 Hoe te Gebruiken



**1. Maak de Workflow aan**

Maak een nieuw bestand in je repository op `.github/workflows/zombie-graph.yml` en voeg de volgende code toe:



```yaml

name: GitHub Zombie Survival Graph



on:

  schedule:

    - cron: "0 0 * * *"

  workflow_dispatch: 



jobs:

  build:

    runs-on: ubuntu-latest

    permissions:

      contents: write



    steps:

      - name: Checkout Repository

        uses: actions/checkout@v4



      - name: Generate Zombie Survival Graph

        uses: achexus/github-zombie-graph@main

        with:

          github_token: ${{ secrets.GITHUB_TOKEN }}



      - name: Commit and Push the generated SVG

        uses: stefanzweifel/git-auto-commit-action@v5

        with:

          commit_message: "Update GitHub Zombie Survival Graph"

          file_pattern: zombie-graph.svg

```



> **⚠️ Belangrijke Opmerking:** Zorg ervoor dat je repository Actions toestaat om te lezen en schrijven. Ga naar **Settings > Actions > General**, scrol naar **Workflow permissions** en selecteer **"Read and write permissions"**.



**2. Werk je README bij**

Voeg de gegenereerde SVG toe aan de `README.md` van je profiel:



```html

<div align="center">

  <img src="zombie-graph.svg" alt="My Zombie Survival Status" />

</div>

```



---



<h2 id="polski">🇵🇱 Polski</h2>



Przekształć swój standardowy wykres aktywności GitHub w postapokaliptyczny system taktycznego przetrwania! Ta akcja GitHub generuje dynamiczny SVG pokazujący Twoją serię przetrwania, wyeliminowane zombie (commity) i rangę taktyczną.



### 🚀 Jak Używać



**1. Utwórz Workflow**

Utwórz nowy plik w swoim repozytorium pod adresem `.github/workflows/zombie-graph.yml` i dodaj następujący kod:



```yaml

name: GitHub Zombie Survival Graph



on:

  schedule:

    - cron: "0 0 * * *"

  workflow_dispatch: 



jobs:

  build:

    runs-on: ubuntu-latest

    permissions:

      contents: write



    steps:

      - name: Checkout Repository

        uses: actions/checkout@v4



      - name: Generate Zombie Survival Graph

        uses: achexus/github-zombie-graph@main

        with:

          github_token: ${{ secrets.GITHUB_TOKEN }}



      - name: Commit and Push the generated SVG

        uses: stefanzweifel/git-auto-commit-action@v5

        with:

          commit_message: "Update GitHub Zombie Survival Graph"

          file_pattern: zombie-graph.svg

```



> **⚠️ Ważna Uwaga:** Upewnij się, że Twoje repozytorium zezwala Actions na odczyt i zapis. Przejdź do **Settings > Actions > General**, przewiń do **Workflow permissions** i wybierz **"Read and write permissions"**.



**2. Zaktualizuj README**

Dodaj wygenerowany plik SVG do `README.md` w swoim profilu:



```html

<div align="center">

  <img src="zombie-graph.svg" alt="My Zombie Survival Status" />

</div>

```

bunu güncelleyip ver tek code parçası içine yaz açıklamaları ve bütün bilgileride içericek çekilde. yml dosyasını güncelle ve arayüzdeki şeyleri ve oyunun amacını anlat. tek kod parçası olarak vermen çok önemli her dil için aynı şekilde ver uzunca bir tek parça kod olarak almayı bekliyorum senden

Harika bir fikir! Sürüm v1.1.2 ile getirdiğimiz yeni özellikleri (Streak mantığı, siberpunk renkleri, yükleme ekranı ve oyunun amacını) içeren, güncellenmiş tetikleyicilerle (push tetikleyicisi dahil) tam donanımlı yepyeni README dosyanı aşağıda hazırladım.

Kopyalarken sorun yaşamaman için tüm metni tek bir Markdown kod bloğu içine aldım. Bunu kopyalayıp doğrudan depondaki README.md dosyana yapıştırabilirsin:

Markdown
# 🧟‍♂️ GitHub Zombie Survival Graph

<div align="center">
  <table>
    <tr>
      <td align="center"><a href="#english">🇬🇧 English</a></td>
      <td align="center"><a href="#turkce">🇹🇷 Türkçe</a></td>
      <td align="center"><a href="#espanol">🇪🇸 Español</a></td>
      <td align="center"><a href="#deutsch">🇩🇪 Deutsch</a></td>
      <td align="center"><a href="#francais">🇫🇷 Français</a></td>
    </tr>
    <tr>
      <td align="center"><a href="#italiano">🇮🇹 Italiano</a></td>
      <td align="center"><a href="#portugues">🇵🇹 Português</a></td>
      <td align="center"><a href="#русский">🇷🇺 Русский</a></td>
      <td align="center"><a href="#nederlands">🇳🇱 Nederlands</a></td>
      <td align="center"><a href="#polski">🇵🇱 Polski</a></td>
    </tr>
  </table>
</div>

<br>

<div align="center">
  <img src="zombie-graph.svg" alt="GitHub Zombie Survival Graph" />
</div>

---

<h2 id="english">🇬🇧 English</h2>

Transform your standard GitHub contribution graph into a post-apocalyptic tactical survival system! This GitHub Action generates a dynamic SVG showing your survival streak, eliminated zombies (commits), and tactical rank based on your daily GitHub activity.

### 🎯 The Goal & Mechanics
Survive the apocalypse by writing code! Every day, a deterministic number of zombies (1 to 4) attacks your sector. You must make enough GitHub commits to eliminate them.
* **Cleared:** Your Commits >= Zombies. Sector secured!
* **Invaded:** Your Commits < Zombies. The sector is overrun.
* **Survival Streak:** If you make **0 commits** in a day, your active "Survival Day" streak resets to 0. Don't break the chain!
* **🖥️ UI Features:** Cyberpunk terminal aesthetics, "Corrupted System" dark crimson colors for offline/invaded days, a local radar, live cam, and a terminal-style XP loading bar.

### 🚀 How to Use

**1. Create the Workflow**
Create a new file in your repository at `.github/workflows/zombie-graph.yml` and add the following code:

```yaml
name: GitHub Zombie Survival Graph

on:
  push:
    branches:
      - main # Updates the graph every time you push code
  schedule:
    - cron: "0 0 * * *" # Runs automatically every midnight
  workflow_dispatch: # Allows manual trigger

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Generate Zombie Survival Graph
        uses: achexus/github-zombie-graph@v1.1.2
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}

      - name: Commit and Push the generated SVG
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "chore: update zombie survival graph"
          file_pattern: zombie-graph.svg
⚠️ Important Note: Ensure your repository allows Actions to read and write. Go to Settings > Actions > General, scroll down to Workflow permissions, and select "Read and write permissions".

2. Update your README
Add the generated SVG to your profile's README.md:

HTML
<div align="center">
  <img src="zombie-graph.svg" alt="My Zombie Survival Status" />
</div>
Klasik GitHub katkı grafiğinizi kıyamet sonrası taktiksel bir hayatta kalma sistemine dönüştürün! Bu GitHub Action, günlük GitHub aktivitenize dayanarak hayatta kalma serinizi, yok edilen zombileri (commit'ler) ve taktiksel rütbenizi gösteren dinamik bir SVG oluşturur.

🎯 Oyunun Amacı ve Mekanikler
Kod yazarak kıyametten sağ çıkın! Her gün, bölgenize rastgele sayıda (1-4) zombi saldırır. Onları yok etmek için yeterli sayıda GitHub commit'i atmalısınız.

Temizlendi (Cleared): Commit >= Zombi. Bölge güvende!

İstila Edildi (Invaded): Commit < Zombi. Bölge ele geçirildi.

Hayatta Kalma Serisi (Streak): Bir gün boyunca hiç commit atmazsanız (0 commit), "Survival Day" seriniz 0'a sıfırlanır. Zinciri kırmayın!

🖥️ Arayüz Özellikleri: Siberpunk terminal estetiği, çevrimdışı günler için "Bozulmuş Sistem" (koyu bordo) renkleri, yerel radar, canlı kamera ve terminal tarzı XP yükleme çubuğu.

🚀 Nasıl Kullanılır?
1. Workflow Dosyasını Oluşturun
Deponuzda .github/workflows/zombie-graph.yml yolunda yeni bir dosya oluşturun ve aşağıdaki kodu ekleyin:

YAML
name: GitHub Zombie Survival Graph

on:
  push:
    branches:
      - main # Her kod gönderdiğinizde grafiği günceller
  schedule:
    - cron: "0 0 * * *" # Her gece yarısı otomatik çalışır
  workflow_dispatch: # Manuel tetiklemeye izin verir

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Generate Zombie Survival Graph
        uses: achexus/github-zombie-graph@v1.1.2
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}

      - name: Commit and Push the generated SVG
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "chore: update zombie survival graph"
          file_pattern: zombie-graph.svg
⚠️ Önemli Not: Deponuzun Action'lar için okuma ve yazma iznine sahip olduğundan emin olun. Settings > Actions > General sekmesine gidin, en alttaki Workflow permissions kısmından "Read and write permissions" seçeneğini işaretleyip kaydedin.

2. README Dosyanızı Güncelleyin
Oluşturulan SVG dosyasını profilinizin README.md dosyasına ekleyin:

HTML
<div align="center">
  <img src="zombie-graph.svg" alt="My Zombie Survival Status" />
</div>
¡Transforma tu gráfico de contribuciones de GitHub estándar en un sistema táctico de supervivencia post-apocalíptico! Esta GitHub Action genera un SVG dinámico que muestra tu racha de supervivencia, zombis eliminados (commits) y rango táctico.

🎯 El Objetivo y Mecánicas
¡Sobrevive al apocalipsis escribiendo código! Cada día, un número de zombis (1-4) ataca tu sector. Debes hacer suficientes commits para eliminarlos.

Despejado (Cleared): Commits >= Zombis. ¡Sector asegurado!

Invadido (Invaded): Commits < Zombis. El sector ha sido invadido.

Racha (Streak): Si haces 0 commits en un día, tu racha de "Survival Day" se reinicia a 0. ¡No rompas la cadena!

🖥️ Interfaz: Estética de terminal ciberpunk, colores carmesí oscuro de "Sistema Corrupto", radar local, cámara en vivo y barra de XP de terminal.

🚀 Cómo Utilizar
1. Crear el Flujo de Trabajo (Workflow)
Crea un nuevo archivo en tu repositorio en .github/workflows/zombie-graph.yml y añade el siguiente código:

YAML
name: GitHub Zombie Survival Graph

on:
  push:
    branches:
      - main
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch: 

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Generate Zombie Survival Graph
        uses: achexus/github-zombie-graph@v1.1.2
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}

      - name: Commit and Push the generated SVG
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "chore: update zombie survival graph"
          file_pattern: zombie-graph.svg
⚠️ Nota Importante: Asegúrate de que tu repositorio permite a las Actions leer y escribir. Ve a Settings > Actions > General, desplázate hasta Workflow permissions y selecciona "Read and write permissions".

2. Actualizar el README
Añade el SVG generado al README.md de tu perfil:

HTML
<div align="center">
  <img src="zombie-graph.svg" alt="My Zombie Survival Status" />
</div>
Verwandle dein standardmäßiges GitHub-Beitragsdiagramm in ein postapokalyptisches taktisches Überlebenssystem! Diese GitHub Action generiert eine dynamische SVG, die deine Überlebenssträhne, eliminierte Zombies (Commits) und deinen taktischen Rang anzeigt.

🎯 Das Ziel & Mechanik
Überlebe die Apokalypse, indem du Code schreibst! Jeden Tag greifen Zombies (1-4) deinen Sektor an. Du musst genug Commits machen, um sie zu eliminieren.

Geräumt (Cleared): Commits >= Zombies. Sektor gesichert!

Überrannt (Invaded): Commits < Zombies. Der Sektor wird überrannt.

Überlebensserie (Streak): Wenn du an einem Tag 0 Commits machst, wird deine "Survival Day"-Serie auf 0 zurückgesetzt. Brich die Kette nicht!

🖥️ UI-Funktionen: Cyberpunk-Terminal-Ästhetik, dunkelrote "Corrupted System"-Farben, lokales Radar, Live-Kamera und Terminal-XP-Leiste.

🚀 Verwendung
1. Workflow Erstellen
Erstelle eine neue Datei in deinem Repository unter .github/workflows/zombie-graph.yml und füge den folgenden Code hinzu:

YAML
name: GitHub Zombie Survival Graph

on:
  push:
    branches:
      - main
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch: 

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Generate Zombie Survival Graph
        uses: achexus/github-zombie-graph@v1.1.2
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}

      - name: Commit and Push the generated SVG
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "chore: update zombie survival graph"
          file_pattern: zombie-graph.svg
⚠️ Wichtiger Hinweis: Stelle sicher, dass dein Repository Lese- und Schreibrechte für Actions erlaubt. Gehe zu Settings > Actions > General, scrolle zu Workflow permissions und wähle "Read and write permissions".

2. README Aktualisieren
Füge die generierte SVG-Datei zur README.md deines Profils hinzu:

HTML
<div align="center">
  <img src="zombie-graph.svg" alt="My Zombie Survival Status" />
</div>
Transformez votre graphique de contributions GitHub standard en un système de survie tactique post-apocalyptique ! Cette GitHub Action génère un SVG dynamique affichant votre série de survie, les zombies éliminés (commits) et votre rang tactique.

🎯 L'Objectif et Mécaniques
Survivez à l'apocalypse en écrivant du code ! Chaque jour, des zombies (1-4) attaquent votre secteur. Vous devez faire suffisamment de commits pour les éliminer.

Sécurisé (Cleared) : Commits >= Zombies. Secteur sécurisé !

Envahi (Invaded) : Commits < Zombies. Le secteur est envahi.

Série de survie (Streak) : Si vous faites 0 commit en un jour, votre série "Survival Day" retombe à 0. Ne brisez pas la chaîne !

🖥️ Interface : Esthétique de terminal cyberpunk, couleurs cramoisi sombre "Système Corrompu", radar local, caméra en direct et barre d'XP style terminal.

🚀 Comment l'utiliser
1. Créer le Workflow
Créez un nouveau fichier dans votre dépôt à l'emplacement .github/workflows/zombie-graph.yml et ajoutez le code suivant :

YAML
name: GitHub Zombie Survival Graph

on:
  push:
    branches:
      - main
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch: 

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Generate Zombie Survival Graph
        uses: achexus/github-zombie-graph@v1.1.2
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}

      - name: Commit and Push the generated SVG
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "chore: update zombie survival graph"
          file_pattern: zombie-graph.svg
⚠️ Remarque Importante : Assurez-vous que votre dépôt autorise les Actions à lire et écrire. Allez dans Settings > Actions > General, descendez jusqu'à Workflow permissions, et sélectionnez "Read and write permissions".

2. Mettre à jour votre README
Ajoutez le SVG généré au README.md de votre profil :

HTML
<div align="center">
  <img src="zombie-graph.svg" alt="My Zombie Survival Status" />
</div>
Trasforma il tuo grafico standard dei contributi di GitHub in un sistema tattico di sopravvivenza post-apocalittico! Questa GitHub Action genera un SVG dinamico che mostra la tua serie di sopravvivenza, gli zombie eliminati (commit) e il tuo grado tattico.

🎯 L'Obiettivo e Meccaniche
Sopravvivi all'apocalisse scrivendo codice! Ogni giorno, degli zombie (1-4) attaccano il tuo settore. Devi fare abbastanza commit per eliminarli.

Liberato (Cleared): Commit >= Zombie. Settore sicuro!

Invaso (Invaded): Commit < Zombie. Il settore è invaso.

Serie (Streak): Se fai 0 commit in un giorno, la tua serie "Survival Day" si azzera. Non spezzare la catena!

🖥️ Interfaccia: Estetica terminale cyberpunk, colori cremisi scuro "Sistema Corrotto", radar locale, live cam e barra XP da terminale.

🚀 Come Usarlo
1. Creare il Workflow
Crea un nuovo file nel tuo repository in .github/workflows/zombie-graph.yml e aggiungi il seguente codice:

YAML
name: GitHub Zombie Survival Graph

on:
  push:
    branches:
      - main
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch: 

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Generate Zombie Survival Graph
        uses: achexus/github-zombie-graph@v1.1.2
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}

      - name: Commit and Push the generated SVG
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "chore: update zombie survival graph"
          file_pattern: zombie-graph.svg
⚠️ Nota Importante: Assicurati che il tuo repository consenta alle Action di leggere e scrivere. Vai su Settings > Actions > General, scorri fino a Workflow permissions e seleziona "Read and write permissions".

2. Aggiornare il README
Aggiungi l'SVG generato al README.md del tuo profilo:

HTML
<div align="center">
  <img src="zombie-graph.svg" alt="My Zombie Survival Status" />
</div>
Transforme seu gráfico de contribuições padrão do GitHub em um sistema tático de sobrevivência pós-apocalíptico! Esta GitHub Action gera um SVG dinâmico mostrando sua sequência de sobrevivência, zumbis eliminados (commits) e rank tático.

🎯 O Objetivo e Mecânicas
Sobreviva ao apocalipse escrevendo código! Todos os dias, zumbis (1-4) atacam seu setor. Você deve fazer commits suficientes para eliminá-los.

Livre (Cleared): Commits >= Zumbis. Setor seguro!

Invadido (Invaded): Commits < Zumbis. O setor foi invadido.

Sequência (Streak): Se você fizer 0 commits em um dia, sua sequência de "Survival Day" zera. Não quebre a corrente!

🖥️ Interface: Estética de terminal cyberpunk, cores carmesim escuro "Sistema Corrompido", radar local, câmera ao vivo e barra de XP de terminal.

🚀 Como Usar
1. Criar o Workflow
Crie um novo arquivo no seu repositório em .github/workflows/zombie-graph.yml e adicione o seguinte código:

YAML
name: GitHub Zombie Survival Graph

on:
  push:
    branches:
      - main
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch: 

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Generate Zombie Survival Graph
        uses: achexus/github-zombie-graph@v1.1.2
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}

      - name: Commit and Push the generated SVG
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "chore: update zombie survival graph"
          file_pattern: zombie-graph.svg
⚠️ Nota Importante: Certifique-se de que seu repositório permite que as Actions leiam e escrevam. Vá para Settings > Actions > General, role até Workflow permissions e selecione "Read and write permissions".

2. Atualizar o README
Adicione o SVG gerado ao README.md do seu perfil:

HTML
<div align="center">
  <img src="zombie-graph.svg" alt="My Zombie Survival Status" />
</div>
Превратите ваш стандартный график активности GitHub в постапокалиптическую тактическую систему выживания! Этот GitHub Action создает динамический SVG, показывающий вашу серию выживания, уничтоженных зомби (коммиты) и тактический ранг.

🎯 Цель и Механика
Выживите в апокалипсисе, создавая код! Каждый день зомби (1-4) атакуют ваш сектор. Сделайте достаточно коммитов, чтобы уничтожить их.

Очищено (Cleared): Коммиты >= Зомби. Сектор в безопасности!

Захвачено (Invaded): Коммиты < Зомби. Сектор захвачен.

Серия выживания (Streak): Если вы сделаете 0 коммитов за день, ваша серия "Survival Day" сбросится до 0. Не прерывайте цепь!

🖥️ Интерфейс: Эстетика киберпанк-терминала, темно-бордовые цвета "Поврежденной системы", локальный радар, прямая трансляция и шкала XP в стиле терминала.

🚀 Как Использовать
1. Создайте рабочий процесс (Workflow)
Создайте новый файл в вашем репозитории по пути .github/workflows/zombie-graph.yml и добавьте следующий код:

YAML
name: GitHub Zombie Survival Graph

on:
  push:
    branches:
      - main
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch: 

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Generate Zombie Survival Graph
        uses: achexus/github-zombie-graph@v1.1.2
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}

      - name: Commit and Push the generated SVG
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "chore: update zombie survival graph"
          file_pattern: zombie-graph.svg
⚠️ Важное Примечание: Убедитесь, что ваш репозиторий разрешает Actions чтение и запись. Перейдите в Settings > Actions > General, прокрутите до Workflow permissions и выберите "Read and write permissions".

2. Обновите ваш README
Добавьте сгенерированный SVG в README.md вашего профиля:

HTML
<div align="center">
  <img src="zombie-graph.svg" alt="My Zombie Survival Status" />
</div>
Transformeer je standaard GitHub bijdragegrafiek in een post-apocalyptisch tactisch overlevingssysteem! Deze GitHub Action genereert een dynamische SVG die je overlevingsreeks, geëlimineerde zombies (commits) en tactische rang toont.

🎯 Het Doel & Mechanica
Overleef de apocalyps door code te schrijven! Elke dag vallen zombies (1-4) je sector aan. Je moet genoeg commits maken om ze te elimineren.

Gevrijwaard (Cleared): Commits >= Zombies. Sector veilig!

Overspoeld (Invaded): Commits < Zombies. De sector is overspoeld.

Overlevingsreeks (Streak): Als je 0 commits op een dag maakt, wordt je "Survival Day"-reeks gereset naar 0. Verbreek de ketting niet!

🖥️ Interface: Cyberpunk terminal esthetiek, donkerrode "Corrupted System" kleuren, lokale radar, live cam en terminal-stijl XP balk.

🚀 Hoe te Gebruiken
1. Maak de Workflow aan
Maak een nieuw bestand in je repository op .github/workflows/zombie-graph.yml en voeg de volgende code toe:

YAML
name: GitHub Zombie Survival Graph

on:
  push:
    branches:
      - main
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch: 

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Generate Zombie Survival Graph
        uses: achexus/github-zombie-graph@v1.1.2
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}

      - name: Commit and Push the generated SVG
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "chore: update zombie survival graph"
          file_pattern: zombie-graph.svg
⚠️ Belangrijke Opmerking: Zorg ervoor dat je repository Actions toestaat om te lezen en schrijven. Ga naar Settings > Actions > General, scrol naar Workflow permissions en selecteer "Read and write permissions".

2. Werk je README bij
Voeg de gegenereerde SVG toe aan de README.md van je profiel:

HTML
<div align="center">
  <img src="zombie-graph.svg" alt="My Zombie Survival Status" />
</div>
Przekształć swój standardowy wykres aktywności GitHub w postapokaliptyczny system taktycznego przetrwania! Ta akcja GitHub generuje dynamiczny SVG pokazujący Twoją serię przetrwania, wyeliminowane zombie (commity) i rangę taktyczną.

🎯 Cel i Mechanika
Przetrwaj apokalipsę pisząc kod! Codziennie zombie (1-4) atakują twój sektor. Musisz zrobić wystarczająco dużo commitów, aby ich wyeliminować.

Oczyszczono (Cleared): Commity >= Zombie. Sektor bezpieczny!

Zajęto (Invaded): Commity < Zombie. Sektor został zajęty.

Seria przetrwania (Streak): Jeśli w ciągu dnia zrobisz 0 commitów, twoja seria "Survival Day" zresetuje się do 0. Nie przerywaj łańcucha!

🖥️ Interfejs: Estetyka cyberpunkowego terminala, ciemnoszkarłatne kolory "Zepsutego Systemu", lokalny radar, kamera na żywo i pasek XP w stylu terminala.

🚀 Jak Używać
1. Utwórz Workflow
Utwórz nowy plik w swoim repozytorium pod adresem .github/workflows/zombie-graph.yml i dodaj następujący kod:

YAML
name: GitHub Zombie Survival Graph

on:
  push:
    branches:
      - main
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch: 

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Generate Zombie Survival Graph
        uses: achexus/github-zombie-graph@v1.1.2
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}

      - name: Commit and Push the generated SVG
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "chore: update zombie survival graph"
          file_pattern: zombie-graph.svg
⚠️ Ważna Uwaga: Upewnij się, że Twoje repozytorium zezwala Actions na odczyt i zapis. Przejdź do Settings > Actions > General, przewiń do Workflow permissions i wybierz "Read and write permissions".

2. Zaktualizuj README
Dodaj wygenerowany plik SVG do README.md w swoim profilu:

HTML
<div align="center">
  <img src="zombie-graph.svg" alt="My Zombie Survival Status" />
</div>
açıklamaları da kodun içinde verme kuralına uymamışsın senden uzun açıklamalar değil. açıklamaları belirlenmiş tek parça yapıştırılabilir kod istiyorum bekliyorum.

⚠️ Important Note: Ensure your repository allows Actions to read and write. Go to Settings > Actions > General, scroll down to Workflow permissions, and select "Read and write permissions".

2. Update your README
Add the generated SVG to your profile's README.md:

HTML
<div align="center">
  <img src="zombie-graph.svg" alt="My Zombie Survival Status" />
</div>
Klasik GitHub katkı grafiğinizi kıyamet sonrası taktiksel bir hayatta kalma sistemine dönüştürün! Bu GitHub Action, günlük GitHub aktivitenize dayanarak hayatta kalma serinizi, yok edilen zombileri (commit'ler) ve taktiksel rütbenizi gösteren dinamik bir SVG oluşturur.

🎯 Oyunun Amacı ve Mekanikler
Kod yazarak kıyametten sağ çıkın! Her gün, bölgenize rastgele sayıda (1-4) zombi saldırır. Onları yok etmek için yeterli sayıda GitHub commit'i atmalısınız.

Temizlendi (Cleared): Commit >= Zombi. Bölge güvende!

İstila Edildi (Invaded): Commit < Zombi. Bölge ele geçirildi.

Hayatta Kalma Serisi (Streak): Bir gün boyunca hiç commit atmazsanız (0 commit), "Survival Day" seriniz 0'a sıfırlanır. Zinciri kırmayın!

🖥️ Arayüz Özellikleri: Siberpunk terminal estetiği, çevrimdışı günler için "Bozulmuş Sistem" (koyu bordo) renkleri, yerel radar, canlı kamera ve terminal tarzı XP yükleme çubuğu.

🚀 Nasıl Kullanılır?
1. Workflow Dosyasını Oluşturun
Deponuzda .github/workflows/zombie-graph.yml yolunda yeni bir dosya oluşturun ve aşağıdaki kodu ekleyin:

YAML
name: GitHub Zombie Survival Graph

on:
  push:
    branches:
      - main # Her kod gönderdiğinizde grafiği günceller
  schedule:
    - cron: "0 0 * * *" # Her gece yarısı otomatik çalışır
  workflow_dispatch: # Manuel tetiklemeye izin verir

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Generate Zombie Survival Graph
        uses: achexus/github-zombie-graph@v1.1.2
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}

      - name: Commit and Push the generated SVG
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "chore: update zombie survival graph"
          file_pattern: zombie-graph.svg
⚠️ Önemli Not: Deponuzun Action'lar için okuma ve yazma iznine sahip olduğundan emin olun. Settings > Actions > General sekmesine gidin, en alttaki Workflow permissions kısmından "Read and write permissions" seçeneğini işaretleyip kaydedin.

2. README Dosyanızı Güncelleyin
Oluşturulan SVG dosyasını profilinizin README.md dosyasına ekleyin:

HTML
<div align="center">
  <img src="zombie-graph.svg" alt="My Zombie Survival Status" />
</div>
¡Transforma tu gráfico de contribuciones de GitHub estándar en un sistema táctico de supervivencia post-apocalíptico! Esta GitHub Action genera un SVG dinámico que muestra tu racha de supervivencia, zombis eliminados (commits) y rango táctico.

🎯 El Objetivo y Mecánicas
¡Sobrevive al apocalipsis escribiendo código! Cada día, un número de zombis (1-4) ataca tu sector. Debes hacer suficientes commits para eliminarlos.

Despejado (Cleared): Commits >= Zombis. ¡Sector asegurado!

Invadido (Invaded): Commits < Zombis. El sector ha sido invadido.

Racha (Streak): Si haces 0 commits en un día, tu racha de "Survival Day" se reinicia a 0. ¡No rompas la cadena!

🖥️ Interfaz: Estética de terminal ciberpunk, colores carmesí oscuro de "Sistema Corrupto", radar local, cámara en vivo y barra de XP de terminal.

🚀 Cómo Utilizar
1. Crear el Flujo de Trabajo (Workflow)
Crea un nuevo archivo en tu repositorio en .github/workflows/zombie-graph.yml y añade el siguiente código:

YAML
name: GitHub Zombie Survival Graph

on:
  push:
    branches:
      - main
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch: 

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Generate Zombie Survival Graph
        uses: achexus/github-zombie-graph@v1.1.2
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}

      - name: Commit and Push the generated SVG
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "chore: update zombie survival graph"
          file_pattern: zombie-graph.svg
⚠️ Nota Importante: Asegúrate de que tu repositorio permite a las Actions leer y escribir. Ve a Settings > Actions > General, desplázate hasta Workflow permissions y selecciona "Read and write permissions".

2. Actualizar el README
Añade el SVG generado al README.md de tu perfil:

HTML
<div align="center">
  <img src="zombie-graph.svg" alt="My Zombie Survival Status" />
</div>
Verwandle dein standardmäßiges GitHub-Beitragsdiagramm in ein postapokalyptisches taktisches Überlebenssystem! Diese GitHub Action generiert eine dynamische SVG, die deine Überlebenssträhne, eliminierte Zombies (Commits) und deinen taktischen Rang anzeigt.

🎯 Das Ziel & Mechanik
Überlebe die Apokalypse, indem du Code schreibst! Jeden Tag greifen Zombies (1-4) deinen Sektor an. Du musst genug Commits machen, um sie zu eliminieren.

Geräumt (Cleared): Commits >= Zombies. Sektor gesichert!

Überrannt (Invaded): Commits < Zombies. Der Sektor wird überrannt.

Überlebensserie (Streak): Wenn du an einem Tag 0 Commits machst, wird deine "Survival Day"-Serie auf 0 zurückgesetzt. Brich die Kette nicht!

🖥️ UI-Funktionen: Cyberpunk-Terminal-Ästhetik, dunkelrote "Corrupted System"-Farben, lokales Radar, Live-Kamera und Terminal-XP-Leiste.

🚀 Verwendung
1. Workflow Erstellen
Erstelle eine neue Datei in deinem Repository unter .github/workflows/zombie-graph.yml und füge den folgenden Code hinzu:

YAML
name: GitHub Zombie Survival Graph

on:
  push:
    branches:
      - main
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch: 

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Generate Zombie Survival Graph
        uses: achexus/github-zombie-graph@v1.1.2
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}

      - name: Commit and Push the generated SVG
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "chore: update zombie survival graph"
          file_pattern: zombie-graph.svg
⚠️ Wichtiger Hinweis: Stelle sicher, dass dein Repository Lese- und Schreibrechte für Actions erlaubt. Gehe zu Settings > Actions > General, scrolle zu Workflow permissions und wähle "Read and write permissions".

2. README Aktualisieren
Füge die generierte SVG-Datei zur README.md deines Profils hinzu:

HTML
<div align="center">
  <img src="zombie-graph.svg" alt="My Zombie Survival Status" />
</div>
Transformez votre graphique de contributions GitHub standard en un système de survie tactique post-apocalyptique ! Cette GitHub Action génère un SVG dynamique affichant votre série de survie, les zombies éliminés (commits) et votre rang tactique.

🎯 L'Objectif et Mécaniques
Survivez à l'apocalypse en écrivant du code ! Chaque jour, des zombies (1-4) attaquent votre secteur. Vous devez faire suffisamment de commits pour les éliminer.

Sécurisé (Cleared) : Commits >= Zombies. Secteur sécurisé !

Envahi (Invaded) : Commits < Zombies. Le secteur est envahi.

Série de survie (Streak) : Si vous faites 0 commit en un jour, votre série "Survival Day" retombe à 0. Ne brisez pas la chaîne !

🖥️ Interface : Esthétique de terminal cyberpunk, couleurs cramoisi sombre "Système Corrompu", radar local, caméra en direct et barre d'XP style terminal.

🚀 Comment l'utiliser
1. Créer le Workflow
Créez un nouveau fichier dans votre dépôt à l'emplacement .github/workflows/zombie-graph.yml et ajoutez le code suivant :

YAML
name: GitHub Zombie Survival Graph

on:
  push:
    branches:
      - main
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch: 

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Generate Zombie Survival Graph
        uses: achexus/github-zombie-graph@v1.1.2
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}

      - name: Commit and Push the generated SVG
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "chore: update zombie survival graph"
          file_pattern: zombie-graph.svg
⚠️ Remarque Importante : Assurez-vous que votre dépôt autorise les Actions à lire et écrire. Allez dans Settings > Actions > General, descendez jusqu'à Workflow permissions, et sélectionnez "Read and write permissions".

2. Mettre à jour votre README
Ajoutez le SVG généré au README.md de votre profil :

HTML
<div align="center">
  <img src="zombie-graph.svg" alt="My Zombie Survival Status" />
</div>
Trasforma il tuo grafico standard dei contributi di GitHub in un sistema tattico di sopravvivenza post-apocalittico! Questa GitHub Action genera un SVG dinamico che mostra la tua serie di sopravvivenza, gli zombie eliminati (commit) e il tuo grado tattico.

🎯 L'Obiettivo e Meccaniche
Sopravvivi all'apocalisse scrivendo codice! Ogni giorno, degli zombie (1-4) attaccano il tuo settore. Devi fare abbastanza commit per eliminarli.

Liberato (Cleared): Commit >= Zombie. Settore sicuro!

Invaso (Invaded): Commit < Zombie. Il settore è invaso.

Serie (Streak): Se fai 0 commit in un giorno, la tua serie "Survival Day" si azzera. Non spezzare la catena!

🖥️ Interfaccia: Estetica terminale cyberpunk, colori cremisi scuro "Sistema Corrotto", radar locale, live cam e barra XP da terminale.

🚀 Come Usarlo
1. Creare il Workflow
Crea un nuovo file nel tuo repository in .github/workflows/zombie-graph.yml e aggiungi il seguente codice:

YAML
name: GitHub Zombie Survival Graph

on:
  push:
    branches:
      - main
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch: 

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Generate Zombie Survival Graph
        uses: achexus/github-zombie-graph@v1.1.2
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}

      - name: Commit and Push the generated SVG
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "chore: update zombie survival graph"
          file_pattern: zombie-graph.svg
⚠️ Nota Importante: Assicurati che il tuo repository consenta alle Action di leggere e scrivere. Vai su Settings > Actions > General, scorri fino a Workflow permissions e seleziona "Read and write permissions".

2. Aggiornare il README
Aggiungi l'SVG generato al README.md del tuo profilo:

HTML
<div align="center">
  <img src="zombie-graph.svg" alt="My Zombie Survival Status" />
</div>
Transforme seu gráfico de contribuições padrão do GitHub em um sistema tático de sobrevivência pós-apocalíptico! Esta GitHub Action gera um SVG dinâmico mostrando sua sequência de sobrevivência, zumbis eliminados (commits) e rank tático.

🎯 O Objetivo e Mecânicas
Sobreviva ao apocalipse escrevendo código! Todos os dias, zumbis (1-4) atacam seu setor. Você deve fazer commits suficientes para eliminá-los.

Livre (Cleared): Commits >= Zumbis. Setor seguro!

Invadido (Invaded): Commits < Zumbis. O setor foi invadido.

Sequência (Streak): Se você fizer 0 commits em um dia, sua sequência de "Survival Day" zera. Não quebre a corrente!

🖥️ Interface: Estética de terminal cyberpunk, cores carmesim escuro "Sistema Corrompido", radar local, câmera ao vivo e barra de XP de terminal.

🚀 Como Usar
1. Criar o Workflow
Crie um novo arquivo no seu repositório em .github/workflows/zombie-graph.yml e adicione o seguinte código:

YAML
name: GitHub Zombie Survival Graph

on:
  push:
    branches:
      - main
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch: 

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Generate Zombie Survival Graph
        uses: achexus/github-zombie-graph@v1.1.2
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}

      - name: Commit and Push the generated SVG
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "chore: update zombie survival graph"
          file_pattern: zombie-graph.svg
⚠️ Nota Importante: Certifique-se de que seu repositório permite que as Actions leiam e escrevam. Vá para Settings > Actions > General, role até Workflow permissions e selecione "Read and write permissions".

2. Atualizar o README
Adicione o SVG gerado ao README.md do seu perfil:

HTML
<div align="center">
  <img src="zombie-graph.svg" alt="My Zombie Survival Status" />
</div>
Превратите ваш стандартный график активности GitHub в постапокалиптическую тактическую систему выживания! Этот GitHub Action создает динамический SVG, показывающий вашу серию выживания, уничтоженных зомби (коммиты) и тактический ранг.

🎯 Цель и Механика
Выживите в апокалипсисе, создавая код! Каждый день зомби (1-4) атакуют ваш сектор. Сделайте достаточно коммитов, чтобы уничтожить их.

Очищено (Cleared): Коммиты >= Зомби. Сектор в безопасности!

Захвачено (Invaded): Коммиты < Зомби. Сектор захвачен.

Серия выживания (Streak): Если вы сделаете 0 коммитов за день, ваша серия "Survival Day" сбросится до 0. Не прерывайте цепь!

🖥️ Интерфейс: Эстетика киберпанк-терминала, темно-бордовые цвета "Поврежденной системы", локальный радар, прямая трансляция и шкала XP в стиле терминала.

🚀 Как Использовать
1. Создайте рабочий процесс (Workflow)
Создайте новый файл в вашем репозитории по пути .github/workflows/zombie-graph.yml и добавьте следующий код:

YAML
name: GitHub Zombie Survival Graph

on:
  push:
    branches:
      - main
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch: 

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Generate Zombie Survival Graph
        uses: achexus/github-zombie-graph@v1.1.2
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}

      - name: Commit and Push the generated SVG
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "chore: update zombie survival graph"
          file_pattern: zombie-graph.svg
⚠️ Важное Примечание: Убедитесь, что ваш репозиторий разрешает Actions чтение и запись. Перейдите в Settings > Actions > General, прокрутите до Workflow permissions и выберите "Read and write permissions".

2. Обновите ваш README
Добавьте сгенерированный SVG в README.md вашего профиля:

HTML
<div align="center">
  <img src="zombie-graph.svg" alt="My Zombie Survival Status" />
</div>
Transformeer je standaard GitHub bijdragegrafiek in een post-apocalyptisch tactisch overlevingssysteem! Deze GitHub Action genereert een dynamische SVG die je overlevingsreeks, geëlimineerde zombies (commits) en tactische rang toont.

🎯 Het Doel & Mechanica
Overleef de apocalyps door code te schrijven! Elke dag vallen zombies (1-4) je sector aan. Je moet genoeg commits maken om ze te elimineren.

Gevrijwaard (Cleared): Commits >= Zombies. Sector veilig!

Overspoeld (Invaded): Commits < Zombies. De sector is overspoeld.

Overlevingsreeks (Streak): Als je 0 commits op een dag maakt, wordt je "Survival Day"-reeks gereset naar 0. Verbreek de ketting niet!

🖥️ Interface: Cyberpunk terminal esthetiek, donkerrode "Corrupted System" kleuren, lokale radar, live cam en terminal-stijl XP balk.

🚀 Hoe te Gebruiken
1. Maak de Workflow aan
Maak een nieuw bestand in je repository op .github/workflows/zombie-graph.yml en voeg de volgende code toe:

YAML
name: GitHub Zombie Survival Graph

on:
  push:
    branches:
      - main
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch: 

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Generate Zombie Survival Graph
        uses: achexus/github-zombie-graph@v1.1.2
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}

      - name: Commit and Push the generated SVG
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "chore: update zombie survival graph"
          file_pattern: zombie-graph.svg
⚠️ Belangrijke Opmerking: Zorg ervoor dat je repository Actions toestaat om te lezen en schrijven. Ga naar Settings > Actions > General, scrol naar Workflow permissions en selecteer "Read and write permissions".

2. Werk je README bij
Voeg de gegenereerde SVG toe aan de README.md van je profiel:

HTML
<div align="center">
  <img src="zombie-graph.svg" alt="My Zombie Survival Status" />
</div>
Przekształć swój standardowy wykres aktywności GitHub w postapokaliptyczny system taktycznego przetrwania! Ta akcja GitHub generuje dynamiczny SVG pokazujący Twoją serię przetrwania, wyeliminowane zombie (commity) i rangę taktyczną.

🎯 Cel i Mechanika
Przetrwaj apokalipsę pisząc kod! Codziennie zombie (1-4) atakują twój sektor. Musisz zrobić wystarczająco dużo commitów, aby ich wyeliminować.

Oczyszczono (Cleared): Commity >= Zombie. Sektor bezpieczny!

Zajęto (Invaded): Commity < Zombie. Sektor został zajęty.

Seria przetrwania (Streak): Jeśli w ciągu dnia zrobisz 0 commitów, twoja seria "Survival Day" zresetuje się do 0. Nie przerywaj łańcucha!

🖥️ Interfejs: Estetyka cyberpunkowego terminala, ciemnoszkarłatne kolory "Zepsutego Systemu", lokalny radar, kamera na żywo i pasek XP w stylu terminala.

🚀 Jak Używać
1. Utwórz Workflow
Utwórz nowy plik w swoim repozytorium pod adresem .github/workflows/zombie-graph.yml i dodaj następujący kod:

YAML
name: GitHub Zombie Survival Graph

on:
  push:
    branches:
      - main
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch: 

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Generate Zombie Survival Graph
        uses: achexus/github-zombie-graph@v1.1.2
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}

      - name: Commit and Push the generated SVG
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "chore: update zombie survival graph"
          file_pattern: zombie-graph.svg
⚠️ Ważna Uwaga: Upewnij się, że Twoje repozytorium zezwala Actions na odczyt i zapis. Przejdź do Settings > Actions > General, przewiń do Workflow permissions i wybierz "Read and write permissions".

2. Zaktualizuj README
Dodaj wygenerowany plik SVG do README.md w swoim profilu:

HTML
<div align="center">
  <img src="zombie-graph.svg" alt="My Zombie Survival Status" />
</div>
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
    
print("[file-tag: code-generated-file-readme-md]")
write_readme()


```text?code_stdout&code_event_index=1
[file-tag: code-generated-file-readme-md]

Your Markdown file is ready

MD icon
README
 MD 
Open
This file contains the complete, updated README content as requested.




Gemini is AI and can make mistakes.

Analyzing
# 🧟‍♂️ GitHub Zombie Survival Graph

<div align="center">
  <table>
    <tr>
      <td align="center"><a href="#english">🇬🇧 English</a></td>
      <td align="center"><a href="#turkce">🇹🇷 Türkçe</a></td>
      <td align="center"><a href="#espanol">🇪🇸 Español</a></td>
      <td align="center"><a href="#deutsch">🇩🇪 Deutsch</a></td>
      <td align="center"><a href="#francais">🇫🇷 Français</a></td>
    </tr>
    <tr>
      <td align="center"><a href="#italiano">🇮🇹 Italiano</a></td>
      <td align="center"><a href="#portugues">🇵🇹 Português</a></td>
      <td align="center"><a href="#русский">🇷🇺 Русский</a></td>
      <td align="center"><a href="#nederlands">🇳🇱 Nederlands</a></td>
      <td align="center"><a href="#polski">🇵🇱 Polski</a></td>
    </tr>
  </table>
</div>

<br>

<div align="center">
  <img src="zombie-graph.svg" alt="GitHub Zombie Survival Graph" />
</div>

---

<h2 id="english">🇬🇧 English</h2>

Transform your standard GitHub contribution graph into a post-apocalyptic tactical survival system! This GitHub Action generates a dynamic SVG showing your survival streak, eliminated zombies (commits), and tactical rank based on your daily GitHub activity.

### 🎯 The Goal & Mechanics
Survive the apocalypse by writing code! Every day, a deterministic number of zombies (1 to 4) attacks your sector. You must make enough GitHub commits to eliminate them.
* **Cleared:** Your Commits >= Zombies. Sector secured!
* **Invaded:** Your Commits < Zombies. The sector is overrun.
* **Survival Streak:** If you make **0 commits** in a day, your active "Survival Day" streak resets to 0. Don't break the chain!
* **🖥️ UI Features:** Cyberpunk terminal aesthetics, "Corrupted System" dark crimson colors for offline/invaded days, a local radar, live cam, and a terminal-style XP loading bar.

### 🚀 How to Use

**1. Create the Workflow**
Create a new file in your repository at `.github/workflows/zombie-graph.yml` and add the following code:

```yaml
name: GitHub Zombie Survival Graph

on:
  push:
    branches:
      - main # Updates the graph every time you push code
  schedule:
    - cron: "0 0 * * *" # Runs automatically every midnight
  workflow_dispatch: # Allows manual trigger

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Generate Zombie Survival Graph
        uses: achexus/github-zombie-graph@v1.1.2
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}

      - name: Commit and Push the generated SVG
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "chore: update zombie survival graph"
          file_pattern: zombie-graph.svg
```

> **⚠️ Important Note:** Ensure your repository allows Actions to read and write. Go to **Settings > Actions > General**, scroll down to **Workflow permissions**, and select **"Read and write permissions"**.

**2. Update your README**
Add the generated SVG to your profile's `README.md`:

```html
<div align="center">
  <img src="zombie-graph.svg" alt="My Zombie Survival Status" />
</div>
```

---

<h2 id="turkce">🇹🇷 Türkçe</h2>

Klasik GitHub katkı grafiğinizi kıyamet sonrası taktiksel bir hayatta kalma sistemine dönüştürün! Bu GitHub Action, günlük GitHub aktivitenize dayanarak hayatta kalma serinizi, yok edilen zombileri (commit'ler) ve taktiksel rütbenizi gösteren dinamik bir SVG oluşturur.

### 🎯 Oyunun Amacı ve Mekanikler
Kod yazarak kıyametten sağ çıkın! Her gün, bölgenize rastgele sayıda (1-4) zombi saldırır. Onları yok etmek için yeterli sayıda GitHub commit'i atmalısınız.
* **Temizlendi (Cleared):** Commit >= Zombi. Bölge güvende!
* **İstila Edildi (Invaded):** Commit < Zombi. Bölge ele geçirildi.
* **Hayatta Kalma Serisi (Streak):** Bir gün boyunca hiç commit atmazsanız (0 commit), "Survival Day" seriniz 0'a sıfırlanır. Zinciri kırmayın!
* **🖥️ Arayüz Özellikleri:** Siberpunk terminal estetiği, çevrimdışı günler için "Bozulmuş Sistem" (koyu bordo) renkleri, yerel radar, canlı kamera ve terminal tarzı XP yükleme çubuğu.

### 🚀 Nasıl Kullanılır?

**1. Workflow Dosyasını Oluşturun**
Deponuzda `.github/workflows/zombie-graph.yml` yolunda yeni bir dosya oluşturun ve aşağıdaki kodu ekleyin:

```yaml
name: GitHub Zombie Survival Graph

on:
  push:
    branches:
      - main # Her kod gönderdiğinizde grafiği günceller
  schedule:
    - cron: "0 0 * * *" # Her gece yarısı otomatik çalışır
  workflow_dispatch: # Manuel tetiklemeye izin verir

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Generate Zombie Survival Graph
        uses: achexus/github-zombie-graph@v1.1.2
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}

      - name: Commit and Push the generated SVG
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "chore: update zombie survival graph"
          file_pattern: zombie-graph.svg
```

> **⚠️ Önemli Not:** Deponuzun Action'lar için okuma ve yazma iznine sahip olduğundan emin olun. **Settings > Actions > General** sekmesine gidin, en alttaki **Workflow permissions** kısmından **"Read and write permissions"** seçeneğini işaretleyip kaydedin.

**2. README Dosyanızı Güncelleyin**
Oluşturulan SVG dosyasını profilinizin `README.md` dosyasına ekleyin:

```html
<div align="center">
  <img src="zombie-graph.svg" alt="My Zombie Survival Status" />
</div>
```

---

<h2 id="espanol">🇪🇸 Español</h2>

¡Transforma tu gráfico de contribuciones de GitHub estándar en un sistema táctico de supervivencia post-apocalíptico! Esta GitHub Action genera un SVG dinámico que muestra tu racha de supervivencia, zombis eliminados (commits) y rango táctico.

### 🎯 El Objetivo y Mecánicas
¡Sobrevive al apocalipsis escribiendo código! Cada día, un número de zombis (1-4) ataca tu sector. Debes hacer suficientes commits para eliminarlos.
* **Despejado (Cleared):** Commits >= Zombis. ¡Sector asegurado!
* **Invadido (Invaded):** Commits < Zombis. El sector ha sido invadido.
* **Racha (Streak):** Si haces **0 commits** en un día, tu racha de "Survival Day" se reinicia a 0. ¡No rompas la cadena!
* **🖥️ Interfaz:** Estética de terminal ciberpunk, colores carmesí oscuro de "Sistema Corrupto", radar local, cámara en vivo y barra de XP de terminal.

### 🚀 Cómo Utilizar

**1. Crear el Flujo de Trabajo (Workflow)**
Crea un nuevo archivo en tu repositorio en `.github/workflows/zombie-graph.yml` y añade el siguiente código:

```yaml
name: GitHub Zombie Survival Graph

on:
  push:
    branches:
      - main
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch: 

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Generate Zombie Survival Graph
        uses: achexus/github-zombie-graph@v1.1.2
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}

      - name: Commit and Push the generated SVG
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "chore: update zombie survival graph"
          file_pattern: zombie-graph.svg
```

> **⚠️ Nota Importante:** Asegúrate de que tu repositorio permite a las Actions leer y escribir. Ve a **Settings > Actions > General**, desplázate hasta **Workflow permissions** y selecciona **"Read and write permissions"**.

**2. Actualizar el README**
Añade el SVG generado al `README.md` de tu perfil:

```html
<div align="center">
  <img src="zombie-graph.svg" alt="My Zombie Survival Status" />
</div>
```

---

<h2 id="deutsch">🇩🇪 Deutsch</h2>

Verwandle dein standardmäßiges GitHub-Beitragsdiagramm in ein postapokalyptisches taktisches Überlebenssystem! Diese GitHub Action generiert eine dynamische SVG, die deine Überlebenssträhne, eliminierte Zombies (Commits) und deinen taktischen Rang anzeigt.

### 🎯 Das Ziel & Mechanik
Überlebe die Apokalypse, indem du Code schreibst! Jeden Tag greifen Zombies (1-4) deinen Sektor an. Du musst genug Commits machen, um sie zu eliminieren.
* **Geräumt (Cleared):** Commits >= Zombies. Sektor gesichert!
* **Überrannt (Invaded):** Commits < Zombies. Der Sektor wird überrannt.
* **Überlebensserie (Streak):** Wenn du an einem Tag **0 Commits** machst, wird deine "Survival Day"-Serie auf 0 zurückgesetzt. Brich die Kette nicht!
* **🖥️ UI-Funktionen:** Cyberpunk-Terminal-Ästhetik, dunkelrote "Corrupted System"-Farben, lokales Radar, Live-Kamera und Terminal-XP-Leiste.

### 🚀 Verwendung

**1. Workflow Erstellen**
Erstelle eine neue Datei in deinem Repository unter `.github/workflows/zombie-graph.yml` und füge den folgenden Code hinzu:

```yaml
name: GitHub Zombie Survival Graph

on:
  push:
    branches:
      - main
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch: 

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Generate Zombie Survival Graph
        uses: achexus/github-zombie-graph@v1.1.2
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}

      - name: Commit and Push the generated SVG
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "chore: update zombie survival graph"
          file_pattern: zombie-graph.svg
```

> **⚠️ Wichtiger Hinweis:** Stelle sicher, dass dein Repository Lese- und Schreibrechte für Actions erlaubt. Gehe zu **Settings > Actions > General**, scrolle zu **Workflow permissions** und wähle **"Read and write permissions"**.

**2. README Aktualisieren**
Füge die generierte SVG-Datei zur `README.md` deines Profils hinzu:

```html
<div align="center">
  <img src="zombie-graph.svg" alt="My Zombie Survival Status" />
</div>
```

---

<h2 id="francais">🇫🇷 Français</h2>

Transformez votre graphique de contributions GitHub standard en un système de survie tactique post-apocalyptique ! Cette GitHub Action génère un SVG dynamique affichant votre série de survie, les zombies éliminés (commits) et votre rang tactique.

### 🎯 L'Objectif et Mécaniques
Survivez à l'apocalypse en écrivant du code ! Chaque jour, des zombies (1-4) attaquent votre secteur. Vous devez faire suffisamment de commits pour les éliminer.
* **Sécurisé (Cleared) :** Commits >= Zombies. Secteur sécurisé !
* **Envahi (Invaded) :** Commits < Zombies. Le secteur est envahi.
* **Série de survie (Streak) :** Si vous faites **0 commit** en un jour, votre série "Survival Day" retombe à 0. Ne brisez pas la chaîne !
* **🖥️ Interface :** Esthétique de terminal cyberpunk, couleurs cramoisi sombre "Système Corrompu", radar local, caméra en direct et barre d'XP style terminal.

### 🚀 Comment l'utiliser

**1. Créer le Workflow**
Créez un nouveau fichier dans votre dépôt à l'emplacement `.github/workflows/zombie-graph.yml` et ajoutez le code suivant :

```yaml
name: GitHub Zombie Survival Graph

on:
  push:
    branches:
      - main
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch: 

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Generate Zombie Survival Graph
        uses: achexus/github-zombie-graph@v1.1.2
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}

      - name: Commit and Push the generated SVG
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "chore: update zombie survival graph"
          file_pattern: zombie-graph.svg
```

> **⚠️ Remarque Importante :** Assurez-vous que votre dépôt autorise les Actions à lire et écrire. Allez dans **Settings > Actions > General**, descendez jusqu'à **Workflow permissions**, et sélectionnez **"Read and write permissions"**.

**2. Mettre à jour votre README**
Ajoutez le SVG généré au `README.md` de votre profil :

```html
<div align="center">
  <img src="zombie-graph.svg" alt="My Zombie Survival Status" />
</div>
```

---

<h2 id="italiano">🇮🇹 Italiano</h2>

Trasforma il tuo grafico standard dei contributi di GitHub in un sistema tattico di sopravvivenza post-apocalittico! Questa GitHub Action genera un SVG dinamico che mostra la tua serie di sopravvivenza, gli zombie eliminati (commit) e il tuo grado tattico.

### 🎯 L'Obiettivo e Meccaniche
Sopravvivi all'apocalisse scrivendo codice! Ogni giorno, degli zombie (1-4) attaccano il tuo settore. Devi fare abbastanza commit per eliminarli.
* **Liberato (Cleared):** Commit >= Zombie. Settore sicuro!
* **Invaso (Invaded):** Commit < Zombie. Il settore è invaso.
* **Serie (Streak):** Se fai **0 commit** in un giorno, la tua serie "Survival Day" si azzera. Non spezzare la catena!
* **🖥️ Interfaccia:** Estetica terminale cyberpunk, colori cremisi scuro "Sistema Corrotto", radar locale, live cam e barra XP da terminale.

### 🚀 Come Usarlo

**1. Creare il Workflow**
Crea un nuovo file nel tuo repository in `.github/workflows/zombie-graph.yml` e aggiungi il seguente codice:

```yaml
name: GitHub Zombie Survival Graph

on:
  push:
    branches:
      - main
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch: 

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Generate Zombie Survival Graph
        uses: achexus/github-zombie-graph@v1.1.2
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}

      - name: Commit and Push the generated SVG
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "chore: update zombie survival graph"
          file_pattern: zombie-graph.svg
```

> **⚠️ Nota Importante:** Assicurati che il tuo repository consenta alle Action di leggere e scrivere. Vai su **Settings > Actions > General**, scorri fino a **Workflow permissions** e seleziona **"Read and write permissions"**.

**2. Aggiornare il README**
Aggiungi l'SVG generato al `README.md` del tuo profilo:

```html
<div align="center">
  <img src="zombie-graph.svg" alt="My Zombie Survival Status" />
</div>
```

---

<h2 id="portugues">🇵🇹 Português</h2>

Transforme seu gráfico de contribuições padrão do GitHub em um sistema tático de sobrevivência pós-apocalíptico! Esta GitHub Action gera um SVG dinâmico mostrando sua sequência de sobrevivência, zumbis eliminados (commits) e rank tático.

### 🎯 O Objetivo e Mecânicas
Sobreviva ao apocalipse escrevendo código! Todos os dias, zumbis (1-4) atacam seu setor. Você deve fazer commits suficientes para eliminá-los.
* **Livre (Cleared):** Commits >= Zumbis. Setor seguro!
* **Invadido (Invaded):** Commits < Zumbis. O setor foi invadido.
* **Sequência (Streak):** Se você fizer **0 commits** em um dia, sua sequência de "Survival Day" zera. Não quebre a corrente!
* **🖥️ Interface:** Estética de terminal cyberpunk, cores carmesim escuro "Sistema Corrompido", radar local, câmera ao vivo e barra de XP de terminal.

### 🚀 Como Usar

**1. Criar o Workflow**
Crie um novo arquivo no seu repositório em `.github/workflows/zombie-graph.yml` e adicione o seguinte código:

```yaml
name: GitHub Zombie Survival Graph

on:
  push:
    branches:
      - main
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch: 

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Generate Zombie Survival Graph
        uses: achexus/github-zombie-graph@v1.1.2
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}

      - name: Commit and Push the generated SVG
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "chore: update zombie survival graph"
          file_pattern: zombie-graph.svg
```

> **⚠️ Nota Importante:** Certifique-se de que seu repositório permite que as Actions leiam e escrevam. Vá para **Settings > Actions > General**, role até **Workflow permissions** e selecione **"Read and write permissions"**.

**2. Atualizar o README**
Adicione o SVG gerado ao `README.md` do seu perfil:

```html
<div align="center">
  <img src="zombie-graph.svg" alt="My Zombie Survival Status" />
</div>
```

---

<h2 id="русский">🇷🇺 Русский</h2>

Превратите ваш стандартный график активности GitHub в постапокалиптическую тактическую систему выживания! Этот GitHub Action создает динамический SVG, показывающий вашу серию выживания, уничтоженных зомби (коммиты) и тактический ранг.

### 🎯 Цель и Механика
Выживите в апокалипсисе, создавая код! Каждый день зомби (1-4) атакуют ваш сектор. Сделайте достаточно коммитов, чтобы уничтожить их.
* **Очищено (Cleared):** Коммиты >= Зомби. Сектор в безопасности!
* **Захвачено (Invaded):** Коммиты < Зомби. Сектор захвачен.
* **Серия выживания (Streak):** Если вы сделаете **0 коммитов** за день, ваша серия "Survival Day" сбросится до 0. Не прерывайте цепь!
* **🖥️ Интерфейс:** Эстетика киберпанк-терминала, темно-бордовые цвета "Поврежденной системы", локальный радар, прямая трансляция и шкала XP в стиле терминала.

### 🚀 Как Использовать

**1. Создайте рабочий процесс (Workflow)**
Создайте новый файл в вашем репозитории по пути `.github/workflows/zombie-graph.yml` и добавьте следующий код:

```yaml
name: GitHub Zombie Survival Graph

on:
  push:
    branches:
      - main
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch: 

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Generate Zombie Survival Graph
        uses: achexus/github-zombie-graph@v1.1.2
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}

      - name: Commit and Push the generated SVG
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "chore: update zombie survival graph"
          file_pattern: zombie-graph.svg
```

> **⚠️ Важное Примечание:** Убедитесь, что ваш репозиторий разрешает Actions чтение и запись. Перейдите в **Settings > Actions > General**, прокрутите до **Workflow permissions** и выберите **"Read and write permissions"**.

**2. Обновите ваш README**
Добавьте сгенерированный SVG в `README.md` вашего профиля:

```html
<div align="center">
  <img src="zombie-graph.svg" alt="My Zombie Survival Status" />
</div>
```

---

<h2 id="nederlands">🇳🇱 Nederlands</h2>

Transformeer je standaard GitHub bijdragegrafiek in een post-apocalyptisch tactisch overlevingssysteem! Deze GitHub Action genereert een dynamische SVG die je overlevingsreeks, geëlimineerde zombies (commits) en tactische rang toont.

### 🎯 Het Doel & Mechanica
Overleef de apocalyps door code te schrijven! Elke dag vallen zombies (1-4) je sector aan. Je moet genoeg commits maken om ze te elimineren.
* **Gevrijwaard (Cleared):** Commits >= Zombies. Sector veilig!
* **Overspoeld (Invaded):** Commits < Zombies. De sector is overspoeld.
* **Overlevingsreeks (Streak):** Als je **0 commits** op een dag maakt, wordt je "Survival Day"-reeks gereset naar 0. Verbreek de ketting niet!
* **🖥️ Interface:** Cyberpunk terminal esthetiek, donkerrode "Corrupted System" kleuren, lokale radar, live cam en terminal-stijl XP balk.

### 🚀 Hoe te Gebruiken

**1. Maak de Workflow aan**
Maak een nieuw bestand in je repository op `.github/workflows/zombie-graph.yml` en voeg de volgende code toe:

```yaml
name: GitHub Zombie Survival Graph

on:
  push:
    branches:
      - main
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch: 

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Generate Zombie Survival Graph
        uses: achexus/github-zombie-graph@v1.1.2
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}

      - name: Commit and Push the generated SVG
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "chore: update zombie survival graph"
          file_pattern: zombie-graph.svg
```

> **⚠️ Belangrijke Opmerking:** Zorg ervoor dat je repository Actions toestaat om te lezen en schrijven. Ga naar **Settings > Actions > General**, scrol naar **Workflow permissions** en selecteer **"Read and write permissions"**.

**2. Werk je README bij**
Voeg de gegenereerde SVG toe aan de `README.md` van je profiel:

```html
<div align="center">
  <img src="zombie-graph.svg" alt="My Zombie Survival Status" />
</div>
```

---

<h2 id="polski">🇵🇱 Polski</h2>

Przekształć swój standardowy wykres aktywności GitHub w postapokaliptyczny system taktycznego przetrwania! Ta akcja GitHub generuje dynamiczny SVG pokazujący Twoją serię przetrwania, wyeliminowane zombie (commity) i rangę taktyczną.

### 🎯 Cel i Mechanika
Przetrwaj apokalipsę pisząc kod! Codziennie zombie (1-4) atakują twój sektor. Musisz zrobić wystarczająco dużo commitów, aby ich wyeliminować.
* **Oczyszczono (Cleared):** Commity >= Zombie. Sektor bezpieczny!
* **Zajęto (Invaded):** Commity < Zombie. Sektor został zajęty.
* **Seria przetrwania (Streak):** Jeśli w ciągu dnia zrobisz **0 commitów**, twoja seria "Survival Day" zresetuje się do 0. Nie przerywaj łańcucha!
* **🖥️ Interfejs:** Estetyka cyberpunkowego terminala, ciemnoszkarłatne kolory "Zepsutego Systemu", lokalny radar, kamera na żywo i pasek XP w stylu terminala.

### 🚀 Jak Używać

**1. Utwórz Workflow**
Utwórz nowy plik w swoim repozytorium pod adresem `.github/workflows/zombie-graph.yml` i dodaj następujący kod:

```yaml
name: GitHub Zombie Survival Graph

on:
  push:
    branches:
      - main
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch: 

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Generate Zombie Survival Graph
        uses: achexus/github-zombie-graph@v1.1.2
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}

      - name: Commit and Push the generated SVG
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "chore: update zombie survival graph"
          file_pattern: zombie-graph.svg
```

> **⚠️ Ważna Uwaga:** Upewnij się, że Twoje repozytorium zezwala Actions na odczyt i zapis. Przejdź do **Settings > Actions > General**, przewiń do **Workflow permissions** i wybierz **"Read and write permissions"**.

**2. Zaktualizuj README**
Dodaj wygenerowany plik SVG do `README.md` w swoim profilu:

```html
<div align="center">
  <img src="zombie-graph.svg" alt="My Zombie Survival Status" />
</div>
```
README.md
Displaying README.md.
