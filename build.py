# Builds the static pages from one shared shell so the header, footer and
# stylesheet stay identical across the site. Run: python3 build.py
# The output is plain HTML. Nothing on the live site depends on this script.

import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")
SITE = "https://jurongtownrotary.org"

NAV = [
    ("", "Home"),
    ("about/", "About us"),
    ("projects/", "What we do"),
    ("youth/", "Youth"),
    ("join/", "Join us"),
    ("partner/", "Partner"),
    ("contact/", "Contact"),
]

MARK = (
    '<svg width="40" height="40" viewBox="0 0 100 100" aria-hidden="true" focusable="false">'
    '<circle cx="50" cy="50" r="47" fill="#0067C8"/>'
    '<circle cx="50" cy="50" r="29" fill="none" stroke="#F7A81B" stroke-width="8"/>'
    '<circle cx="50" cy="50" r="8" fill="#F7A81B"/>'
    '<g stroke="#F7A81B" stroke-width="8"><line x1="50" y1="21" x2="50" y2="79"/>'
    '<line x1="21" y1="50" x2="79" y2="50"/></g></svg>'
)

SHELL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{site}/{slug}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Rotary Club of Jurong Town, Singapore">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{site}/{slug}">
<link rel="icon" href="{p}favicon.svg" type="image/svg+xml">
<!-- Fonts load from Google. See fonts/README.txt to serve them from this site instead. -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Open+Sans:wdth,wght@75..100,300..800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}assets/style.css">
</head>
<body>

<a class="skip" href="#main">Skip to content</a>

<div class="util">
  <div class="wrap">
    <span>Rotary International District 3310 &nbsp;|&nbsp; Chartered 11 June 1971</span>
    <span><a href="{p}contact/">Visiting Rotarian? Meeting details</a></span>
  </div>
</div>

<nav class="main">
  <div class="wrap">
    <a class="brand" href="{p}">
      {mark}
      <span><b>Rotary Club of Jurong Town</b><span>Singapore</span></span>
    </a>
    <button class="burger" aria-expanded="false" aria-controls="links">Menu</button>
    <div class="links" id="links">
{nav}
    </div>
  </div>
</nav>

<main id="main">
{body}
</main>

<footer>
  <div class="wrap">
    <div>
      <h4>Rotary Club of Jurong Town, Singapore</h4>
      <p style="color:#fff;font-size:18px;margin-bottom:12px">Service Above Self</p>
      <p class="small">2nd and 4th Tuesday of every month, 12.50 pm.<br>Tang Yun Restaurant, Level 2, The Tanglin Club, 5 Stevens Road, Singapore 257814.</p>
    </div>
    <div><h4>About</h4><a href="{p}about/">Our story</a><a href="{p}about/">Club leadership</a></div>
    <div><h4>What we do</h4><a href="{p}projects/">Projects</a><a href="{p}youth/">Interact and Rotaract</a><a href="{p}partner/">Partner with us</a></div>
    <div><h4>Get involved</h4><a href="{p}join/">Join us</a><a href="{p}contact/">Visit a meeting</a><a href="https://www.facebook.com/RCJTSingapore" rel="noopener">Facebook</a></div>
  </div>
  <div class="legal">
    <div class="wrap">
      <span>&copy; 2026 Rotary Club of Jurong Town, Singapore. Rotary marks used under licence from Rotary International.</span>
      <span><a href="{p}privacy/">Privacy notice (PDPA)</a></span>
    </div>
  </div>
</footer>

<script src="{p}assets/site.js"></script>
</body>
</html>
"""


def nav_html(prefix, current):
    rows = []
    for slug, label in NAV:
        cls = ' class="active"' if slug == current else ""
        rows.append('      <a href="%s%s"%s>%s</a>' % (prefix, slug, cls, label))
    return "\n".join(rows)


def write(slug, title, desc, body, in_nav=None):
    prefix = "" if slug == "" else "../"
    current = in_nav if in_nav is not None else slug
    html = SHELL.format(
        title=title, desc=desc, site=SITE, slug=slug, p=prefix,
        mark=MARK, nav=nav_html(prefix, current), body=body.strip(),
    )
    folder = OUT if slug == "" else os.path.join(OUT, slug.rstrip("/"))
    if not os.path.isdir(folder):
        os.makedirs(folder)
    with open(os.path.join(folder, "index.html"), "w") as f:
        f.write(html)
    print("wrote", slug or "/")


def banner(crumb, heading):
    return ('  <div class="banner"><div class="wrap"><p class="crumb">%s</p>'
            '<h1>%s</h1></div></div>\n' % (crumb, heading))


# ---------------------------------------------------------------- forms
# Both forms post to Web3Forms. Replace REPLACE_WITH_ACCESS_KEY in this file
# with the key emailed to the club, then run this script again. Until then the
# forms will show an error on submit rather than silently losing a message.
def form(idp, consent):
    return """
        <form class="form" action="https://api.web3forms.com/submit" method="POST">
          <!-- Get a free key at web3forms.com using the club enquiry address. -->
          <input type="hidden" name="access_key" value="REPLACE_WITH_ACCESS_KEY">
          <input type="hidden" name="subject" value="Website enquiry, Rotary Club of Jurong Town">
          <input type="hidden" name="from_name" value="RCJT website">
          <input type="checkbox" name="botcheck" class="hp" tabindex="-1" autocomplete="off">
          <div class="field"><label for="{i}name">Your name</label><input id="{i}name" name="name" type="text" autocomplete="name" required></div>
          <div class="field"><label for="{i}email">Your email</label><input id="{i}email" name="email" type="email" autocomplete="email" required></div>
          <div class="field"><label for="{i}subject">Subject</label><input id="{i}subject" name="enquiry_subject" type="text" required></div>
          <div class="field"><label for="{i}message">Your message</label><textarea id="{i}message" name="message" required></textarea></div>
          <label class="consent"><input type="checkbox" name="consent" value="yes" required> <span>{c}</span></label>
          <button class="btn btn-azure" type="submit">Send message</button>
        </form>
""".format(i=idp, c=consent)


# ---------------------------------------------------------------- home
home = """
  <div class="hero">
    <div class="wrap">
      <div>
        <h1>Founded by the people who built Jurong. <span class="hl">Still building.</span></h1>
        <p class="lede">Twenty two industrialists chartered this club on 11 June 1971, the fourth Rotary club in Singapore. Today we are business and professional leaders who meet twice a month and put those hours into service, at home and across the region.</p>
        <div class="hero-cta">
          <a class="btn btn-gold" href="join/">Join us</a>
          <a class="btn btn-ghost" href="projects/">See our work</a>
        </div>
      </div>
      <!-- IMAGE SLOT: main photograph. Replace this div with an <img class="media" src="img/hero.jpg" alt="..."> -->
      <div class="media"></div>
    </div>
  </div>

  <div class="meeting">
    <div class="wrap">
      <div>
        <span class="lbl">Next meeting</span>
        <span class="when" id="nextDate">Tuesday</span>
      </div>
      <p>12.50 pm, 2nd and 4th Tuesday of every month. Tang Yun Restaurant, Level 2, The Tanglin Club, 5 Stevens Road, Singapore 257814. Contact us for the venue or the online link.</p>
      <a class="btn btn-gold" href="contact/">Tell us you are coming</a>
    </div>
  </div>

  <div class="sec wrap">
    <div class="facts">
      <div class="fact"><b>1971</b><span>Chartered on 11 June, the fourth Rotary club in Singapore</span></div>
      <div class="fact"><b>22</b><span>Charter members, drawn from the pioneers of Jurong Industrial Estate</span></div>
      <div class="fact"><b>13</b><span>Consecutive years running a nursing award with our charity partner</span></div>
    </div>
  </div>

  <div class="sec grey">
    <div class="wrap">
      <div class="sechead"><h2>What we <span class="hl">do</span></h2></div>
      <div class="cards">
        <article class="card">
          <div class="media media-soft"></div>
          <div class="in"><span class="avenue">Community service</span><h3>The Happiness Fund</h3>
          <p>Built from a 2011 conference on the ageing workforce and later topped up by government. Youth groups draw on it to run projects with older adults.</p></div>
        </article>
        <article class="card">
          <div class="media media-soft"></div>
          <div class="in"><span class="avenue">Youth service</span><h3>Scholarships and study loans</h3>
          <p>Scholarships for primary school pupils, bursaries for tertiary institutions and interest free study loans for polytechnic students.</p></div>
        </article>
        <article class="card">
          <div class="media media-soft"></div>
          <div class="in"><span class="avenue">International service</span><h3>Matching grant projects</h3>
          <p>Work funded jointly with sister clubs overseas, including a school built in Qing Hai, China and wheelchairs for people with disabilities.</p></div>
        </article>
      </div>
      <p style="margin-top:26px"><a class="btn btn-outline" href="projects/">All our projects</a></p>
    </div>
  </div>

  <div class="sec wrap">
    <div class="two">
      <div>
        <h2>A club <span class="hl">worth joining</span></h2>
        <p>Rotarians provide humanitarian service, encourage high ethical standards in all vocations, and help build goodwill and peace in the world. Our members are a diverse group of professional and community leaders working on local and international needs.</p>
        <a class="btn btn-azure" href="join/">How to join</a>
      </div>
      <blockquote>Sustaining the ideal of service above self. Our members are our most important asset.</blockquote>
    </div>
  </div>
"""

# ---------------------------------------------------------------- about
about = banner("Home / About us", 'About the <span class="hl">club</span>') + """
  <div class="sec wrap">
    <div class="two">
      <div>
        <p class="lede">Rotary arrived in Singapore on 6 June 1930. As the Jurong Industrial Estate grew, a club drawing members from its pioneering industrialists became inevitable, and the Rotary Club of Jurong Town was chartered on 11 June 1971 with 22 charter members, the fourth Rotary club in Singapore.</p>
        <p>Our Rotarians are part of a diverse group of professional and community leaders working on local community and international service needs. Through the years the club has run projects across the five avenues of service: club, vocational, community, international and youth service.</p>
        <p>The challenge going forward is the same one it has always been: staying relevant to the community as that community changes, by sustaining a vibrant membership and attracting members who believe in living the ideal of service above self.</p>
      </div>
      <div class="tl">
        <div><b>1971</b><span>Chartered on 11 June with 22 charter members.</span></div>
        <div><b>1983</b><span>Sponsored the founding of a new Rotary club in Singapore.</span></div>
        <div><b>1992</b><span>A past president elected District Governor for District 3310.</span></div>
        <div><b>1996</b><span>First woman inducted as a member. Ten years later, the club elected its first woman president.</span></div>
        <div><b>2011</b><span>Age Friendly Workforce Asia raises the money behind the Happiness Fund.</span></div>
      </div>
    </div>
  </div>

  <!-- ============================================================
       CLUB LEADERSHIP
       Left out on purpose: no names were confirmed for this build.
       To add the section, delete this comment wrapper and fill in the
       names below. Repeat the <div> for each officer.

  <div class="sec grey">
    <div class="wrap">
      <div class="sechead"><h2>Club <span class="hl">leadership</span></h2></div>
      <div class="three">
        <div><h3>President</h3><p class="small muted">Name, and one line on their year in office.</p></div>
        <div><h3>Secretary</h3><p class="small muted">Name.</p></div>
        <div><h3>Treasurer</h3><p class="small muted">Name.</p></div>
      </div>
    </div>
  </div>

       ============================================================ -->

  <div class="sec grey">
    <div class="wrap">
      <div class="two">
        <div>
          <h2>Meet the <span class="hl">club</span></h2>
          <p>The best way to understand a Rotary club is to sit at the table. Visiting Rotarians and guests are welcome at our lunch meetings.</p>
          <a class="btn btn-azure" href="../contact/">Arrange a visit</a>
        </div>
        <blockquote>Service above self.</blockquote>
      </div>
    </div>
  </div>
"""

# ---------------------------------------------------------------- projects
projects = banner("Home / What we do", 'Our <span class="hl">projects</span>') + """
  <div class="sec wrap">
    <div class="sechead">
      <p class="lede">Since its inception the club has undertaken community service projects benefiting a wide spectrum of the community, locally and internationally. Our work sits under Rotary's five avenues of service.</p>
    </div>
    <div class="cards">
      <article class="card">
        <div class="media media-soft"></div>
        <div class="in"><span class="avenue">Community service</span><h3>The Happiness Fund</h3>
        <p>In 2011 the club organised Age Friendly Workforce Asia, a conference on issues facing the ageing workforce, and raised one hundred thousand dollars. Topped up by government, the fund now stands at one hundred and fifty thousand and is available to youth groups running intergenerational projects with older adults.</p></div>
      </article>
      <article class="card">
        <div class="media media-soft"></div>
        <div class="in"><span class="avenue">Vocational service</span><h3>Recognising the professions</h3>
        <p>A nursing award run with our charity partner for thirteen consecutive years, alongside long running recognition for committed workers in other professions including bus drivers and telephone operators.</p></div>
      </article>
      <article class="card">
        <div class="media media-soft"></div>
        <div class="in"><span class="avenue">Youth service</span><h3>Scholarships and study loans</h3>
        <p>Scholarships for primary school pupils, bursary awards for tertiary institutions, and interest free financial assistance loans for polytechnic students through the club's education fund. We also run annual career guidance seminars.</p></div>
      </article>
      <article class="card">
        <div class="media media-soft"></div>
        <div class="in"><span class="avenue">International service</span><h3>Matching grant projects</h3>
        <p>Projects funded jointly with our overseas sister clubs, including the building of a school in Qing Hai, China, and wheelchairs for people with disabilities in Singapore supported by sister clubs worldwide.</p></div>
      </article>
      <article class="card">
        <div class="media media-soft"></div>
        <div class="in"><span class="avenue">Community service</span><h3>Meals, mobility and care</h3>
        <p>Regular meals provided to homes for older adults, an ambulance donated to a home nursing charity, and assistance to students with hearing loss both locally and internationally.</p></div>
      </article>
      <article class="card">
        <div class="media media-soft"></div>
        <div class="in"><span class="avenue">Vocational service</span><h3>Business plan competition</h3>
        <p>A business plan writing competition backed by Rotarian mentors, encouraging entrepreneurship among young adults in Singapore.</p></div>
      </article>
    </div>
    <div class="two" style="margin-top:44px">
      <div>
        <h2>Bring us a <span class="hl">project</span></h2>
        <p>If your organisation is working on something we could help with, or you would like to fund a project, we would like to hear about it.</p>
        <a class="btn btn-outline" href="../partner/">Partner with us</a>
      </div>
    </div>
  </div>
"""

# ---------------------------------------------------------------- youth
youth = banner("Home / Youth", 'Youth <span class="hl">pathway</span>') + """
  <div class="sec wrap">
    <div class="sechead">
      <p class="lede">Rotary's youth programmes run in sequence. Students start in Interact, young professionals continue in Rotaract, and some later join us at the table.</p>
    </div>
    <div class="pathway">
      <div class="row">
        <span class="age">Interact &middot; 12 to 18</span>
        <div><h3>School based service clubs</h3>
        <p>The club is heavily involved in youth outreach. We support Interact Clubs at local institutions and run joint projects with them, including international experiences, an annual vocational seminar and vocational attachments.</p></div>
      </div>
      <div class="row">
        <span class="age">Rotaract &middot; 18 to 30</span>
        <div><h3>Young leaders taking action</h3>
        <p>Join the global movement of young leaders taking action to build a better world. Exchange ideas with leaders in your community and mobilise your friends to develop innovative solutions to the world's most pressing common challenges.</p></div>
      </div>
      <div class="row">
        <span class="age">Rotary &middot; any age</span>
        <div><h3>Members</h3>
        <p>Business and professional leaders who commit time, expertise and networks to service, locally and internationally.</p></div>
      </div>
    </div>
    <p style="margin-top:30px">
      <a class="btn btn-outline" href="../projects/">Youth projects we run</a>
      <a class="btn btn-azure" href="../contact/" style="margin-left:8px">Ask about Interact and Rotaract</a>
    </p>
  </div>
"""

# ---------------------------------------------------------------- join
join = banner("Home / Join us", 'Join <span class="hl">us</span>') + """
  <div class="sec wrap">
    <div class="two">
      <div>
        <p class="lede">Rotarians from any club around the world are warmly welcomed to join in our club meetings and activities.</p>
        <p><b>Membership is by invitation only.</b> To be a Rotary member, a prospective candidate is invited to attend club meetings and activities. The sponsor will submit the candidate's application to the club's Board of Directors for review. Transferring Rotarians are required to submit a letter of good standing from the prior Rotary club.</p>
        <p>Members are expected to attend scheduled club meetings and maintain a 50% attendance record. Missed meetings can be made up at any other Rotary clubs anywhere in the world or online. Members are required to pay a modest annual fee, which will include administrative costs of running the club and dues to district and Rotary International.</p>
        <p>If you like what we do and are interested to join us, send us your details and we will get back to you.</p>
""" + form("j", "I consent to the club contacting me about membership and storing my details for that purpose.") + """
        <!-- MEMBERSHIP BROCHURE
             When the club supplies the file, put it in /img/ (or a /docs/ folder)
             and uncomment the line below.
        <p class="small" style="margin-top:18px"><a href="../docs/membership-brochure.pdf">Download the membership brochure (PDF)</a></p>
        -->
      </div>

      <div>
        <div class="panel">
          <h3>Before you apply, come along</h3>
          <p class="small">Meetings are on the 2nd and 4th Tuesday of every month at 12.50 pm, at Tang Yun Restaurant, Level 2, The Tanglin Club, 5 Stevens Road, Singapore 257814.</p>
          <a class="btn btn-gold" href="../contact/">Ask about visiting</a>
        </div>
        <div class="deflist" style="margin-top:26px">
          <div><b>Attendance</b><span>Two lunch meetings a month, with a 50% attendance record expected.</span></div>
          <div><b>Missed a meeting</b><span>Make it up at any Rotary club in the world, or online.</span></div>
          <div><b>Cost</b><span>A modest annual fee covering club administration and dues to district and Rotary International.</span></div>
          <div><b>Transferring</b><span>Bring a letter of good standing from your previous club.</span></div>
        </div>
      </div>
    </div>
  </div>
"""

# ---------------------------------------------------------------- partner
partner = banner("Home / Partner", 'Partner <span class="hl">with us</span>') + """
  <div class="sec wrap">
    <div class="sechead">
      <p class="lede">Charities, community groups and companies work with us in three ways. Whichever fits, the first step is the same: tell us what you have in mind.</p>
    </div>
    <div class="three">
      <div><h3>Propose a project</h3><p class="small">Charities and community groups can bring us a need. Tell us who it serves, what it costs, and what changes if it works.</p></div>
      <div><h3>Sponsor the work</h3><p class="small">Companies fund specific projects and events, and we report back with outcomes rather than photographs alone.</p></div>
      <div><h3>Give</h3><p class="small">Contribute to a current appeal, or to The Rotary Foundation.
      <!-- Add a line here on tax deductibility once the club confirms its status. --></p></div>
    </div>
    <p style="margin-top:30px"><a class="btn btn-outline" href="../contact/">Get in touch</a></p>
  </div>
"""

# ---------------------------------------------------------------- contact
contact = banner("Home / Contact", 'Contact <span class="hl">us</span>') + """
  <div class="sec wrap">
    <div class="two">
      <div>
        <h2>Visit a <span class="hl">meeting</span></h2>
        <p>Rotarians from any club are welcome, and so are guests who want to see what we do before applying. Let us know which Tuesday suits you.</p>
        <div class="deflist">
          <div><b>When</b><span>2nd and 4th Tuesday of every month, 12.50 pm</span></div>
          <div><b>Where</b><span>Tang Yun Restaurant, Level 2, The Tanglin Club, 5 Stevens Road, Singapore 257814</span></div>
          <div><b>Online</b><span>Meetings are also held online. Contact us for the venue or the link.</span></div>
          <div><b>Enquiries</b><span>Send a message using the form and a member of the club will reply.</span></div>
        </div>
        <p style="margin-top:22px"><a class="btn btn-outline" href="https://www.google.com/maps/search/?api=1&amp;query=The+Tanglin+Club+5+Stevens+Road+Singapore+257814" rel="noopener">Open the venue in Maps</a></p>
      </div>
      <div>
        <h2>Send a <span class="hl">message</span></h2>
""" + form("c", "I consent to the club storing my details in order to reply to this enquiry.") + """
      </div>
    </div>
  </div>
"""

# ---------------------------------------------------------------- privacy
privacy = banner("Home / Privacy", 'Privacy <span class="hl">notice</span>') + """
  <div class="sec wrap">
    <div style="max-width:70ch">
      <p class="lede">This notice explains how the Rotary Club of Jurong Town handles personal data collected through this website, under Singapore's Personal Data Protection Act.</p>

      <!-- ============================================================
           DRAFT. The board needs to approve this wording and fill in the
           two items marked below before the site goes live.
           ============================================================ -->

      <h2>What we collect</h2>
      <p>When you send a message through a form on this site, we collect the name, email address, subject and message you provide. We do not collect anything else, and this site does not use advertising or tracking cookies.</p>

      <h2>Why we collect it</h2>
      <p>To reply to your enquiry, and where you have asked about membership, to follow up with you about joining the club.</p>

      <h2>How long we keep it</h2>
      <p>[TO CONFIRM: how long the club retains enquiries. A stated period, for example two years, is better than saying nothing.]</p>

      <h2>Who else sees it</h2>
      <p>Messages are delivered by a third party form service and sent to the club's enquiry address. They are not sold or shared for marketing.</p>

      <h2>Your rights</h2>
      <p>You can ask us what personal data we hold about you, ask us to correct it, or ask us to delete it.</p>

      <h2>Contact</h2>
      <p>[TO CONFIRM: the name of the club's data protection officer and the address enquiries should go to. The PDPA requires a designated contact.]</p>
    </div>
  </div>
"""

write("", "Rotary Club of Jurong Town, Singapore",
      "Chartered in 1971 by the pioneers of Jurong Industrial Estate. Business and professional leaders serving the community in Singapore and across the region. Meetings on the 2nd and 4th Tuesday of every month.",
      home)
write("about/", "About the club | Rotary Club of Jurong Town",
      "Chartered on 11 June 1971 with 22 charter members, the fourth Rotary club in Singapore. Our history, and what the club stands for.",
      about)
write("projects/", "Our projects | Rotary Club of Jurong Town",
      "The Happiness Fund, scholarships and study loans, matching grant projects overseas, and vocational awards. What the club does across Rotary's five avenues of service.",
      projects)
write("youth/", "Youth pathway | Rotary Club of Jurong Town",
      "Interact for students, Rotaract for young professionals, and Rotary membership. How young people get involved with the club.",
      youth)
write("join/", "Join us | Rotary Club of Jurong Town",
      "How Rotary membership works, what is expected of members, and how to start a conversation about joining the club.",
      join)
write("partner/", "Partner with us | Rotary Club of Jurong Town",
      "Propose a project, sponsor our work, or give. How charities, community groups and companies work with the club.",
      partner)
write("contact/", "Contact us | Rotary Club of Jurong Town",
      "Meeting day, time and venue, and a form to reach the club. Visiting Rotarians and guests are welcome.",
      contact)
write("privacy/", "Privacy notice | Rotary Club of Jurong Town",
      "How the club handles personal data collected through this website, under Singapore's Personal Data Protection Act.",
      privacy, in_nav="none")
