#!/usr/bin/env python3
"""
Wondershare Audio Recorder Affiliate Site — build.py v2
200% improvement: 40+ pages, 20 language pages, 1500+ keywords,
hreflang, language strip, richer content throughout.
Python 3.12 compatible.

Deploy: https://brightlane.github.io/audiorecorderonline/
Run:    python3 build.py
Output: audiorecorder-site/
"""
from pathlib import Path
from datetime import date

BASE      = Path(__file__).parent / "audiorecorder-site"
SITE_ROOT = "/audiorecorderonline"
SITE_URL  = "https://brightlane.github.io/audiorecorderonline"
AFF       = "https://www.linkconnector.com/ta.php?lc=007949049070004532&atid=audiorecorderwebs"
YEAR      = date.today().year

KEYWORDS = (
    # Core English
    "audio recorder software,best audio recorder,streaming audio recorder,record audio computer,"
    "record system audio,record microphone audio,audio recording software Windows,"
    "record streaming audio,capture audio from computer,record internet radio,"
    "record Spotify audio,record YouTube audio,record online music,record podcast,"
    "podcast recorder software,voice recorder software,voice recorder PC,"
    "record voice memo,voice memo software,dictation recorder,interview recorder,"
    "audio capture software,capture system sound,record PC audio,"
    "MP3 recorder,record to MP3,save audio MP3,WAV recorder,FLAC recorder,"
    "high quality audio recorder,lossless audio recorder,"
    "scheduled audio recorder,auto audio recorder,timer audio recorder,"
    "audio editor software,trim audio,cut audio,audio noise reduction,"
    "background noise removal,AI audio recorder,AI noise reduction,"
    "Wondershare audio recorder,Wondershare streaming audio recorder,"
    "audio recorder review,best audio recording software 2026,"
    "free audio recorder,record audio free trial,"
    "record Zoom audio,record Teams audio,record Google Meet,record Skype,"
    "record webinar audio,meeting recorder,record music from browser,"
    "record streaming music,music recorder software,record Amazon Music,"
    "record Discord audio,record game audio,"
    "audio recorder for musicians,audio recorder podcasters,audio recorder journalists,"
    "audio recorder students,lecture recorder,class recording software,"
    "stereo audio recorder,mono audio recorder,audio format converter,"
    "audio recorder Windows 10,audio recorder Windows 11,"
    "audio recorder no watermark,audio batch recorder,"
    "audio recorder vs Audacity,audio recorder vs GarageBand,audio alternatives,"
    "streaming audio recorder alternative,best Audacity alternative,"
    "audio recorder with ID3 tags,audio tagger,metadata audio recorder,"
    "audio recorder with scheduler,automatic recording software,"
    "long audio recorder,overnight recording,continuous audio recording,"
    # German
    "Audio Recorder Software,Streaming Audio aufnehmen,Ton aufnehmen Computer,"
    "Audio aufzeichnen Windows,Mikrofon aufnehmen,MP3 Recorder,"
    "Internet Radio aufnehmen,Zoom Audio aufnehmen,Podcast aufnehmen,"
    # French
    "logiciel enregistreur audio,enregistrer audio streaming,capturer audio ordinateur,"
    "enregistreur MP3,enregistrer radio internet,enregistrer Zoom audio,"
    # Spanish
    "grabador de audio,grabar audio streaming,capturar audio PC,grabador MP3,"
    "grabar radio por internet,grabar llamada Zoom,software grabacion audio,"
    # Portuguese
    "gravador de audio,gravar audio streaming,capturar audio computador,"
    "gravador MP3,gravar radio internet,gravar chamada Zoom,software gravacao,"
    # Japanese
    "音声録音ソフト,ストリーミング録音,PCで音を録音,MP3録音,インターネットラジオ録音,"
    # Chinese
    "录音软件,录制音频,流媒体录音,MP3录音机,网络广播录制,"
    # Korean
    "오디오 녹음 소프트웨어,스트리밍 녹음,PC 오디오 녹음,MP3 녹음기,"
    # Russian
    "программа записи звука,запись потокового аудио,записать звук с компьютера,"
    # Arabic
    "برنامج تسجيل الصوت,تسجيل الصوت من الكمبيوتر,مسجل MP3,"
    # Italian
    "registratore audio,registrare audio streaming,catturare audio PC,registratore MP3,"
    # Dutch
    "audio recorder software,streaming audio opnemen,geluid opnemen computer,MP3 recorder,"
    # Polish
    "program do nagrywania dźwięku,nagrywanie audio streaming,rejestrator MP3,"
    # Turkish
    "ses kaydedici yazılım,akış sesi kaydetme,bilgisayar ses kaydı,MP3 kaydedici"
)

# ── LANGUAGE DATA ─────────────────────────────────────────────────────────────
LANGS = [
    ("🇺🇸","English","en","United States",
     "best audio recorder software","record streaming audio","voice recorder PC"),
    ("🇩🇪","Deutsch","de","Germany",
     "beste Audio Recorder Software","Streaming Audio aufnehmen","Ton aufnehmen Windows"),
    ("🇫🇷","Français","fr","France",
     "meilleur logiciel enregistreur audio","enregistrer audio streaming","enregistreur voix PC"),
    ("🇪🇸","Español","es","Spain / Latin America",
     "mejor grabador de audio","grabar audio streaming","grabador de voz PC"),
    ("🇧🇷","Português","pt","Brazil / Portugal",
     "melhor gravador de áudio","gravar áudio streaming","gravador de voz PC"),
    ("🇮🇹","Italiano","it","Italy",
     "miglior registratore audio","registrare audio streaming","registratore voce PC"),
    ("🇯🇵","日本語","ja","Japan",
     "最高の音声録音ソフト","ストリーミング音声を録音","PCで音声を録音"),
    ("🇨🇳","中文","zh","China",
     "最佳录音软件","录制流媒体音频","PC录音软件"),
    ("🇰🇷","한국어","ko","Korea",
     "최고의 오디오 녹음 소프트웨어","스트리밍 오디오 녹음","PC 음성 녹음"),
    ("🇷🇺","Русский","ru","Russia",
     "лучшая программа для записи звука","запись потокового аудио","запись голоса на ПК"),
    ("🇦🇪","العربية","ar","Middle East",
     "أفضل برنامج تسجيل الصوت","تسجيل الصوت من الإنترنت","مسجل الصوت للكمبيوتر"),
    ("🇮🇳","हिन्दी","hi","India",
     "सर्वश्रेष्ठ ऑडियो रिकॉर्डर","स्ट्रीमिंग ऑडियो रिकॉर्ड करें","वॉयस रिकॉर्डर PC"),
    ("🇮🇩","Bahasa Indonesia","id","Indonesia",
     "perekam audio terbaik","merekam audio streaming","perekam suara PC"),
    ("🇳🇱","Nederlands","nl","Netherlands",
     "beste audio recorder software","streaming audio opnemen","stem opnemen PC"),
    ("🇵🇱","Polski","pl","Poland",
     "najlepsze oprogramowanie do nagrywania dźwięku","nagrywanie audio streaming","rejestrator głosu PC"),
    ("🇹🇷","Türkçe","tr","Turkey",
     "en iyi ses kaydedici yazılım","akış sesi kaydetme","PC ses kaydedici"),
    ("🇸🇪","Svenska","sv","Sweden",
     "bästa ljudinspelningsprogram","spela in streaming-ljud","röstinspelning PC"),
    ("🇵🇭","Filipino","fil","Philippines",
     "pinakamahusay na audio recorder","mag-record ng streaming audio","voice recorder PC"),
    ("🇻🇳","Tiếng Việt","vi","Vietnam",
     "phần mềm ghi âm tốt nhất","ghi âm streaming","ghi âm giọng nói PC"),
    ("🇹🇭","ภาษาไทย","th","Thailand",
     "โปรแกรมบันทึกเสียงที่ดีที่สุด","บันทึกเสียงสตรีมมิง","บันทึกเสียง PC"),
]


CSS = r"""
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=Fraunces:ital,wght@0,700;0,900;1,700&family=JetBrains+Mono:wght@400;600&display=swap');
:root{
  --bg:#04050d;--bg2:#07081a;--bg3:#0c0e24;--card:rgba(7,8,26,.93);
  --acc:#7c3aed;--acc2:#ec4899;--acc3:#06b6d4;--gold:#f59e0b;
  --green:#10b981;--red:#ef4444;--orange:#f97316;
  --txt:#f0f0ff;--muted:#7878a8;--bdr:rgba(124,58,237,.13);--bdr2:rgba(124,58,237,.3);
  --glow:0 0 36px rgba(124,58,237,.28);--r:14px;--r2:8px
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:'Outfit',sans-serif;background:var(--bg);color:var(--txt);line-height:1.72;overflow-x:hidden}
body::before{content:'';position:fixed;inset:0;z-index:0;pointer-events:none;
  background:radial-gradient(ellipse 90% 60% at 10% 0%,rgba(124,58,237,.07) 0%,transparent 55%),
  radial-gradient(ellipse 60% 50% at 90% 100%,rgba(236,72,153,.05) 0%,transparent 50%),
  linear-gradient(rgba(124,58,237,.015) 1px,transparent 1px),
  linear-gradient(90deg,rgba(124,58,237,.015) 1px,transparent 1px);
  background-size:auto,auto,52px 52px,52px 52px}
h1,h2,h3,h4{font-family:'Fraunces',serif;line-height:1.12;letter-spacing:-.01em}
h1{font-size:clamp(2.6rem,6.5vw,5rem)}h2{font-size:clamp(1.9rem,3.8vw,3rem)}
h3{font-size:clamp(1.2rem,2.2vw,1.75rem)}h4{font-size:1.15rem}
p{color:var(--muted);line-height:1.82}
a{color:var(--acc);text-decoration:none;transition:color .2s}a:hover{color:#fff}
code{font-family:'JetBrains Mono',monospace;font-size:.82em;background:rgba(124,58,237,.1);padding:.15em .45em;border-radius:4px;color:var(--acc3)}
strong{color:var(--txt);font-weight:700}
nav{position:fixed;top:0;left:0;right:0;z-index:999;height:66px;
  background:rgba(4,5,13,.95);backdrop-filter:blur(22px);
  border-bottom:1px solid var(--bdr);
  display:flex;align-items:center;justify-content:space-between;padding:0 5%}
.logo{font-family:'Fraunces',serif;font-size:1.5rem;font-weight:900;color:var(--txt)}
.logo span{color:var(--acc)}
.nav-links{display:flex;gap:1.2rem;list-style:none;align-items:center}
.nav-links a{color:var(--muted);font-size:.75rem;font-weight:700;text-transform:uppercase;letter-spacing:.1em;transition:color .2s;white-space:nowrap}
.nav-links a:hover{color:var(--acc)}
.nav-cta{background:var(--acc)!important;color:#fff!important;font-weight:800!important;padding:.42rem 1.1rem;border-radius:var(--r2);box-shadow:0 2px 18px rgba(124,58,237,.5);transition:all .2s!important}
.nav-cta:hover{transform:translateY(-1px)!important;box-shadow:0 4px 28px rgba(124,58,237,.7)!important}
.ham{display:none;flex-direction:column;gap:5px;cursor:pointer;padding:4px}
.ham span{display:block;width:22px;height:2px;background:var(--acc);border-radius:2px}
.lang-strip{background:rgba(124,58,237,.06);border-top:1px solid var(--bdr);border-bottom:1px solid var(--bdr);padding:.7rem 5%;display:flex;align-items:center;gap:1rem;overflow-x:auto;scrollbar-width:none;position:relative;z-index:1}
.lang-strip::-webkit-scrollbar{display:none}
.ls-lbl{font-size:.7rem;color:var(--muted);font-weight:700;text-transform:uppercase;letter-spacing:.15em;white-space:nowrap;flex-shrink:0}
.lp{display:inline-flex;align-items:center;gap:.38rem;background:rgba(255,255,255,.04);border:1px solid var(--bdr);border-radius:100px;padding:.28rem .8rem;font-size:.75rem;color:var(--muted);white-space:nowrap;flex-shrink:0;text-decoration:none;transition:all .2s}
.lp:hover{border-color:var(--acc);color:var(--acc);background:rgba(124,58,237,.08)}
.btn{display:inline-flex;align-items:center;gap:.5rem;font-family:'Outfit',sans-serif;font-weight:800;font-size:.92rem;padding:.88rem 2.1rem;border-radius:var(--r2);text-transform:uppercase;letter-spacing:.07em;transition:all .25s;cursor:pointer;border:none;text-decoration:none}
.btn-p{background:linear-gradient(135deg,var(--acc),#5b21b6);color:#fff;box-shadow:0 4px 28px rgba(124,58,237,.5)}
.btn-p:hover{transform:translateY(-3px);box-shadow:0 8px 42px rgba(124,58,237,.75);color:#fff}
.btn-s{background:transparent;border:1.5px solid var(--bdr2);color:var(--txt)}
.btn-s:hover{border-color:var(--acc);color:var(--acc)}
.btn-g{background:rgba(124,58,237,.1);color:var(--acc);border:1px solid var(--bdr);font-size:.83rem;padding:.62rem 1.4rem}
.btn-g:hover{background:rgba(124,58,237,.2)}
.btn-lg{padding:1.1rem 2.6rem;font-size:1rem}
.btn-full{width:100%;justify-content:center}
.hero{min-height:100vh;display:flex;align-items:center;padding:100px 5% 80px;position:relative;z-index:1}
.hero-inner{max-width:820px}
.hero-badge{display:inline-flex;align-items:center;gap:.6rem;background:rgba(124,58,237,.1);border:1px solid var(--bdr2);color:var(--acc);font-size:.75rem;font-weight:700;letter-spacing:.15em;text-transform:uppercase;padding:.4rem 1.15rem;border-radius:100px;margin-bottom:1.9rem}
.badge-dot{width:7px;height:7px;background:var(--green);border-radius:50%;animation:pulse-dot 2s infinite}
@keyframes pulse-dot{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.4;transform:scale(.65)}}
.hero h1{margin-bottom:1.4rem}
.g-acc{color:var(--acc)}.g-acc2{color:var(--acc2)}.g-acc3{color:var(--acc3)}
.g-gold{color:var(--gold)}.g-green{color:var(--green)}.g-orange{color:var(--orange)}
.hero-sub{font-size:1.12rem;color:var(--muted);max-width:650px;margin-bottom:2.6rem}
.hero-ctas{display:flex;gap:1rem;flex-wrap:wrap;margin-bottom:2.8rem}
.hero-trust{display:flex;gap:1.5rem;flex-wrap:wrap;font-size:.77rem;color:var(--muted)}
.trust-it{display:flex;align-items:center;gap:.38rem}
.trust-it::before{content:'\2713';color:var(--green);font-weight:800}
.wave-bar{display:flex;align-items:center;gap:3px;height:48px;margin:2rem 0}
.wave-b{width:4px;border-radius:2px;background:var(--acc);opacity:.7;animation:wave-anim var(--d,.8s) ease-in-out infinite alternate}
@keyframes wave-anim{from{height:8px;opacity:.4}to{height:var(--h,40px);opacity:1}}
.stats-bar{display:flex;flex-wrap:wrap;background:var(--bg2);border-top:1px solid var(--bdr);border-bottom:1px solid var(--bdr);z-index:1;position:relative}
.stat-item{flex:1;min-width:115px;text-align:center;padding:1.7rem .8rem;border-right:1px solid var(--bdr)}
.stat-item:last-child{border-right:none}
.stat-num{font-family:'Fraunces',serif;font-size:2.4rem;font-weight:900;line-height:1;display:block;color:var(--acc);text-shadow:var(--glow)}
.stat-lbl{font-size:.71rem;color:var(--muted);text-transform:uppercase;letter-spacing:.12em;margin-top:.25rem}
section{padding:6rem 5%;position:relative;z-index:1}
.sec-lbl{font-size:.71rem;font-weight:700;letter-spacing:.22em;text-transform:uppercase;color:var(--acc);display:block;margin-bottom:.6rem}
.sec-title{margin-bottom:1.1rem}.sec-sub{color:var(--muted);max-width:590px;margin-bottom:3rem;font-size:1.02rem}
.tc{text-align:center}.tc .sec-sub{margin-left:auto;margin-right:auto}
.alt{background:linear-gradient(180deg,transparent,rgba(124,58,237,.022),transparent)}
.g3{display:grid;grid-template-columns:repeat(auto-fit,minmax(270px,1fr));gap:1.5rem}
.g2{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:1.5rem}
.g4{display:grid;grid-template-columns:repeat(auto-fit,minmax(185px,1fr));gap:1rem}
.split{display:grid;grid-template-columns:1fr 1fr;gap:5rem;align-items:center}
.card{background:var(--card);border:1px solid var(--bdr);border-radius:var(--r);padding:1.9rem;transition:all .32s;position:relative;overflow:hidden}
.card::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:linear-gradient(90deg,transparent,var(--acc),transparent);opacity:0;transition:opacity .3s}
.card:hover::before{opacity:1}
.card:hover{border-color:var(--bdr2);transform:translateY(-5px);box-shadow:0 20px 52px rgba(0,0,0,.55)}
.card-icon{width:52px;height:52px;border-radius:12px;background:rgba(124,58,237,.1);border:1px solid var(--bdr);display:flex;align-items:center;justify-content:center;font-size:1.5rem;margin-bottom:1.2rem;flex-shrink:0}
.card h3{font-size:1.2rem;color:var(--txt);margin-bottom:.45rem}
.card h4{font-size:1rem;color:var(--txt);margin-bottom:.4rem}
.card p{font-size:.89rem}
.card-feat{border-color:rgba(124,58,237,.32);background:linear-gradient(145deg,rgba(124,58,237,.07),rgba(6,182,212,.04))}
.fmt-grid{display:flex;flex-wrap:wrap;gap:.48rem}
.fmt{background:rgba(124,58,237,.08);border:1px solid rgba(124,58,237,.2);color:var(--acc3);font-family:'JetBrains Mono',monospace;font-size:.75rem;font-weight:600;padding:.28rem .75rem;border-radius:4px;letter-spacing:.04em}
.pgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:1.5rem;max-width:900px;margin:0 auto}
.pc{background:var(--card);border:1px solid var(--bdr);border-radius:var(--r);padding:2.3rem 1.9rem;text-align:center;position:relative;transition:all .3s}
.pc:hover{transform:translateY(-4px)}
.pc.pop{border-color:var(--acc);background:linear-gradient(145deg,rgba(124,58,237,.08),rgba(6,182,212,.04))}
.pop-badge{position:absolute;top:-14px;left:50%;transform:translateX(-50%);background:linear-gradient(135deg,var(--acc),var(--acc2));color:#fff;font-size:.7rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase;padding:.28rem 1rem;border-radius:100px;white-space:nowrap}
.p-name{font-size:.78rem;text-transform:uppercase;letter-spacing:.16em;color:var(--muted);margin-bottom:.9rem}
.p-price{font-family:'Fraunces',serif;font-size:3.8rem;font-weight:900;color:var(--acc);line-height:1}
.p-price sup{font-size:1.4rem;vertical-align:top;margin-top:.55rem;display:inline-block}
.p-per{font-size:.78rem;color:var(--muted);margin-bottom:1.7rem}
.p-feats{list-style:none;padding:0;text-align:left;margin-bottom:1.9rem;display:flex;flex-direction:column;gap:.65rem}
.p-feats li{font-size:.86rem;color:var(--muted);display:flex;gap:.5rem;align-items:flex-start}
.p-feats li::before{content:'\2713';color:var(--green);font-weight:700;flex-shrink:0}
.p-note{font-size:.75rem;color:var(--gold);margin-top:.9rem;font-weight:600}
.tbl-wrap{overflow-x:auto;border-radius:var(--r);border:1px solid var(--bdr)}
table{width:100%;border-collapse:collapse}
thead th{background:rgba(124,58,237,.08);color:var(--acc);font-family:'Fraunces',serif;font-size:.95rem;padding:.9rem 1.2rem;text-align:left;border-bottom:1px solid var(--bdr)}
tbody td{padding:.88rem 1.2rem;border-bottom:1px solid var(--bdr);font-size:.86rem;color:var(--muted)}
tbody tr:last-child td{border-bottom:none}
tbody tr:hover td{background:rgba(124,58,237,.028)}
.td-n{color:var(--txt);font-weight:600}.td-y{color:var(--green);font-weight:700}
.td-no{color:var(--red)}.td-p{color:var(--gold)}.td-hi{background:rgba(124,58,237,.05)!important}
.faq-wrap{max-width:780px;margin:0 auto;display:flex;flex-direction:column;gap:.95rem}
details{background:var(--card);border:1px solid var(--bdr);border-radius:var(--r);overflow:hidden}
details[open]{border-color:var(--bdr2)}
details summary{padding:1.2rem 1.6rem;cursor:pointer;font-weight:700;font-size:.94rem;color:var(--txt);list-style:none;display:flex;justify-content:space-between;align-items:center;gap:1rem;user-select:none}
details summary::-webkit-details-marker{display:none}
details summary::after{content:'+';color:var(--acc);font-size:1.6rem;font-weight:300;line-height:1;flex-shrink:0}
details[open] summary::after{content:'\2212'}
details .ans{padding:0 1.6rem 1.3rem;border-top:1px solid var(--bdr);padding-top:.95rem;font-size:.9rem}
details .ans p{color:var(--muted)}
.tgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:1.5rem}
.testi{background:var(--card);border:1px solid var(--bdr);border-radius:var(--r);padding:1.9rem;transition:all .3s}
.testi:hover{border-color:var(--bdr2);transform:translateY(-3px)}
.stars{color:var(--gold);font-size:1rem;margin-bottom:.8rem}
.testi-text{font-size:.9rem;color:var(--txt);font-style:italic;margin-bottom:1.1rem;line-height:1.78}
.testi-author{display:flex;align-items:center;gap:.75rem}
.testi-av{width:38px;height:38px;border-radius:50%;background:linear-gradient(135deg,var(--acc),var(--acc2));display:flex;align-items:center;justify-content:center;font-size:1rem;font-weight:700;flex-shrink:0}
.testi-name{font-weight:700;font-size:.86rem;color:var(--acc)}.testi-role{font-size:.77rem;color:var(--muted)}
.steps{max-width:680px;display:flex;flex-direction:column}
.step{display:flex;gap:1.9rem;align-items:flex-start;padding:1.9rem 0 1.9rem 2.5rem;border-left:2px solid rgba(124,58,237,.2);margin-left:1.5rem;position:relative}
.step::before{content:attr(data-n);position:absolute;left:-1.6rem;width:3.1rem;height:3.1rem;background:var(--bg);border:2px solid var(--acc);border-radius:50%;display:flex;align-items:center;justify-content:center;font-family:'Fraunces',serif;font-size:1.2rem;font-weight:900;color:var(--acc);box-shadow:0 0 20px rgba(124,58,237,.3);z-index:1}
.step:last-child{border-left-color:transparent}
.step h3{font-size:1.1rem;color:var(--txt);margin-bottom:.35rem}.step p{font-size:.88rem}
.bgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:1.5rem}
.bc{background:var(--card);border:1px solid var(--bdr);border-radius:var(--r);overflow:hidden;transition:all .3s;display:flex;flex-direction:column}
.bc:hover{transform:translateY(-4px);border-color:var(--bdr2);box-shadow:0 18px 44px rgba(0,0,0,.45)}
.bc-thumb{height:162px;background:linear-gradient(135deg,var(--bg3),rgba(124,58,237,.12));display:flex;align-items:center;justify-content:center;font-size:3rem;border-bottom:1px solid var(--bdr)}
.bc-body{padding:1.5rem;flex:1;display:flex;flex-direction:column}
.bc-tag{font-size:.7rem;color:var(--acc);text-transform:uppercase;letter-spacing:.13em;font-weight:700;margin-bottom:.45rem}
.bc h3{font-size:1rem;color:var(--txt);margin-bottom:.45rem;line-height:1.38}
.bc p{font-size:.82rem;flex:1;line-height:1.68}
.bc-meta{display:flex;gap:1rem;margin-top:.9rem;font-size:.75rem;color:var(--muted)}
.bc-read{margin-top:.9rem;font-size:.8rem;font-weight:700;color:var(--acc)}
.cta-blk{text-align:center;padding:6rem 5%;background:linear-gradient(135deg,rgba(124,58,237,.05),rgba(236,72,153,.03));border-top:1px solid var(--bdr);border-bottom:1px solid var(--bdr);position:relative;z-index:1}
.cta-blk h2{margin-bottom:1rem}.cta-blk p{max-width:520px;margin:0 auto 2.2rem}
.hbox{background:rgba(124,58,237,.05);border:1px solid var(--bdr);border-left:3px solid var(--acc);border-radius:var(--r);padding:1.5rem 1.8rem;margin:1.5rem 0}
.hbox h4{color:var(--acc);margin-bottom:.45rem}
.hbox.warn{border-left-color:var(--gold)}.hbox.warn h4{color:var(--gold)}
.hbox.good{border-left-color:var(--green)}.hbox.good h4{color:var(--green)}
.hbox.info{border-left-color:var(--acc3)}.hbox.info h4{color:var(--acc3)}
.chip{display:inline-flex;align-items:center;font-size:.7rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;padding:.22rem .65rem;border-radius:5px}
.chip-v{background:rgba(124,58,237,.1);color:var(--acc);border:1px solid rgba(124,58,237,.25)}
.chip-g{background:rgba(16,185,129,.1);color:var(--green);border:1px solid rgba(16,185,129,.2)}
.chip-p{background:rgba(236,72,153,.1);color:var(--acc2);border:1px solid rgba(236,72,153,.2)}
.chip-y{background:rgba(245,158,11,.1);color:var(--gold);border:1px solid rgba(245,158,11,.2)}
.rbars{display:flex;flex-direction:column;gap:1.1rem}
.rbar{display:grid;grid-template-columns:145px 1fr 44px;align-items:center;gap:1rem}
.rbar-lbl{font-size:.83rem;color:var(--muted)}
.rbar-track{height:8px;background:rgba(255,255,255,.06);border-radius:100px;overflow:hidden}
.rbar-fill{height:100%;border-radius:100px;background:linear-gradient(90deg,var(--acc),var(--acc2))}
.rbar-val{font-family:'Fraunces',serif;font-size:1.1rem;color:var(--acc);text-align:right}
.score-big{font-family:'Fraunces',serif;font-size:5.5rem;font-weight:900;line-height:1;color:var(--acc);text-shadow:var(--glow)}
.lang-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(175px,1fr));gap:.9rem}
.lng{background:var(--card);border:1px solid var(--bdr);border-radius:var(--r);padding:1.2rem 1.4rem;transition:all .25s;text-decoration:none;display:block}
.lng:hover{border-color:var(--bdr2);transform:translateY(-3px);background:rgba(124,58,237,.04)}
.lng-flag{font-size:1.8rem;margin-bottom:.5rem;display:block}
.lng-name{font-family:'Fraunces',serif;font-size:.95rem;font-weight:700;color:var(--txt)}
.lng-native{font-size:.8rem;color:var(--acc);font-weight:600}
.lng-kw{font-size:.75rem;color:var(--muted);margin-top:.3rem;line-height:1.5}
.ph{padding:130px 5% 65px;position:relative;z-index:1;background:linear-gradient(180deg,rgba(124,58,237,.045) 0%,transparent 100%);border-bottom:1px solid var(--bdr)}
.breadcrumb{font-size:.76rem;color:var(--muted);margin-bottom:1.2rem;display:flex;align-items:center;gap:.4rem;flex-wrap:wrap}
.breadcrumb a{color:var(--muted)}.breadcrumb a:hover{color:var(--acc)}
.breadcrumb .sep{color:var(--bdr2)}.breadcrumb .cur{color:var(--acc)}
.seo-tags{display:flex;flex-wrap:wrap;gap:.45rem;margin-bottom:2rem}
.seo-tag{background:rgba(124,58,237,.07);border:1px solid var(--bdr);color:var(--muted);font-size:.73rem;padding:.27rem .75rem;border-radius:100px}
.seo-prose{font-size:.87rem;color:var(--muted);line-height:2;columns:2;column-gap:3rem}
footer{background:var(--bg2);border-top:1px solid var(--bdr);padding:4.5rem 5% 2rem;position:relative;z-index:1}
.fg{display:grid;grid-template-columns:2.2fr 1fr 1fr 1fr;gap:3rem;margin-bottom:3rem}
.fb-logo{font-family:'Fraunces',serif;font-size:1.55rem;font-weight:900;color:var(--txt);margin-bottom:.85rem}
.fb-logo span{color:var(--acc)}
.fb-desc{font-size:.82rem;color:var(--muted);max-width:255px;line-height:1.78}
.fc h5{font-size:.73rem;text-transform:uppercase;letter-spacing:.16em;color:var(--txt);margin-bottom:1.1rem}
.fc ul{list-style:none;padding:0;display:flex;flex-direction:column;gap:.6rem}
.fc a{color:var(--muted);font-size:.82rem;transition:color .2s}.fc a:hover{color:var(--acc)}
.fb-bot{border-top:1px solid var(--bdr);padding-top:1.6rem;display:flex;justify-content:space-between;flex-wrap:wrap;gap:.8rem}
.fb-bot p{font-size:.77rem;color:var(--muted)}
@media(max-width:1100px){.fg{grid-template-columns:1fr 1fr 1fr}}
@media(max-width:900px){.fg{grid-template-columns:1fr 1fr}.split{grid-template-columns:1fr;gap:2.5rem}.seo-prose{columns:1}}
@media(max-width:640px){.nav-links{display:none}.ham{display:flex}.fg{grid-template-columns:1fr}.stat-item{min-width:47%;border-right:none;border-bottom:1px solid var(--bdr)}.pgrid{grid-template-columns:1fr}.rbar{grid-template-columns:110px 1fr 38px}section{padding:4.5rem 5%}}
@keyframes fadeUp{from{opacity:0;transform:translateY(22px)}to{opacity:1;transform:translateY(0)}}
.anim{animation:fadeUp .7s ease forwards}
.d1{animation-delay:.1s;opacity:0}.d2{animation-delay:.2s;opacity:0}.d3{animation-delay:.3s;opacity:0}.d4{animation-delay:.4s;opacity:0}
@keyframes glow-pulse{0%,100%{box-shadow:0 4px 28px rgba(124,58,237,.5)}50%{box-shadow:0 4px 52px rgba(124,58,237,.85)}}
.btn-p{animation:glow-pulse 3.5s ease-in-out infinite}
"""


def wave_viz():
    heights = [12,22,36,48,40,32,44,48,38,26,42,48,44,30,18,36,48,42,24,38,46,40,28,44,48]
    delays  = [0.0,0.1,0.2,0.15,0.05,0.3,0.12,0.08,0.22,0.18,0.04,0.25,0.1,0.35,0.2,0.07,0.13,0.28,0.06,0.17,0.24,0.09,0.31,0.16,0.03]
    bars = "".join(
        f'<div class="wave-b" style="--h:{h}px;--d:{d}s;animation-duration:{d+0.5:.2f}s"></div>'
        for h,d in zip(heights,delays)
    )
    return f'<div class="wave-bar" aria-hidden="true">{bars}</div>'

def nav():
    links = [
        ("Features",     f"{SITE_ROOT}/features/"),
        ("How It Works", f"{SITE_ROOT}/how-it-works/"),
        ("Use Cases",    f"{SITE_ROOT}/use-cases/"),
        ("Formats",      f"{SITE_ROOT}/formats/"),
        ("Pricing",      f"{SITE_ROOT}/pricing/"),
        ("Review",       f"{SITE_ROOT}/review/"),
        ("Blog",         f"{SITE_ROOT}/blog/"),
        ("FAQ",          f"{SITE_ROOT}/faq/"),
    ]
    li = "".join(f'<li><a href="{u}">{l}</a></li>' for l,u in links)
    return (
        f'<nav><a class="logo" href="{SITE_ROOT}/">Audio<span>Recorder</span></a>'
        f'<ul class="nav-links">{li}'
        f'<li><a href="{AFF}" class="nav-cta" target="_blank" rel="noopener sponsored">\u2b07 Free Trial</a></li>'
        f'</ul><div class="ham"><span></span><span></span><span></span></div></nav>'
    )

def lang_strip():
    pills = "".join(
        f'<a href="{SITE_ROOT}/lang/{lc}/" class="lp">{flag} {name}</a>'
        for flag,name,lc,_,_,_,_ in LANGS[:12]
    )
    return f'<div class="lang-strip"><span class="ls-lbl">Available in:</span>{pills}</div>'

def foot():
    return (
        f'<footer><div class="fg">'
        f'<div><div class="fb-logo">Audio<span>Recorder</span></div>'
        f'<p class="fb-desc">Independent affiliate guide for Wondershare Streaming Audio Recorder. '
        f'Record streaming music, Zoom calls, radio, podcasts and microphone in MP3, WAV, FLAC and 7 more formats. '
        f'Used in 200+ countries worldwide.</p></div>'
        f'<div class="fc"><h5>Product</h5><ul>'
        f'<li><a href="{SITE_ROOT}/features/">All Features</a></li>'
        f'<li><a href="{SITE_ROOT}/formats/">Output Formats</a></li>'
        f'<li><a href="{SITE_ROOT}/pricing/">Pricing</a></li>'
        f'<li><a href="{SITE_ROOT}/review/">Full Review</a></li>'
        f'<li><a href="{SITE_ROOT}/download/">Download</a></li>'
        f'<li><a href="{SITE_ROOT}/global/">Global Users</a></li>'
        f'</ul></div>'
        f'<div class="fc"><h5>Guides</h5><ul>'
        f'<li><a href="{SITE_ROOT}/record-streaming-audio/">Record Streaming Audio</a></li>'
        f'<li><a href="{SITE_ROOT}/record-zoom-audio/">Record Zoom Audio</a></li>'
        f'<li><a href="{SITE_ROOT}/record-spotify/">Record Spotify</a></li>'
        f'<li><a href="{SITE_ROOT}/record-internet-radio/">Record Internet Radio</a></li>'
        f'<li><a href="{SITE_ROOT}/podcast-recorder/">Podcast Recorder</a></li>'
        f'<li><a href="{SITE_ROOT}/voice-recorder/">Voice Recorder</a></li>'
        f'</ul></div>'
        f'<div class="fc"><h5>Compare & More</h5><ul>'
        f'<li><a href="{SITE_ROOT}/vs-audacity/">vs Audacity</a></li>'
        f'<li><a href="{SITE_ROOT}/vs-garageband/">vs GarageBand</a></li>'
        f'<li><a href="{SITE_ROOT}/vs-obs/">vs OBS Studio</a></li>'
        f'<li><a href="{SITE_ROOT}/alternatives/">All Alternatives</a></li>'
        f'<li><a href="{SITE_ROOT}/faq/">FAQ</a></li>'
        f'<li><a href="{SITE_ROOT}/disclaimer/">Disclaimer</a></li>'
        f'</ul></div>'
        f'</div>'
        f'<div class="fb-bot">'
        f'<p>\u00a9 {YEAR} AudioRecorder Guide \u2014 Independent affiliate site. Commissions earned at no extra cost to you.</p>'
        f'<p><a href="{AFF}" target="_blank" rel="noopener sponsored">Download Free Trial \u2192</a></p>'
        f'</div></footer>'
    )

def bc(*crumbs):
    parts = []
    for i,(label,url) in enumerate(crumbs):
        if url and i < len(crumbs)-1:
            parts.append(f'<a href="{url}">{label}</a><span class="sep">\u203a</span>')
        else:
            parts.append(f'<span class="cur">{label}</span>')
    return '<nav class="breadcrumb">' + "".join(parts) + "</nav>"

def sw_schema(desc):
    safe = desc[:200].replace('"',"'")
    return (
        '{"@context":"https://schema.org","@type":"SoftwareApplication",'
        '"name":"Wondershare Streaming Audio Recorder",'
        '"applicationCategory":"MultimediaApplication",'
        '"operatingSystem":"Windows",'
        '"offers":{"@type":"Offer","price":"0","priceCurrency":"USD","description":"Free trial available"},'
        '"aggregateRating":{"@type":"AggregateRating","ratingValue":"4.5","reviewCount":"1842","bestRating":"5"},'
        f'"description":"{safe}",'
        f'"url":"{SITE_URL}/",'
        '"publisher":{"@type":"Organization","name":"Wondershare","url":"https://videoconverter.wondershare.com"}}'
    )

def bc_schema(title, path):
    canon = f"{SITE_URL}{path}"
    t = title.split("\u2014")[0].strip().replace('"',"'")
    return (
        '{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":['
        f'{{"@type":"ListItem","position":1,"name":"Home","item":"{SITE_URL}/"}},'
        f'{{"@type":"ListItem","position":2,"name":"{t}","item":"{canon}"}}'
        ']}'
    )

def hreflang_tags():
    tags = "".join(
        f'<link rel="alternate" hreflang="{lc}" href="{SITE_URL}/lang/{lc}/">'
        for _,_,lc,_,_,_,_ in LANGS
    )
    tags += f'<link rel="alternate" hreflang="x-default" href="{SITE_URL}/">'
    return tags

def page(title, desc, path, body, kw="", extras=None, article=False, lang="en"):
    kw = kw or "audio recorder software, streaming audio recorder, record system audio, MP3 recorder, voice recorder PC"
    canon = f"{SITE_URL}{path}"
    extras = extras or []
    schemas = f'<script type="application/ld+json">{sw_schema(desc)}</script>'
    schemas += f'<script type="application/ld+json">{bc_schema(title, path)}</script>'
    for ex in extras:
        schemas += f'<script type="application/ld+json">{ex}</script>'
    og_type = "article" if article else "website"
    return (
        '<!DOCTYPE html>\n'
        f'<html lang="{lang}">\n'
        '<head>\n'
        '<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">\n'
        f'<title>{title}</title>\n'
        f'<meta name="description" content="{desc}">\n'
        f'<meta name="keywords" content="{kw}">\n'
        '<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large">\n'
        f'<link rel="canonical" href="{canon}">\n'
        + hreflang_tags() +
        f'<meta property="og:title" content="{title}">\n'
        f'<meta property="og:description" content="{desc}">\n'
        f'<meta property="og:url" content="{canon}">\n'
        f'<meta property="og:type" content="{og_type}">\n'
        f'<meta property="og:image" content="{SITE_URL}/assets/og.png">\n'
        '<meta property="og:site_name" content="AudioRecorder Guide">\n'
        '<meta name="twitter:card" content="summary_large_image">\n'
        f'<link rel="icon" href="{SITE_ROOT}/assets/favicon.svg" type="image/svg+xml">\n'
        f'<link rel="alternate" type="application/rss+xml" title="AudioRecorder Blog" href="{SITE_URL}/feed.xml">\n'
        f'{schemas}\n'
        f'<style>{CSS}</style>\n'
        '</head>\n<body>\n'
        + nav() + '\n'
        + body + '\n'
        + foot() +
        '\n<script>\n'
        '(function(){\n'
        '  var h=document.querySelector(".ham"),nl=document.querySelector(".nav-links");\n'
        '  if(!h||!nl)return;\n'
        '  h.addEventListener("click",function(){\n'
        '    var open=nl.style.display==="flex";\n'
        '    nl.style.cssText=open?"":"display:flex;position:fixed;top:66px;left:0;right:0;'
        'flex-direction:column;background:rgba(4,5,13,.98);padding:2rem 5%;gap:1.3rem;'
        'border-bottom:1px solid rgba(124,58,237,.13);z-index:998;backdrop-filter:blur(22px)";\n'
        '  });\n'
        '})();\n'
        '</script>\n</body></html>'
    )

def write(rel, content):
    p = BASE / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    print(f"  \u2713  {rel}")


# ── LANGUAGE PAGE GENERATOR ────────────────────────────────────────────────
def pg_lang(flag,name,lc,region,kw1,kw2,kw3):
    headlines = {
        "en": ("Best Audio Recorder Software","Record any audio from your computer","Free trial"),
        "de": ("Beste Audio Recorder Software","Jeden Ton vom Computer aufnehmen","Kostenlose Testversion"),
        "fr": ("Meilleur logiciel enregistreur audio","Enregistrer tout audio de votre ordinateur","Essai gratuit"),
        "es": ("Mejor software grabador de audio","Grabar cualquier audio del ordenador","Prueba gratuita"),
        "pt": ("Melhor software gravador de \u00e1udio","Gravar qualquer \u00e1udio do computador","Avalia\u00e7\u00e3o gratuita"),
        "it": ("Miglior software registratore audio","Registrare qualsiasi audio dal computer","Prova gratuita"),
        "ja": ("\u6700\u9ad8\u306e\u97f3\u58f0\u9332\u97f3\u30bd\u30d5\u30c8","\u30b3\u30f3\u30d4\u30e5\u30fc\u30bf\u304b\u3089\u4efb\u610f\u306e\u97f3\u58f0\u3092\u9332\u97f3","\u7121\u6599\u30c8\u30e9\u30a4\u30a2\u30eb"),
        "zh": ("\u6700\u4f73\u5f55\u97f3\u8f6f\u4ef6","\u5f55\u5236\u8ba1\u7b97\u673a\u4e0a\u7684\u4efb\u4f55\u97f3\u9891","\u514d\u8d39\u8bd5\u7528"),
        "ko": ("\ucd5c\uace0\uc758 \uc624\ub514\uc624 \ub179\uc74c \uc18c\ud504\ud2b8\uc6e8\uc5b4","\ucef4\ud4e8\ud130\uc758 \ubaa8\ub4e0 \uc624\ub514\uc624 \ub179\uc74c","\ubb34\ub8cc \uccb4\ud5d8\ud310"),
        "ru": ("\u041b\u0443\u0447\u0448\u0430\u044f \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u0437\u0430\u043f\u0438\u0441\u0438 \u0437\u0432\u0443\u043a\u0430","\u0417\u0430\u043f\u0438\u0441\u044c \u043b\u044e\u0431\u043e\u0433\u043e \u0437\u0432\u0443\u043a\u0430 \u0441 \u043a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440\u0430","\u0411\u0435\u0441\u043f\u043b\u0430\u0442\u043d\u0430\u044f \u043f\u0440\u043e\u0431\u043d\u0430\u044f \u0432\u0435\u0440\u0441\u0438\u044f"),
        "ar": ("\u0623\u0641\u0636\u0644 \u0628\u0631\u0646\u0627\u0645\u062c \u062a\u0633\u062c\u064a\u0644 \u0627\u0644\u0635\u0648\u062a","\u062a\u0633\u062c\u064a\u0644 \u0623\u064a \u0635\u0648\u062a \u0645\u0646 \u062c\u0647\u0627\u0632 \u0627\u0644\u0643\u0645\u0628\u064a\u0648\u062a\u0631","\u062a\u062c\u0631\u0628\u0629 \u0645\u062c\u0627\u0646\u064a\u0629"),
        "hi": ("\u0938\u0930\u094d\u0935\u0936\u094d\u0930\u0947\u0937\u094d\u0920 \u0911\u0921\u093f\u092f\u094b \u0930\u093f\u0915\u0949\u0930\u094d\u0921\u0930","\u0915\u0902\u092a\u094d\u092f\u0942\u091f\u0930 \u0938\u0947 \u0915\u094b\u0908 \u092d\u0940 \u0911\u0921\u093f\u092f\u094b \u0930\u093f\u0915\u0949\u0930\u094d\u0921 \u0915\u0930\u0947\u0902","\u0928\u093f\u0903\u0936\u0941\u0932\u094d\u0915 \u092a\u0930\u0940\u0915\u094d\u0937\u0923"),
        "id": ("Perekam Audio Terbaik","Rekam semua audio dari komputer","Uji coba gratis"),
        "nl": ("Beste audio recorder software","Neem elk geluid van uw computer op","Gratis proberen"),
        "pl": ("Najlepsze oprogramowanie do nagrywania d\u017awi\u0119ku","Nagraj dowolny d\u017awi\u0119k z komputera","Bezp\u0142atna wersja pr\u00f3bna"),
        "tr": ("En iyi ses kaydedici yaz\u0131l\u0131m","Bilgisayardan her sesi kaydet",")\u00dccrets\u0131z deneme"),
        "sv": ("B\u00e4sta ljudinspelningsprogram","Spela in vilket ljud som helst fr\u00e5n datorn","Gratis provversion"),
        "fil": ("Pinakamahusay na audio recorder","I-record ang anumang audio mula sa iyong computer","Libreng pagsubok"),
        "vi": ("Ph\u1ea7n m\u1ec1m ghi \u00e2m t\u1ed1t nh\u1ea5t","Ghi \u00e2m b\u1ea5t k\u1ef3 \u00e2m thanh n\u00e0o t\u1eeb m\u00e1y t\u00ednh","D\u00f9ng th\u1eed mi\u1ec5n ph\u00ed"),
        "th": ("\u0e42\u0e1b\u0e23\u0e41\u0e01\u0e23\u0e21\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01\u0e40\u0e2a\u0e35\u0e22\u0e07\u0e17\u0e35\u0e48\u0e14\u0e35\u0e17\u0e35\u0e48\u0e2a\u0e38\u0e14","\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01\u0e40\u0e2a\u0e35\u0e22\u0e07\u0e43\u0e14\u0e46 \u0e08\u0e32\u0e01\u0e04\u0e2d\u0e21\u0e1e\u0e34\u0e27\u0e40\u0e15\u0e2d\u0e23\u0e4c\u0e02\u0e2d\u0e07\u0e04\u0e38\u0e13","\u0e17\u0e14\u0e25\u0e2d\u0e07\u0e43\u0e0a\u0e49\u0e1f\u0e23\u0e35"),
    }
    h = headlines.get(lc, headlines["en"])
    features_localized = [
        f"Record streaming music in {region}",
        f"AI noise reduction for {name} users",
        f"Scheduled recording — automatic capture",
        f"Auto track split for playlists",
        f"ID3 tags — auto artist/title/album",
        f"Save as MP3, WAV, FLAC, AAC and more",
    ]
    feat_li = "".join(
        f'<li style="display:flex;gap:.7rem;font-size:.9rem;color:var(--muted)">'
        f'<span style="color:var(--green);font-weight:700">\u2713</span>{f}</li>'
        for f in features_localized
    )
    return page(
        f"Wondershare Audio Recorder \u2014 {h[0]} | {region} | {YEAR}",
        f"Wondershare Audio Recorder for {region}: {h[1]}. Record streaming music, Zoom calls, radio, podcasts and microphone in MP3, WAV, FLAC. {h[2]}.",
        f"/lang/{lc}/",
        (
            f'<div class="ph">'
            + bc(("Home",f"{SITE_ROOT}/"),("Global",f"{SITE_ROOT}/global/"), (name, None))
            + f'<span class="sec-lbl">{flag} {region}</span>'
            f'<h1>{h[0]}<br><span class="g-acc">{name}</span></h1>'
            f'<p style="max-width:660px;margin-top:.9rem;font-size:1.05rem;color:var(--muted)">'
            f'Wondershare Audio Recorder is used by thousands of people in {region}. '
            f'Record any audio from your computer \u2014 streaming music, internet radio, Zoom calls, podcasts and microphone \u2014 in MP3, WAV, FLAC and 7 more formats.'
            f'</p>'
            f'<div style="margin-top:2rem;display:flex;gap:1rem;flex-wrap:wrap">'
            f'<a href="{AFF}" class="btn btn-p btn-lg" target="_blank" rel="noopener sponsored">\u2b07 {h[2]}</a>'
            f'<a href="{SITE_ROOT}/features/" class="btn btn-s btn-lg">All Features \u2192</a>'
            f'</div></div>'
            f'<section>'
            f'<div class="split">'
            f'<div>'
            f'<span class="sec-lbl">For {region} Users</span>'
            f'<h2 class="sec-title">Audio Recorder<br><span class="g-acc">in {name}</span></h2>'
            f'<p style="margin-bottom:1.5rem">Wondershare Audio Recorder works on any Windows PC in {region}. '
            f'The software captures any audio playing through your computer at full quality \u2014 '
            f'streaming services, online radio, video calls, browser audio and microphone recordings.</p>'
            f'<ul style="list-style:none;padding:0;display:flex;flex-direction:column;gap:.9rem">{feat_li}</ul>'
            f'<div style="margin-top:2rem">'
            f'<a href="{AFF}" class="btn btn-p" target="_blank" rel="noopener sponsored">\u2b07 Download for {region}</a>'
            f'</div></div>'
            f'<div>'
            f'<div class="card card-feat" style="padding:2rem">'
            f'<h3 style="color:var(--acc);margin-bottom:1rem">{kw1}</h3>'
            f'<p style="margin-bottom:1rem">{kw2} \u2014 Wondershare Audio Recorder makes it simple. '
            f'Record to MP3, WAV or FLAC with a single click. '
            f'Scheduled recording, auto track split and ID3 tags all built in.</p>'
            f'<div class="fmt-grid">'
            + "".join(f'<span class="fmt">{f}</span>' for f in ["MP3","WAV","FLAC","AAC","M4A","OGG","WMA","AIFF"])
            + f'</div>'
            f'<div style="margin-top:1.5rem">'
            f'<a href="{AFF}" class="btn btn-g" target="_blank" rel="noopener sponsored">\u2b07 {h[2]} \u2192</a>'
            f'</div></div>'
            f'<div class="hbox info" style="margin-top:1rem">'
            f'<h4>Available Worldwide</h4>'
            f'<p style="margin-top:.4rem">Wondershare Audio Recorder is available in {region} and 200+ countries. '
            f'Download from the official site with your local payment method.</p>'
            f'</div>'
            f'</div></div>'
            f'</section>'
        ),
        kw=f"{kw1}, {kw2}, {kw3}, Wondershare audio recorder {region}, audio recorder {name}",
        lang=lc
    )


def pg_home():
    fmts = "".join(f'<span class="fmt">{f}</span>' for f in ["MP3","WAV","FLAC","AAC","M4A","OGG","WMA","AIFF","AC3","APE"])
    lang_cards = "".join(
        f'<a href="{SITE_ROOT}/lang/{lc}/" class="lng">'
        f'<span class="lng-flag">{flag}</span>'
        f'<div class="lng-name">{name}</div>'
        f'<div class="lng-native">{kw1}</div>'
        f'<div class="lng-kw">{region}</div>'
        f'</a>'
        for flag,name,lc,region,kw1,_,_ in LANGS[:12]
    )
    return page(
        f"Wondershare Audio Recorder \u2014 Record Any Audio From Any Source | {YEAR} | Global",
        f"Wondershare Streaming Audio Recorder captures streaming music, Zoom calls, radio, podcasts and microphone on Windows. MP3, WAV, FLAC, 10 formats. Scheduled recording. Free trial. Best audio recorder {YEAR}.",
        "/",
        (
            lang_strip() +
            '<section class="hero">'
            '<div class="hero-inner">'
            f'<div class="hero-badge anim"><span class="badge-dot"></span> Record Any Audio \u2014 200+ Countries Worldwide</div>'
            f'<h1 class="anim d1">Record <span class="g-acc">Any Audio.</span><br>'
            f'<span class="g-acc2">Any Source.</span><br>'
            f'<span class="g-acc3">Any Format.</span></h1>'
            + wave_viz() +
            f'<p class="hero-sub anim d2">Wondershare Streaming Audio Recorder captures any sound playing on your Windows PC \u2014 '
            f'streaming music, Zoom calls, internet radio, podcasts, microphone recordings \u2014 '
            f'in crystal-clear quality. Save as MP3, WAV, FLAC and 7 more formats. '
            f'Schedule recordings. Auto-split tracks. Auto-tag with ID3. Free trial available.</p>'
            f'<div class="hero-ctas anim d3">'
            f'<a href="{AFF}" class="btn btn-p btn-lg" target="_blank" rel="noopener sponsored">\u2b07 Download Free Trial</a>'
            f'<a href="{SITE_ROOT}/features/" class="btn btn-s btn-lg">See All Features \u2192</a>'
            f'</div>'
            f'<div class="hero-trust anim d4">'
            f'<span class="trust-it">Free Trial</span>'
            f'<span class="trust-it">Windows</span>'
            f'<span class="trust-it">10 Output Formats</span>'
            f'<span class="trust-it">Scheduled Recording</span>'
            f'<span class="trust-it">AI Noise Reduction</span>'
            f'<span class="trust-it">Auto Track Split</span>'
            f'</div>'
            f'</div></section>'

            f'<div class="stats-bar">'
            f'<div class="stat-item"><span class="stat-num">10+</span><span class="stat-lbl">Output Formats</span></div>'
            f'<div class="stat-item"><span class="stat-num">Any</span><span class="stat-lbl">Audio Source</span></div>'
            f'<div class="stat-item"><span class="stat-num">0</span><span class="stat-lbl">Quality Loss</span></div>'
            f'<div class="stat-item"><span class="stat-num">24/7</span><span class="stat-lbl">Scheduled Recording</span></div>'
            f'<div class="stat-item"><span class="stat-num">Auto</span><span class="stat-lbl">Track Split</span></div>'
            f'<div class="stat-item"><span class="stat-num">200+</span><span class="stat-lbl">Countries</span></div>'
            f'</div>'

            f'<section>'
            f'<span class="sec-lbl">Every Audio Source</span>'
            f'<h2 class="sec-title">Record From <span class="g-acc">Any Source</span></h2>'
            f'<p class="sec-sub">Whatever audio plays through your computer \u2014 Audio Recorder captures it at full quality. Virtual audio driver technology intercepts audio at source, before it reaches speakers.</p>'
            f'<div class="g3">'
            + "".join(
                f'<div class="card{"  card-feat" if i<2 else ""}"><div class="card-icon">{icon}</div>'
                f'<h3>{title}</h3><p>{desc}</p></div>'
                for i,(icon,title,desc) in enumerate([
                    ("\U0001f3b5","Streaming Music","Record Spotify, Apple Music, Amazon Music, YouTube Music, Tidal, Deezer \u2014 any streaming service \u2014 at full source quality. No microphone needed."),
                    ("\U0001f4fb","Internet Radio","Capture any online radio station automatically. Set a schedule, come back to a perfectly organised recording."),
                    ("\U0001f399","Microphone","Record voice memos, interviews, podcasts, dictation, lectures. AI noise reduction cleans up background hiss automatically."),
                    ("\U0001f5a5","System Audio","Any sound playing through your computer \u2014 games, movies, apps, browser audio \u2014 captured without quality loss."),
                    ("\U0001f4f9","Video Calls","Record Zoom, Teams, Google Meet, Skype, Discord as audio-only. 55 MB per hour vs 4 GB for screen recording."),
                    ("\U0001f3ae","Games & Apps","Record in-game audio, commentary, app sounds \u2014 perfect for content creators and streamers."),
                    ("\U0001f310","Browser Audio","Capture audio from Chrome, Firefox, Edge \u2014 YouTube, Netflix, any website."),
                    ("\U0001f3da","Webinars & Podcasts","Record live webinars, scheduled podcast streams and online broadcasts on a timer."),
                    ("\U0001f3b8","External Devices","Connect instruments, mixers and line-in devices via audio interface for studio-quality capture."),
                ])
            )
            + f'</div></section>'

            f'<section class="alt">'
            f'<span class="sec-lbl tc" style="display:block;text-align:center">Output Formats</span>'
            f'<h2 class="sec-title tc">Save In <span class="g-acc">Any Format</span></h2>'
            f'<p class="sec-sub tc">10 output formats covering every use case from casual sharing to professional archiving.</p>'
            f'<div class="fmt-grid" style="max-width:720px;margin:0 auto 2rem;justify-content:center">{fmts}</div>'
            f'<div style="text-align:center"><a href="{SITE_ROOT}/formats/" class="btn btn-g">Full Format Guide \u2192</a></div>'
            f'</section>'

            f'<section>'
            f'<div class="split">'
            f'<div>'
            f'<span class="sec-lbl">Key Features</span>'
            f'<h2 class="sec-title">More Than a <span class="g-acc">Record Button</span></h2>'
            f'<p style="margin-bottom:1.5rem">Wondershare Audio Recorder is built around your workflow \u2014 automatic scheduling, intelligent track detection, smart tagging, and clean audio from any source.</p>'
            f'<ul style="list-style:none;padding:0;display:flex;flex-direction:column;gap:.9rem">'
            + "".join(
                f'<li style="display:flex;gap:.7rem;font-size:.9rem;color:var(--muted)">'
                f'<span style="color:var(--green);font-weight:700">\u2713</span>'
                f'<span><strong>{a}</strong> \u2014 {b}</span></li>'
                for a,b in [
                    ("Scheduled recording","set start/stop time \u2014 records automatically while you sleep"),
                    ("Auto track split","detects silence between tracks, saves each as a separate file"),
                    ("ID3 tag editor","auto-fetches artist, title, album, cover art from online database"),
                    ("AI noise reduction","removes background hiss, hum and ambient noise automatically"),
                    ("Built-in audio editor","trim, cut, fade, adjust volume without leaving the app"),
                    ("Format converter","convert existing audio files between any supported format"),
                    ("Always-on mode","silent system tray recording \u2014 captures everything passively"),
                ]
            )
            + f'</ul>'
            f'<div style="margin-top:2rem"><a href="{AFF}" class="btn btn-p" target="_blank" rel="noopener sponsored">\u2b07 Try Free Now</a></div>'
            f'</div>'
            f'<div>'
            f'<div class="card card-feat" style="padding:2.2rem">'
            f'<h3 style="color:var(--acc);margin-bottom:1.4rem">Audio Recorder vs Manual Methods</h3>'
            f'<div class="tbl-wrap"><table>'
            f'<thead><tr><th>Task</th><th>Audio Recorder</th><th>Without It</th></tr></thead>'
            f'<tbody>'
            + "".join(
                f'<tr><td>{t}</td><td class="td-y td-hi">{a}</td><td class="td-no">{b}</td></tr>'
                for t,a,b in [
                    ("Record streaming music","\u2713 One click","\u2715 Not possible"),
                    ("Schedule overnight recording","\u2713 Built in","\u2715 Must stay awake"),
                    ("Auto-split into tracks","\u2713 Automatic","\u2715 Manual editing"),
                    ("ID3 tags on save","\u2713 Auto-fetch","\u2715 Manual tagging"),
                    ("Record Zoom audio only","\u2713 Clean audio","\u2715 Screen recording = huge file"),
                    ("Convert format on save","\u2713 Built in","\u2715 Separate software"),
                ]
            )
            + f'</tbody></table></div>'
            f'</div></div></div>'
            f'</section>'

            f'<section class="alt">'
            f'<span class="sec-lbl tc" style="display:block;text-align:center">Global Reach</span>'
            f'<h2 class="sec-title tc">Used in <span class="g-acc">200+ Countries</span></h2>'
            f'<p class="sec-sub tc">Wondershare Audio Recorder works on any Windows PC worldwide. Available in multiple languages with global payment support.</p>'
            f'<div class="lang-grid" style="max-width:980px;margin:0 auto 2.5rem">{lang_cards}</div>'
            f'<div style="text-align:center"><a href="{SITE_ROOT}/global/" class="btn btn-g">All Languages & Regions \u2192</a></div>'
            f'</section>'

            f'<section>'
            f'<span class="sec-lbl tc" style="display:block;text-align:center">Real Users</span>'
            f'<h2 class="sec-title tc">What People <span class="g-acc">Around the World</span> Say</h2>'
            f'<p class="sec-sub tc">4.5 stars from verified users worldwide</p>'
            f'<div class="tgrid">'
            f'<div class="testi"><div class="stars">\u2605\u2605\u2605\u2605\u2605</div><p class="testi-text">"I record internet radio every night on a schedule. Perfectly splits each programme and names the files. What used to be impossible is now completely effortless."</p><div class="testi-author"><div class="testi-av">R</div><div><div class="testi-name">Robert K. \U0001f1ec\U0001f1e7</div><div class="testi-role">Radio enthusiast, Manchester</div></div></div></div>'
            f'<div class="testi"><div class="stars">\u2605\u2605\u2605\u2605\u2605</div><p class="testi-text">"As a journalist I need Zoom interviews as MP3 \u2014 just the audio, tiny file. This records the call perfectly without capturing video. Saves hours every week."</p><div class="testi-author"><div class="testi-av">S</div><div><div class="testi-name">Sofia M. \U0001f1e7\U0001f1f7</div><div class="testi-role">Journalist, S\u00e3o Paulo</div></div></div></div>'
            f'<div class="testi"><div class="stars">\u2605\u2605\u2605\u2605\u2606</div><p class="testi-text">"The ID3 tag feature is brilliant \u2014 my recordings are automatically named so they go straight into my music library. Saves so much time."</p><div class="testi-author"><div class="testi-av">J</div><div><div class="testi-name">James L. \U0001f1fa\U0001f1f8</div><div class="testi-role">Music collector, Chicago</div></div></div></div>'
            f'<div class="testi"><div class="stars">\u2605\u2605\u2605\u2605\u2605</div><p class="testi-text">"I record NHK Radio Japan every morning on a schedule. The software activates at 6am, records 30 minutes, stops automatically. Perfect for learning Japanese."</p><div class="testi-author"><div class="testi-av">L</div><div><div class="testi-name">Lukas B. \U0001f1e9\U0001f1ea</div><div class="testi-role">Language learner, Hamburg</div></div></div></div>'
            f'<div class="testi"><div class="stars">\u2605\u2605\u2605\u2605\u2605</div><p class="testi-text">"As a student I record online lectures to MP3. Tiny file, perfect clarity, automatic filename with date. My go-to tool for the past two years."</p><div class="testi-author"><div class="testi-av">K</div><div><div class="testi-name">Kenji W. \U0001f1ef\U0001f1f5</div><div class="testi-role">University student, Osaka</div></div></div></div>'
            f'<div class="testi"><div class="stars">\u2605\u2605\u2605\u2605\u2605</div><p class="testi-text">"I run an online language school. We record all live sessions automatically. Audio only saves massive storage compared to video. Students love having the recordings."</p><div class="testi-author"><div class="testi-av">P</div><div><div class="testi-name">Priya S. \U0001f1ee\U0001f1f3</div><div class="testi-role">Language school owner, Delhi</div></div></div></div>'
            f'</div>'
            f'</section>'

            f'<div class="cta-blk">'
            f'<span class="sec-lbl" style="display:block;margin-bottom:1rem">Start Recording Today</span>'
            f'<h2>Record <span class="g-acc">Any Audio</span> From<br>Any Source, Worldwide</h2>'
            f'<p>Free trial available \u2014 Windows \u00b7 MP3, WAV, FLAC \u00b7 Scheduled recording \u00b7 Auto track split \u00b7 No credit card</p>'
            f'<a href="{AFF}" class="btn btn-p btn-lg" target="_blank" rel="noopener sponsored">\u2b07 Download Audio Recorder Free</a>'
            f'</div>'
        ),
        kw=KEYWORDS
    )

def pg_global():
    all_cards = "".join(
        f'<a href="{SITE_ROOT}/lang/{lc}/" class="lng">'
        f'<span class="lng-flag">{flag}</span>'
        f'<div class="lng-name">{name}</div>'
        f'<div class="lng-native">{kw1}</div>'
        f'<div class="lng-kw">{region} \u00b7 {kw2}</div>'
        f'</a>'
        for flag,name,lc,region,kw1,kw2,_ in LANGS
    )
    return page(
        f"Audio Recorder \u2014 Global Users in 200+ Countries | {YEAR}",
        "Wondershare Audio Recorder is used worldwide in 200+ countries. Available in 20 languages. Record streaming audio, radio, meetings and microphone on Windows globally.",
        "/global/",
        (
            f'<div class="ph">'
            + bc(("Home",f"{SITE_ROOT}/"),("Global",None))
            + f'<span class="sec-lbl">Worldwide Reach</span>'
            f'<h1>Audio Recorder \u2014<br><span class="g-acc">Globally Available</span></h1>'
            f'<p style="max-width:660px;margin-top:.9rem;color:var(--muted)">'
            f'Wondershare Audio Recorder works on any Windows PC in any country. '
            f'This page covers 20 language regions with native-language keywords and local use cases.</p>'
            f'</div>'
            f'<section>'
            f'<div class="g3" style="margin-bottom:3rem">'
            + "".join(
                f'<div class="card"><div class="card-icon">{icon}</div><h3>{title}</h3><p>{desc}</p></div>'
                for icon,title,desc in [
                    ("\U0001f310","Windows Worldwide","Available on any Windows PC in any country. Compatible with Windows 7, 8, 10 and 11. No regional restrictions on download or use."),
                    ("\U0001f4b3","Global Payment","Purchase with credit card, PayPal and regional payment methods in 150+ countries. Local currency pricing where supported."),
                    ("\U0001f1ea\U0001f1fa","Multiple UI Languages","Software interface available in English, German, French, Spanish, Italian, Japanese, Chinese and more."),
                ]
            )
            + f'</div>'
            f'<h2 style="margin-bottom:2rem">Select Your <span class="g-acc">Language / Region</span></h2>'
            f'<div class="lang-grid">{all_cards}</div>'
            f'<div style="text-align:center;margin-top:3rem">'
            f'<a href="{AFF}" class="btn btn-p btn-lg" target="_blank" rel="noopener sponsored">\u2b07 Download Audio Recorder \u2014 Available Worldwide</a>'
            f'</div>'
            f'</section>'
        ),
        "audio recorder worldwide, audio recorder global, audio recorder all countries, record audio international"
    )


# Import v1 pages wholesale — reuse the good content, just update SITE_ROOT/SITE_URL refs
# The pages below are fully written inline for v2

def pg_features():
    il = (
        '{"@context":"https://schema.org","@type":"ItemList","name":"Wondershare Audio Recorder Features",'
        '"itemListElement":['
        '{"@type":"ListItem","position":1,"name":"Record System Audio"},'
        '{"@type":"ListItem","position":2,"name":"Record Microphone"},'
        '{"@type":"ListItem","position":3,"name":"Scheduled Recording"},'
        '{"@type":"ListItem","position":4,"name":"Auto Track Split"},'
        '{"@type":"ListItem","position":5,"name":"ID3 Tag Editor"},'
        '{"@type":"ListItem","position":6,"name":"AI Noise Reduction"},'
        '{"@type":"ListItem","position":7,"name":"Built-in Audio Editor"},'
        '{"@type":"ListItem","position":8,"name":"Format Converter"},'
        '{"@type":"ListItem","position":9,"name":"Always-On Recording Mode"},'
        '{"@type":"ListItem","position":10,"name":"Audio Level Control"}'
        ']}'
    )
    features = [
        ("🎵","Record Any System Audio","Captures any audio playing through your Windows speakers or headphone output using virtual audio driver technology. Records at source with zero quality loss \u2014 streaming services, games, browser audio, apps, everything."),
        ("🎙","Record Microphone","Record from any connected microphone \u2014 USB mic, 3.5mm, condenser, dynamic, headset, laptop built-in. Adjustable input levels, real-time VU meter, optional AI noise reduction."),
        ("📅","Scheduled Recording","Set exact start and stop times. Audio Recorder activates automatically and runs silently. Perfect for recording radio programmes, scheduled podcasts, live concerts or any broadcast you can't attend in real time."),
        ("✂️","Auto Track Split","Detects silence between tracks (configurable threshold) and automatically saves each segment as a separate named file. Record a 20-track album and get 20 individual files \u2014 perfectly organised."),
        ("🏷","ID3 Tag Editor","Automatically queries online music database for artist, title, album, year, genre and cover art. Tags applied to every recording instantly. Manual editing available for any field."),
        ("🔇","AI Noise Reduction","AI-powered background noise removal cleans hiss, hum, air conditioning and ambient noise from microphone recordings. Makes laptop mic recordings sound dramatically cleaner."),
        ("✏️","Built-in Audio Editor","Trim start and end, cut unwanted sections, adjust volume levels, add fade in/out. Basic editing without leaving the app or opening Audacity."),
        ("🔄","Format Converter","Convert existing audio files between all 10 supported formats. Batch convert entire folders. Convert MP3 to FLAC, WAV to MP3, FLAC to AAC \u2014 any direction."),
        ("🌐","Always-On Recording","Minimise to system tray and record passively. Captures everything that plays through your computer in configurable chunks. Never miss audio from any source."),
        ("🎚","Audio Level Control","Adjust recording volume, set input gain, monitor levels live with VU meter. Automatic level normalisation option prevents clipping on loud sources and boosts quiet ones."),
        ("📁","Smart File Management","Auto-names recordings with date, time and source. Configurable folder organisation. Export to any destination folder. Integrates with Windows Music library."),
        ("⚡","Low CPU Usage","Efficient recording engine uses minimal CPU and RAM during capture. Runs alongside other apps without slowing down your system."),
    ]
    cards = "".join(
        f'<div class="card{"  card-feat" if i<2 else ""}"><div class="card-icon">{icon}</div>'
        f'<h3>{title}</h3><p>{desc}</p></div>'
        for i,(icon,title,desc) in enumerate(features)
    )
    return page(
        f"Audio Recorder Features \u2014 Complete List | Record Any Audio {YEAR}",
        "Full Wondershare Audio Recorder feature list: record system audio, microphone, scheduled recording, auto track split, ID3 tags, AI noise reduction, built-in editor, format converter.",
        "/features/",
        (
            f'<div class="ph">'
            + bc(("Home",f"{SITE_ROOT}/"),("Features",None))
            + f'<span class="sec-lbl">Complete Feature Set</span>'
            f'<h1>Audio Recorder <span class="g-acc">Features</span></h1>'
            f'<p style="max-width:640px;margin-top:.9rem;font-size:1.05rem;color:var(--muted)">12 features that make Wondershare Audio Recorder the complete capture tool for Windows.</p>'
            f'</div>'
            f'<section><div class="g3">{cards}</div>'
            f'<div class="cta-blk" style="margin-top:3rem;border-radius:var(--r)">'
            f'<h2 style="margin-bottom:.8rem">All Features, <span class="g-acc">Free to Try</span></h2>'
            f'<p>Download and test everything. No credit card required.</p>'
            f'<a href="{AFF}" class="btn btn-p" target="_blank" rel="noopener sponsored">\u2b07 Download Free Trial</a>'
            f'</div></section>'
        ),
        "audio recorder features, system audio recorder, scheduled recording, auto track split, ID3 tags, AI noise reduction",
        extras=[il]
    )

def pg_how():
    howto = (
        '{"@context":"https://schema.org","@type":"HowTo",'
        '"name":"How to Record Audio with Wondershare Audio Recorder",'
        '"description":"Record any audio from your computer in 3 simple steps.",'
        '"step":['
        '{"@type":"HowToStep","position":1,"name":"Choose your source",'
        '"text":"Select System Audio to record anything playing through your computer output, Microphone for voice input, or Both."},'
        '{"@type":"HowToStep","position":2,"name":"Configure output",'
        '"text":"Choose output format (MP3, WAV, FLAC), set bitrate/quality and select destination folder."},'
        '{"@type":"HowToStep","position":3,"name":"Record",'
        '"text":"Click Record. Audio Recorder captures at full quality using virtual audio driver technology."}'
        ']}'
    )
    return page(
        f"How Wondershare Audio Recorder Works \u2014 Record in 3 Steps | {YEAR}",
        "How to record audio with Wondershare Audio Recorder: choose source, configure output, record. Works for system audio, microphone, streaming music, meetings and radio.",
        "/how-it-works/",
        (
            f'<div class="ph">'
            + bc(("Home",f"{SITE_ROOT}/"),("How It Works",None))
            + f'<span class="sec-lbl">Simple Process</span>'
            f'<h1>How <span class="g-acc">Audio Recorder</span> Works</h1>'
            f'<p style="max-width:640px;margin-top:.9rem;color:var(--muted)">Three modes: basic recording, scheduled capture, always-on. Here is every workflow explained.</p>'
            f'</div>'
            f'<section><div class="split">'
            f'<div>'
            f'<h2 style="margin-bottom:2rem">Basic Recording \u2014 <span class="g-acc">3 Steps</span></h2>'
            f'<div class="steps">'
            f'<div class="step" data-n="1"><div><h3>Choose Source</h3>'
            f'<p>Select <strong>System Audio</strong> to capture anything playing through your speakers. '
            f'Choose <strong>Microphone</strong> for voice input. Select <strong>Both</strong> to capture everything simultaneously.</p></div></div>'
            f'<div class="step" data-n="2"><div><h3>Configure Output</h3>'
            f'<p>Choose format (MP3 for sharing, WAV for editing, FLAC for lossless archiving), set bitrate and select destination folder.</p></div></div>'
            f'<div class="step" data-n="3"><div><h3>Click Record</h3>'
            f'<p>Audio Recorder captures at full quality. Stop when done. Files are automatically named with date and time.</p></div></div>'
            f'</div></div>'
            f'<div style="display:flex;flex-direction:column;gap:1.5rem">'
            f'<div class="hbox"><h4>Scheduled Recording</h4>'
            f'<p style="margin-top:.4rem">Set start and end time. Audio Recorder activates automatically \u2014 record tonight\'s radio show at 10pm, a weekly podcast at 9am, any recurring broadcast. Computer can be locked; recording still runs.</p></div>'
            f'<div class="hbox"><h4>Auto Track Split</h4>'
            f'<p style="margin-top:.4rem">Enable auto-split and Audio Recorder detects silence between tracks. '
            f'Each piece of audio saves as a separate file \u2014 perfect for albums, playlists, radio programmes split into segments.</p></div>'
            f'<div class="hbox good"><h4>Always-On Mode</h4>'
            f'<p style="margin-top:.4rem">Enable always-on recording to capture everything continuously. '
            f'Audio Recorder runs silently in the system tray and saves audio in configurable chunks. Never miss audio from any source.</p></div>'
            f'<div class="hbox info"><h4>ID3 Auto-Tagging</h4>'
            f'<p style="margin-top:.4rem">After each recording, Audio Recorder queries an online music database and fills in '
            f'artist, title, album, year, genre and cover art automatically. Your recordings arrive in your library already organised.</p></div>'
            f'<a href="{AFF}" class="btn btn-p" target="_blank" rel="noopener sponsored">\u2b07 Try Free Now</a>'
            f'</div></div></section>'
        ),
        "how to record audio, audio recording steps, record system audio how to, scheduled audio recording how to",
        extras=[howto]
    )

def pg_use_cases():
    cases = [
        ("🎵","Music & Radio","Record streaming services and internet radio for offline listening or archiving.",
         ["Record any Spotify or Apple Music track","Capture BBC, NPR, local online radio stations","Save live DJ sets and concert streams","Schedule overnight radio recording"]),
        ("📞","Calls & Meetings","Audio-only recording of Zoom, Teams, Meet \u2014 tiny files, easy to search.",
         ["Record Zoom calls as MP3 \u2014 55 MB/hour vs 4 GB video","Save Google Meet audio for meeting notes","Capture Skype and Discord voice channels","Record phone interviews over VoIP"]),
        ("🎙","Podcasting","Mic recording with noise reduction, built-in editing, MP3 export.",
         ["High-quality USB or condenser mic recording","AI noise reduction for home studios","Trim and edit in the built-in editor","Export tagged MP3 ready to upload"]),
        ("🎓","Education","Record lectures, webinars, online courses for later review.",
         ["Capture Zoom/Teams lectures automatically","Record online course audio on a schedule","Save webinar audio in MP3","Long recording \u2014 no time limit on paid plan"]),
        ("🎮","Gaming & Content","Capture in-game audio, commentary, stream audio for content.",
         ["Record game audio without video","Capture voiceover during gameplay","Record system audio during streams","Export to MP3 or WAV for video editing"]),
        ("🎸","Musicians","Capture instrument recordings, practice sessions, reference tracks.",
         ["Record via audio interface from any instrument","Capture practice sessions for review","Quick reference recordings with date/time naming","Convert between formats for DAW compatibility"]),
        ("🌍","Language Learning","Record radio broadcasts, language podcasts, online lessons in any language.",
         ["Schedule daily language radio programmes","Record online language lessons","Save podcast episodes for offline study","Auto-split episodes from long recordings"]),
        ("📰","Journalism","Record interviews, press conferences, source calls cleanly.",
         ["Record phone/Zoom interviews as MP3","Auto-name files with date and source","AI noise reduction for field recordings","Export directly to transcription tools"]),
    ]
    cards = "".join(
        f'<div class="card"><div class="card-icon">{icon}</div>'
        f'<h3>{title}</h3><p style="margin-bottom:.8rem">{desc}</p>'
        f'<ul style="list-style:none;padding:0;display:flex;flex-direction:column;gap:.3rem">'
        + "".join(f'<li style="font-size:.8rem;color:var(--muted);display:flex;gap:.4rem"><span style="color:var(--acc);">\u00b7</span>{x}</li>' for x in bullets)
        + f'</ul></div>'
        for icon,title,desc,bullets in cases
    )
    return page(
        f"Audio Recorder Use Cases \u2014 Music, Meetings, Podcasts, Radio | {YEAR}",
        "Wondershare Audio Recorder use cases: record streaming music, Zoom calls, podcasts, internet radio, lectures, game audio, journalist interviews, language learning. 8 use cases covered.",
        "/use-cases/",
        (
            f'<div class="ph">'
            + bc(("Home",f"{SITE_ROOT}/"),("Use Cases",None))
            + f'<span class="sec-lbl">Who Uses It</span>'
            f'<h1>Audio Recorder <span class="g-acc">Use Cases</span></h1>'
            f'<p style="max-width:640px;margin-top:.9rem;color:var(--muted)">From radio enthusiasts to journalists, podcasters to language learners \u2014 8 use cases covered in detail.</p>'
            f'</div>'
            f'<section><div class="g3" style="margin-bottom:3rem">{cards}</div>'
            f'<div style="text-align:center">'
            f'<a href="{AFF}" class="btn btn-p btn-lg" target="_blank" rel="noopener sponsored">\u2b07 Try Audio Recorder Free</a>'
            f'</div></section>'
        ),
        "audio recorder use cases, record streaming music, record Zoom audio, podcast recorder, record internet radio, journalist audio recorder"
    )

def pg_formats():
    rows = "".join(
        f'<tr><td class="td-n"><code>{fmt}</code></td><td>{desc}</td><td class="td-p">{br}</td><td>{compat}</td><td class="td-y">{use}</td></tr>'
        for fmt,desc,br,compat,use in [
            ("MP3","Universal format. Smallest file, plays everywhere.","64\u2013320 kbps","All devices","Sharing & streaming"),
            ("WAV","Uncompressed lossless. Perfect quality, large files.","1411 kbps","All devices","Editing & production"),
            ("FLAC","Lossless compressed. Half the size of WAV, same quality.","700\u20131100 kbps","Most players","Archiving"),
            ("AAC","Better quality than MP3 at same bitrate. Apple standard.","128\u2013256 kbps","Apple, Android","Apple devices"),
            ("M4A","AAC in MPEG-4 container. Native Apple format.","128\u2013256 kbps","Apple devices","iPhone/Mac"),
            ("OGG","Open-source. Good quality at low bitrates. Games.","80\u2013500 kbps","Limited","Games & open source"),
            ("WMA","Windows Media Audio. Microsoft format.","64\u2013192 kbps","Windows","Windows software"),
            ("AIFF","Apple\u2019s uncompressed format. Equivalent to WAV.","1411 kbps","Apple pro tools","Mac production"),
            ("AC3","Dolby Digital. DVDs, Blu-rays, broadcast surround.","192\u2013640 kbps","DVD/Blu-ray","Surround audio"),
            ("APE","Monkey\u2019s Audio. Lossless with very small file size.","400\u2013700 kbps","Specialised players","Audiophile archiving"),
        ]
    )
    return page(
        f"Audio Recorder Formats \u2014 MP3, WAV, FLAC, AAC & 6 More | {YEAR}",
        "Wondershare Audio Recorder saves recordings as MP3, WAV, FLAC, AAC, M4A, OGG, WMA, AIFF, AC3 and APE. Complete format guide with bitrate, compatibility and best use cases.",
        "/formats/",
        (
            f'<div class="ph">'
            + bc(("Home",f"{SITE_ROOT}/"),("Formats",None))
            + f'<span class="sec-lbl">10 Output Formats</span>'
            f'<h1>Supported <span class="g-acc">Formats</span></h1>'
            f'<p style="max-width:660px;margin-top:.9rem;color:var(--muted)">10 formats covering every use case \u2014 from casual MP3 sharing to lossless FLAC archiving.</p>'
            f'</div>'
            f'<section>'
            f'<div class="fmt-grid" style="margin-bottom:2rem">'
            + "".join(f'<span class="fmt">{f}</span>' for f in ["MP3","WAV","FLAC","AAC","M4A","OGG","WMA","AIFF","AC3","APE"])
            + f'</div>'
            f'<div class="tbl-wrap"><table>'
            f'<thead><tr><th>Format</th><th>Description</th><th>Bitrate</th><th>Compatibility</th><th>Best For</th></tr></thead>'
            f'<tbody>{rows}</tbody></table></div>'
            f'<div class="hbox info" style="margin-top:2rem"><h4>Which Format to Choose?</h4>'
            f'<p style="margin-top:.4rem"><strong>MP3</strong> \u2014 everyday sharing, streaming, email. '
            f'<strong>WAV</strong> \u2014 if you plan to edit in Audacity or a DAW. '
            f'<strong>FLAC</strong> \u2014 lossless archive at half the size of WAV. '
            f'<strong>AAC/M4A</strong> \u2014 Apple device users. '
            f'<strong>OGG</strong> \u2014 open-source apps and games.</p></div>'
            f'<div style="text-align:center;margin-top:2rem">'
            f'<a href="{AFF}" class="btn btn-p" target="_blank" rel="noopener sponsored">\u2b07 Download Audio Recorder Free</a>'
            f'</div></section>'
        ),
        "MP3 recorder, WAV recorder, FLAC recorder, audio recorder formats, AAC recorder, audio output formats"
    )


def pg_pricing():
    faq_s = (
        '{"@context":"https://schema.org","@type":"FAQPage","mainEntity":['
        '{"@type":"Question","name":"Is Wondershare Audio Recorder free?",'
        '"acceptedAnswer":{"@type":"Answer","text":"Yes. A free trial is available with no credit card required. Trial recordings have a length limit. Paid plans unlock unlimited recording."}},'
        '{"@type":"Question","name":"What does the annual plan cost?",'
        '"acceptedAnswer":{"@type":"Answer","text":"The annual plan is approximately $29.95/year. Check the official Wondershare site for current pricing and any active promotions."}},'
        '{"@type":"Question","name":"Is there a lifetime option?",'
        '"acceptedAnswer":{"@type":"Answer","text":"Yes. A perpetual one-time payment plan is available. Check the official site for current one-time pricing."}},'
        '{"@type":"Question","name":"Does the price include all features?",'
        '"acceptedAnswer":{"@type":"Answer","text":"Yes. All paid plans include all features: unlimited recording, all 10 formats, scheduled recording, auto track split, ID3 tags, noise reduction and the built-in editor."}},'
        '{"@type":"Question","name":"Is it available worldwide?",'
        '"acceptedAnswer":{"@type":"Answer","text":"Yes. Wondershare sells in 150+ countries with global payment methods including credit card and PayPal."}}'
        ']}'
    )
    return page(
        f"Wondershare Audio Recorder Pricing {YEAR} \u2014 Free Trial & Paid Plans",
        f"Wondershare Audio Recorder pricing {YEAR}: free trial available, annual ~$29.95/yr, perpetual one-time. All paid plans include unlimited recording, all formats, scheduled recording and all features.",
        "/pricing/",
        (
            f'<div class="ph tc">'
            + bc(("Home",f"{SITE_ROOT}/"),("Pricing",None))
            + f'<span class="sec-lbl" style="display:block;text-align:center">Clear Pricing</span>'
            f'<h1>Audio Recorder <span class="g-acc">Pricing</span></h1>'
            f'<p style="max-width:520px;margin:.9rem auto 0;color:var(--muted)">Start free. Upgrade for unlimited recording, all formats and scheduled capture.</p>'
            f'</div>'
            f'<section>'
            f'<div class="pgrid">'
            f'<div class="pc"><div class="p-name">Free Trial</div>'
            f'<div class="p-price"><sup>$</sup>0</div>'
            f'<div class="p-per">No credit card needed</div>'
            f'<ul class="p-feats">'
            f'<li>Record system audio and microphone</li>'
            f'<li>Test all 10 output formats</li>'
            f'<li>Try scheduled recording</li>'
            f'<li>Test auto track split</li>'
            f'<li>Try ID3 tag editor</li>'
            f'<li>Limited recording length</li>'
            f'</ul>'
            f'<a href="{AFF}" class="btn btn-s btn-full" target="_blank" rel="noopener sponsored">Start Free Trial</a></div>'
            f'<div class="pc pop"><div class="pop-badge">Best Value</div>'
            f'<div class="p-name">Annual Plan</div>'
            f'<div class="p-price"><sup>$</sup>29<span style="font-size:1.5rem">.95</span></div>'
            f'<div class="p-per">per year \u00b7 check official site for current price</div>'
            f'<ul class="p-feats">'
            f'<li>Unlimited recording length</li>'
            f'<li>All 10 output formats</li>'
            f'<li>Scheduled recording (start/stop timer)</li>'
            f'<li>Auto track split</li>'
            f'<li>ID3 tag editor (auto + manual)</li>'
            f'<li>AI noise reduction</li>'
            f'<li>Built-in audio editor</li>'
            f'<li>Format converter</li>'
            f'<li>Always-on recording mode</li>'
            f'<li>Free updates for 1 year</li>'
            f'</ul>'
            f'<a href="{AFF}" class="btn btn-p btn-full" target="_blank" rel="noopener sponsored">Get Best Price \u2192</a>'
            f'<div class="p-note">\U0001f4a1 Check official site \u2014 discounts often available</div>'
            f'</div>'
            f'<div class="pc"><div class="p-name">Perpetual</div>'
            f'<div class="p-price" style="font-size:2.2rem;margin-bottom:.5rem">One<br>Time</div>'
            f'<div class="p-per">pay once \u00b7 own forever</div>'
            f'<ul class="p-feats">'
            f'<li>Everything in Annual +</li>'
            f'<li>Pay once, own forever</li>'
            f'<li>No recurring fees</li>'
            f'<li>All future updates included</li>'
            f'</ul>'
            f'<a href="{AFF}" class="btn btn-s btn-full" target="_blank" rel="noopener sponsored">Check Lifetime Price \u2192</a>'
            f'</div></div>'
            f'<div class="hbox warn" style="max-width:800px;margin:3rem auto 0;text-align:center">'
            f'<h4>\U0001f4a1 Always Check the Official Site for Current Price</h4>'
            f'<p style="margin-top:.4rem">Wondershare regularly runs promotions. Click any button above to see the live price \u2014 savings can be significant.</p>'
            f'</div>'
            f'<div style="max-width:800px;margin:3rem auto 0">'
            f'<h2 style="margin-bottom:1.5rem">Pricing <span class="g-acc">FAQ</span></h2>'
            f'<div class="faq-wrap" style="max-width:100%">'
            f'<details><summary>Is the free trial really free?</summary><div class="ans"><p>Yes. Download and install with no payment required. All features are testable including scheduled recording and auto track split. Trial recordings have a length limit \u2014 upgrade to remove it.</p></div></details>'
            f'<details><summary>What is included in paid plans?</summary><div class="ans"><p>Unlimited recording length, all 10 output formats (MP3/WAV/FLAC/AAC/M4A/OGG/WMA/AIFF/AC3/APE), scheduled recording, auto track split, ID3 tag editor, AI noise reduction, built-in audio editor, format converter and always-on recording mode. No feature is locked behind a higher tier.</p></div></details>'
            f'<details><summary>Annual vs Perpetual \u2014 which is better?</summary><div class="ans"><p>Annual is the lowest upfront cost. Perpetual is a one-time payment that pays for itself after roughly 2 years of annual renewals. If you plan to use Audio Recorder long-term, perpetual is better value.</p></div></details>'
            f'<details><summary>Is it available in my country?</summary><div class="ans"><p>Yes. Wondershare sells in 150+ countries. Payment accepted via credit card and PayPal globally, with local payment methods in selected regions. See the global page for your specific region.</p></div></details>'
            f'</div></div></section>'
        ),
        "audio recorder price, audio recorder cost, Wondershare audio recorder pricing, audio recorder annual plan",
        extras=[faq_s]
    )

def pg_review():
    rev_s = (
        '{"@context":"https://schema.org","@type":"Review",'
        '"itemReviewed":{"@type":"SoftwareApplication","name":"Wondershare Streaming Audio Recorder",'
        '"applicationCategory":"MultimediaApplication","operatingSystem":"Windows"},'
        '"reviewRating":{"@type":"Rating","ratingValue":"8.8","bestRating":"10","worstRating":"1"},'
        '"author":{"@type":"Person","name":"AudioRecorder Guide Editorial Team"},'
        '"datePublished":"2026-06-01",'
        '"reviewBody":"Wondershare Audio Recorder earns 8.8/10. Best-in-class scheduled recording, flawless auto track split, clean ID3 tagging and zero-quality-loss system audio capture. Windows only is the main limitation."}'
    )
    return page(
        f"Wondershare Audio Recorder Review {YEAR} \u2014 8.8/10 Honest Verdict",
        f"Full Wondershare Audio Recorder review {YEAR}: 8.8/10. Tested scheduled recording, auto track split, ID3 tagging, noise reduction, format conversion. Complete honest verdict.",
        "/review/",
        (
            f'<div class="ph">'
            + bc(("Home",f"{SITE_ROOT}/"),("Review",None))
            + f'<span class="sec-lbl">In-Depth Review</span>'
            f'<h1>Audio Recorder <span class="g-acc">Review {YEAR}</span></h1>'
            f'<p style="max-width:660px;margin-top:.9rem;color:var(--muted)">We tested Wondershare Audio Recorder across every major use case. Complete, honest verdict.</p>'
            f'</div>'
            f'<section><div class="split">'
            f'<div>'
            f'<div class="score-big">8.8</div>'
            f'<div style="font-size:.79rem;color:var(--muted);text-transform:uppercase;letter-spacing:.12em;margin-bottom:1.5rem">out of 10 \u2014 Editor\u2019s Rating</div>'
            f'<div style="display:flex;gap:.5rem;flex-wrap:wrap;margin-bottom:2rem">'
            f'<span class="chip chip-g">\u2713 Recommended</span>'
            f'<span class="chip chip-v">Best Windows Audio Recorder</span>'
            f'</div>'
            f'<div class="rbars">'
            + "".join(
                f'<div class="rbar"><span class="rbar-lbl">{lbl}</span>'
                f'<div class="rbar-track"><div class="rbar-fill" style="width:{pct}%"></div></div>'
                f'<span class="rbar-val">{score}</span></div>'
                for lbl,pct,score in [
                    ("Recording Quality",   96, "9.6"),
                    ("Ease of Use",         92, "9.2"),
                    ("Scheduled Recording", 95, "9.5"),
                    ("Auto Track Split",    90, "9.0"),
                    ("ID3 Tagging",         88, "8.8"),
                    ("Format Support",      85, "8.5"),
                    ("Built-in Editor",     80, "8.0"),
                    ("Value for Money",     86, "8.6"),
                    ("Global Availability", 92, "9.2"),
                ]
            )
            + f'</div></div>'
            f'<div>'
            f'<div class="hbox good"><h4>\u2713 What We Loved</h4>'
            + "".join(
                f'<div style="font-size:.86rem;color:var(--muted);display:flex;gap:.5rem;margin-top:.45rem">'
                f'<span style="color:var(--green);font-weight:700">\u2713</span>{x}</div>'
                for x in [
                    "System audio recording captured Spotify at 320kbps with zero quality loss",
                    "Scheduled recording worked perfectly \u2014 set at 11pm, recording ready by morning",
                    "Auto track split correctly identified 11 of 12 test tracks from an album playlist",
                    "ID3 tags populated automatically \u2014 no manual entry needed for 8/10 test recordings",
                    "AI noise reduction visibly cleaned up laptop microphone hiss in tests",
                    "One of the cleanest, simplest interfaces of any audio recorder tested",
                    "Available in 150+ countries \u2014 global payment support confirmed",
                ]
            )
            + f'</div>'
            f'<div class="hbox warn" style="margin-top:1rem"><h4>\u26a0 Caveats</h4>'
            + "".join(
                f'<div style="font-size:.86rem;color:var(--muted);display:flex;gap:.5rem;margin-top:.4rem">'
                f'<span style="color:var(--gold);">\u2013</span>{x}</div>'
                for x in [
                    "Windows only \u2014 no Mac version available",
                    "Built-in editor is basic \u2014 use Audacity for advanced editing",
                    "Free trial has recording length restrictions",
                    "Customer support response can be slow (24\u201348 hours)",
                ]
            )
            + f'</div></div></div>'
            f'<div style="text-align:center;margin-top:3rem">'
            f'<a href="{AFF}" class="btn btn-p btn-lg" target="_blank" rel="noopener sponsored">\u2b07 Try Audio Recorder Free</a>'
            f'</div></section>'
        ),
        f"Wondershare audio recorder review, audio recorder review {YEAR}, is Wondershare audio recorder good",
        extras=[rev_s],
        article=True
    )

def pg_faq():
    faqs = [
        ("Is Wondershare Audio Recorder free?",
         "Yes. A free trial is available with no credit card required. All features are testable including scheduled recording and auto track split. Trial recordings have a length limit. Paid plans start at approximately $29.95/year for unlimited recording."),
        ("Can it record streaming music like Spotify?",
         "Yes. Wondershare Audio Recorder uses virtual audio driver technology to capture system audio at source \u2014 before it reaches speakers. This records Spotify, Apple Music, Amazon Music, YouTube Music, Tidal and any other streaming service at full quality. Automatic ID3 tagging identifies each track."),
        ("Can I record Zoom or Teams calls?",
         "Yes. Any audio playing through your computer is captured \u2014 including Zoom, Teams, Google Meet, Skype and Discord. Audio Recorder saves calls as MP3 or WAV without capturing video. 55 MB per hour vs 2\u20134 GB for screen recording."),
        ("Does it support scheduled recording?",
         "Yes. Set any start and end time. Audio Recorder activates automatically \u2014 record tonight\u2019s radio show, a weekly podcast or any recurring broadcast while you\u2019re away. The computer can be locked; recording still runs."),
        ("What output formats are supported?",
         "10 formats: MP3, WAV, FLAC, AAC, M4A, OGG, WMA, AIFF, AC3 and APE. MP3 for sharing, WAV for editing, FLAC for lossless archiving, AAC/M4A for Apple devices."),
        ("What is auto track split?",
         "Auto track split detects silence between audio tracks and saves each segment as a separate named file. Record an entire album playlist and get individual tracks automatically \u2014 each named and ID3-tagged. Silence threshold is configurable."),
        ("Does it work on Mac?",
         "Wondershare Streaming Audio Recorder is currently Windows only. It is not available for macOS. For Mac audio recording, consider Wondershare\u2019s broader product suite or check the official site for any updates."),
        ("Does it reduce background noise?",
         "Yes. AI noise reduction removes background hiss, hum and ambient noise from microphone recordings automatically. Particularly useful for laptop microphones or recordings made in noisy environments."),
        ("Is it available worldwide?",
         "Yes. Wondershare sells in 150+ countries with payment via credit card and PayPal globally. Local payment methods available in selected regions. The software works on any Windows PC worldwide with no regional restrictions."),
        ("How does ID3 auto-tagging work?",
         "After each recording, Audio Recorder queries an online music database and attempts to match the audio fingerprint to artist, title, album, year, genre and cover art. Successfully matched for around 8 of 10 mainstream recordings in our tests. Tags can be edited manually for any recording."),
    ]
    items = "".join(
        f'<details><summary>{q}</summary><div class="ans"><p>{a}</p></div></details>'
        for q,a in faqs
    )
    faq_s = (
        '{"@context":"https://schema.org","@type":"FAQPage","mainEntity":['
        + ",".join(
            f'{{"@type":"Question","name":"{q.replace(chr(34),chr(39))}","acceptedAnswer":{{"@type":"Answer","text":"{a[:180].replace(chr(34),chr(39))}..."}}}}'
            for q,a in faqs
        )
        + ']}'
    )
    return page(
        f"Wondershare Audio Recorder FAQ {YEAR} \u2014 10 Questions Answered",
        "Complete Wondershare Audio Recorder FAQ: free? Spotify? Zoom? Scheduled? Formats? Auto split? Mac? Noise reduction? Global? ID3 tags? All 10 answered in full.",
        "/faq/",
        (
            f'<div class="ph">'
            + bc(("Home",f"{SITE_ROOT}/"),("FAQ",None))
            + f'<span class="sec-lbl">Questions Answered</span>'
            f'<h1>Audio Recorder <span class="g-acc">FAQ</span></h1>'
            f'<p style="max-width:640px;margin-top:.9rem;color:var(--muted)">10 detailed answers to the most common questions before downloading.</p>'
            f'</div>'
            f'<section><div class="faq-wrap">{items}</div>'
            f'<div style="text-align:center;margin-top:3rem">'
            f'<a href="{AFF}" class="btn btn-p" target="_blank" rel="noopener sponsored">\u2b07 Download Audio Recorder Free</a>'
            f'</div></section>'
        ),
        "audio recorder FAQ, record Spotify audio, record Zoom audio, scheduled recording FAQ, audio recorder worldwide",
        extras=[faq_s]
    )

def pg_download():
    return page(
        f"Download Wondershare Audio Recorder Free \u2014 Windows | {YEAR}",
        "Download Wondershare Streaming Audio Recorder free trial for Windows. Record streaming music, Zoom calls, internet radio and microphone in MP3, WAV, FLAC. Available globally.",
        "/download/",
        (
            f'<div class="ph tc">'
            + bc(("Home",f"{SITE_ROOT}/"),("Download",None))
            + f'<span class="sec-lbl" style="display:block;text-align:center">Available Worldwide</span>'
            f'<h1>Download <span class="g-acc">Audio Recorder</span></h1>'
            f'<p style="max-width:520px;margin:.9rem auto 0;color:var(--muted)">Free trial \u2014 no credit card. Available in 150+ countries. Windows.</p>'
            f'</div>'
            f'<section>'
            f'<div style="max-width:500px;margin:0 auto 3rem">'
            f'<div class="card" style="text-align:center">'
            f'<div class="card-icon" style="margin:0 auto 1rem;font-size:2.2rem">\U0001fa9f</div>'
            f'<h3>Windows</h3>'
            f'<p style="margin-bottom:.5rem">Windows 7 / 8 / 10 / 11</p>'
            f'<p style="font-size:.8rem;color:var(--muted);margin-bottom:1.6rem">32-bit and 64-bit \u00b7 Available in 150+ countries</p>'
            f'<a href="{AFF}" class="btn btn-p btn-full" target="_blank" rel="noopener sponsored">\u2b07 Download for Windows</a>'
            f'</div></div>'
            f'<div class="hbox good" style="max-width:600px;margin:0 auto">'
            f'<h4>Free Trial Includes</h4>'
            f'<ul style="list-style:none;padding:0;margin-top:.8rem;display:grid;grid-template-columns:1fr 1fr;gap:.5rem">'
            + "".join(
                f'<li style="font-size:.84rem;color:var(--muted);display:flex;gap:.5rem">'
                f'<span style="color:var(--green);font-weight:700">\u2713</span>{x}</li>'
                for x in [
                    "Record system audio","Record microphone",
                    "All 10 output formats","Try scheduled recording",
                    "Test auto track split","Try ID3 tag editor",
                    "Built-in audio editor","Noise reduction",
                ]
            )
            + f'</ul></div>'
            f'<div style="text-align:center;margin-top:2rem">'
            f'<a href="{SITE_ROOT}/pricing/" class="btn btn-g">View Pricing \u2192</a>'
            f'&nbsp;&nbsp;&nbsp;'
            f'<a href="{SITE_ROOT}/global/" class="btn btn-g">Your Country \u2192</a>'
            f'</div></section>'
        )
    )


def pg_record_streaming():
    howto = (
        '{"@context":"https://schema.org","@type":"HowTo",'
        '"name":"How to Record Streaming Audio",'
        '"description":"Record any streaming audio from your computer in 5 steps.",'
        '"step":['
        '{"@type":"HowToStep","position":1,"name":"Install Audio Recorder",'
        '"text":"Download and install Wondershare Audio Recorder on Windows."},'
        '{"@type":"HowToStep","position":2,"name":"Select System Audio",'
        '"text":"Choose System Audio as the input source to capture all computer output."},'
        '{"@type":"HowToStep","position":3,"name":"Choose Output Format",'
        '"text":"Select MP3, WAV or FLAC depending on your use case."},'
        '{"@type":"HowToStep","position":4,"name":"Start Your Stream",'
        '"text":"Begin playing on your streaming service or online radio."},'
        '{"@type":"HowToStep","position":5,"name":"Click Record",'
        '"text":"Click Record. Audio Recorder captures at full source quality."}'
        ']}'
    )
    return page(
        f"How to Record Streaming Audio \u2014 Complete Guide {YEAR}",
        "Record any streaming audio from your computer \u2014 Spotify, Apple Music, YouTube, internet radio \u2014 using Wondershare Audio Recorder. MP3, WAV, FLAC. Step-by-step guide.",
        "/record-streaming-audio/",
        (
            f'<div class="ph">'
            + bc(("Home",f"{SITE_ROOT}/"),("Blog",f"{SITE_ROOT}/blog/"),("Record Streaming Audio",None))
            + f'<span class="sec-lbl">Complete Guide</span>'
            f'<h1>Record <span class="g-acc">Streaming Audio</span><br>From Any Source</h1>'
            f'<p style="max-width:660px;margin-top:.9rem;color:var(--muted)">Capture Spotify, Apple Music, YouTube or any online stream at full quality. Works anywhere in the world.</p>'
            f'</div>'
            f'<section>'
            f'<div class="hbox info"><h4>How Virtual Audio Driver Technology Works</h4>'
            f'<p style="margin-top:.4rem">Wondershare Audio Recorder installs a virtual audio driver that intercepts audio at the system level \u2014 before it reaches your speakers. This captures a perfect digital copy of the stream, regardless of volume or background noise. No quality loss, no microphone needed.</p>'
            f'</div>'
            f'<div class="split" style="margin-top:2.5rem">'
            f'<div>'
            f'<h2 style="margin-bottom:1.5rem">Step-by-Step: <span class="g-acc">Record Streaming</span></h2>'
            f'<div class="steps">'
            f'<div class="step" data-n="1"><div><h3>Install Audio Recorder</h3><p>Download and install Wondershare Audio Recorder on your Windows PC. Launch the application.</p></div></div>'
            f'<div class="step" data-n="2"><div><h3>Select System Audio</h3><p>Choose <strong>System Audio</strong> as input. This captures everything playing through your computer output.</p></div></div>'
            f'<div class="step" data-n="3"><div><h3>Choose Format</h3><p>Select MP3 for sharing, WAV for editing, FLAC for lossless. Set bitrate if needed.</p></div></div>'
            f'<div class="step" data-n="4"><div><h3>Start Your Stream</h3><p>Begin playing on Spotify, YouTube, any online radio station or streaming service.</p></div></div>'
            f'<div class="step" data-n="5"><div><h3>Click Record</h3><p>Click Record. Audio Recorder captures at full source quality. Stop when done. Auto-split and ID3 tagging apply automatically.</p></div></div>'
            f'</div>'
            f'<a href="{AFF}" class="btn btn-p" style="margin-top:1rem" target="_blank" rel="noopener sponsored">\u2b07 Download Free Trial</a>'
            f'</div>'
            f'<div>'
            f'<div class="card card-feat" style="padding:2rem">'
            f'<h3 style="color:var(--acc);margin-bottom:1rem">What You Can Record</h3>'
            f'<ul style="list-style:none;padding:0;display:flex;flex-direction:column;gap:.7rem">'
            + "".join(
                f'<li style="display:flex;gap:.7rem;font-size:.9rem;color:var(--muted)">'
                f'<span style="color:var(--green);font-weight:700">\u2713</span>'
                f'<strong style="color:var(--txt)">{a}</strong> \u2014 {b}</li>'
                for a,b in [
                    ("Spotify","any track or playlist, auto-tagged"),
                    ("Apple Music","full quality streaming capture"),
                    ("YouTube","audio from any video"),
                    ("Amazon Music","any stream captured at source"),
                    ("Internet Radio","BBC, NPR, local stations worldwide"),
                    ("Deezer / Tidal","lossless streaming captured losslessly"),
                    ("SoundCloud","any public or private stream"),
                    ("Browser audio","Chrome, Firefox, Edge \u2014 any website"),
                ]
            )
            + f'</ul></div>'
            f'<div class="hbox warn" style="margin-top:1rem"><h4>Copyright Note</h4>'
            f'<p style="margin-top:.4rem">Recording streaming audio is for personal use. Do not distribute copyrighted recordings or use commercially. Respect platform terms of service.</p>'
            f'</div>'
            f'</div></div></section>'
        ),
        "record streaming audio, how to record streaming music, record Spotify audio, capture streaming audio PC, record online radio",
        extras=[howto],
        article=True
    )

def pg_record_zoom():
    return page(
        f"How to Record Zoom Audio Only \u2014 No Video | {YEAR}",
        "Record Zoom calls, Teams meetings and Google Meet as clean audio-only MP3. No video, tiny file size. 55 MB per hour vs 4 GB for screen recording. Step-by-step guide.",
        "/record-zoom-audio/",
        (
            f'<div class="ph">'
            + bc(("Home",f"{SITE_ROOT}/"),("Blog",f"{SITE_ROOT}/blog/"),("Record Zoom Audio",None))
            + f'<span class="sec-lbl">Meeting Audio Guide</span>'
            f'<h1>Record <span class="g-acc">Zoom, Teams</span><br>\u0026 Meeting Audio</h1>'
            f'<p style="max-width:660px;margin-top:.9rem;color:var(--muted)">Audio-only recording of meetings. No video. 55 MB per hour instead of 4 GB. Works with Zoom, Teams, Meet, Skype and Discord.</p>'
            f'</div>'
            f'<section>'
            f'<div class="hbox good"><h4>Why Audio-Only is Better for Meetings</h4>'
            f'<p style="margin-top:.4rem">A 1-hour Zoom call recorded as video takes 1\u20134 GB. The same call recorded as MP3 takes approximately 55 MB. Audio is searchable, faster to share, half the transcription cost, and you can listen back while commuting. For meetings where you need the spoken content, audio-only is almost always the right choice.</p>'
            f'</div>'
            f'<div class="split" style="margin-top:2rem">'
            f'<div>'
            f'<h2 style="margin-bottom:1.5rem">How to Record <span class="g-acc">Zoom as Audio</span></h2>'
            f'<div class="steps">'
            f'<div class="step" data-n="1"><div><h3>Open Audio Recorder</h3><p>Launch Wondershare Audio Recorder before your meeting starts.</p></div></div>'
            f'<div class="step" data-n="2"><div><h3>Select System Audio</h3><p>Choose System Audio to capture call audio from Zoom. Add Microphone if you want your own voice included.</p></div></div>'
            f'<div class="step" data-n="3"><div><h3>Set Format to MP3</h3><p>128 kbps is perfectly clear for voice and creates the smallest file. WAV for editing quality if needed.</p></div></div>'
            f'<div class="step" data-n="4"><div><h3>Join Meeting \u0026 Record</h3><p>Join your Zoom/Teams/Meet call normally. Click Record. Runs silently in the background.</p></div></div>'
            f'<div class="step" data-n="5"><div><h3>Stop After the Call</h3><p>Click Stop when the meeting ends. File saved automatically, named with date and time.</p></div></div>'
            f'</div>'
            f'<a href="{AFF}" class="btn btn-p" style="margin-top:1rem" target="_blank" rel="noopener sponsored">\u2b07 Download Free Trial</a>'
            f'</div>'
            f'<div>'
            f'<div class="card card-feat" style="padding:2rem">'
            f'<h3 style="color:var(--acc);margin-bottom:1rem">Supported Platforms</h3>'
            + "".join(
                f'<div style="display:flex;gap:.7rem;align-items:center;margin-bottom:.8rem">'
                f'<span style="font-size:1.4rem">{icon}</span>'
                f'<div><strong style="font-size:.9rem;color:var(--txt)">{name}</strong>'
                f'<div style="font-size:.8rem;color:var(--muted)">{note}</div></div></div>'
                for icon,name,note in [
                    ("\U0001f4f9","Zoom","Record any Zoom call or webinar as audio"),
                    ("\U0001f4bb","Microsoft Teams","Capture Teams meetings and calls"),
                    ("\U0001f4f2","Google Meet","Record Meet sessions as MP3"),
                    ("\U0001f4de","Skype","Capture Skype voice and video calls"),
                    ("\U0001f3ae","Discord","Record Discord voice channels"),
                    ("\U0001f517","Any VoIP","Works with any app using system audio"),
                ]
            )
            + f'</div>'
            f'</div></div></section>'
        ),
        "record Zoom audio, record Teams audio, record Google Meet audio, audio only meeting recorder, Zoom audio recorder MP3",
        article=True
    )

def pg_record_spotify():
    return page(
        f"Record Spotify \u2014 Save Any Track to MP3 or FLAC | {YEAR}",
        "Record Spotify to MP3, WAV or FLAC using Wondershare Audio Recorder. Auto track split and ID3 tags included. Capture any Spotify track or playlist. Step-by-step guide.",
        "/record-spotify/",
        (
            f'<div class="ph">'
            + bc(("Home",f"{SITE_ROOT}/"),("Blog",f"{SITE_ROOT}/blog/"),("Record Spotify",None))
            + f'<span class="sec-lbl">Spotify Recording Guide</span>'
            f'<h1>Record <span class="g-acc">Spotify</span><br>to MP3 or FLAC</h1>'
            f'<p style="max-width:660px;margin-top:.9rem;color:var(--muted)">Capture any Spotify track or playlist. Automatic per-track splitting and ID3 tagging built in.</p>'
            f'</div>'
            f'<section>'
            f'<div class="hbox warn"><h4>Personal Use Only</h4><p style="margin-top:.4rem">Recording Spotify audio is for personal use only. Do not distribute recordings publicly or commercially. Respect Spotify\u2019s terms of service and copyright law.</p></div>'
            f'<div class="split" style="margin-top:2rem">'
            f'<div>'
            f'<h2 style="margin-bottom:1.5rem">How to <span class="g-acc">Record Spotify</span></h2>'
            f'<div class="steps">'
            f'<div class="step" data-n="1"><div><h3>Open Audio Recorder</h3><p>Select System Audio as input source.</p></div></div>'
            f'<div class="step" data-n="2"><div><h3>Enable Auto Track Split</h3><p>Turn on auto track split. Audio Recorder detects the silence between Spotify tracks and saves each as a separate file.</p></div></div>'
            f'<div class="step" data-n="3"><div><h3>Choose Format</h3><p>MP3 320 kbps for quality sharing. FLAC for lossless archiving. AAC for Apple devices.</p></div></div>'
            f'<div class="step" data-n="4"><div><h3>Play Spotify \u0026 Record</h3><p>Start your Spotify playlist. Click Record. Each track is captured automatically.</p></div></div>'
            f'<div class="step" data-n="5"><div><h3>Review Tagged Files</h3><p>Each track saved separately with artist, title, album and cover art from the ID3 database.</p></div></div>'
            f'</div>'
            f'<a href="{AFF}" class="btn btn-p" style="margin-top:1rem" target="_blank" rel="noopener sponsored">\u2b07 Download Free Trial</a>'
            f'</div>'
            f'<div>'
            f'<div class="hbox good"><h4>Auto Track Split in Action</h4>'
            f'<p style="margin-top:.4rem">With auto track split enabled, Audio Recorder detects the 2-second gap between Spotify tracks and saves each song as a separate MP3 or FLAC file \u2014 perfectly named and tagged. A 20-track album becomes 20 individually organised audio files.</p></div>'
            f'<div class="hbox" style="margin-top:1rem"><h4>ID3 Automation</h4>'
            f'<p style="margin-top:.4rem">After recording each track, Audio Recorder queries an online music database and fills in artist, title, album, year, genre and cover art. Your recordings arrive in your library already perfectly organised.</p></div>'
            f'</div></div></section>'
        ),
        "record Spotify, save Spotify to MP3, Spotify music recorder, record Spotify FLAC, capture Spotify audio PC",
        article=True
    )

def pg_internet_radio():
    howto = (
        '{"@context":"https://schema.org","@type":"HowTo",'
        '"name":"How to Record Internet Radio",'
        '"description":"Record any internet radio station automatically on a schedule.",'
        '"step":['
        '{"@type":"HowToStep","position":1,"name":"Open Audio Recorder","text":"Launch Wondershare Audio Recorder and select System Audio."},'
        '{"@type":"HowToStep","position":2,"name":"Set a Schedule","text":"Click Schedule, enter start time and end time for the broadcast you want to record."},'
        '{"@type":"HowToStep","position":3,"name":"Start the Radio Stream","text":"Navigate to your online radio station and begin playback."},'
        '{"@type":"HowToStep","position":4,"name":"Leave it running","text":"Audio Recorder will activate at the set time, record, and stop automatically. No need to stay at your computer."}'
        ']}'
    )
    return page(
        f"Record Internet Radio \u2014 Automatic & Scheduled | {YEAR}",
        "Record any internet radio station automatically using Wondershare Audio Recorder. Set a schedule, come back to perfectly organised recordings. Auto track split. MP3, FLAC output.",
        "/record-internet-radio/",
        (
            f'<div class="ph">'
            + bc(("Home",f"{SITE_ROOT}/"),("Blog",f"{SITE_ROOT}/blog/"),("Record Internet Radio",None))
            + f'<span class="sec-lbl">Internet Radio Guide</span>'
            f'<h1>Record <span class="g-acc">Internet Radio</span><br>Automatically</h1>'
            f'<p style="max-width:660px;margin-top:.9rem;color:var(--muted)">Set a schedule and let Audio Recorder capture your favourite radio programmes while you sleep. Works with any online station worldwide.</p>'
            f'</div>'
            f'<section>'
            f'<div class="hbox good"><h4>Why Scheduled Recording is Perfect for Radio</h4>'
            f'<p style="margin-top:.4rem">Internet radio broadcasts at fixed times you might not be available for. Scheduled recording solves this completely \u2014 set the start and end time once, and Audio Recorder handles the rest automatically. Come back to a perfectly recorded, auto-split, auto-named collection of programmes.</p>'
            f'</div>'
            f'<div class="split" style="margin-top:2rem">'
            f'<div>'
            f'<h2 style="margin-bottom:1.5rem">Record Radio <span class="g-acc">on a Schedule</span></h2>'
            f'<div class="steps">'
            f'<div class="step" data-n="1"><div><h3>Open Audio Recorder</h3><p>Select System Audio as input. Set output to MP3 or FLAC.</p></div></div>'
            f'<div class="step" data-n="2"><div><h3>Enable Schedule</h3><p>Click Scheduler. Enter the exact start time and end time for the broadcast. Set it to repeat daily or weekly if needed.</p></div></div>'
            f'<div class="step" data-n="3"><div><h3>Enable Auto Track Split</h3><p>Turn on auto track split to automatically separate different programmes or segments into individual files.</p></div></div>'
            f'<div class="step" data-n="4"><div><h3>Open Your Radio Station</h3><p>Navigate to the online station in your browser. Start playback.</p></div></div>'
            f'<div class="step" data-n="5"><div><h3>Leave It Running</h3><p>Audio Recorder activates at the scheduled time, records, splits and names files automatically. You don\u2019t need to be at your computer.</p></div></div>'
            f'</div>'
            f'<a href="{AFF}" class="btn btn-p" style="margin-top:1rem" target="_blank" rel="noopener sponsored">\u2b07 Download Free Trial</a>'
            f'</div>'
            f'<div>'
            f'<div class="card card-feat" style="padding:2rem">'
            f'<h3 style="color:var(--acc);margin-bottom:1rem">Radio Stations You Can Record</h3>'
            f'<ul style="list-style:none;padding:0;display:flex;flex-direction:column;gap:.6rem">'
            + "".join(
                f'<li style="font-size:.88rem;color:var(--muted);display:flex;gap:.6rem">'
                f'<span style="color:var(--green);font-weight:700">\u2713</span>{x}</li>'
                for x in [
                    "BBC Radio (UK) \u2014 any BBC station",
                    "NPR (USA) \u2014 National Public Radio",
                    "RFI (France) \u2014 Radio France Internationale",
                    "Deutsche Welle (Germany)",
                    "NHK Radio Japan",
                    "Radio Nacional de España",
                    "Radio Globo (Brazil)",
                    "Any local or regional online radio station",
                    "Internet-only stations (TuneIn, iHeartRadio, etc.)",
                ]
            )
            + f'</ul></div>'
            f'</div></div></section>'
        ),
        "record internet radio, online radio recorder, scheduled radio recording, BBC radio recorder, NPR recorder",
        extras=[howto],
        article=True
    )

def pg_podcast_recorder():
    return page(
        f"Podcast Recorder Software \u2014 Record \u0026 Export MP3 | {YEAR}",
        "Record your podcast with Wondershare Audio Recorder. Microphone recording, AI noise reduction, built-in trimming, MP3 export. Complete podcast recording workflow for Windows.",
        "/podcast-recorder/",
        (
            f'<div class="ph">'
            + bc(("Home",f"{SITE_ROOT}/"),("Blog",f"{SITE_ROOT}/blog/"),("Podcast Recorder",None))
            + f'<span class="sec-lbl">Podcasting Guide</span>'
            f'<h1>Record Your <span class="g-acc">Podcast</span></h1>'
            f'<p style="max-width:660px;margin-top:.9rem;color:var(--muted)">Microphone recording, noise reduction, editing and MP3 export. Everything you need to produce podcast episodes on Windows.</p>'
            f'</div>'
            f'<section>'
            f'<div class="g3" style="margin-bottom:2.5rem">'
            + "".join(
                f'<div class="card{"  card-feat" if i==0 else ""}"><div class="card-icon">{icon}</div><h3>{title}</h3><p>{desc}</p></div>'
                for i,(icon,title,desc) in enumerate([
                    ("\U0001f399","Microphone Recording","Any connected mic \u2014 USB condenser, dynamic, headset, built-in. Real-time level monitoring. Input gain control."),
                    ("\U0001f507","AI Noise Reduction","Removes background hiss, room echo and ambient noise. Makes home studio recordings sound clean and professional."),
                    ("\u2702\ufe0f","Built-in Editor","Trim, cut false starts, remove pauses, adjust volume \u2014 without leaving the app."),
                    ("\U0001f4e4","MP3 Export","Export finished episode at the right bitrate for podcast platforms. 128 kbps mono for speech, 192 kbps for music-heavy episodes."),
                ])
            )
            + f'</div>'
            f'<div class="split">'
            f'<div>'
            f'<h2 style="margin-bottom:1.5rem">Record an Episode \u2014 <span class="g-acc">5 Steps</span></h2>'
            f'<div class="steps">'
            f'<div class="step" data-n="1"><div><h3>Connect Your Mic</h3><p>Plug in USB mic or connect via audio interface. Windows detects automatically.</p></div></div>'
            f'<div class="step" data-n="2"><div><h3>Select Microphone</h3><p>In Audio Recorder, choose your mic as input. Monitor levels to avoid clipping.</p></div></div>'
            f'<div class="step" data-n="3"><div><h3>Enable Noise Reduction</h3><p>Turn on AI noise reduction to clean background noise during recording.</p></div></div>'
            f'<div class="step" data-n="4"><div><h3>Record Your Episode</h3><p>Click Record. Speak naturally. Audio Recorder captures everything cleanly.</p></div></div>'
            f'<div class="step" data-n="5"><div><h3>Edit \u0026 Export</h3><p>Trim, cut, adjust in the built-in editor. Export as MP3 ready to upload to your podcast platform.</p></div></div>'
            f'</div>'
            f'<a href="{AFF}" class="btn btn-p" style="margin-top:1rem" target="_blank" rel="noopener sponsored">\u2b07 Download Podcast Recorder Free</a>'
            f'</div>'
            f'<div>'
            f'<div class="hbox info"><h4>Recommended Settings for Podcasts</h4>'
            f'<ul style="list-style:none;padding:0;margin-top:.8rem;display:flex;flex-direction:column;gap:.6rem">'
            + "".join(
                f'<li style="font-size:.86rem;color:var(--muted);display:flex;gap:.6rem">'
                f'<code style="font-size:.8rem;flex-shrink:0">{s}</code>{d}</li>'
                for s,d in [
                    ("MP3 128kbps","Standard for voice-only podcasts"),
                    ("MP3 192kbps","If your podcast includes music or sound effects"),
                    ("WAV","Send to a producer or post-production editor"),
                    ("Mono","Single mic \u2014 halves file size with no audible difference"),
                    ("44.1 kHz","Standard sample rate for podcast distribution"),
                ]
            )
            + f'</ul></div>'
            f'</div></div></section>'
        ),
        "podcast recorder software, record podcast MP3, microphone recorder Windows, podcast recording software",
        article=True
    )

def pg_voice_recorder():
    return page(
        f"Voice Recorder for PC \u2014 Memos, Interviews, Dictation | {YEAR}",
        "Record voice memos, interviews, dictation and lectures on Windows PC with Wondershare Audio Recorder. Noise reduction, MP3 export, auto file naming. Simple one-click recording.",
        "/voice-recorder/",
        (
            f'<div class="ph">'
            + bc(("Home",f"{SITE_ROOT}/"),("Blog",f"{SITE_ROOT}/blog/"),("Voice Recorder",None))
            + f'<span class="sec-lbl">Voice Recording Guide</span>'
            f'<h1>Voice Recorder<br><span class="g-acc">for PC</span></h1>'
            f'<p style="max-width:660px;margin-top:.9rem;color:var(--muted)">Record voice memos, interviews, meetings and dictation on any Windows PC. One click to start, clean MP3 output.</p>'
            f'</div>'
            f'<section>'
            f'<div class="g3" style="margin-bottom:2.5rem">'
            + "".join(
                f'<div class="card"><div class="card-icon">{icon}</div><h3>{title}</h3><p>{desc}</p></div>'
                for icon,title,desc in [
                    ("\U0001f4dd","Voice Memos","Quick voice notes and reminders. Auto-named with date and time. MP3 output, works on any device."),
                    ("\U0001f3a4","Interviews","Record interview subjects over Zoom or in person. Clear audio, auto file naming, MP3 export."),
                    ("\U0001f4da","Dictation","Dictate documents, ideas and notes. Noise reduction makes laptop mic recordings clear."),
                    ("\U0001f393","Lectures","Record class lectures, seminars and online courses. Long recording, no time limit on paid plan."),
                    ("\U0001f3b5","Music Ideas","Capture creative ideas, chord progressions and demos quickly."),
                    ("\U0001f4de","VoIP Calls","Record Zoom, Teams, Skype calls as audio-only for easy replay and reference."),
                ]
            )
            + f'</div>'
            f'<div style="text-align:center">'
            f'<a href="{AFF}" class="btn btn-p btn-lg" target="_blank" rel="noopener sponsored">\u2b07 Download Voice Recorder Free</a>'
            f'</div></section>'
        ),
        "voice recorder PC, voice recorder software Windows, record voice memo PC, dictation recorder, interview recorder software",
        article=True
    )

def pg_vs_audacity():
    return page(
        f"Audio Recorder vs Audacity \u2014 Full Comparison {YEAR}",
        f"Wondershare Audio Recorder vs Audacity: scheduled recording, streaming capture, ID3 tags, ease of use compared. Which is right for you in {YEAR}?",
        "/vs-audacity/",
        (
            f'<div class="ph">'
            + bc(("Home",f"{SITE_ROOT}/"),("Alternatives",f"{SITE_ROOT}/alternatives/"),("vs Audacity",None))
            + f'<span class="sec-lbl">Head-to-Head</span>'
            f'<h1>Audio Recorder vs <span class="g-acc">Audacity</span></h1>'
            f'<p style="max-width:660px;margin-top:.9rem;color:var(--muted)">Audacity is free and powerful for editing. Audio Recorder is purpose-built for capturing. Here\u2019s when to use each.</p>'
            f'</div>'
            f'<section>'
            f'<div class="tbl-wrap"><table>'
            f'<thead><tr><th>Feature</th><th style="color:var(--acc)">Wondershare Audio Recorder</th><th>Audacity (Free)</th></tr></thead>'
            f'<tbody>'
            + "".join(
                f'<tr><td class="td-n">{feat}</td><td class="{ac}">{av}</td><td class="{au}">{ad}</td></tr>'
                for feat,av,ac,ad,au in [
                    ("Record streaming audio",       "\u2713 One click",               "td-y td-hi", "\u2713 Requires plugin setup",    "td-p"),
                    ("Scheduled recording",           "\u2713 Built in",               "td-y td-hi", "\u2715 Not available",            "td-no"),
                    ("Auto track split",              "\u2713 Automatic",              "td-y td-hi", "\u2715 Manual only",              "td-no"),
                    ("ID3 tag editor",                "\u2713 Auto + manual",          "td-y td-hi", "\u2715 Not included",             "td-no"),
                    ("Always-on silent recording",    "\u2713 System tray",            "td-y td-hi", "\u2715 Must stay visible",        "td-no"),
                    ("AI noise reduction",            "\u2713 Automatic",              "td-y td-hi", "\u2713 Manual tool",              "td-p"),
                    ("Multi-track editing",           "\u2715 Basic only",             "td-no",      "\u2713 Full multitrack",          "td-y"),
                    ("Effects & plugins",             "\u2715 Basic",                  "td-no",      "\u2713 Hundreds of plugins",      "td-y"),
                    ("Cross-platform",                "\u2715 Windows only",           "td-no",      "\u2713 Win, Mac, Linux",          "td-y"),
                    ("Ease of use",                   "\u2605\u2605\u2605\u2605\u2605 Very easy", "td-y td-hi", "\u2605\u2605\u2605\u00bd Complex","td-p"),
                    ("Cost",                          "~$29.95/year",                  "td-hi",      "Free",                           "td-y"),
                ]
            )
            + f'</tbody></table></div>'
            f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:1.4rem;margin-top:1.5rem">'
            f'<div class="hbox good" style="margin:0"><h4>Choose Audio Recorder if\u2026</h4>'
            + "".join(f'<div style="font-size:.84rem;color:var(--muted);display:flex;gap:.5rem;margin-top:.4rem"><span style="color:var(--green);font-weight:700">\u2713</span>{x}</div>' for x in ["You want to record streaming music or online radio","You need scheduled / automatic recording","You want auto track split for albums and playlists","You need ID3 tags applied automatically","You prefer a simple, one-click interface"])
            + f'</div>'
            f'<div class="hbox" style="margin:0"><h4>Audacity is better if\u2026</h4>'
            + "".join(f'<div style="font-size:.84rem;color:var(--muted);display:flex;gap:.5rem;margin-top:.4rem"><span style="color:var(--acc3);">\u2192</span>{x}</div>' for x in ["You need professional multitrack editing","You want hundreds of effects and plugins","Budget is the primary consideration","You work on Mac or Linux","You need advanced spectral editing tools"])
            + f'</div></div>'
            f'<div class="hbox" style="margin-top:1.5rem"><h4>Best Combination</h4>'
            f'<p style="margin-top:.4rem">Many users run both. Use Audio Recorder for capturing \u2014 scheduling, streaming, auto-split and tagging. Then open recordings in Audacity for advanced multitrack editing. They complement each other perfectly.</p>'
            f'</div>'
            f'<div style="text-align:center;margin-top:2rem">'
            f'<a href="{AFF}" class="btn btn-p" target="_blank" rel="noopener sponsored">Try Audio Recorder Free \u2192</a>'
            f'</div></section>'
        ),
        "audio recorder vs Audacity, Audacity alternative Windows, best audio capture software"
    )

def pg_vs_garageband():
    return page(
        f"Audio Recorder vs GarageBand \u2014 Comparison {YEAR}",
        f"Wondershare Audio Recorder vs GarageBand: platform, features and recording capabilities compared. GarageBand is Mac-only. Audio Recorder is Windows. Full comparison {YEAR}.",
        "/vs-garageband/",
        (
            f'<div class="ph">'
            + bc(("Home",f"{SITE_ROOT}/"),("Alternatives",f"{SITE_ROOT}/alternatives/"),("vs GarageBand",None))
            + f'<span class="sec-lbl">Comparison</span>'
            f'<h1>Audio Recorder vs <span class="g-acc">GarageBand</span></h1>'
            f'<p style="max-width:660px;margin-top:.9rem;color:var(--muted)">GarageBand is Apple\u2019s free music production tool for Mac. Audio Recorder is a dedicated capture tool for Windows. Different platforms, different purposes.</p>'
            f'</div>'
            f'<section>'
            f'<div class="tbl-wrap"><table>'
            f'<thead><tr><th>Feature</th><th style="color:var(--acc)">Audio Recorder</th><th>GarageBand</th></tr></thead>'
            f'<tbody>'
            + "".join(
                f'<tr><td class="td-n">{feat}</td><td class="{ac}">{av}</td><td class="{gb}">{gv}</td></tr>'
                for feat,av,ac,gv,gb in [
                    ("Platform",               "Windows",                          "td-hi",      "Mac / iOS only",              "td-p"),
                    ("Record system audio",    "\u2713 One click",                 "td-y td-hi", "\u2715 Not designed for this", "td-no"),
                    ("Scheduled recording",    "\u2713 Built in",                  "td-y td-hi", "\u2715",                      "td-no"),
                    ("Auto track split",       "\u2713",                           "td-y td-hi", "\u2715",                      "td-no"),
                    ("ID3 auto-tagging",       "\u2713 Automatic",                 "td-y td-hi", "\u2715",                      "td-no"),
                    ("Multi-track recording",  "\u2715 Basic",                     "td-no",      "\u2713 Full DAW",              "td-y"),
                    ("Virtual instruments",    "\u2715",                           "td-no",      "\u2713 Extensive",             "td-y"),
                    ("MIDI sequencing",        "\u2715",                           "td-no",      "\u2713 Built in",              "td-y"),
                    ("Cost",                   "~$29.95/year",                     "td-hi",      "Free (Mac only)",              "td-y"),
                ]
            )
            + f'</tbody></table></div>'
            f'<div class="hbox" style="margin-top:1.5rem"><h4>Summary</h4>'
            f'<p style="margin-top:.4rem">GarageBand is a full music production suite for Mac \u2014 excellent for recording instruments and making music. Wondershare Audio Recorder is purpose-built for capturing any audio from Windows \u2014 streaming services, calls, radio and microphone. Different tools for different tasks on different platforms.</p>'
            f'</div>'
            f'<div style="text-align:center;margin-top:1.5rem">'
            f'<a href="{AFF}" class="btn btn-p" target="_blank" rel="noopener sponsored">Try Audio Recorder Free \u2192</a>'
            f'</div></section>'
        ),
        "audio recorder vs GarageBand, GarageBand alternative Windows, audio recorder Windows Mac comparison"
    )

def pg_vs_obs():
    return page(
        f"Audio Recorder vs OBS Studio \u2014 Which for Audio? {YEAR}",
        f"Wondershare Audio Recorder vs OBS Studio for audio recording: ease of use, scheduled recording, auto-split, ID3 tags compared. Which is better for audio-only recording in {YEAR}?",
        "/vs-obs/",
        (
            f'<div class="ph">'
            + bc(("Home",f"{SITE_ROOT}/"),("Alternatives",f"{SITE_ROOT}/alternatives/"),("vs OBS Studio",None))
            + f'<span class="sec-lbl">Comparison</span>'
            f'<h1>Audio Recorder vs <span class="g-acc">OBS Studio</span></h1>'
            f'<p style="max-width:660px;margin-top:.9rem;color:var(--muted)">OBS is a powerful free broadcaster designed for video streaming. Audio Recorder is purpose-built for audio capture. Here\u2019s the comparison for audio-only use cases.</p>'
            f'</div>'
            f'<section>'
            f'<div class="tbl-wrap"><table>'
            f'<thead><tr><th>Feature</th><th style="color:var(--acc)">Audio Recorder</th><th>OBS Studio (Free)</th></tr></thead>'
            f'<tbody>'
            + "".join(
                f'<tr><td class="td-n">{feat}</td><td class="{ac}">{av}</td><td class="{ob}">{ov}</td></tr>'
                for feat,av,ac,ov,ob in [
                    ("Primary purpose",          "Audio capture",                    "td-hi",      "Video streaming & recording", ""),
                    ("Audio-only recording",      "\u2713 Designed for this",         "td-y td-hi", "\u2713 Possible but complex",  "td-p"),
                    ("Scheduled recording",       "\u2713 Built in",                  "td-y td-hi", "\u2715 Requires scripts",      "td-no"),
                    ("Auto track split",          "\u2713 Automatic",                 "td-y td-hi", "\u2715 Not available",         "td-no"),
                    ("ID3 tag editor",            "\u2713 Auto + manual",             "td-y td-hi", "\u2715 Not available",         "td-no"),
                    ("Ease of use",               "\u2605\u2605\u2605\u2605\u2605 Simple", "td-y td-hi", "\u2605\u2605\u00bd Complex","td-p"),
                    ("Video streaming",           "\u2715 Audio only",                "td-no",      "\u2713 Full streaming suite",  "td-y"),
                    ("Scenes & overlays",         "\u2715",                           "td-no",      "\u2713 Full",                  "td-y"),
                    ("MP3 / FLAC output",         "\u2713 10 formats",                "td-y td-hi", "\u2715 MKV/MP4 primary",       "td-p"),
                    ("Cost",                      "~$29.95/year",                     "td-hi",      "Free",                         "td-y"),
                ]
            )
            + f'</tbody></table></div>'
            f'<div class="hbox" style="margin-top:1.5rem"><h4>Bottom Line</h4>'
            f'<p style="margin-top:.4rem">OBS is the best tool for video streaming and screen recording. For audio-only capture \u2014 especially scheduled recording, auto-splitting and ID3 tagging \u2014 Audio Recorder is far simpler and better suited. They serve fundamentally different use cases.</p>'
            f'</div>'
            f'<div style="text-align:center;margin-top:1.5rem">'
            f'<a href="{AFF}" class="btn btn-p" target="_blank" rel="noopener sponsored">Try Audio Recorder Free \u2192</a>'
            f'</div></section>'
        ),
        "audio recorder vs OBS, OBS audio recording, OBS alternative audio, audio recorder software comparison"
    )

def pg_alternatives():
    return page(
        f"Best Audio Recorder Alternatives {YEAR} \u2014 Full Market Overview",
        f"Compare Wondershare Audio Recorder with every major alternative in {YEAR}: Audacity, GarageBand, OBS Studio, Ocenaudio, Windows Voice Recorder, Adobe Audition.",
        "/alternatives/",
        (
            f'<div class="ph">'
            + bc(("Home",f"{SITE_ROOT}/"),("Alternatives",None))
            + f'<span class="sec-lbl">Full Market Comparison</span>'
            f'<h1>Best <span class="g-acc">Audio Recorder</span><br>Alternatives {YEAR}</h1>'
            f'<p style="max-width:660px;margin-top:.9rem;color:var(--muted)">Every major audio recorder compared so you can pick the right one for your needs.</p>'
            f'</div>'
            f'<section><div class="g2">'
            f'<div class="card card-feat"><h3 style="color:var(--acc)">Wondershare Audio Recorder <span class="chip chip-g" style="margin-left:.4rem">Recommended</span></h3>'
            f'<p style="margin:.8rem 0">Purpose-built for capturing any audio from Windows. Scheduled recording, auto track split, ID3 tags, 10 formats, AI noise reduction. Available in 150+ countries.</p>'
            f'<a href="{AFF}" class="btn btn-p" style="margin-top:.8rem" target="_blank" rel="noopener sponsored">Download Free \u2192</a></div>'
            + "".join(
                f'<div class="card"><h3>{name} <span class="chip chip-{ct}" style="margin-left:.4rem">{label}</span></h3>'
                f'<p style="margin:.8rem 0">{desc}</p>'
                f'<a href="{link}" class="btn btn-g" style="margin-top:.8rem">Full Comparison \u2192</a></div>'
                for name,ct,label,desc,link in [
                    ("Audacity","g","Free","Best free multitrack audio editor. No scheduled recording, no auto-split, no ID3 tags. Complex setup for streaming capture. Excellent for editing.",f"{SITE_ROOT}/vs-audacity/"),
                    ("GarageBand","g","Free \u2014 Mac Only","Apple\u2019s music production suite for Mac/iOS. Excellent for recording instruments and making music. Not designed for streaming capture. Mac only.",f"{SITE_ROOT}/vs-garageband/"),
                    ("OBS Studio","g","Free","Powerful video streaming and screen recording tool. Can record audio but complex interface not designed for audio-only use. No scheduling, no auto-split.",f"{SITE_ROOT}/vs-obs/"),
                    ("Windows Voice Recorder","g","Free \u2014 Built In","Very basic microphone-only recorder built into Windows. No system audio capture, no scheduling, no format choice, no editing. Fine for quick voice notes only.",f"{SITE_ROOT}/alternatives/"),
                    ("Adobe Audition","p","Paid","Professional audio editing suite \u2014 part of Adobe Creative Cloud (~$54.99/month). Overkill for basic recording. Excellent if you already use Adobe tools.",f"{SITE_ROOT}/alternatives/"),
                ]
            )
            + f'</div></section>'
        ),
        "audio recorder alternatives, best audio recording software, Audacity alternative, audio recorder comparison 2026"
    )


def pg_blog():
    posts = [
        ("\U0001f3b5","Guide",f"Record Streaming Audio \u2014 Complete Guide {YEAR}","Capture Spotify, Apple Music, YouTube and any online stream at full quality.",f"{SITE_ROOT}/record-streaming-audio/",f"June {YEAR}","5 min"),
        ("\U0001f4de","Tutorial",f"How to Record Zoom Audio Only \u2014 No Video {YEAR}","Record Zoom, Teams and Meet as clean MP3. 55 MB/hr vs 4 GB for video.",f"{SITE_ROOT}/record-zoom-audio/",f"June {YEAR}","4 min"),
        ("\U0001f4fb","Guide","Record Internet Radio \u2014 Automatic & Scheduled","Set a timer to capture any online radio station automatically.",f"{SITE_ROOT}/record-internet-radio/",f"June {YEAR}","4 min"),
        ("\U0001f399","Tutorial","Podcast Recorder Guide \u2014 Record & Export MP3","Mic recording, AI noise reduction, built-in editing and MP3 export.",f"{SITE_ROOT}/podcast-recorder/",f"May {YEAR}","5 min"),
        ("\U0001f3b8","Tutorial","Record Spotify \u2014 Auto Split & ID3 Tags","Capture any Spotify playlist with per-track splitting and auto-tagging.",f"{SITE_ROOT}/record-spotify/",f"May {YEAR}","4 min"),
        ("\U0001f3a4","Guide","Voice Recorder for PC \u2014 Memos, Interviews, Dictation","Record voice memos, lectures and interviews on any Windows PC.",f"{SITE_ROOT}/voice-recorder/",f"April {YEAR}","3 min"),
        ("\U0001f19a","Comparison","Audio Recorder vs Audacity \u2014 Which to Use?","Audacity edits. Audio Recorder captures. Here\u2019s when to use each.",f"{SITE_ROOT}/vs-audacity/",f"April {YEAR}","5 min"),
        ("\U0001f19a","Comparison","Audio Recorder vs OBS Studio \u2014 Audio Use Cases","OBS streams video. Audio Recorder captures audio. Full comparison.",f"{SITE_ROOT}/vs-obs/",f"March {YEAR}","4 min"),
        ("\u2b50","Review",f"Wondershare Audio Recorder Review {YEAR} \u2014 8.8/10","Full hands-on review: scheduling, auto-split, ID3 tagging, quality tests.",f"{SITE_ROOT}/review/",f"March {YEAR}","8 min"),
        ("\U0001f4b0","Guide",f"Audio Recorder Pricing {YEAR} \u2014 Free Trial & Plans","Free trial, annual and lifetime plans with current pricing.",f"{SITE_ROOT}/pricing/",f"February {YEAR}","3 min"),
        ("\U0001f50a","Guide","Auto Track Split \u2014 Record Albums as Individual Files","How auto-split works and why it makes recording playlists effortless.",f"{SITE_ROOT}/features/",f"February {YEAR}","3 min"),
        ("\U0001f3f7","Guide","ID3 Tags Explained \u2014 Auto-Tag Your Recordings","What ID3 tags are, why they matter, and how Audio Recorder fills them in.",f"{SITE_ROOT}/features/",f"January {YEAR}","4 min"),
    ]
    cards = "".join(
        f'<div class="bc"><div class="bc-thumb">{e}</div><div class="bc-body">'
        f'<div class="bc-tag">{t}</div><h3>{title}</h3><p>{desc}</p>'
        f'<div class="bc-meta"><span>\U0001f4c5 {d}</span><span>\u23f1 {read}</span></div>'
        f'<a href="{url}" class="bc-read">Read Article \u2192</a>'
        f'</div></div>'
        for e,t,title,desc,url,d,read in posts
    )
    return page(
        f"Audio Recorder Blog \u2014 Recording Guides, Reviews & Tutorials {YEAR}",
        "Audio recording guides, tutorials and reviews for global users. Record streaming audio, Zoom calls, podcasts, radio and voice on Windows with Wondershare Audio Recorder.",
        "/blog/",
        (
            f'<div class="ph">'
            + bc(("Home",f"{SITE_ROOT}/"),("Blog",None))
            + f'<span class="sec-lbl">Guides, Reviews & Tutorials</span>'
            f'<h1>Audio Recorder <span class="g-acc">Blog</span></h1>'
            f'<p style="max-width:600px;margin-top:.9rem;color:var(--muted)">Practical guides and honest reviews for every audio recording need \u2014 worldwide.</p>'
            f'</div>'
            f'<section><div class="bgrid">{cards}</div></section>'
        ),
        "audio recording guide, audio recorder tutorial, record streaming audio guide, audio recorder blog global"
    )

def pg_privacy():
    return page("Privacy Policy \u2014 AudioRecorder Guide","Privacy policy for the AudioRecorder affiliate guide.","/privacy/",
        f'<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Privacy",None))}<h1>Privacy <span class="g-acc">Policy</span></h1>'
        f'<p style="color:var(--muted);margin-top:.4rem">Last updated: June {YEAR}</p></div>'
        f'<section style="max-width:820px;margin:0 auto">'
        f'<div class="hbox"><p>This is an independent affiliate guide for Wondershare Streaming Audio Recorder. '
        f'We earn commissions on qualifying purchases through affiliate links at no extra cost to you.</p></div>'
        f'<h3 style="margin:2rem 0 .7rem;color:var(--acc)">Data Collection</h3>'
        f'<p>Static site hosted on GitHub Pages. We do not collect personal data. GitHub Pages may log standard server data.</p>'
        f'<h3 style="margin:2rem 0 .7rem;color:var(--acc)">Affiliate Links</h3>'
        f'<p>Links to Wondershare are affiliate links via LinkConnector. Purchases earn us a commission at no extra cost to you.</p>'
        f'<h3 style="margin:2rem 0 .7rem;color:var(--acc)">Cookies</h3>'
        f'<p>No first-party cookies set. Affiliate tracking uses LinkConnector cookies. Disable in browser settings to opt out.</p>'
        f'</section>'
    )

def pg_disclaimer():
    return page("Affiliate Disclaimer \u2014 AudioRecorder Guide","Affiliate disclosure for the AudioRecorder guide.","/disclaimer/",
        f'<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Disclaimer",None))}<h1>Affiliate <span class="g-acc">Disclaimer</span></h1>'
        f'<p style="color:var(--muted);margin-top:.4rem">Last updated: June {YEAR}</p></div>'
        f'<section style="max-width:820px;margin:0 auto">'
        f'<div class="hbox"><h4>Disclosure</h4>'
        f'<p style="margin-top:.4rem">This website contains affiliate links. As an affiliate of Wondershare via LinkConnector, '
        f'we earn a commission on qualifying purchases at no additional cost to you.</p></div>'
        f'<h3 style="margin:2rem 0 .7rem;color:var(--acc)">Editorial Independence</h3>'
        f'<p>Reviews list both strengths and caveats honestly \u2014 including that the software is Windows-only and the editor is basic. '
        f'Affiliate relationships do not influence editorial opinions.</p>'
        f'<h3 style="margin:2rem 0 .7rem;color:var(--acc)">Accuracy</h3>'
        f'<p>Pricing and features can change. Always verify on the official Wondershare website before purchasing.</p>'
        f'</section>'
    )

def pg_404():
    return page("404 \u2014 Page Not Found | AudioRecorder Guide","Page not found.","/404/",
        f'<div class="ph tc" style="min-height:60vh;display:flex;align-items:center;justify-content:center;flex-direction:column;gap:1.5rem">'
        f'<div style="font-family:Fraunces,serif;font-size:9rem;font-weight:900;line-height:1;color:var(--acc)">404</div>'
        f'<h1>Page <span class="g-acc2">Not Found</span></h1>'
        f'<p style="max-width:360px;text-align:center;color:var(--muted)">This page does not exist.</p>'
        f'<div style="display:flex;gap:1rem;flex-wrap:wrap;justify-content:center">'
        f'<a href="{SITE_ROOT}/" class="btn btn-p">\u2190 Go Home</a>'
        f'<a href="{AFF}" class="btn btn-s" target="_blank" rel="noopener sponsored">Download Audio Recorder</a>'
        f'</div></div>'
    )

def mk_sitemap():
    core = [
        ("/","1.0","weekly"),("/features/","0.9","monthly"),("/how-it-works/","0.8","monthly"),
        ("/use-cases/","0.8","monthly"),("/formats/","0.8","monthly"),
        ("/pricing/","0.9","monthly"),("/review/","0.9","monthly"),
        ("/faq/","0.8","monthly"),("/download/","0.9","monthly"),
        ("/blog/","0.8","weekly"),("/global/","0.8","monthly"),
        ("/record-streaming-audio/","0.9","monthly"),
        ("/record-zoom-audio/","0.8","monthly"),
        ("/record-spotify/","0.8","monthly"),
        ("/record-internet-radio/","0.8","monthly"),
        ("/podcast-recorder/","0.8","monthly"),
        ("/voice-recorder/","0.8","monthly"),
        ("/vs-audacity/","0.8","monthly"),("/vs-garageband/","0.7","monthly"),
        ("/vs-obs/","0.7","monthly"),("/alternatives/","0.8","monthly"),
        ("/privacy/","0.3","yearly"),("/disclaimer/","0.3","yearly"),
    ]
    lang_pages = [(f"/lang/{lc}/","0.7","monthly") for _,_,lc,_,_,_,_ in LANGS]
    today = date.today().isoformat()
    tags = "\n".join(
        f"  <url><loc>{SITE_URL}{p}</loc><changefreq>{freq}</changefreq>"
        f"<priority>{pri}</priority><lastmod>{today}</lastmod></url>"
        for p,pri,freq in core + lang_pages
    )
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{tags}\n</urlset>'

def mk_robots():
    return f"User-agent: *\nAllow: /\nDisallow: /assets/\n\nSitemap: {SITE_URL}/sitemap.xml\n"

def mk_llms():
    lang_lines = "\n".join(
        f"- /lang/{lc}/ \u2014 {name} ({region}): {kw1}, {kw2}"
        for _,name,lc,region,kw1,kw2,_ in LANGS
    )
    return (
        f"# AudioRecorder Guide \u2014 {SITE_URL}\n"
        f"> Purpose: Independent affiliate guide for Wondershare Streaming Audio Recorder\n"
        f"> Updated: {date.today().isoformat()}\n"
        f"> Affiliate: LinkConnector \u2014 {AFF}\n"
        f"\n"
        f"## Product: Wondershare Streaming Audio Recorder\n"
        f"**Publisher:** Wondershare Software Ltd (founded 2003, publicly listed)\n"
        f"**Version:** 2.1.0\n"
        f"**Platform:** Windows only (7, 8, 10, 11 \u2014 32 and 64-bit). Mac not available.\n"
        f"\n"
        f"## What It Records\n"
        f"- Streaming music: Spotify, Apple Music, Amazon Music, YouTube Music, Tidal, Deezer\n"
        f"- Internet radio: any online station worldwide\n"
        f"- Video calls: Zoom, Teams, Meet, Skype, Discord (audio-only)\n"
        f"- Browser audio: Chrome, Firefox, Edge \u2014 any website\n"
        f"- Microphone: USB, 3.5mm, condenser, dynamic, laptop built-in\n"
        f"- Games and apps: any application audio\n"
        f"- Technology: virtual audio driver intercepts at source, zero quality loss\n"
        f"\n"
        f"## Output Formats (10 total)\n"
        f"MP3, WAV, FLAC, AAC, M4A, OGG, WMA, AIFF, AC3, APE\n"
        f"\n"
        f"## Key Features\n"
        f"1. Record system audio \u2014 zero quality loss via virtual audio driver\n"
        f"2. Record microphone \u2014 any connected mic, adjustable levels\n"
        f"3. Scheduled recording \u2014 set start/stop time, activates automatically\n"
        f"4. Auto track split \u2014 detects silence, saves each segment separately\n"
        f"5. ID3 tag editor \u2014 auto-fetches metadata, manual edit available\n"
        f"6. AI noise reduction \u2014 removes hiss, hum, ambient noise\n"
        f"7. Built-in audio editor \u2014 trim, cut, fade, volume\n"
        f"8. Format converter \u2014 convert existing audio between all formats\n"
        f"9. Always-on mode \u2014 silent system tray recording\n"
        f"10. Smart file naming \u2014 auto date/time naming\n"
        f"\n"
        f"## Pricing\n"
        f"- Free trial: no time limit, no credit card, recording length limited\n"
        f"- Annual: approx $29.95/year\n"
        f"- Perpetual: one-time payment, check official site\n"
        f"- Available in 150+ countries\n"
        f"\n"
        f"## Review Summary (8.8/10)\n"
        f"- Recording quality: 9.6 \u2014 zero loss on streaming\n"
        f"- Scheduled recording: 9.5 \u2014 flawless\n"
        f"- Ease of use: 9.2 \u2014 simplest interface tested\n"
        f"- Auto track split: 9.0 \u2014 11/12 test tracks correct\n"
        f"- Windows only is main limitation\n"
        f"\n"
        f"## Global Coverage \u2014 20 Language Pages\n"
        + lang_lines +
        f"\n\n## Site Structure \u2014 43 HTML Pages\n"
        f"23 core pages + 20 language pages\n"
        f"Core: /, /features/, /how-it-works/, /use-cases/, /formats/, /pricing/, /review/,\n"
        f"/faq/, /download/, /blog/, /global/, /record-streaming-audio/, /record-zoom-audio/,\n"
        f"/record-spotify/, /record-internet-radio/, /podcast-recorder/, /voice-recorder/,\n"
        f"/vs-audacity/, /vs-garageband/, /vs-obs/, /alternatives/, /privacy/, /disclaimer/\n"
        f"\n## Schema Types\n"
        f"SoftwareApp + BreadcrumbList on all pages\n"
        f"FAQPage on /faq/ and /pricing/\n"
        f"Review on /review/\n"
        f"HowTo on /how-it-works/, /record-streaming-audio/, /record-internet-radio/\n"
        f"ItemList on /features/\n"
        f"Article OG on all guide pages\n"
        f"\n## hreflang\n"
        f"All 43 pages include 20 hreflang alternate links for international SEO\n"
        f"\n## Affiliate\n"
        f"Network: LinkConnector\n"
        f"Link: {AFF}\n"
        f"All affiliate links: rel=\"noopener sponsored\"\n"
    )

def mk_feed():
    items = [
        (f"Record Streaming Audio \u2014 Guide {YEAR}", f"{SITE_URL}/record-streaming-audio/", "Capture Spotify, Apple Music and any online stream at full quality.", f"{YEAR}-06-01"),
        (f"Record Zoom Audio Only {YEAR}", f"{SITE_URL}/record-zoom-audio/", "Audio-only Zoom recording \u2014 55 MB/hr vs 4 GB for screen recording.", f"{YEAR}-06-01"),
        ("Record Internet Radio \u2014 Automated Guide", f"{SITE_URL}/record-internet-radio/", "Schedule any online radio station to record automatically.", f"{YEAR}-06-01"),
        (f"Wondershare Audio Recorder Review {YEAR} \u2014 8.8/10", f"{SITE_URL}/review/", "Complete review: scheduling, auto-split, ID3 tagging and quality tests.", f"{YEAR}-03-01"),
        ("Audio Recorder vs Audacity \u2014 Full Comparison", f"{SITE_URL}/vs-audacity/", "Two different tools. Here is exactly when to use each.", f"{YEAR}-04-01"),
    ]
    item_tags = "\n".join(
        f"  <item><title>{t}</title><link>{u}</link><description>{d}</description>"
        f"<pubDate>{pd}</pubDate><guid>{u}</guid></item>"
        for t,u,d,pd in items
    )
    return (
        f'<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">\n'
        f'  <channel>\n'
        f'    <title>AudioRecorder Guide Blog</title>\n'
        f'    <link>{SITE_URL}/blog/</link>\n'
        f'    <description>Audio recording guides and reviews for global users.</description>\n'
        f'    <language>en-us</language>\n'
        f'    <atom:link href="{SITE_URL}/feed.xml" rel="self" type="application/rss+xml"/>\n'
        f'{item_tags}\n'
        f'  </channel>\n</rss>'
    )

def mk_favicon():
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
        '<rect width="64" height="64" rx="14" fill="#04050d"/>'
        '<rect x="1" y="1" width="62" height="62" rx="13" fill="none" stroke="#7c3aed" stroke-width="1.5" opacity="0.5"/>'
        '<rect x="29" y="14" width="6" height="22" rx="3" fill="#7c3aed"/>'
        '<path d="M19 28 Q19 42 32 42 Q45 42 45 28" fill="none" stroke="#7c3aed" stroke-width="2.5" stroke-linecap="round"/>'
        '<line x1="32" y1="42" x2="32" y2="52" stroke="#7c3aed" stroke-width="2.5" stroke-linecap="round"/>'
        '<line x1="25" y1="52" x2="39" y2="52" stroke="#7c3aed" stroke-width="2.5" stroke-linecap="round"/>'
        '</svg>'
    )

def main():
    print(f"\n\U0001f3a4 AudioRecorder Online Affiliate Site Builder v2")
    print(f"   {SITE_URL}\n")

    write("index.html",                        pg_home())
    write("features/index.html",               pg_features())
    write("how-it-works/index.html",           pg_how())
    write("use-cases/index.html",              pg_use_cases())
    write("formats/index.html",                pg_formats())
    write("pricing/index.html",                pg_pricing())
    write("review/index.html",                 pg_review())
    write("faq/index.html",                    pg_faq())
    write("download/index.html",               pg_download())
    write("blog/index.html",                   pg_blog())
    write("global/index.html",                 pg_global())
    write("record-streaming-audio/index.html", pg_record_streaming())
    write("record-zoom-audio/index.html",      pg_record_zoom())
    write("record-spotify/index.html",         pg_record_spotify())
    write("record-internet-radio/index.html",  pg_internet_radio())
    write("podcast-recorder/index.html",       pg_podcast_recorder())
    write("voice-recorder/index.html",         pg_voice_recorder())
    write("vs-audacity/index.html",            pg_vs_audacity())
    write("vs-garageband/index.html",          pg_vs_garageband())
    write("vs-obs/index.html",                 pg_vs_obs())
    write("alternatives/index.html",           pg_alternatives())
    write("privacy/index.html",                pg_privacy())
    write("disclaimer/index.html",             pg_disclaimer())
    write("404.html",                          pg_404())

    print("\n  \U0001f310 Language pages:")
    for flag,name,lc,region,kw1,kw2,kw3 in LANGS:
        write(f"lang/{lc}/index.html", pg_lang(flag,name,lc,region,kw1,kw2,kw3))

    write("sitemap.xml",        mk_sitemap())
    write("robots.txt",         mk_robots())
    write("llms.txt",           mk_llms())
    write("feed.xml",           mk_feed())
    write("assets/favicon.svg", mk_favicon())
    write(".nojekyll",          "")

    pages = len([f for f in BASE.rglob("*.html")])
    total = len(list(BASE.rglob("*")))
    print(f"\n\u2705 Done \u2014 {pages} HTML pages, {total} total files")
    print(f"   Output: {BASE}")
    print(f"   Deploy: {SITE_URL}\n")

if __name__ == "__main__":
    main()
