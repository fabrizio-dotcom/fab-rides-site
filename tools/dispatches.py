"""Dispatches for Fab Rides: stories, thank-yous and plans sent back from the places we ride, climb and ski.

One entry per dispatch; tools/build.py turns each into site/dispatch-<slug>.html and lists it on
site/dispatches.html. `draft` holds questions still open for Fabrizio. While any draft questions remain on a
page, tools/check.py fails, so a draft can't go live by accident. Delete the questions once he has answered them.

Only write what Fabrizio has said. No invented details, numbers, quotes or dates.
"""

DISPATCHES = {
    "darren": {
        "title": "Thank you, Darren",
        "tag": "Thank you",
        "tagline": "The mechanic who got my bikes ready for South Africa.",
        "summary": "Before we raced Wines2Whales, Darren got my bikes ready. This is a thank you that took too long.",
        "sections": [
            ("The bikes were ready", [
                'In 2025 a group of us raced <a href="place-wines2whales.html">Wines2Whales</a> in South Africa. '
                "Before we flew, Darren got my bikes ready.",
                "Darren runs an independent workshop. He was professional and kind, and he helped me put everything in order before the race.",
            ]),
            ("The thank you I owe him", [
                "I wanted to write this as soon as we got back. It took me too long.",
                "Darren, thank you, and sorry for the wait. If I can help you in return, I will.",
            ]),
        ],
        "draft": [
            "Has Darren seen this and agreed to be named? Add his surname, his workshop and a link only if he wants them. A link to a new website needs your approval.",
            "Your earlier draft also mentioned bringing your family to try cyclocross with Darren. It is left out for now. Add it back?",
            "Your earlier draft also described the race and what Darren checked on the bikes (distance, terrain, &ldquo;no mechanical issues&rdquo;). Those details did not come from you, so they are left out. Add the real ones if you want them.",
            "Date for the post, and is &ldquo;2025&rdquo; right for the race?",
            "Is Darren the mechanic the Ride page means by &ldquo;We know a great mechanic&rdquo;?",
        ],
    },
}

# Placeholders shown on the Dispatches page until there is something to publish.
COMING = [
    ("Social Field Notes", "Fab Riders, shorter",
     "A short, social take on Fab&rsquo;s Friday Field Notes, from our rides, crags and mountains. "
     "The full Field Notes stay on Fabrizio&rsquo;s own site."),
    ("Planning 2027 and 2028", "Trips",
     "Early ideas for the trips ahead, shared here before they become plans."),
]

INDEX_DRAFT = [
    "Name: &ldquo;Dispatches&rdquo; or &ldquo;Field Reports&rdquo;? The name sits in one line of the build file, so it is easy to change.",
    "The two &ldquo;Coming&rdquo; cards are placeholders. Is the wording right, and do you want both?",
    "Do you want a link to Dispatches on the Home page as well as in the menu?",
]
