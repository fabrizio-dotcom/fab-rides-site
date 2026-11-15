"""Location pages for Fab Rides. One entry per place; tools/build.py turns each into site/place-<slug>.html.

Each place: name, tagline, facts (label, value) pairs, sections (heading, [paragraphs]), and
`draft`: questions still open for Fabrizio. While any place has draft questions, tools/check.py fails,
so a draft can't go live by accident. Delete the questions once he has answered them.
Content follows Fabrizio's answers of 15 November 2026 (handbook, "PR #4 questions").
"""

PARTHIAN_FIRST_VISIT = "https://parthianclimbing.com/become-a-member-2/"
ORTESIDA = "https://www.in-lombardia.it/en/where-to-stay/ortesida-0"
W2W_OFFICIAL = "https://www.epic-series.com/wines2whales"

PLACES = {
    "qecp": {
        "name": "Queen Elizabeth Country Park",
        "tagline": "Our home trails, on the edge of the South Downs.",
        "facts": [
            ("Where", "East Hampshire, beside the A3 near Horndean, in the South Downs National Park"),
            ("What we do", "Mountain biking"),
            ("When", "Friday mornings and Sunday family rides, all year"),
            ("From Winchester", "About 40 minutes by car"),
        ],
        "sections": [
            ("What it&rsquo;s like", [
                "Beech woodland and chalk downland, with Butser Hill rising on the other side of the A3. "
                "The trails run through the trees, so it rides well when the open downs are blowing a gale.",
                "There&rsquo;s something for every rider, from flowing blue trails to steeper red descents, "
                "and a pump track we never skip.",
            ]),
            ("How we ride it", [
                "We pick the trails to suit the riders on the day: usually a blue and a red, and the pump track every time. "
                "When the group is up for it, we head beyond the waymarked trails to the north side. "
                "You&rsquo;ll find most of our segments on Trailforks.",
                "Usually we meet in the main car park. Some days we start from Buriton or from the Red Lion at Chalton instead, "
                "which keeps the best pubs close to the finish. The plan is confirmed each week in the Signal group.",
            ]),
            ("Good to know", [
                "Our tip: once you know the waymarked loops, ask us about the trails north of the red route.",
                "Parking is pay and display, with a visitor centre and caf&eacute; by the main car park. "
                "Chalk turns slippery after rain: expect mud from October to April and bring a spare layer.",
            ]),
        ],
        "draft": [],
    },
    "surrey-hills": {
        "name": "Surrey Hills",
        "tagline": "Saturday destination rides on the best singletrack in the South East.",
        "facts": [
            ("Where", "Surrey Hills National Landscape, starting from Peaslake"),
            ("What we do", "Mountain biking"),
            ("When", "Saturdays, all year"),
            ("From Winchester", "About an hour and a half by car. We share cars."),
        ],
        "sections": [
            ("What it&rsquo;s like", [
                "Sandy, rooty singletrack through pine and birch on the greensand hills south of Guildford. "
                "The soil drains fast, so it stays rideable when Hampshire chalk has turned to grease.",
                "The trails are technical and varied: short sharp climbs, then long descents that reward good line choice. "
                "Leith Hill, the highest point in Surrey, is never far away.",
            ]),
            ("How we ride it", [
                "We usually start from Peaslake, the village at the heart of the Hurtwood trails. "
                "We carpool from Winchester, ride for a few hours, regroup often, and eat before the drive home.",
                "Caf&eacute;s and pubs come and go, so our post-ride stop changes too. Got a favourite? Tell us.",
            ]),
            ("Good to know", [
                "The Hurtwood is looked after by Friends of the Hurtwood, a small charity that keeps the paths, car parks "
                "and public access going with one full-time ranger and donations. We don&rsquo;t support them yet. "
                "If you ride there often, they&rsquo;re well worth a donation.",
                "Peaslake gets busy on weekends. Arriving early makes parking easier.",
            ]),
        ],
        "draft": [],
    },
    "winchester": {
        "name": "Winchester",
        "tagline": "Where most of our rides start, and where the conversation carries on.",
        "facts": [
            ("Where", "Winchester, Hampshire, at the western end of the South Downs"),
            ("What we do", "Weekday training loops on the bike"),
            ("When", "Tuesday or Friday sessions, as announced"),
            ("Meeting point", "The Battery in Oliver&rsquo;s Battery, or Fab&rsquo;s Cave"),
        ],
        "sections": [
            ("What it&rsquo;s like", [
                "Winchester sits where the chalk downs meet the Itchen valley. The South Downs Way starts here "
                "and runs a hundred miles east, so good riding begins at the edge of town.",
                "West Wood is the loop we ride most. Short, varied and close to home, it fits before work.",
            ]),
            ("How we ride it", [
                "We meet at the Battery in Oliver&rsquo;s Battery, or at Fab&rsquo;s Cave. "
                "Local sessions are quick and unfussy: an hour or two, mixed terrain, back in time for the day. "
                "They&rsquo;re a good first ride with us.",
            ]),
            ("Good to know", [
                "Bridleways around Winchester are shared with walkers and horses. We slow down, say hello and give way.",
            ]),
        ],
        "draft": [],
    },
    "portland": {
        "name": "Portland",
        "tagline": "Sport climbing on Dorset limestone, with the sea below.",
        "facts": [
            ("Where", "Isle of Portland, Dorset, on the Jurassic Coast"),
            ("What we do", "Sport climbing"),
            ("Typical grades", "6a to 7a"),
            ("From Winchester", "About an hour and a half by car"),
        ],
        "sections": [
            ("What it&rsquo;s like", [
                "Portland is a block of limestone tied to the mainland by Chesil Beach. The stone that built St Paul&rsquo;s "
                "Cathedral now gives us sea cliffs and old quarries full of bolted routes.",
                "There are routes for every grade, a big sky, and a sea that changes the mood of the day.",
            ]),
            ("How we climb it", [
                "We go as a small group and pick a sector that suits the conditions and the climbers. "
                "These days most of our routes sit between 6a and 7a, picked to suit whoever turns up.",
                "Newer climbers are very welcome. Come along with the group, second routes and climb on top rope "
                "while you build your confidence.",
            ]),
            ("What to bring", [
                "Bring your own harness, helmet and shoes; we share the rest of the kit. "
                "Helmets are compulsory on our outdoor days: sea cliffs and old quarries drop loose rock.",
            ]),
            ("Good to know", [
                "It&rsquo;s exposed: sun, wind and salt all play a part. Sea-cliff sectors depend on tide and swell.",
                "Some areas have access agreements or seasonal restrictions. We check the BMC Regional Access Database before we go.",
            ]),
        ],
        "draft": [],
    },
    "swanage": {
        "name": "Swanage",
        "tagline": "Purbeck sea cliffs, trad and sport, and a classic Dorset day out.",
        "facts": [
            ("Where", "Isle of Purbeck, Dorset, on the Jurassic Coast"),
            ("What we do", "Trad and sport climbing"),
            ("Who it suits", "Beginners and experienced climbers"),
            ("From Winchester", "About an hour and a half by car, longer on summer weekends"),
        ],
        "sections": [
            ("What it&rsquo;s like", [
                "Long limestone cliffs drop straight into the sea around Durlston Head, just south of Swanage. "
                "Many routes start at the bottom of an abseil, just above the waves.",
                "It&rsquo;s committing and beautiful. A good day here stays with you for a long time.",
            ]),
            ("How we climb it", [
                "We climb both trad and sport here, depending on the day and the group, and it&rsquo;s a good place "
                "to take your first steps on Purbeck rock.",
                "We&rsquo;ve run introductory trad and sport days at Swanage. Fab is a qualified Mountain Leader with decades "
                "of climbing in the Alps and the UK, and he&rsquo;s working towards the Rock Climbing Instructor award. "
                "He isn&rsquo;t a qualified climbing instructor yet, so these days are informal: we climb together, "
                "share what we know, and he sharpens his coaching along the way.",
                "Days are planned around the forecast and the tide, and we match routes to the group. "
                "Helmets are compulsory on our outdoor days.",
            ]),
            ("Good to know", [
                "Tide, swell and wet rock decide what&rsquo;s possible. We check the forecast the evening before and again in the morning.",
                "Seabirds nest on parts of these cliffs, and some sections are closed in the breeding season. "
                "We check the BMC Regional Access Database before every visit.",
            ]),
        ],
        "draft": [],
    },
    "parthian-southampton": {
        "name": "Parthian Southampton",
        "tagline": "Indoor climbing three evenings a week, whatever the weather.",
        "facts": [
            ("Where", "Parthian Climbing, Southampton"),
            ("What we do", "Indoor climbing and bouldering"),
            ("When", "Monday, Wednesday and Friday evenings"),
            ("Who it suits", "All levels, first-timers included"),
        ],
        "sections": [
            ("What it&rsquo;s like", [
                "Graded walls under a roof. It&rsquo;s where we keep strength and technique going through the winter "
                "and where most new climbers start with us before moving outside.",
            ]),
            ("How we climb here", [
                "Our regular sessions are Monday, Wednesday and Friday evenings. They&rsquo;re relaxed: "
                "we warm up together, pick problems or routes to work on, and swap beta.",
            ]),
            ("Before your first visit", [
                "Parthian asks every new climber to pre-register before their first visit. For bouldering, "
                "watch their short induction video; for roped climbing, they run Adult Intro sessions. "
                f'Check their <a href="{PARTHIAN_FIRST_VISIT}">First Visit page</a> before you come. '
                "You can hire shoes at the wall.",
            ]),
        ],
        "draft": [],
    },
    "valtellina": {
        "name": "Valtellina",
        "tagline": "Our Alpine base: mountain biking, three kinds of rock and long days from Easter to October.",
        "facts": [
            ("Where", "Lombardy, Italy: the valley of the Adda, from Lake Como up to Bormio"),
            ("What we do", "Mountain biking; climbing on granite, Verrucano and limestone"),
            ("When", "Trips from Easter to October"),
            ("Getting there", "Fly to Milan or Bergamo, then about two hours by car"),
        ],
        "sections": [
            ("What it&rsquo;s like", [
                "Valtellina runs east from the top of Lake Como into the high Alps. The sunny slopes are stepped with "
                "terraced vineyards; the shaded side is forest, pasture and side valleys that climb fast.",
                "There are more than fifty mountain bike routes in the valley and the peaks around it, from old mule tracks "
                "to proper Alpine descents.",
            ]),
            ("Three kinds of rock", [
                "Val di Mello, a short drive up Val Masino, is a nature reserve of granite slabs, boulders and clear water: "
                "friction, cracks and big walls.",
                "Valgerola has something rarer: the purple-red Verrucano Lombardo, a conglomerate you won&rsquo;t find at home.",
                'And down at <a href="place-lake-como.html">Lake Como</a>, limestone and multi-pitch above Lecco.',
            ]),
            ("Where to stay", [
                "Stay close to Fab&rsquo;s base in Sacco, in Valgerola. We usually point people to "
                f'<a href="{ORTESIDA}">Agriturismo Ortesida</a>, near Morbegno. '
                "A friend&rsquo;s place in Dossa is coming soon: details to follow.",
            ]),
            ("How we use it", [
                "Our Valtellina season runs from Easter to October. Trips mix riding and climbing days, "
                "with evenings that move slowly.",
                'Those terraces grow the Nebbiolo behind the valley&rsquo;s wines. Taste them through '
                '<a href="https://fab-wines.co.uk">Fab Wines</a>.',
            ]),
        ],
        "draft": [],
    },
    "valtellina-ski-touring": {
        "name": "Valtellina ski touring",
        "tagline": "Quiet valleys, no queues, and turns you&rsquo;ve earned.",
        "facts": [
            ("Where", "Valgerola, Val Tartano, Valle Spluga (Italy) and the Maloja Pass (Switzerland)"),
            ("What we do", "Ski touring, plus resort days at Pescegallo, Madesimo and Chiesa in Valmalenco"),
            ("When", "Trips in January and April"),
            ("Who it suits", "Confident intermediate ski tourers with full kit. Not for beginners."),
        ],
        "sections": [
            ("What it&rsquo;s like", [
                "Away from the big resorts, the side valleys of lower Valtellina and the Orobie Alps are wide open "
                "in winter. You skin up through larch and pasture, take in the silence at the top, and pick your line down.",
                "Further north, Valle Spluga and the Maloja Pass at the head of Val Bregaglia add high, snow-sure terrain "
                "within a short drive.",
            ]),
            ("How we tour", [
                "Small groups, early starts, and a plan that bends to the snow. January is for deep winter days; "
                "April is for long spring tours on firm snow. For resort days we head to Pescegallo, Madesimo "
                "or Chiesa in Valmalenco.",
                "Touring with us is for confident intermediate ski tourers with their full kit. It isn&rsquo;t for beginners.",
            ]),
            ("Guides and responsibility", [
                "Want a guide? We&rsquo;ll put you in touch with qualified mountain guides: our first choice is Stefano Pizzagalli, "
                "and we know the other good ones in the valley. Or join us as part of an experienced group.",
                "We don&rsquo;t guide: everyone is responsible for themselves and makes their own final call, "
                "and we may ask you not to join a tour that isn&rsquo;t right for you.",
            ]),
            ("Safety", [
                "We read the avalanche bulletin every day and choose the route around it. We practise transceiver searches together. "
                "Everyone brings full kit in good working order: transceiver, probe, shovel and skins.",
            ]),
        ],
        "draft": [
            "Liability wording under &ldquo;Guides and responsibility&rdquo;: validate with legal counsel before it goes live.",
        ],
    },
    "lake-como": {
        "name": "Lake Como",
        "tagline": "Limestone multi-pitch, the Wayfarer&rsquo;s Path and long lunches above the lake.",
        "facts": [
            ("Where", "Lombardy, Italy: Lecco and the eastern shore of the lake"),
            ("What we do", "Limestone climbing and multi-pitch, walking"),
            ("When", "All year: Galbiate and Piani d&rsquo;Erna in winter, Versasio and Nibbio in summer"),
            ("Getting there", "About an hour from Milan"),
        ],
        "sections": [
            ("What it&rsquo;s like", [
                "Steep limestone mountains rising straight out of deep water. The Sentiero del Viandante, "
                "the Wayfarer&rsquo;s Path, follows the eastern shore on old trade routes from Abbadia Lariana to Colico.",
            ]),
            ("Lecco", [
                "Lecco is a climbing town with a long tradition, and its limestone is where we do our multi-pitch. "
                "Our focus now is Galbiate and Piani d&rsquo;Erna in winter, Versasio and Nibbio in summer.",
            ]),
            ("How we use it", [
                "A stage of the Viandante, a day of climbing around Lecco, or a good walk that ends at a restaurant "
                "above Dervio, Bellano or Varenna. Lake Como days fit neatly around a Valtellina trip.",
            ]),
        ],
        "draft": [],
    },
    "dolomites": {
        "name": "Dolomites",
        "tagline": "Where the adventures scale up.",
        "facts": [
            ("Where", "North-east Italy: Pale di San Martino, Tre Cime di Lavaredo and around"),
            ("What we do", "Multi-pitch climbing, enduro riding, skiing"),
            ("When", "Every year, May to July"),
            ("Getting there", "Fly to Venice or Verona, then two to three hours by car"),
        ],
        "sections": [
            ("What it&rsquo;s like", [
                "Pale walls of dolomite rising out of green meadows, a UNESCO World Heritage landscape. "
                "The Pale di San Martino above San Martino di Castrozza, and the three towers of the Tre Cime di Lavaredo, "
                "are among the most recognisable mountains in the Alps.",
            ]),
            ("How we climb here", [
                "Multi-pitch days are a group effort, and only once we&rsquo;ve climbed together and know each other&rsquo;s skills. "
                "We don&rsquo;t usually hire guides for these days, unless they come along as friends.",
            ]),
            ("Weather", [
                "We plan to be off exposed ground from early afternoon until about five, when storms tend to build. "
                "We keep an eye on temperature and pressure through the day, and we avoid descending by via ferrata "
                "when a storm could arrive.",
            ]),
        ],
        "draft": [],
    },
    "bormio": {
        "name": "Bormio",
        "tagline": "Big vertical, a historic town and our main resort base in January.",
        "facts": [
            ("Where", "Upper Valtellina, Lombardy, on the edge of the Stelvio National Park"),
            ("What we do", "Resort skiing, off-piste when conditions allow, ski touring"),
            ("When", "January trip"),
            ("Who it suits", "Confident on red runs, minimum"),
        ],
        "sections": [
            ("What it&rsquo;s like", [
                "An old town of stone and frescoes under a long, steep mountain. The Stelvio piste is one of the great "
                "downhill courses, and in 2026 Bormio hosted the men&rsquo;s alpine events and the first Olympic ski mountaineering races.",
            ]),
            ("How we use it", [
                "Bormio is our main resort base in January. We ski as a group, stop for a proper mountain lunch, "
                "and split into smaller groups when the snow invites it.",
                "When the legs ask for it, we finish in hot water: the Bagni Vecchi, the Bagni Nuovi, or a natural hot spring "
                "hidden in a nearby valley that we only share on the trip.",
            ]),
        ],
        "draft": [],
    },
    "livigno": {
        "name": "Livigno",
        "tagline": "High, cold and snow-sure, with bikes once the snow has gone.",
        "facts": [
            ("Where", "A high valley in the Lombard Alps, close to the Swiss border"),
            ("What we do", "Off-piste and piste skiing; mountain biking in summer"),
            ("When", "Day trips from Valtellina"),
            ("Who it suits", "Intermediate and advanced skiers"),
        ],
        "sections": [
            ("What it&rsquo;s like", [
                "Livigno sits at around 1,800 metres, so the snow arrives early and stays late. "
                "It hosted the freestyle and snowboard events of the 2026 Winter Olympics.",
            ]),
            ("How we use it", [
                "Plenty of off-piste, good piste days when the group wants them, and mountain biking once the snow has gone.",
            ]),
        ],
        "draft": [],
    },
    "valle-dei-forni": {
        "name": "Valle dei Forni",
        "tagline": "Some of the best ski touring in Europe, above Santa Caterina.",
        "facts": [
            ("Where", "Valfurva, Upper Valtellina, in the Stelvio National Park"),
            ("What we do", "Ski touring"),
            ("When", "During winter trips"),
            ("Who it suits", "Confident ski tourers with full kit"),
        ],
        "sections": [
            ("What it&rsquo;s like", [
                "Above Santa Caterina, the road ends and the Valle dei Forni opens towards the glaciers of the Ortles-Cevedale group. "
                "It holds some of the best ski touring routes in Europe. That&rsquo;s what brings us here.",
            ]),
            ("How we tour here", [
                'Same rules as all our <a href="place-valtellina-ski-touring.html">ski touring</a>: full kit, '
                "the avalanche bulletin first, and everyone makes their own call.",
            ]),
        ],
        "draft": [],
    },
    "wines2whales": {
        "name": "Wines2Whales, South Africa",
        "tagline": "Three days of mountain biking from the Winelands to the coast.",
        "facts": [
            ("Where", "Western Cape, South Africa: from the Winelands near Somerset West to Hermanus"),
            ("What we do", "Mountain bike stage racing, in teams of two"),
            ("When", "We raced it in 2025"),
            ("Who it suits", "Riders ready for three long days in the saddle"),
        ],
        "sections": [
            ("What it&rsquo;s like", [
                "Wines2Whales crosses the mountains of the Western Cape through vineyards, fynbos and forest, "
                "and finishes in Hermanus, famous for its whales.",
                "The organisers, the culture and the people were exceptional.",
            ]),
            ("What&rsquo;s next", [
                "Going back is a dream, this time for the &ldquo;other&rdquo; race, the big one. It takes months of "
                "preparation, so here&rsquo;s what we&rsquo;ve learned so far.",
                "<strong>Build the base early.</strong> Long, steady rides through the winter, then back-to-back days "
                "so your body learns to recover overnight.",
                "<strong>Train with your partner.</strong> You race as a team of two: learn each other&rsquo;s pace, "
                "when to push and when to wait.",
                "<strong>Ride technical trails on tired legs.</strong> The hardest descents tend to come late in the day.",
                "<strong>Practise eating on the bike.</strong> Little and often, with the food you&rsquo;ll race on.",
                "<strong>Get the bike right.</strong> A full service well before, tyres you trust, and spares you know how to fit.",
                "If that sounds like your kind of challenge, start riding with us now and tell us.",
                f'Race details: <a href="{W2W_OFFICIAL}">Wines2Whales official site</a>.',
            ]),
        ],
        "draft": [],
    },
}

# Card names on the existing pages that should link to a place page.
LINKS = {
    "Queen Elizabeth Country Park": "qecp",
    "Surrey Hills": "surrey-hills",
    "Winchester": "winchester",
    "Valtellina, Alps": "valtellina",
    "Valtellina and Val di Mello": "valtellina",
    "Portland": "portland",
    "Swanage": "swanage",
    "Parthian Southampton": "parthian-southampton",
    "Valgerola / Val Tartano / Spluga / Maloja": "valtellina-ski-touring",
    "Backcountry Touring": "valtellina-ski-touring",
    "Lake Como": "lake-como",
    "Dolomites": "dolomites",
    "Bormio": "bormio",
    "Livigno": "livigno",
    "Valle dei Forni": "valle-dei-forni",
}
