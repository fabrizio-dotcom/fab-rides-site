#!/usr/bin/env python3
"""Builds the Fab Rides static site into ../site/ (shared header/footer, 6 pages).
site/assets/site.css is edited by hand; every HTML page is generated from this file."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "site"
WP = "https://fab-rides.co.uk/wp-content/uploads"
# Images still served by the current WordPress site. Before the domain switch,
# copy them into assets/ and change these three lines.
LOGO = f"{WP}/2017/01/cropped-FabRides-Bike-Logo-270x270.png"
HERO = f"{WP}/2017/09/Pale-San-Martino-fav-1-scaled.jpg"
FFFN = "https://fabrizio.deliberali.com/fffn"
EMAIL = "fab@fab-rides.co.uk"

NAV = [("index.html", "Home"), ("ride.html", "Ride"), ("climb.html", "Climb"), ("ski.html", "Ski"),
       ("where-we-gather.html", "Where We Gather"), ("join.html", "Join Us")]


def page(slug, title, desc, body):
    cur = ' aria-current="page"'
    links = "\n".join(
        f'        <li><a href="{h}"{cur if h == slug else ""}>{t}</a></li>' for h, t in NAV)
    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex, nofollow">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{HERO}">
<meta property="og:site_name" content="Fab Rides">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{LOGO}">
<link rel="preload" href="assets/fonts/barlow-condensed-latin-700-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/site.css">
</head>
<body>
<a class="skip" href="#content">Skip to content</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html"><img src="{LOGO}" alt="" width="40" height="40"><span>Fab Rides</span></a>
    <input type="checkbox" id="nav-toggle" class="nav-toggle" aria-label="Show menu">
    <label for="nav-toggle" class="nav-btn">Menu</label>
    <nav class="site-nav" aria-label="Main">
      <ul>
{links}
        <li><a class="ext" href="{FFFN}">Field Notes</a></li>
      </ul>
    </nav>
  </div>
</header>
<main id="content">
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <span>&copy; 2026 Fab Rides &middot; Winchester &amp; the Alps &middot; Run by Fab Campaigns Ltd, registered in England and Wales, company no. 10302961</span>
    <span><a href="join.html">Get in touch</a> &middot; <a href="{FFFN}">Fab&rsquo;s Friday Field Notes</a></span>
  </div>
</footer>
</body>
</html>
"""


def head(title, sub):
    return f"""<div class="page-head"><div class="wrap"><h1>{title}</h1><p>{sub}</p></div></div>"""


def places(items):
    cards = "\n".join(
        f'<div class="card place"><span class="tag">{tag}</span><h4>{name}</h4><p>{text}</p></div>'
        for name, tag, text in items)
    return f'<div class="grid">{cards}</div>'


def table(headers, rows):
    th = "".join(f"<th scope=\"col\">{h}</th>" for h in headers)
    trs = "\n".join("<tr>" + "".join(f'<td data-label="{h}">{c}</td>' for h, c in zip(headers, r)) + "</tr>" for r in rows)
    return f'<div class="table-wrap"><table><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>'


def section(inner):
    return f'<section><div class="wrap">{inner}</div></section>'


# ---------------- Home ----------------
home = f"""
<div class="hero">
  <img src="{HERO}" alt="Pale di San Martino, Dolomites" fetchpriority="high">
  <div class="wrap">
    <h1>We Ride. We Climb. We Explore.</h1>
    <p>A community of outdoor enthusiasts, from Hampshire trails to Dolomite ridgelines, forging authentic relationships through shared adventure.</p>
    <div class="btn-row"><a class="btn" href="join.html">Join the Community &rarr;</a></div>
  </div>
</div>
""" + section("""
<div class="prose">
<h2>What We Believe</h2>
<p>The most profound insights arrive in motion. Not in meeting rooms. Not on screens. Through the physical reality of shared effort: grinding up a climb together, belaying someone through their crux move, reading the mountain before the weather turns.</p>
<p>Fab Rides isn&rsquo;t a club, and it isn&rsquo;t about making money. There are no clients here, only fellow adventurers. What we trade is time, effort and stories. <em>Pochi ma buoni.</em> Few but good.</p>
<blockquote>Real adventure takes you out of your comfort zone with no idea of what the outcome will be.</blockquote>
</div>""") + section("""
<h2>What We Do</h2>
<div class="grid">
  <div class="card"><h3>Ride</h3><p>Mountain biking across Hampshire, Surrey Hills, and the Dolomites. Social first, performance second.</p><a class="more" href="ride.html">Explore &rarr;</a></div>
  <div class="card"><h3>Climb</h3><p>Indoor walls and outdoor crags from Swanage to the Alps. All abilities, no ego.</p><a class="more" href="climb.html">Explore &rarr;</a></div>
  <div class="card"><h3>Ski</h3><p>Winter adventures in Valtellina and the wider Alps. Groomers, touring, fresh lines.</p><a class="more" href="ski.html">Explore &rarr;</a></div>
</div>""") + section("<h2>Our Rhythm</h2>" + table(["When", "What", "Who"], [
    ["<strong>Friday mornings</strong>", "Climbing wall or local MTB loop", "Regulars, flexible schedules"],
    ["<strong>Saturdays</strong>", "Main community ride: Surrey Hills, QECP, destination days", "Open to all"],
    ["<strong>Sunday mornings</strong>", "Family-friendly rides, gentler pace, post-ride coffee", "Families, newer riders"],
    ["<strong>Seasonal trips</strong>", "Dolomites (summer), Valtellina ski (Jan/Apr), international", "Open to all"],
]) + """
<p data-gap>No booking systems. Just an invitation to join.</p>
<p>For now, Fab Rides runs under Fab Campaigns Ltd. We&rsquo;re deciding whether to keep it that way or give Fab Rides a structure of its own, and we&rsquo;ll share the decision here.</p>
<div class="btn-row"><a class="btn ghost" href="where-we-gather.html">See Where We Gather &rarr;</a><a class="btn" href="join.html">Join the Community &rarr;</a></div>""") + section(f"""
<div class="prose">
<h2>Fab Riders</h2>
<p>Fab Riders is the name for all of us: friends new and old who share this ethos. The community has taken us from Hampshire trails to a stage race in South Africa, from family cyclocross sessions to multi-pitch routes in the Dolomites.</p>
<p>The adventures feed directly into the writing. Each Friday, experiences from our rides, crags, and mountains find their way into <strong>Fab&rsquo;s Friday Field Notes</strong>.</p>
<div class="btn-row"><a class="btn ghost" href="{FFFN}">Read Fab&rsquo;s Friday Field Notes &rarr;</a></div>
</div>""")

# ---------------- Ride ----------------
ride = head("Ride", "Social mountain biking. No egos. No drop rides. Just good trails and better company.") + section("""
<div class="prose">
<h2>How We Ride</h2>
<p>Every ride is social first, performance second. We wait at junctions. We regroup on climbs. We stop for photos, for chats, for the view. The goal isn&rsquo;t to smash a segment. It&rsquo;s to share an experience.</p>
<p>That doesn&rsquo;t mean we don&rsquo;t push ourselves. Some rides are technical. Some are long. Some involve proper climbing and descending that&rsquo;ll test your bike handling. But no one gets left behind, and no one feels like they&rsquo;re holding the group back.</p>
<h3>What to Expect</h3>
<ul class="list">
<li><strong>Pace:</strong> Conversational. If we can&rsquo;t chat, we&rsquo;re going too hard.</li>
<li><strong>Duration:</strong> 2&ndash;4 hours. Always communicated in advance.</li>
<li><strong>Terrain:</strong> Mix of singletrack, bridleways, and occasional road links.</li>
<li><strong>Ability:</strong> All levels welcome. First time? Let us know.</li>
<li><strong>Post-ride:</strong> Pub stop or coffee. Half the relationship-building happens after the ride.</li>
</ul>
</div>""") + section("<h2>Where We Ride</h2>" + places([
    ("Queen Elizabeth Country Park", "Local anchor", "Our home trails. Flow tracks, pump track, proper enduro descents. 40 minutes from Winchester, the go-to for Friday mornings and Sunday rides."),
    ("Surrey Hills", "Destination day", "Technical singletrack, chalky climbs, best riding in the South East. Regular Saturday destination days. Carpools from Winchester."),
    ("Winchester", "Local &middot; Weekday", "Training loops from St Catherine&rsquo;s Hill or the Lainston House area. Quick Friday or Tuesday sessions."),
    ("Valtellina, Alps", "Community trips", "Our Alpine base. 50+ routes, proper mountain terrain. Seasonal community trips, typically late summer. Open to all."),
]) + '<p class="note" data-gap>We&rsquo;ve also raced Wines2Whales in South Africa and ridden the Dolomites. Fab Riders have a broad horizon.</p>') + section("""
<div class="prose">
<h2>What&rsquo;s Coming: Cyclocross</h2>
<p>The next frontier, and something I want to explore with my daughters. Mud, barriers, dismounts, laughter. Technical enough to be interesting, forgiving enough to try. Watch this space.</p>
<h2 data-gap>What to Bring</h2>
<ul class="list">
<li>Mountain bike in good working order (hardtail or full suspension)</li>
<li>Helmet, mandatory</li>
<li>Water and snacks</li>
<li>Spare tube, pump, and basic tools</li>
<li>Layers appropriate for conditions</li>
</ul>
<p class="note">Need a bike service before joining? Ask us. We know a great mechanic.</p>
</div>""") + section("""
<div class="callout"><h3>Ready to ride?</h3><p>No booking system. No membership fee. Get in touch and come out for a session.</p><a class="btn" href="join.html">Join a Ride &rarr;</a></div>""")

# ---------------- Climb ----------------
climb = head("Climb", "Indoor walls and outdoor crags. Building strength, technique, and trust, one move at a time.") + section("""
<div class="prose">
<h2>Why We Climb</h2>
<p>Climbing strips everything down to essentials. You, the rock, and the problem in front of you. There&rsquo;s no hiding from your weaknesses. No shortcuts. Just honest feedback about where you are and what you need to work on.</p>
<p>It&rsquo;s also deeply social. Belaying requires trust. Beta-sharing builds connection. Celebrating sends creates community. We climb together because it makes us better, as climbers and as people.</p>
<h2 data-gap>The Journey</h2>
<p>I&rsquo;m currently climbing at 6c onsight and 7a+ redpoint, working toward 7b onsight as a 2026 goal, with 8a redpoint on the longer horizon. I&rsquo;m also pursuing my International Mountain Leader qualification. I share this not as credentials but as context: I&rsquo;m on a journey too, and you&rsquo;re welcome to join wherever you are on yours.</p>
<p>Whether you&rsquo;re touching plastic for the first time or projecting your hardest grade, there&rsquo;s space here.</p>
</div>""") + section("""
<h2>Session Types</h2>
<div class="prose"><h3>Indoor Sessions</h3><p>Regular sessions at Southampton climbing wall. Building strength, technique, year-round regardless of weather. Friday mornings are the usual slot.</p>
<h3 data-gap>Outdoor Crags, UK</h3></div>""" + places([
    ("Portland", "Dorset coast", "World-class sport climbing on Dorset limestone. Sea cliffs, hard routes, extraordinary setting. Always worth the drive."),
    ("Swanage", "Dorset coast", "Coastal limestone with something for every grade. Beautiful setting. A community favourite for outdoor days."),
]) + """
<div class="prose" data-gap><h3>Alpine Climbing</h3><p>Multi-pitch routes in the Dolomites and Valtellina. Longer days, bigger exposure, deeper rewards. Occasional community trips for experienced climbers. The Dolomite limestone is unlike anything in the UK.</p></div>""") + section("""
<div class="prose">
<h2>What to Expect</h2>
<ul class="list">
<li><strong>Supportive atmosphere:</strong> No ego, no pressure. Try hard, fall off, try again.</li>
<li><strong>Mixed abilities:</strong> Everyone finds something to work on.</li>
<li><strong>Gear:</strong> Indoor, hire shoes at the wall if needed. Outdoor, let us know what you have.</li>
<li><strong>Beginners absolutely welcome:</strong> We get you climbing safely from session one.</li>
</ul></div>""") + section("""
<div class="callout"><h3>Come to a session</h3><p>First time climbing? Tell us. We&rsquo;ll make sure you leave wanting to come back.</p><a class="btn" href="join.html">Join a Session &rarr;</a></div>""")

# ---------------- Ski ----------------
ski = head("Ski", "Winter adventures in the Alps. From resort days to backcountry ski touring.") + section("""
<div class="prose">
<h2>Mountains in Winter</h2>
<p>There&rsquo;s nothing quite like the Alps in winter. The scale. The silence. The way a mountain transforms under snow. Whether you&rsquo;re carving groomers, exploring the backcountry on touring skis, or finding fresh lines off-piste, winter in the mountains is adventure in its purest form.</p>
<h2 data-gap>What We Offer</h2>
<h3>Resort Days</h3>
<p>Group days at resorts in Valtellina and the wider Alps. Skiing together, stopping for mountain lunches, sharing the experience. All abilities, from confident intermediates to expert skiers.</p>
<h3>Ski Touring</h3>
<p>For those wanting to go deeper: earn your turns through the backcountry. Skin up, ski down, find your own lines. Requires fitness, avalanche awareness, and appropriate gear. Smaller groups, bigger adventures.</p>
<h3>UK Sessions</h3>
<p>When Scotland delivers, we&rsquo;ll head north. Occasional dry slope sessions for off-season practice and pre-trip preparation.</p>
</div>""") + section("""
<h2>Our Valtellina Base</h2>
<p class="prose">Our Alpine base gives access to world-class skiing without the crowds. Bormio, Livigno, Santa Caterina, all within reach. Plus ski touring terrain that rivals anywhere in the Alps.</p>""" + places([
    ("Bormio", "Resort + Touring", "Long vertical drop, great piste variety, and serious off-piste when conditions are right. Our main resort base for January trips."),
    ("Livigno", "Resort", "High altitude resort with reliable snow. Good for intermediate and advanced skiers. Accessible from Valtellina for a day trip."),
    ("Santa Caterina", "Quieter resort", "Less crowded alternative to Bormio. Excellent terrain, World Cup downhill pedigree. Great for a focused day on the mountain."),
    ("Backcountry Touring", "Earn your turns", "Alpine touring terrain across the Valtellina valley. Requires touring setup and avalanche safety gear. Smaller groups, bigger rewards."),
]) + '<p data-gap>Community trips typically run in <strong>January</strong> and <strong>April</strong>.</p>') + section("""
<div class="prose">
<h2>What You Need</h2>
<ul class="list">
<li><strong>Resort skiing:</strong> Confident on red runs minimum. Own gear or hire locally.</li>
<li><strong>Ski touring:</strong> Good fitness, touring setup, avalanche safety gear (transceiver, probe, shovel). Some backcountry experience preferred.</li>
<li><strong>All trips:</strong> Travel insurance covering winter sports. Flexibility for weather windows.</li>
</ul></div>""") + section("""
<div class="callout"><h3>Interested in a winter trip?</h3><p>Get in touch to find out about the next Valtellina trip or ski touring day.</p><a class="btn" href="join.html">Get in Touch &rarr;</a></div>""")

# ---------------- Where We Gather ----------------
gather = head("Where We Gather", "Fab Rides doesn&rsquo;t have a headquarters. It has a geography: a loose, moving landscape of car parks, crags, trail heads, mountain huts, and the occasional exceptional pub.") + section("""
<div class="prose">
<h2>Winchester, Home Base</h2>
<p>Winchester is where most of us start. The city sits at the edge of good terrain: 40 minutes from Queen Elizabeth Country Park, an hour and a half from the Surrey Hills and from Portland. For rides, we typically meet at the QECP car park or at Fab&rsquo;s cave for local loops in West Wood. For climbing, the Southampton wall on Friday mornings is the default.</p>
<p>After most sessions: either the pub nearest the trailhead, or coffee somewhere on the way back. The debrief is non-negotiable.</p>
</div>""") + section("<h2>South East England</h2>" + places([
    ("Queen Elizabeth Country Park", "MTB &middot; Hampshire", "Our local anchor. Flow trails, pump track, and enduro descents. The Friday morning default and regular Sunday venue. Car park meetup, confirmed per ride via Signal."),
    ("Surrey Hills", "MTB &middot; Surrey", "Saturday destination rides. Box Hill, Leith Hill, Holmbury: serious singletrack in beautiful woodland. Carpools arranged from Winchester. One of our most-visited spots."),
    ("Portland", "Climbing &middot; Dorset", "World-class sport climbing on Dorset limestone. Sea cliffs, hard routes, extraordinary setting. Day trips when conditions are good."),
    ("Swanage", "Climbing &middot; Dorset", "Coastal limestone with something for every grade. Beautiful setting, varied climbing. A community favourite for outdoor days."),
    ("Southampton Climbing Wall", "Indoor &middot; Year-round", "The Monday evening and Friday morning in bad weather default for climbing sessions. Covered, graded for all abilities. Where most new climbers start with us before moving outside."),
])) + section("""<h2>The Alps, Valtellina Base</h2>
<p class="prose">The Alps aren&rsquo;t a destination we visit occasionally. They&rsquo;re part of how Fab Rides thinks and moves. We have a base in Valtellina, near Lake Como, and in the Dolomites, which anchors our seasonal community trips.</p>""" + places([
    ("Valtellina / Lake Como / Val di Mello", "MTB + Climbing", "Over 50 MTB routes in the valley and surrounding peaks. Multi-pitch climbing on proper Alpine limestone. The summer hub for community trips."),
    ("Valgerola / Val Tartano / Spluga / Maloja", "Skiing", "World-class skiing without the overcrowded resorts. January and April community trips. Ski touring terrain that rivals anywhere in the Alps."),
    ("Dolomites", "Climbing + MTB + Skiing", "Pale di San Martino. Tre Cime di Lavaredo. Iconic terrain for multi-day climbing and enduro riding. Where the adventures scale up."),
    ("Lake Como", "Cycling + Hiking + Climbing", "Road and gravel riding on legendary terrain. The Piani di Bobbio. The Muro di Sormano. Extraordinary riding, extraordinary views. The Wayfarer Walk and the superb crags of Lecco."),
])) + section("""
<div class="prose">
<h2>Beyond Europe</h2>
<p>Fab Riders go further when the right opportunity comes together. In 2025, a group of us raced Wines2Whales in South Africa: three days of MTB through the Winelands. The organisers, the culture, the people were all exceptional. We&rsquo;re building the foundation to return stronger, this time with a bigger Winchester and Dolomites contingent.</p>
<p>International trips happen when the right group and the right event align. If you&rsquo;re interested in future adventures, <a href="join.html">get in touch</a>.</p>
</div>""") + section("""
<div class="prose">
<h2>After the Ride</h2>
<blockquote>Half the relationship-building happens after the ride. The trail is the opening; the rest is the conversation.</blockquote>
<p>The pub stop, the coffee, the glass of wine at the end of a long day in the mountains. These aren&rsquo;t afterthoughts. They&rsquo;re part of what makes Fab Rides what it is.</p>
<p>Curious about Fab Wines, the parallel community built around the same ethos, just with bottles rather than bikes? Visit <a href="https://fab-wines.co.uk">fab-wines.co.uk</a>.</p>
</div>""")

# ---------------- Join ----------------
join = head("Join the Community", "No membership form. No subscription. No performance standard. Just show up, ride your own ride, and see if this feels like your kind of people.") + section("""
<div class="prose">
<h2>How It Works</h2>
<p>Fab Rides doesn&rsquo;t run on booking systems or commercial infrastructure. It runs on a Signal group (<a href="https://fabrizio.deliberali.com/idea1">we don&rsquo;t use WhatsApp</a>), word of mouth, and the weekly field notes that go out every Friday. When a session is happening, it&rsquo;s announced. You join if you can. Simple.</p>
<h3>The Weekly Rhythm</h3>
</div>""" + table(["Day", "Activity", "Where", "Who"], [
    ["<strong>Friday AM</strong>", "Climbing wall or local MTB loop", "Southampton wall / QECP", "Flexible schedules, regulars"],
    ["<strong>Saturday</strong>", "Main community ride or crag day", "Surrey Hills, Portland, or local", "Open to all"],
    ["<strong>Sunday AM</strong>", "Family-friendly ride or run", "QECP or Winchester local", "Families, newer riders"],
    ["<strong>Seasonal trips</strong>", "Alps, Dolomites, international adventures", "Valtellina, South Africa, beyond", "Open to all"],
]) + '<p class="note" data-gap>Sessions confirmed mid-week via <a href="https://signal.org">Signal</a>. Get in touch and we&rsquo;ll add you to the group.</p>') + section("""
<h2>Who Joins</h2>
<div class="grid">
  <div class="card"><h4>First-timers</h4><p>Never mountain biked or climbed outdoors? Tell us. We&rsquo;ll match you to the right session.</p></div>
  <div class="card"><h4>Families</h4><p>My daughters ride and climb with us. Sunday mornings are family-paced. The outdoors starts at home.</p></div>
  <div class="card"><h4>Adventure Seekers</h4><p>Ready to go bigger? Alpine trips, international races, multi-day touring. The community has a broad horizon.</p></div>
</div>""") + section("""
<div class="prose">
<h2>Your First Session</h2>
<ul class="list">
<li>Tell us it&rsquo;s your first time. We&rsquo;ll brief you before we set off.</li>
<li>No one gets dropped. We ride together, regroup, wait at junctions.</li>
<li>Bring appropriate kit. See the <a href="ride.html">Ride</a>, <a href="climb.html">Climb</a>, and <a href="ski.html">Ski</a> pages for specifics.</li>
<li>Plan to stay for coffee or a pub stop after.</li>
<li>Ask questions about routes, gear, technique. We like talking about this stuff.</li>
</ul></div>""") + section(f"""
<div class="callout" id="contact">
<h2>Get in Touch</h2>
<p>The simplest way to join is to message directly. No application process, no waitlist. Just a conversation about what you&rsquo;d like to do and when the next suitable session is.</p>
<p class="contact-line">Email <a href="mailto:{EMAIL}?subject=Joining%20Fab%20Rides"><code>{EMAIL}</code></a> with what you&rsquo;d like to do (ride, climb, ski) and we&rsquo;ll add you to the Signal group.</p>
<div class="btn-row"><a class="btn" href="mailto:{EMAIL}?subject=Joining%20Fab%20Rides">Email Fab Rides</a></div>
</div>
<div class="prose" data-gap>
<p>You&rsquo;ll also find Fabrizio&rsquo;s weekly reflections at <a href="{FFFN}"><strong>Fab&rsquo;s Friday Field Notes</strong></a>. The community often coalesces around the ideas and experiences shared there.</p>
<blockquote>The outdoors starts at home. Sometimes the most important adventure is the Sunday morning ride with your kids on a muddy Hampshire bridleway.<footer>Fabrizio, Fab Rides</footer></blockquote>
</div>""")

notfound = head("Off the trail", "This page doesn&rsquo;t exist, or it moved when the site was rebuilt.") + section(
    '<div class="btn-row"><a class="btn" href="index.html">Back to Home</a><a class="btn ghost" href="join.html">Join Us</a></div>')

PAGES = {
    "index.html": ("Fab Rides", "We Ride. We Climb. We Explore. A community of outdoor enthusiasts, from Hampshire trails to Dolomite ridgelines.", home),
    "ride.html": ("Ride | Fab Rides", "Social mountain biking. No egos. No drop rides. Just good trails and better company.", ride),
    "climb.html": ("Climb | Fab Rides", "Indoor walls and outdoor crags. Building strength, technique, and trust, one move at a time.", climb),
    "ski.html": ("Ski | Fab Rides", "Winter adventures in the Alps. From resort days to backcountry ski touring.", ski),
    "where-we-gather.html": ("Where We Gather | Fab Rides", "Car parks, crags, trail heads, mountain huts: the geography of Fab Rides, from Winchester to Valtellina.", gather),
    "join.html": ("Join Us | Fab Rides", "No membership form. No subscription. Just show up and see if this feels like your kind of people.", join),
    "404.html": ("Page not found | Fab Rides", "Page not found.", notfound),
}

for slug, (title, desc, body) in PAGES.items():
    (OUT / slug).write_text(page(slug, title, desc, body), encoding="utf-8")

# Old WordPress URLs with trailing slash / feeds -> new pages (Cloudflare Pages _redirects syntax)
(OUT / "_redirects").write_text("""/feed / 301
/wp-admin / 301
/wp-login.php / 301
""", encoding="utf-8")
(OUT / "_headers").write_text("""/*
  Content-Security-Policy: default-src 'none'; style-src 'self'; font-src 'self'; img-src 'self' https://fab-rides.co.uk; base-uri 'none'; form-action 'none'; frame-ancestors 'none'
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=(), interest-cohort=()
  X-Frame-Options: DENY
/assets/*
  Cache-Control: public, max-age=604800
""", encoding="utf-8")
print("built", sorted(p.name for p in OUT.rglob("*") if p.is_file()))
