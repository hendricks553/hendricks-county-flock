"""Writes the five agency pages from one template so they stay consistent.
Output is plain HTML you can hand-edit afterward. Re-running overwrites them."""

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;700;900&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&family=IBM+Plex+Mono:wght@400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>
<div class="wrap">

<header>
  <div class="notice-bar">
    <span>Community Record &middot; Unofficial</span>
    <span>Hendricks Co., Indiana</span>
  </div>
  <nav class="main">
    <a href="index.html">Overview</a>
    <a href="towns.html" aria-current="page">By town</a>
    <a href="why.html">The case</a>
    <a href="act.html">What you can do</a>
    <a href="documents.html">Documents</a>
  </nav>

  <p class="crumb"><a href="towns.html">By town</a> / {crumb}</p>
  <h1>{h1}</h1>
  <p class="dek">{dek}</p>
</header>

<section>
  <h2>At a glance</h2>
  <div class="stats">
{stats}
  </div>
{glance_note}
</section>

<section>
  <h2>What is on the record <small>and what is not</small></h2>
  <div class="ledger">
{ledger}
  </div>
</section>

{body}

<section>
  <h2>Where to raise it</h2>
{meeting}
</section>

<div class="next">
  <a href="towns.html">&larr; All towns</a>
  <a href="act.html">File your own request &rarr;</a>
</div>

<footer>
  Not affiliated with any town, county, or law-enforcement agency. Nothing here alleges misuse by any local agency. Corrections and documents: <a href="mailto:hendricks553@proton.me">hendricks553@proton.me</a>
</footer>

</div>
</body>
</html>
"""


def stat(n, label, flag=False):
    cls = ' class="stat flag"' if flag else ' class="stat"'
    return f'    <div{cls}><span class="n">{n}</span><span class="l">{label}</span></div>'


def row(head, sub, mark, state):
    return (f'    <div class="ledger-row"><div class="q"><b>{head}</b>'
            f'<span>{sub}</span></div><span class="mark {state}">{mark}</span></div>')


PAGES = {}

# ----------------------------------------------------------------- AVON
PAGES['avon.html'] = dict(
    title="Avon | ALPRs in Hendricks County",
    desc="What is documented about Flock license plate readers in Avon, Indiana: a five-year auto-renewing contract, $15,000 a year, and an unanswered records request.",
    crumb="Avon",
    h1="Avon",
    dek="The largest mapped deployment of any town in the county, on a five-year contract that renews automatically. Avon links its transparency portal from the town website, which is more than most agencies do. A request for its use policy is still open.",
    stats="\n".join([
        stat("26", "cameras mapped in town"),
        stat("6", "cameras on the PD portal"),
        stat("$15k", "per year, Flock contract"),
        stat("343,911", "plate reads / 30 days"),
        stat("~14%", "flagged as hotlist hits"),
        stat("$75k", "over the five-year term"),
    ]),
    glance_note='<div class="note">The gap between 26 mapped and 6 on the portal has ordinary explanations. Cameras inside town limits can belong to the Sheriff\'s Office, to a neighboring agency, or to a private business or HOA that shares its feed with police. Worth asking rather than assuming.</div>',
    ledger="\n".join([
        row("Contract", "In the council agenda packet, 2023", "Public", "yes"),
        row("Pricing", "$15,000 a year, from the EDIT fund", "Public", "yes"),
        row("Written use policy", "Requested July 2026", "Pending", "wait"),
        row("Current invoices", "Requested July 2026", "Pending", "wait"),
        row("Sharing list", "Portal does not include one", "Not published", "wait"),
        row("Council vote on the agreement", "Appears in a packet, vote not confirmed", "Unclear", "wait"),
    ]),
    body="""
<section>
  <h2>What the contract shows</h2>
  <ul>
    <li><strong>It renews automatically.</strong> After the initial 60-month term signed in 2023, running into roughly 2028, the agreement rolls over in 24-month increments unless either side gives notice 30 days before the term ends. Worth knowing when the notice window falls.</li>
    <li><strong>The money.</strong> $15,000 a year for six cameras, $75,000 over five years, paid out of the town's economic development income tax fund. The 2023 deal locked in $2,500 per camera as Flock's list price moved to $3,000.</li>
    <li><strong>Network sharing is a checkbox.</strong> Flock's own proposal describes statewide and national sharing as something an agency opts into. A council can direct that setting without cancelling anything.</li>
    <li><strong>Searches go beyond plates.</strong> The system filters on make, decals, bumper stickers, and roof racks. A car can be located without its plate ever being read.</li>
    <li><strong>The real terms are off-site.</strong> The signed order form incorporates Flock's terms of service by web address. The full legal agreement is not in the council packet.</li>
  </ul>
</section>

<section>
  <h2>Still open</h2>
  <p>A records request for the use policy and current invoices was filed in July 2026 and is still pending. Requests take time, and a summer backlog is a normal reason for one to sit. This page will be updated when the documents arrive.</p>
  <div class="note">If you have filed a request with Avon and heard back, the documents belong on this page. Send them along.</div>
</section>
""",
    meeting="""  <div class="panel">
    <p><strong>Avon Town Council</strong> meets the 2nd and 4th Thursday of the month at 7 PM, with a work session before the second meeting. Town Hall, <a href="https://maps.google.com/?q=6570+E+US+Highway+36,+Avon,+IN+46123" target="_blank" rel="noopener">6570 E US Highway 36</a>.</p>
    <p class="fine">Confirm the date and the public comment procedure against the posted agenda before making the drive. Agendas usually go up about a week out.</p>
  </div>
  <h3>Worth asking</h3>
  <ul>
    <li>Which cameras inside town limits are the town's, and which belong to another agency or a private owner?</li>
    <li>Has the department turned on the shorter retention window Flock made default in August, or kept the longer one?</li>
    <li>Is there a written use policy, and if so, did the council vote on it?</li>
    <li>The contract auto-renews. When does the next notice window open, and will the renewal be a public agenda item?</li>
  </ul>
""",
)

# ------------------------------------------------------------ BROWNSBURG
PAGES['brownsburg.html'] = dict(
    title="Brownsburg | ALPRs in Hendricks County",
    desc="What is documented about Flock license plate readers in Brownsburg, Indiana: roughly $183,700 paid since 2021, and no written use policy.",
    crumb="Brownsburg",
    h1="Brownsburg",
    dek="The most completely documented deployment in the county, because the town answered its records request in full and promptly. What came back is a stack of contracts and invoices, and confirmation that no written use policy exists.",
    stats="\n".join([
        stat("20", "cameras mapped in town"),
        stat("16", "cameras under contract"),
        stat("$40k", "per year, current agreement"),
        stat("$183.7k", "paid to Flock since 2021"),
        stat("$201.3k", "value of the five-year deal"),
        stat("None", "written use policy"),
    ]),
    glance_note='',
    ledger="\n".join([
        row("Contract", "2023 agreement, produced in full", "Public", "yes"),
        row("Invoices", "2024 and 2025, produced in full", "Public", "yes"),
        row("Written use policy", "Request fulfilled without one", "None exists", "no"),
        row("Sharing list", "No portal published", "Not published", "wait"),
        row("Council vote on the agreement", "Order form signed by the Chief", "Unclear", "wait"),
        row("Retention window", "30 days, stated at a council meeting", "Public", "yes"),
    ]),
    body="""
<section>
  <h2>What the records show</h2>
  <ul>
    <li><strong>No use policy exists.</strong> A request asking for any policy, ordinance, or written guidance governing the cameras came back with contracts and invoices only. The cameras run on the vendor's terms of service and nothing the town adopted.</li>
    <li><strong>Roughly $183,700 paid since 2021.</strong> Twelve cameras in 2021 at $30,000 a year, two more added in 2022 on an invoice annotated "(Walmart)," then a 2023 expansion to sixteen cameras at $40,000 a year under a $201,300 five-year agreement with 24-month auto-renewals.</li>
    <li><strong>Billed under vehicle and equipment repairs.</strong> The budget line a resident would have to find does not say cameras or Flock, which makes the spending hard to spot even when it is fully public.</li>
    <li><strong>Signed by the Chief of Police.</strong> The order form lists the police department as the customer. Whether the council voted on the agreement is an open question.</li>
    <li><strong>Sharing is in the base package.</strong> The signed FlockOS tier includes statewide and nationwide lookup, direct sharing with surrounding jurisdictions, and access to privately owned Flock cameras that have been shared with the department.</li>
  </ul>
  <p><a href="documents.html">All Brownsburg documents &rarr;</a></p>
</section>

<section>
  <h2>What happened when the council was asked</h2>
  <p>A resident raised these points during public comment at the August 13, 2026 meeting: the documented misuse record, the hit rates published on neighboring agencies' portals, the absence of any written policy, and a request to end or limit the contract.</p>
  <p>The response, in summary: the police chief pointed to a recently solved robbery as an example of the system working. The council president noted that data is held for 30 days. A member of the public offered the argument that phones already track everyone. The specific figures raised were not contested.</p>
  <div class="note">The 30-day answer is worth holding onto, because Flock moved its own default to 7 days in August 2026. Whether the department has since changed its window is an open and easily answered question.</div>
</section>
""",
    meeting="""  <div class="panel">
    <p><strong>Brownsburg Town Council</strong> meets the 2nd and 4th Thursday of the month at 7 PM, <a href="https://maps.google.com/?q=61+N+Green+St,+Brownsburg,+IN+46112" target="_blank" rel="noopener">61 N. Green St.</a></p>
    <p class="fine">Confirm the date and the public comment procedure against the posted agenda before making the drive.</p>
  </div>
  <h3>Worth asking</h3>
  <ul>
    <li>The records confirm no written use policy. Will the council adopt one?</li>
    <li>Retention was described as 30 days. Flock's default is now 7. Which is the department running?</li>
    <li>Who reviews the search logs, and has anyone ever done so?</li>
    <li>The agreement auto-renews in 24-month increments. Will the next renewal come to a public vote?</li>
    <li>Why is a surveillance contract billed as vehicle and equipment repairs?</li>
  </ul>
""",
)

# --------------------------------------------------------------- DANVILLE
PAGES['danville.html'] = dict(
    title="Danville | ALPRs in Hendricks County",
    desc="A records request about Flock license plate readers in Danville, Indiana was denied on a commercial-purpose presumption, then went unanswered.",
    crumb="Danville",
    h1="Danville",
    dek="The smallest deployment in the county and the least documented. A records request was denied on a commercial-purpose basis, and the follow-up referral to the police department is still open.",
    stats="\n".join([
        stat("3", "cameras mapped in town"),
        stat("23.9", "cameras per 100k residents"),
        stat("?", "annual cost"),
        stat("?", "contract term"),
        stat("?", "retention window"),
        stat("Jul 27", "date referred to the PD"),
    ]),
    glance_note='<div class="note">Each question mark above is a document that has not been produced yet. Danville is the county seat, and it is the only town here where the basic terms are still unknown.</div>',
    ledger="\n".join([
        row("Contract", "Requested, not produced", "Denied", "no"),
        row("Payment records", "Requested, not produced", "Denied", "no"),
        row("Written use policy", "Requested, not produced", "Denied", "no"),
        row("Sharing list", "No portal published", "Not published", "wait"),
        row("Participation in the Flock network", "Listed on Plainfield's sharing lists", "Confirmed", "yes"),
        row("Public comment procedure", "Form at the door, 3 minutes", "Confirmed", "yes"),
    ]),
    body="""
<section>
  <h2>The denial</h2>
  <p>A request for Danville's Flock contract, payment records, and use policy was denied in July 2026. The stated basis was a provision of Indiana's Access to Public Records Act that lets an agency decline records it believes will be used for commercial purposes.</p>
  <p>The requester had already stated in writing that the records were for personal, non-commercial civic use, and confirmed it again after the denial. The request was then forwarded from the clerk-treasurer's office to the police department on July 27, 2026, and remains open.</p>
  <div class="note">Indiana's Act does not set a hard deadline. The Public Access Counselor's office uses roughly 30 days from receipt as a working benchmark, weighed against how large the agency and the request are.</div>
</section>

<section>
  <h2>Why the commercial-purpose basis matters to you</h2>
  <p>The provision exists mainly to stop bulk resale of records like property and licensing data. It was read here to cover a resident asking about camera contracts, which is a broader reading than the exemption is usually given.</p>
  <p>The practical takeaway for anyone filing anywhere: state your purpose inside the request itself. One sentence settles the question before it comes up. The <a href="act.html">request template</a> on this site already includes it.</p>
</section>

<section>
  <h2>What is known anyway</h2>
  <p>Danville's own records are not available yet, but Plainfield publishes its sharing lists and Danville appears on them. That places the town's cameras inside Flock's sharing network rather than a closed local system, which means reads collected here are reachable by agencies outside Indiana.</p>
  <p>Three cameras is a small deployment, and that cuts both ways. It is a modest thing to end, and a modest thing to write a policy for.</p>
</section>
""",
    meeting="""  <div class="panel">
    <p><strong>Danville Town Council</strong> meets the 1st and 3rd Wednesday of the month at 7 PM, Town Hall, <a href="https://maps.google.com/?q=49+N+Wayne+St,+Danville,+IN+46122" target="_blank" rel="noopener">49 N. Wayne St.</a></p>
    <p><strong>Public comment is confirmed:</strong> fill out the request-to-speak form at the door before 7 PM. Three minutes per speaker.</p>
  </div>
  <h3>Worth asking</h3>
  <ul>
    <li>What does the town pay for its license plate readers, and out of which fund?</li>
    <li>Is there a written use policy, and did the council adopt it?</li>
    <li>What is the town's standard for applying the commercial-purpose exemption to a resident's request?</li>
    <li>The request was referred to the police department on July 27. What is its status?</li>
  </ul>
""",
)

# -------------------------------------------------------------- PLAINFIELD
PAGES['plainfield.html'] = dict(
    title="Plainfield | ALPRs in Hendricks County",
    desc="Plainfield, Indiana is the only local town with an adopted ALPR policy and the only one publishing its Flock sharing lists. It also runs a second camera vendor.",
    crumb="Plainfield",
    h1="Plainfield",
    dek="The most transparent agency in the county, and the most informative because of it. Plainfield publishes what the others do not: a sharing network spanning thirty-odd states, a hit rate above one in five, and an adopted policy you can actually read.",
    stats="\n".join([
        stat("22", "cameras mapped in town"),
        stat("24", "cameras on the PD portal"),
        stat("525,866", "plate reads / 30 days"),
        stat("116,210", "hotlist hits in the same period"),
        stat("~22%", "of reads flagged as hits"),
        stat("$28k", "per year to a second vendor"),
    ]),
    glance_note='',
    ledger="\n".join([
        row("Contract", "Flock agreements 2021 to 2026, produced", "Public", "yes"),
        row("Invoices and purchase orders", "Produced", "Public", "yes"),
        row("Written use policy", "Lexipol Policy 427, adopted", "Exists", "yes"),
        row("Sharing list", "Published in full on the portal", "Public", "yes"),
        row("Second vendor", "Traffic Optics, separate contract", "Public", "yes"),
        row("Independent audit of searches", "Policy provides for internal review", "Internal only", "wait"),
    ]),
    body="""
<section>
  <h2>The policy, and its limits</h2>
  <p>Plainfield is the only local department shown to have a written ALPR policy: Lexipol Policy 427, a model policy widely adopted by agencies nationwide. Having one puts Plainfield ahead of its neighbors, and it is the reason this page can say anything specific at all. What the policy contains is the next question.</p>
  <ul>
    <li><strong>No suspicion required to run a search.</strong> The policy does not condition a database query on reasonable suspicion of a crime.</li>
    <li><strong>Auditing is self-auditing.</strong> Review of search logs is handled inside the department. No outside body reviews who searched what.</li>
    <li><strong>It is a model policy rather than a local one.</strong> A widely used template adopted administratively is not the same thing as rules a council debated and voted on, though it is a reasonable starting point for one.</li>
  </ul>
  <div class="note">None of this makes Plainfield the outlier. It makes Plainfield the only place the question can be examined, because it is the only agency that produced a policy to examine.</div>
</section>

<section>
  <h2>The sharing lists</h2>
  <p>Plainfield is the only local portal that publishes who can search its data, and those lists answer a question the other agencies leave open. Every other Hendricks County agency appears on them: the Sheriff's Office, Avon, Brownsburg, Danville, Pittsboro, and Lizton. <strong>All six local deployments participate in the sharing network. Only Plainfield says so publicly.</strong></p>
  <details>
    <summary>How far it reaches</summary>
    <div class="inner">
      <p>Plainfield's data is searchable by agencies across more than 30 states, including federal entities such as the US Postal Inspection Service and Wright-Patterson Air Force Base, state corrections and revenue departments as far away as Alabama, and prosecutors' offices from New Jersey to California.</p>
      <p>The lists also carry stale entries, including one labelled as a dead or old Indiana department. Access hygiene is its own question: who removes an agency from the list when it stops being an agency?</p>
    </div>
  </details>
  <p class="fine">One query through this network reaches cameras far outside Indiana, run under the rules of the agency doing the searching rather than the rules here. Flock does not sell the data. It does not need to.</p>
</section>

<section>
  <h2>A second vendor nobody was talking about</h2>
  <p>Alongside Flock, Plainfield holds a separate contract with Traffic Optics worth roughly $28,000 a year. Different company, different product, its own terms. It surfaced through the records rather than through any public discussion this site is aware of.</p>
  <p>The lesson generalizes: asking a town about "the Flock contract" can miss what it runs. Records requests should ask about license plate readers and camera systems generally, not one vendor by name.</p>
</section>

<section>
  <h2>About that hit rate</h2>
  <p>Roughly 22% of plate reads are flagged as hotlist hits, the highest of the three local portals that publish a rate. That is more than one read in five.</p>
  <p>A hit is not a crime and not an arrest. It means a plate matched a list. Lists include stolen vehicles, but also expired registrations, warrants for unrelated matters, and entries other agencies added. The published numbers do not say how many hits were wrong, and they do not say how many produced a traffic stop. Those are the two numbers a resident would actually want.</p>
</section>
""",
    meeting="""  <div class="panel">
    <p><strong>Plainfield Town Council</strong> meets the 2nd and 4th Monday of the month at 7 PM, Civic Center Council Chambers, <a href="https://maps.google.com/?q=206+W+Main+St,+Plainfield,+IN+46168" target="_blank" rel="noopener">206 W. Main St.</a></p>
    <p class="fine">Confirm the date and the public comment procedure against the posted agenda before making the drive.</p>
  </div>
  <h3>Worth asking</h3>
  <ul>
    <li>Policy 427 does not require reasonable suspicion for a search. Would the council consider adding that requirement?</li>
    <li>Who audits the search logs, how often, and has any audit ever been reviewed outside the department?</li>
    <li>Of 116,210 hits in thirty days, how many were false, and how many led to a stop?</li>
    <li>Would the town consider narrowing its sharing list, as Bloomington did before ending its contract?</li>
    <li>What does the Traffic Optics system collect, and how long is that data kept?</li>
  </ul>
""",
)

# ----------------------------------------------------------------- SHERIFF
PAGES['sheriff.html'] = dict(
    title="Hendricks County Sheriff | ALPRs in Hendricks County",
    desc="The Hendricks County Sheriff's Office runs the county's largest and busiest ALPR deployment. No records request has been filed.",
    crumb="County Sheriff",
    h1="Hendricks County Sheriff",
    dek="The busiest deployment in the county by a wide margin, covering the roads between every town on this site. It is also the least examined: no records request has been filed, and the portal omits the sharing lists.",
    stats="\n".join([
        stat("19", "cameras on the portal"),
        stat("779,097", "plate reads / 30 days"),
        stat("54,356", "hotlist hits in the same period"),
        stat("~7%", "of passing cars flagged"),
        stat("47%", "of all reads counted countywide"),
        stat("None", "records requests filed yet"),
    ]),
    glance_note='<div class="note">Nearly half of every plate read documented in this county comes from the Sheriff\'s cameras, and less is known about them than about any town deployment. Not because anyone refused, but because nobody has asked yet. This is the largest single gap in the record.</div>',
    ledger="\n".join([
        row("Contract", "Never requested", "Unknown", "wait"),
        row("Payment records", "Never requested", "Unknown", "wait"),
        row("Written use policy", "Never requested", "Unknown", "wait"),
        row("Sharing list", "Portal does not include one", "Not published", "wait"),
        row("Participation in the Flock network", "Listed on Plainfield's sharing lists", "Confirmed", "yes"),
        row("Transparency portal", "Published, surfaced by volunteers", "Public", "yes"),
    ]),
    body="""
<section>
  <h2>What the portal says</h2>
  <p>The Sheriff's Office publishes a Flock transparency portal, though it was located by volunteers rather than linked from the county's own site. It reports 19 cameras, 779,097 plate reads in a thirty-day window, and 54,356 hotlist hits, a rate near 7%.</p>
  <p>The portal does not include a sharing list. Plainfield's does, and the Sheriff's Office appears on it, so participation in the network is established. The scope of it is simply not published.</p>
  <p><a href="https://transparency.flocksafety.com/hendricks-county-in-so" target="_blank" rel="noopener">Hendricks County Sheriff transparency portal &rarr;</a></p>
</section>

<section>
  <h2>The gap</h2>
  <p>Every town page on this site rests on documents somebody requested. Nobody has requested the Sheriff's yet, so the contract value, the term, the renewal structure, the funding source, and whether a written use policy exists are all still unknown for the largest deployment in the county.</p>
  <p>A county-level request is filed the same way as a town one. The <a href="act.html">template</a> works unchanged. If you file, send what comes back.</p>
</section>
""",
    meeting="""  <div class="panel">
    <p>County-level decisions run through the <strong>Board of Commissioners</strong> and the <strong>County Council</strong> rather than a town council. Meeting schedules, agendas, and public comment procedures are posted at <a href="https://www.co.hendricks.in.us/" target="_blank" rel="noopener">the county's website</a>.</p>
    <p class="fine">Confirm the current schedule and comment procedure before attending. This site does not list county meeting dates because they have not been verified.</p>
  </div>
  <h3>Worth asking</h3>
  <ul>
    <li>What does the county pay for its plate readers, on what term, and from which budget line?</li>
    <li>Is there a written use policy, and did the commissioners or council adopt it?</li>
    <li>Would the Sheriff's Office consider publishing its sharing list, as Plainfield does?</li>
    <li>Which of Flock's August 2026 settings has the office adopted, including the shorter retention default?</li>
  </ul>
""",
)


for filename, d in PAGES.items():
    with open(filename, "w") as f:
        f.write(TEMPLATE.format(**d))
    print("wrote", filename)
