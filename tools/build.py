#!/usr/bin/env python3
"""Builds index.html from the content below. Run from the repo root: python3 tools/build.py"""
import os
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "img")
EMAIL = "cmarais.work@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/charl-marais-184646199"


def pic(name, alt, pos=None, eager=False, ext="jpg"):
    """A responsive picture: small copy on phones, explicit width/height to avoid layout shift."""
    with Image.open(os.path.join(IMG, f"{name}.{ext}")) as im:
        w, h = im.size
    small = os.path.exists(os.path.join(IMG, f"{name}-s.{ext}"))
    src = f'<source media="(max-width:760px)" srcset="img/{name}-s.{ext}">' if small else ""
    style = f' style="object-position:{pos}"' if pos else ""
    load = ' loading="eager" fetchpriority="high"' if eager else ' loading="lazy"'
    return (f'<picture>{src}<img src="img/{name}.{ext}" alt="{alt}" width="{w}" height="{h}"'
            f'{style}{load} decoding="async"></picture>')


def photo(name, alt, cap=None, cls="", pos=None, eager=False, glass=False):
    c = ("photo " + ("glass " if glass else "") + cls).strip()
    figcap = f'<figcaption class="cap">{cap}</figcaption>' if cap else ""
    return f'<figure class="{c}">{pic(name, alt, pos, eager)}{figcap}</figure>'


def stats(items):
    return '<dl class="rep-s">' + "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for v, k in items) + "</dl>"


def figure(name, alt, cap):
    return f'<figure>{pic(name, alt)}<figcaption>{cap}</figcaption></figure>'


def rep(rid, code, topic, name, summary, body):
    return f'''
    <article class="glass rep rv">
      <h3 class="sr-only">{code}: {topic}, {name}</h3>
      <button class="rep-h" type="button" id="{rid}-h" aria-expanded="false" aria-controls="{rid}-b">
        <span class="k" translate="no">{code}</span>
        <span class="rep-t"><span class="tp">{topic}</span><i class="ar" aria-hidden="true">→</i><b>{name}</b></span>
        <span class="pl" aria-hidden="true"></span>
      </button>
      <div class="rep-b" id="{rid}-b" role="region" aria-labelledby="{rid}-h"><div class="rep-bi">
        <p>{summary}</p>{body}
      </div></div>
    </article>'''


HEAD = f'''<!doctype html>
<html lang="en">
<head>
<script>(function(){{var d=document.documentElement,m=matchMedia,q=location.search,n=navigator,c=n.connection||{{}},ua=n.userAgent||"";
var lite=/[?&]lite/.test(q)||(!/[?&]full/.test(q)&&(m("(max-width:820px)").matches||m("(hover:none)").matches||(n.deviceMemory&&n.deviceMemory<=2)||c.saveData));
d.className+=(lite?" lite":" full")+(/Android/i.test(ua)?" android":(/iPhone|iPad|iPod/i.test(ua)||(n.platform==="MacIntel"&&n.maxTouchPoints>1))?" ios":"");}})();</script>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Charl Marais Portfolio</title>
<meta name="description" content="Portfolio of Charl Marais, electrical engineering student at the University of Pretoria: PCB design, analogue electronics, embedded firmware and control systems.">
<meta name="theme-color" content="#0d0e10">
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=Instrument+Sans:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="css/site.css">
</head>
<body>
'''

NAV = '''
<a class="skip" href="#main">Skip to Content</a>
<div id="intro" aria-hidden="true"><div class="intro-in"><div class="intro-n" translate="no"><span>Charl</span><span>Marais<b>.</b></span></div><div class="intro-s">Electrical Engineering · University of Pretoria</div><div class="intro-l"><i></i></div></div></div>
<div class="orbs" aria-hidden="true"><div class="orb o1"></div><div class="orb o2"></div><div class="orb o3"></div></div>

<header class="site-nav">
  <nav class="nav-in" aria-label="Primary">
    <a class="logo" href="#top" translate="no">Charl Marais<b>.</b></a>
    <div class="links">
      <a href="#about">About</a><a href="#projects">Projects</a><a href="#education">Education</a><a href="#school">School</a><a href="#practicals">Practicals</a><a href="#olifante">Olifante</a><a href="#karate">Karate</a><a href="#contact">Contact</a>
    </div>
  </nav>
</header>
'''

HERO = f'''
<main id="main">
<div class="wrap">
<section class="hero" id="top" aria-label="Introduction">
  <div class="bento">
    <div class="tile glass t-name">
      <p class="eyebrow">Portfolio · Pretoria, South Africa</p>
      <h1 translate="no"><span><i>Charl-<br>Francois</i></span><span><i>Marais</i></span></h1>
      <p class="role">3rd Year Electrical Engineering<br>University of Pretoria</p>
    </div>
    {photo("hero-portrait", "Portrait of Charl Marais in a dark suit", "Charl Marais", "tile glass t-photo", "50% 20%", eager=True)}
    <div class="tile glass t-about">
      <h2 class="tile-h">Profile</h2>
      <p>Electrical engineering student working on analogue electronics, PCB design and embedded firmware, with 3D-printed enclosures for the hardware.</p>
      <p>Interests: control systems, power generation and distribution, robotics and automation.</p>
      <div class="tags"><span class="tag hot">KiCad</span><span class="tag">STM32</span><span class="tag">C++</span><span class="tag">Python</span><span class="tag">MATLAB</span></div>
    </div>
    <div class="tile t-red"><p>Under contract until 2030</p></div>
    <div class="tile glass t-now"><p>Engineer in Training at Cape Gate, <em>Dec&nbsp;2025 – present</em></p></div>
    <div class="tile glass t-n"><b>80.0%</b><span>cumulative GPA, B.Eng</span></div>
    <div class="tile glass t-n"><b>2×</b><span>Dean’s Merit List</span></div>
    <div class="tile glass t-n"><b>84.42%</b><span>NSC final aggregate</span></div>
    <div class="tile glass t-n"><b>2015</b><span>karate since Aug&nbsp;2015</span></div>
    <div class="tile glass t-cta"><p>Contact for work or collaboration</p>
      <div class="cta"><a class="btn primary" href="#projects">See My Work</a><a class="btn" href="#contact">Get in Touch</a><a class="btn" href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn <span aria-hidden="true">↗</span><span class="sr-only">(opens in a new tab)</span></a></div></div>
  </div>
</section>
</div>
'''

ABOUT = f'''
<div class="wrap">
<section id="about" aria-labelledby="about-h">
  <div class="about">
    <div class="rv">
      <p class="eyebrow">About</p>
      <h2 id="about-h">Background<span class="d">&amp; Experience</span></h2>
      <p class="dim">I started the B.Eng in February&nbsp;2024 and work as an Engineer in Training at Cape Gate alongside my studies. I also tutor maths and physics, and was a teaching assistant in the University of Pretoria’s Department of Mathematics and Applied Mathematics from March to June&nbsp;2026.</p>
      <p class="dim">Tools: C++, Python, MATLAB, LTspice, SolidWorks, LaTeX and VHDL.</p>
    </div>
    {photo("about-formal", "Formal portrait of Charl Marais", cls="about-ph glass", pos="50% 15%", eager=True)}
  </div>
  <div class="rv exp">
    <p class="eyebrow">Experience</p>
    <ul class="jobs">
      <li class="job"><h3>Engineer in Training</h3><span class="org">Cape Gate (PTY) LTD</span><time>Dec 2025 – Present</time></li>
      <li class="job"><h3>Maths &amp; Physics Tutor</h3><span class="org">Preply (part time)</span><time>Jan 2026 – Present</time></li>
      <li class="job"><h3>Teaching Assistant</h3><span class="org">University of Pretoria, Dept. of Mathematics &amp; Applied Mathematics</span><time>Mar 2026 – Jun 2026</time></li>
    </ul>
  </div>
</section>

<section id="projects" aria-labelledby="projects-h">
  <p class="eyebrow">Work</p>
  <h2 class="rv" id="projects-h">Selected<span class="d">Projects</span></h2>

  <article class="proj glass rv">
    <div class="shot">{pic("pcb-render", "Annotated black render of the PBCCO-O1000 test PCB")}</div>
    <div class="txt">
      <p class="meta">EPR320 · ongoing · sole designer</p>
      <h3><span translate="no">PBCCO-O1000</span> impedance analyser front end</h3>
      <p>A DIY differential-input oscilloscope built as the measurement core of a full impedance analyser for EPR320. I am the author, designer and systems engineer. It went through several design iterations: a breadboard on lab supplies, a veroboard with a charge pump, and now a fabricated PCB.</p>
      <p>Analogue RMS, peak and zero-crossing front end, ±8&nbsp;V op-amp rails from two buck converters, an STM32 NUCLEO-L432KC, a 2.8″ ILI9341 screen and two rotary encoders for the menu.</p>
      <div class="tags"><span class="tag hot">KiCad</span><span class="tag">LTspice</span><span class="tag">STM32</span><span class="tag">Analogue design</span><span class="tag">JLCPCB</span></div>
    </div>
  </article>

  <article class="proj glass rv">
    <div class="shot">{pic("housing-render", "Annotated black render of the PBCCO-O1000 housing, version 4")}</div>
    <div class="txt">
      <p class="meta">EPR320 · enclosure</p>
      <h3>3D-printed instrument housing</h3>
      <p>A PLA enclosure designed in Fusion for the <span translate="no">PBCCO-O1000</span>, now on its fourth concept. It has a single recessed front panel carrying the screen and the two encoders, ventilation, and a click-detent handle that doubles as a tilt stand.</p>
      <div class="tags"><span class="tag hot">Fusion</span><span class="tag">PLA</span><span class="tag">Design for print</span></div>
    </div>
  </article>

  <div class="projrow">
    <article class="card glass rv">
      <p class="meta">Personal · Apr 2026 – Present</p>
      <h3>Robotic arm prototype</h3>
      <p>An ongoing build covering analogue sensor design, servo and stepper motor control, and an assembly state machine with its firmware.</p>
      <div class="tags"><span class="tag">Sensors</span><span class="tag">Motor control</span><span class="tag">Firmware</span></div>
    </article>
    <article class="card glass rv">
      <p class="meta">EIR210 · May 2025 · with the Olifantes</p>
      <h3>DC motor project</h3>
      <p>Group project for the EIR210 module, completed in May&nbsp;2025 with the Olifantes.</p>
      <div class="tags"><span class="tag">Team project</span><span class="tag">Motors</span></div>
    </article>
  </div>
</section>
</div>
'''

EDU = '''
<div class="band-light" id="education"><div class="wrap">
<section aria-labelledby="edu-h">
  <p class="eyebrow">Education</p>
  <h2 class="rv" id="edu-h">Academic<span class="d">Record</span></h2>
  <div class="edu">
    <div class="glass rv"><div class="small">Feb 2024 – present</div><div class="big">80.0%</div><h3>B.Eng Electrical Engineering</h3><div class="small">University of Pretoria · cumulative average</div></div>
    <div class="glass rv"><div class="small">Jan 2019 – Dec 2023</div><div class="big">84.42%</div><h3>National Senior Certificate</h3><div class="small">Hoërskool Oos-Moot · final aggregate</div></div>
    <div class="glass rv"><div class="small">May 2021 – Oct 2023</div><div class="big">85.0%</div><h3>Advanced Programme Mathematics</h3><div class="small">Admaths (PTY) LTD · further studies</div></div>
  </div>
  <p class="eyebrow">Skills</p>
  <ul class="skills rv"><li>C++</li><li>Python</li><li>MATLAB</li><li>LTspice</li><li>SolidWorks</li><li>LaTeX</li><li>VHDL</li><li>Assembly</li><li>MS Office</li><li>Robotics / Mechatronics</li><li>MV/LV maintenance</li></ul>
  <div class="cols rv">
    <div><h3>Achievements</h3><ul>
      <li>Dean’s Merit List, Faculty of Engineering, 2024, and again for second-year marks</li>
      <li>Bronze award, two years in a row, placing in the top 3 of electrical engineering students in my year group</li>
      <li>Golden Key Award nominee, top 15% in Electrical Engineering</li>
      <li>Gold &amp; silver medallist, Shorin-Ryu Karate National Championship, 2017 – 2023</li>
      <li>Silver medallist, WUKF National Karate Championship, 2024</li>
      <li>Gold medallist, SASKA Shotokan Karate National Championship, 2023</li></ul></div>
    <div><h3>Coursework</h3><ul>
      <li>Analogue Electronics (ongoing)</li><li>Electrical Machines (ongoing)</li><li>Microprocessors (ongoing)</li><li>Electromagnetism (ongoing)</li><li>Linear Systems &amp; Signals</li><li>Digital Systems</li><li>Computer Programming &amp; Simulations</li></ul></div>
  </div>
</section>
</div></div>
'''

SCHOOL = f'''
<div class="wrap">
<section id="school" aria-labelledby="school-h">
  <p class="eyebrow">School</p>
  <h2 class="rv" id="school-h">School<span class="d">&amp; Stage</span></h2>
  <p class="lead rv">Hoërskool Oos-Moot, January&nbsp;2019 to December&nbsp;2023. I finished with a final NSC aggregate of 84.42%, and completed Advanced Programme Mathematics through Admaths with 85.0%.</p>
  <div class="sch rv">
    {photo("school-prizegiving", "Charl receiving a certificate on stage at a school prizegiving", "School prizegiving", "glass sch-a")}
    {photo("school-joseph", "Cast on stage in Joseph and the Technicolour Dreamcoat", "Joseph &amp; the Technicolour Dreamcoat", "glass sch-b")}
    <div class="sch-c">
      <div class="glass"><span class="k">Lead Actor</span><h3>Joseph &amp; the Technicolour Dreamcoat</h3><p>September 2022 to August 2023.</p></div>
      <div class="glass"><span class="k">Debate Team</span><h3>Hoërskool Oos-Moot &amp; Conspirito Cultural Society</h3><p>February 2020 to August 2023.</p></div>
    </div>
  </div>
  <div class="sch-row rv">
    {photo("school-chemistry", "Four school friends in lab coats and safety glasses at a chemistry practical", "Chemistry practical", "glass", "50% 40%")}
    {photo("school-grade11", "Four friends with a pool toy and a rubber duck outside, Grade 11 week", "Grade 11 week", "glass", "50% 35%")}
  </div>
</section>
</div>
'''

REPS = "".join([
    rep("ene", "ENE 310", "Analogue Electronics", "Active Filter Design",
        "Multiple-feedback filter stages designed, simulated in LTspice and measured, with a Monte Carlo tolerance analysis.",
        stats([("20.01&nbsp;kHz", "measured −3&nbsp;dB cutoff"), ("28.80&nbsp;dB", "measured passband gain"), ("20.20&nbsp;kHz", "Monte Carlo mean cutoff")])
        + '<div class="rep-f two">' + figure("ene-measured", "Measured magnitude response of the filter", "Measured magnitude response")
        + figure("ene-montecarlo", "Monte Carlo magnitude response of the filter", "Monte Carlo magnitude response") + "</div>"),
    rep("elx", "ELX 311", "Induction Motors", "Equivalent Circuit",
        "Equivalent-circuit parameters from DC, no-load and blocked-rotor tests, compared with load-test results.",
        '<div class="rep-f">' + figure("elx-torque", "Output torque against slip, theoretical and practical", "Output torque against slip: theoretical and practical") + "</div>"),
    rep("ebb", "EBB 320", "Control Systems", "PID Controller Design",
        "Root-locus and frequency-response designs, tested on the hardware.",
        stats([("ζ&nbsp;=&nbsp;0.591", "G11 root-locus damping line"), ("60&nbsp;°C / 50&nbsp;°C", "G11 / G22 references")])
        + '<div class="rep-f">' + figure("ebb-pid-results", "Temperature tracking and control signals for the G11 and G22 loops", "Measured temperature tracking and control signals, root-locus design (60&nbsp;°C / 50&nbsp;°C)") + "</div>"
        + '<div class="rep-ph">'
        + photo("ebb-setup", "Laptop showing temperature and control-signal plots beside a breadboard circuit", "EBB 320 practical set-up", pos="50% 50%")
        + '</div><p class="source">Photo: @eeceup, University of Pretoria.</p>'),
    rep("ekk", "EKK 320", "Three-Phase Transformers", "Transformer Bank",
        "Y-Y, Y-Δ and Δ-Δ banks agreed within about 1% (theory vs simulation) and 5% (measured), secondary side.",
        stats([("77.70&nbsp;V", "Y-Δ secondary, simulated (rms)"), ("4.80&nbsp;W → 4.29&nbsp;W", "Y-Δ per-phase power in → out, simulated")])
        + '<div class="rep-f">' + figure("ekk-setup", "Annotated lab setup with three transformers, a P&amp;T board and a resistor load", "Lab setup for the transformer bank tests") + "</div>"),
    rep("edf", "EDF 320", "DC-DC Converters", "Buck and Boost Converters",
        "Practical measurements at 5&nbsp;kHz and 20&nbsp;kHz: lower frequency gave higher efficiency at every buck duty ratio tested.",
        stats([("73.57 → 86.65%", "5&nbsp;kHz, δ&nbsp;=&nbsp;0.4 → 0.7"), ("64.82 → 81.36%", "20&nbsp;kHz, δ&nbsp;=&nbsp;0.4 → 0.7")])
        + '<div class="rep-f three">' + figure("edf-waveforms", "Measured voltage and current waveforms at 5 kHz", "Measured voltage and current, 5&nbsp;kHz, δ&nbsp;=&nbsp;0.6")
        + figure("edf-spectra", "Measured input spectra at 20 kHz", "Measured input spectra, 20&nbsp;kHz, δ&nbsp;=&nbsp;0.7")
        + figure("edf-efficiency", "Loss and efficiency estimates against duty setting", "Loss and efficiency estimates against duty setting") + "</div>"),
])

PRACTICALS = f'''
<div class="wrap">
<section id="practicals" aria-labelledby="prac-h">
  <p class="eyebrow">Coursework</p>
  <h2 class="rv" id="prac-h" style="font-size:clamp(32px,5.4vw,68px)">Relevant Assignments<span class="d">&amp; Practical Laboratory Work</span></h2>
  <p class="lead rv">Reports from assignments and laboratory practicals in my degree, written in LaTeX with my lab group. Hover over one, or select it, to open it.</p>
  <div class="reps">{REPS}
  </div>
</section>
</div>
'''

OLIFANTE = f'''
<div class="wrap">
<section id="olifante" aria-labelledby="oli-h">
  <p class="eyebrow">Team collaboration</p>
  <div class="olihead"><h2 class="rv" id="oli-h" translate="no">Pienk BCC<span class="d">Olifante</span></h2><img class="oli-logo" src="img/olifante-logo.png" alt="Pienk BCC Olifante logo" width="520" height="321" decoding="async"></div>
  <div class="oli rv">
    {photo("olifante-exam", "Members of Pienk BCC Olifante at a restaurant after an exam", "After an exam", "glass oli-ph")}
    <div class="oli-tx"><p class="dim">Pienk BCC Olifante is a friend group of electrical engineering students at the University of Pretoria. Charl Marais and Dirk-David Krause started the group on 14 February&nbsp;2024, Ulrich Snyman joined about two weeks later, and Jonathan Oliver joined on 4 March&nbsp;2025.</p>
    <p class="dim">The group studies and builds together, and puts good marks first. It is where the shared projects start, beginning with the EIR210 DC motor in May&nbsp;2025. The <span translate="no">PBCCO-O1000</span> for EPR320 is my own project; I am its sole author, designer and systems engineer.</p></div>
  </div>
  <figure class="glass oli-team rv">{pic("ebb-lab", "Charl and his EBB 320 team at a lab bench with a laptop and breadboard", "50% 40%")}<figcaption>EBB 320 team practical · Charl, Carla, Clarise and Dominik<br><span class="source">Photo: @eeceup, University of Pretoria</span></figcaption></figure>
  <div class="glass tl-card rv">
    <div class="tl-scroll" tabindex="0" role="group" aria-label="Group timeline, scrolls sideways on small screens">
      <div class="tl" aria-hidden="true">
        <div class="axis"></div>
        <span class="yr first" style="left:0%">Feb 2024</span><span class="yr" style="left:36.2%">Jan 2025</span><span class="yr" style="left:75.9%">Jan 2026</span><span class="yr" style="left:97%">Oct 2026</span>
        <div class="join up" style="left:0.4%;--h:70px"><span class="dot"></span><span class="stem"></span><div class="lab"><em>14 Feb 2024</em><b>Charl Marais &amp; Dirk-David Krause</b><span>Started the group.</span></div></div>
        <div class="join dn" style="left:2.6%;--h:46px"><span class="dot"></span><span class="stem"></span><div class="lab"><em>≈ end Feb 2024</em><b>Ulrich Snyman</b><span>Joined about two weeks later.</span></div></div>
        <div class="join up" style="left:39.7%;--h:70px"><span class="dot"></span><span class="stem"></span><div class="lab"><em>4 Mar 2025</em><b>Jonathan Oliver</b><span>Joined the group.</span></div></div>
        <div class="lane" style="left:46.9%;width:3.1%;top:236px;padding:0"></div>
        <span class="ms" style="left:46.9%"></span><span class="ms" style="left:50%"></span>
        <span class="lbl-out" style="left:46%;top:241px;transform:translateX(-100%)">EIR210 DC motor · May 2025</span>
        <div class="lane open" style="left:84%;right:0;top:296px">EPR320</div>
        <span class="ms" style="left:84%;top:309px"></span>
        <span class="lbl-out" style="right:0;top:332px">PBCCO-O1000 · sole designer</span>
        <span class="lbl-out" style="left:0;top:364px">◇ project milestone &nbsp; ● member joined &nbsp; bars show project duration</span>
      </div>
    </div>
    <ol class="sr-only">
      <li>14 February 2024: Charl Marais and Dirk-David Krause started the group.</li>
      <li>About the end of February 2024: Ulrich Snyman joined.</li>
      <li>4 March 2025: Jonathan Oliver joined.</li>
      <li>May 2025: EIR210 DC motor project.</li>
      <li>EPR320 project, ongoing. PBCCO-O1000, sole designer.</li>
    </ol>
  </div>
</section>
</div>
'''

KARATE = f'''
<div class="band-light" id="karate"><div class="wrap">
<section aria-labelledby="karate-h">
  <p class="eyebrow">Outside engineering</p>
  <h2 class="rv" id="karate-h">Karate<span class="d">Shorin-Ryu</span></h2>
  <p class="lead rv">I have trained Shorin-Ryu karate with the Villieria Tigers in Pretoria since August&nbsp;2015. I compete in kata and kumite and train with weapons, with gold and silver medals at national level.</p>
  <div class="kar rv">
    {photo("karate-nationals", "Charl performing kata in a black belt at the Shorin-Ryu national championship, 6 October 2023", "Nationals · 6 Oct 2023", "g-a")}
    {photo("karate-weapons", "Charl performing a weapons kata with crossed kama", "Weapons kata", "g-b")}
    {photo("karate-team", "Shorin-Ryu Shorinkan South Africa team with trophies and the championship sword", "Shorin-Ryu Shorinkan South Africa team", "g-wide", "50% 40%")}
    {photo("karate-trophy", "Charl with two teammates and an official holding a karate trophy", "Trophy presentation", "g-sq", "50% 30%")}
    {photo("karate-podium", "Charl on the top step of a medal podium at the SASKA tournament, 2022, in front of a Shotokan banner", "SASKA tournament · 2022 · Gold", "g-sq", "50% 30%")}
    {photo("karate-kata", "Charl performing kata in a black belt", "Kata", "g-sq", "50% 20%")}
    {photo("karate-certificates", "Charl holding two rank certificates with two instructors", "Rank certificates", "g-sq", "50% 30%")}
    {photo("karate-dojo", "Dojo members in a group photo holding rank certificates", "Dojo group with rank certificates", "g-wide", "50% 40%")}
  </div>
  <div class="dojo rv">
    <div class="glass"><span class="k">Dojo</span><h3>Villieria Tigers</h3><p>Shorin-Ryu Shorinkan karate dojo in Villieria, Pretoria. It opened in 1970, and chief instructor Kyoshi Riaan Coetzee (7th&nbsp;Dan) has led it since 1991. It also teaches Okinawan kobudo.</p></div>
    <div class="glass"><span class="k">Style</span><h3>Shorin-Ryu</h3><p>An Okinawan karate style. Shorin-Ryu Shorinkan came to South Africa on 15 January&nbsp;1994, and the dojo traces its lineage through Shugoro and Minoru Nakazato.</p></div>
    <div class="glass"><span class="k">Dojo motto</span><h3>No retreat, no surrender</h3><p>The motto on the Tigers’ website, kept through the dojo’s changes of location and instructors.</p></div>
  </div>
  <p class="source rv">Source: shorinryu-tigers.co.za</p>
  <ul class="medals">
    <li class="glass"><b>Gold &amp; silver</b><span>Shorin-Ryu National Championship, 2017 – 2023</span></li>
    <li class="glass"><b>Gold</b><span>SASKA Shotokan National Championship, 2023</span></li>
    <li class="glass"><b>Silver</b><span>WUKF National Championship, 2024</span></li>
  </ul>
</section>
</div></div>
'''

CONTACT = f'''
<div class="wrap">
<section id="contact" aria-labelledby="contact-h">
  <div class="ct">
    <div>
      <p class="eyebrow">Contact</p>
      <h2 class="rv" id="contact-h">Get in<span class="d">Touch</span></h2>
      <p class="dim rv">To talk engineering or collaborate on a project, email me or message me on LinkedIn.</p>
      <div class="mail rv"><code id="addr" translate="no">{EMAIL}</code><button class="btn" id="copy" type="button">Copy Address</button><span id="copy-status" class="sr-only" role="status" aria-live="polite"></span></div>
      <div class="cta"><a class="btn primary" href="mailto:{EMAIL}">Email Me</a><a class="btn" href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn <span aria-hidden="true">↗</span><span class="sr-only">(opens in a new tab)</span></a></div>
    </div>
    <div class="ct-ph rv">
      {photo("portrait-wall", "Charl leaning against a brick wall in a denim jacket", cls="glass")}
      {photo("portrait-stairs", "Charl sitting on metal stairs in a denim jacket", cls="glass")}
    </div>
  </div>
</section>
</div>
</main>

<footer class="site-footer"><span translate="no">© 2026 Charl Marais</span><span>Pretoria, South Africa</span></footer>
<script src="js/site.js" defer></script>
</body>
</html>
'''

out = HEAD + NAV + HERO + ABOUT + EDU + SCHOOL + PRACTICALS + OLIFANTE + KARATE + CONTACT
with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
    f.write(out)
print("index.html", len(out) // 1024, "KB")
