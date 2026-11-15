"""Location pages for Fab Rides. One entry per place; tools/build.py turns each into site/place-<slug>.html.

Each place: name, tagline, facts (label, value) pairs, sections (heading, [paragraphs]), and
`draft`: questions for Fabrizio. While any place has draft questions, tools/check.py fails,
so a draft can't go live by accident. Delete the questions once he has answered them.
"""

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
                "There&rsquo;s something for every rider: flowing tracks for a first outing, and steeper descents "
                "for anyone who wants to push. It&rsquo;s close enough for a morning session and good enough to keep coming back.",
            ]),
            ("How we ride it", [
                "QECP is our default. Friday mornings are for the regulars on flexible schedules. "
                "Sundays are slower and family-paced, with time for coffee at the end.",
                "We meet in the main car park. The exact time is confirmed each week in the Signal group.",
            ]),
            ("Good to know", [
                "Parking is pay and display. There&rsquo;s a visitor centre and caf&eacute; by the car park.",
                "Chalk turns slippery after rain. Expect mud from October to April and bring a spare layer.",
            ]),
        ],
        "draft": [
            "Which trails do we usually ride, and is the pump track still part of a typical session?",
            "Is the main car park the right meeting point for both Friday and Sunday?",
            "Any local tip worth sharing (best loop, where we stop, the coffee)?",
        ],
    },
    "surrey-hills": {
        "name": "Surrey Hills",
        "tagline": "Saturday destination rides on the best singletrack in the South East.",
        "facts": [
            ("Where", "Surrey Hills National Landscape: Peaslake, Holmbury Hill, Pitch Hill, Leith Hill"),
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
                "These are our big Saturday days. We carpool from Winchester, ride for a few hours, regroup often, "
                "and finish with food before the drive home.",
            ]),
            ("Good to know", [
                "Much of the riding is on land where access is a privilege, and volunteer trail builders keep it running. "
                "We ride the way-marked trails, stay off closed lines and leave it as we found it.",
                "Peaslake gets busy on weekends. Arriving early makes parking easier.",
            ]),
        ],
        "draft": [
            "Where do we usually start: Peaslake, Holmbury or Leith Hill?",
            "Do we support a local trail group (for example by donating) that we want to name here?",
            "Which caf&eacute; or pub is our regular stop?",
        ],
    },
    "winchester": {
        "name": "Winchester",
        "tagline": "Where most of our rides start, and where the conversation carries on.",
        "facts": [
            ("Where", "Winchester, Hampshire, at the western end of the South Downs"),
            ("What we do", "Weekday training loops on the bike, local runs"),
            ("When", "Tuesday or Friday sessions, as announced"),
            ("Meeting point", "Fab&rsquo;s cave, or the trailhead of the day"),
        ],
        "sections": [
            ("What it&rsquo;s like", [
                "Winchester sits where the chalk downs meet the Itchen valley. The South Downs Way starts here "
                "and runs a hundred miles east, so good riding begins at the edge of town.",
                "St Catherine&rsquo;s Hill, West Wood and the lanes around Sparsholt give us short loops that fit "
                "before work.",
            ]),
            ("How we ride it", [
                "Local sessions are quick and unfussy: an hour or two, mixed terrain, back in time for the day. "
                "They&rsquo;re a good first ride with us.",
            ]),
            ("Good to know", [
                "Bridleways around Winchester are shared with walkers and horses. We slow down, say hello and give way.",
            ]),
        ],
        "draft": [
            "Which loops do we ride most often (St Catherine&rsquo;s Hill, West Wood, Lainston, others)?",
            "Is &ldquo;Fab&rsquo;s cave&rdquo; the right way to describe the meeting point publicly, without an address?",
        ],
    },
    "portland": {
        "name": "Portland",
        "tagline": "Sport climbing on Dorset limestone, with the sea below.",
        "facts": [
            ("Where", "Isle of Portland, Dorset, on the Jurassic Coast"),
            ("What we do", "Sport climbing"),
            ("When", "Day trips when the weather is right, mostly spring to autumn"),
            ("From Winchester", "About an hour and a half by car"),
        ],
        "sections": [
            ("What it&rsquo;s like", [
                "Portland is a block of limestone tied to the mainland by Chesil Beach. The stone that built St Paul&rsquo;s "
                "Cathedral now gives us sea cliffs and old quarries full of bolted routes.",
                "There are routes for every grade, a big sky, and a sea that changes the mood of the day.",
            ]),
            ("How we climb it", [
                "We go as a small group, pick a sector that suits the conditions and the climbers, and share ropes and beta.",
            ]),
            ("Good to know", [
                "It&rsquo;s exposed: sun, wind and salt all play a part. Sea-cliff sectors depend on tide and swell.",
                "Some areas have access agreements or seasonal restrictions. We check the BMC Regional Access Database before we go.",
            ]),
        ],
        "draft": [
            "Which grades should we mention as typical for our group days here?",
            "How do newer climbers take part here (seconding, top-rope)? (Safety wording)",
            "Do we lend gear to newer climbers, or should they bring their own harness and shoes?",
        ],
    },
    "swanage": {
        "name": "Swanage",
        "tagline": "Purbeck sea cliffs and a classic Dorset day out.",
        "facts": [
            ("Where", "Isle of Purbeck, Dorset, on the Jurassic Coast"),
            ("What we do", "Climbing on coastal limestone"),
            ("When", "Outdoor days in settled weather"),
            ("From Winchester", "To confirm"),
        ],
        "sections": [
            ("What it&rsquo;s like", [
                "Long limestone cliffs drop straight into the sea around Durlston Head, just south of Swanage. "
                "Many routes start at the bottom of an abseil, just above the waves.",
                "It&rsquo;s committing and beautiful. A good day here stays with you for a long time.",
            ]),
            ("How we climb it", [
                "Swanage days are planned around the forecast and the tide, and we match routes to the group.",
            ]),
            ("Good to know", [
                "Tide, swell and wet rock decide what&rsquo;s possible. We check the forecast the evening before and again in the morning.",
                "Seabirds nest on parts of these cliffs, and some sections are closed in the breeding season. "
                "We check the BMC Regional Access Database before every visit.",
            ]),
        ],
        "draft": [
            "Drive time from Winchester you&rsquo;re happy to publish.",
            "Is Swanage suitable for beginners in our group, or should the page say it&rsquo;s for experienced climbers? (Safety wording)",
            "Do we climb trad here, sport, or both?",
        ],
    },
    "southampton-wall": {
        "name": "Southampton Climbing Wall",
        "tagline": "Indoor climbing, all year, whatever the weather.",
        "facts": [
            ("Where", "Southampton"),
            ("What we do", "Indoor climbing and bouldering"),
            ("When", "Friday mornings, and Monday evenings in bad weather"),
            ("From Winchester", "To confirm"),
        ],
        "sections": [
            ("What it&rsquo;s like", [
                "Graded walls under a roof. It&rsquo;s where we keep strength and technique going through the winter "
                "and where most new climbers start with us before moving outside.",
            ]),
            ("How we climb here", [
                "Sessions are relaxed. We warm up together, pick problems or routes to work on, and swap beta. "
                "First-timers get a proper briefing and a partner who knows the ropes.",
            ]),
            ("Good to know", [
                "You can hire shoes at the wall. Entry is paid at the desk.",
            ]),
        ],
        "draft": [
            "Which wall is it? Name and link (we need to approve the domain).",
            "Is the travel time right, and is Monday evening still a regular slot?",
            "Does the wall require its own registration or induction before a first visit?",
        ],
    },
    "valtellina": {
        "name": "Valtellina",
        "tagline": "Our Alpine base: mountain biking, granite and long summer days.",
        "facts": [
            ("Where", "Lombardy, Italy: the valley of the Adda, from Lake Como up to Bormio"),
            ("What we do", "Mountain biking, multi-pitch and granite climbing in Val di Mello"),
            ("When", "Community trips in summer, typically late summer"),
            ("Getting there", "Fly to Milan or Bergamo, then about two hours by car"),
        ],
        "sections": [
            ("What it&rsquo;s like", [
                "Valtellina runs east from the top of Lake Como into the high Alps. The sunny slopes are stepped with "
                "terraced vineyards; the shaded side is forest, pasture and side valleys that climb fast.",
                "There are more than fifty mountain bike routes in the valley and the peaks around it, from old mule tracks "
                "to proper Alpine descents.",
            ]),
            ("Val di Mello", [
                "A short drive up Val Masino, Val di Mello is a nature reserve of granite slabs, boulders and clear water. "
                "It&rsquo;s a different kind of climbing from the limestone at home: friction, cracks and big walls.",
            ]),
            ("How we use it", [
                "This is where Fab Rides feels most at home. Summer trips mix riding and climbing days, "
                "with evenings that move slowly and a glass of the valley&rsquo;s own wine.",
            ]),
        ],
        "draft": [
            "Should we say where in Valtellina we stay, or keep it general?",
            "Which month do summer trips usually run?",
            "Link to Fab Wines here, given the terraced vineyards?",
        ],
    },
    "valtellina-ski-touring": {
        "name": "Valtellina ski touring",
        "tagline": "Quiet valleys, no queues, and turns you&rsquo;ve earned.",
        "facts": [
            ("Where", "Valgerola, Val Tartano, Valle Spluga (Italy) and the Maloja Pass (Switzerland)"),
            ("What we do", "Ski touring and quieter resort days"),
            ("When", "Community trips in January and April"),
            ("Who it suits", "Fit skiers with touring kit and avalanche training"),
        ],
        "sections": [
            ("What it&rsquo;s like", [
                "Away from the big resorts, the side valleys of lower Valtellina and the Orobie Alps are wide open "
                "in winter. You skin up through larch and pasture, take in the silence at the top, and pick your line down.",
                "Further north, Valle Spluga and the Maloja Pass at the head of Val Bregaglia add high, snow-sure terrain "
                "within a short drive.",
            ]),
            ("How we tour", [
                "Small groups, early starts, and a plan that bends to the snow and the avalanche bulletin. "
                "January is for deep winter days; April is for long spring tours on firm snow.",
            ]),
            ("Good to know", [
                "Every tourer carries a transceiver, probe and shovel and knows how to use them. "
                "We read the local avalanche bulletin each day and turn back when it says so.",
            ]),
        ],
        "draft": [
            "Do we tour with a qualified mountain guide? If so, say so here. (Safety and qualifications)",
            "Which minimum experience do you want to ask of new tourers?",
            "Confirm the avalanche-bulletin practice described under Good to know. (Safety wording)",
            "Is Pescegallo or Madesimo used for resort days we should mention?",
        ],
    },
    "lake-como": {
        "name": "Lake Como",
        "tagline": "Legendary roads, lakeside paths and the climbing town of Lecco.",
        "facts": [
            ("Where", "Lombardy, Italy: the lake and the mountains between Como, Lecco and Colico"),
            ("What we do", "Road and gravel riding, hiking, climbing"),
            ("When", "Spring to autumn"),
            ("Getting there", "About an hour from Milan"),
        ],
        "sections": [
            ("What it&rsquo;s like", [
                "Steep mountains straight out of deep water. The roads are part of cycling history: "
                "the Muro di Sormano is one of the hardest climbs in Italy, and the Giro di Lombardia has raced here for generations.",
                "On foot, the Sentiero del Viandante, the Wayfarer&rsquo;s Path, follows the eastern shore on old trade routes "
                "from Abbadia Lariana to Colico.",
            ]),
            ("Lecco", [
                "Lecco is a climbing town with a long tradition. The crags and the Grigna massif above it have shaped "
                "generations of Italian alpinists.",
            ]),
            ("How we use it", [
                "Lake Como days fit around a Valtellina trip: a big road or gravel loop, a stage of the Viandante, "
                "or a day on Lecco rock.",
            ]),
        ],
        "draft": [
            "Which of these do we actually do on trips (road, gravel, Viandante, Lecco climbing)?",
            "Piani di Bobbio was on the old page: keep it, and for which activity?",
        ],
    },
    "dolomites": {
        "name": "Dolomites",
        "tagline": "Where the adventures scale up.",
        "facts": [
            ("Where", "North-east Italy: Pale di San Martino, Tre Cime di Lavaredo and around"),
            ("What we do", "Multi-pitch climbing, enduro riding, skiing"),
            ("When", "Summer for climbing and riding; winter for skiing"),
            ("Getting there", "Fly to Venice or Verona, then two to three hours by car"),
        ],
        "sections": [
            ("What it&rsquo;s like", [
                "Pale walls of dolomite rising out of green meadows, a UNESCO World Heritage landscape. "
                "The Pale di San Martino above San Martino di Castrozza, and the three towers of the Tre Cime di Lavaredo, "
                "are among the most recognisable mountains in the Alps.",
            ]),
            ("How we use it", [
                "Dolomite trips are for longer days: multi-pitch routes on rock unlike anything in the UK, "
                "enduro descents from high passes, and winter days on the snow.",
            ]),
            ("Good to know", [
                "Afternoon storms are common in summer. We start early and plan to be off the wall by early afternoon.",
            ]),
        ],
        "draft": [
            "Who leads multi-pitch days? Is a guide involved? (Safety and qualifications)",
            "Do Dolomite trips run every year, and in which month?",
            "Confirm the early-start rule for summer storms. (Safety wording)",
        ],
    },
    "bormio": {
        "name": "Bormio",
        "tagline": "Big vertical, a historic town and our main resort base in January.",
        "facts": [
            ("Where", "Upper Valtellina, Lombardy, on the edge of the Stelvio National Park"),
            ("What we do", "Resort skiing, off-piste when conditions allow, ski touring"),
            ("When", "January community trip"),
            ("Who it suits", "Confident on red runs, minimum"),
        ],
        "sections": [
            ("What it&rsquo;s like", [
                "An old town of stone and frescoes under a long, steep mountain. The Stelvio piste is one of the great "
                "downhill courses, and in 2026 Bormio hosted the men&rsquo;s alpine events and the first Olympic ski mountaineering races.",
                "After a long day, the thermal baths in the valley are part of the routine.",
            ]),
            ("How we use it", [
                "Bormio is our main resort base in January. We ski as a group, stop for a proper mountain lunch, "
                "and split into smaller groups when the snow invites it.",
            ]),
        ],
        "draft": [
            "Mention the thermal baths as something we actually do?",
        ],
    },
    "livigno": {
        "name": "Livigno",
        "tagline": "High, cold and snow-sure.",
        "facts": [
            ("Where", "A high valley in the Lombard Alps, close to the Swiss border"),
            ("What we do", "Resort skiing"),
            ("When", "Day trips from Valtellina during winter trips"),
            ("Who it suits", "Intermediate and advanced skiers"),
        ],
        "sections": [
            ("What it&rsquo;s like", [
                "Livigno sits at around 1,800 metres, so the snow arrives early and stays late. "
                "It hosted the freestyle and snowboard events of the 2026 Winter Olympics.",
                "Wide slopes on both sides of the valley make it easy to keep a group together.",
            ]),
            ("How we use it", [
                "A day trip from our Valtellina base when we want reliable snow and a change of scene.",
            ]),
        ],
        "draft": [
            "Anything specific we do in Livigno you want mentioned?",
        ],
    },
    "santa-caterina": {
        "name": "Santa Caterina",
        "tagline": "The quieter alternative, with World Cup pedigree.",
        "facts": [
            ("Where", "Valfurva, Upper Valtellina, Lombardy"),
            ("What we do", "Resort skiing"),
            ("When", "During winter trips"),
            ("Who it suits", "Confident skiers who like steep, quiet pistes"),
        ],
        "sections": [
            ("What it&rsquo;s like", [
                "A small village at the end of the road below the Gavia Pass. Fewer people than Bormio, "
                "and a downhill piste that has hosted World Cup races.",
            ]),
            ("How we use it", [
                "A focused day on the mountain when Bormio is busy: long runs, short lift queues, lunch in the sun.",
            ]),
        ],
        "draft": [
            "Should we name the Deborah Compagnoni piste, and do we ski it as a group?",
        ],
    },
    "wines2whales": {
        "name": "Wines2Whales, South Africa",
        "tagline": "Three days of mountain biking from the Winelands to the coast.",
        "facts": [
            ("Where", "Western Cape, South Africa: from the Winelands near Somerset West to Hermanus"),
            ("What we do", "Mountain bike stage racing, in teams of two"),
            ("When", "We raced it in 2025 and plan to return"),
            ("Who it suits", "Riders ready for three long days in the saddle"),
        ],
        "sections": [
            ("What it&rsquo;s like", [
                "Wines2Whales crosses the mountains of the Western Cape "
                "through vineyards, fynbos and forest, and finishes in Hermanus, famous for its whales.",
                "The organisers, the culture and the people were exceptional.",
            ]),
            ("How we&rsquo;re approaching it", [
                "We&rsquo;re building the foundation to return stronger, with a bigger Winchester and Dolomites contingent. "
                "If you&rsquo;d like to be part of the next team, start riding with us now and tell us.",
            ]),
        ],
        "draft": [
            "Which year do we plan to return? Keep it vague, or name it?",
            "Link to the official race site? (We need to approve the domain.)",
        ],
    },
}

# Card names on the existing pages that should link to a place page.
LINKS = {
    "Queen Elizabeth Country Park": "qecp",
    "Surrey Hills": "surrey-hills",
    "Winchester": "winchester",
    "Valtellina, Alps": "valtellina",
    "Valtellina / Lake Como / Val di Mello": "valtellina",
    "Portland": "portland",
    "Swanage": "swanage",
    "Southampton Climbing Wall": "southampton-wall",
    "Valgerola / Val Tartano / Spluga / Maloja": "valtellina-ski-touring",
    "Backcountry Touring": "valtellina-ski-touring",
    "Lake Como": "lake-como",
    "Dolomites": "dolomites",
    "Bormio": "bormio",
    "Livigno": "livigno",
    "Santa Caterina": "santa-caterina",
}
