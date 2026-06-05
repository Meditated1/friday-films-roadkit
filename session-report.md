# 🚛 Moving Trip — Session Report
**FryDay Films · Salina, KS → Leesburg, FL**
Session date: June 4–5, 2026 · Move date: **July 10, 2026**

---

## 1. What we set out to do
Plan the full move: fastest/easiest route for a convoy towing the T-bucket, broken into 4 days / 3 nights, with gas, hotels, food, and rest stops — then make it fun, like an old AAA TripTik / Rand McNally atlas.

**Convoy:** 2018 Tacoma TRD Off-Road (towing a 2,300 lb T-bucket roadster) + 2024 Land Cruiser. One 10-month-old aboard. Staying in **Leesburg, FL** the first month before Winter Park.

---

## 2. The route decision (locked)
**Southern flat route — chosen for easiest towing.**

> I-135 → I-35 → I-40 → I-22 → I-65 → US-231 → I-10 → I-75 (Exit 329, Wildwood) → Leesburg

- **Destination:** 34407 Shadewood Circle, Leesburg, FL 34788 (first-month base) — via I-75 Exit 329 (Wildwood)
- **~1,555 miles · ~23.5 driving hours · $0 tolls**
- **Why this and not the standard route:** avoids Monteagle Mountain (I-24) — one of the steepest interstate grades in the country — plus the Chattanooga/North-Georgia climbs and Atlanta traffic. Costs only ~60–90 min more but is far easier on the Tacoma's brakes with the trailer. Toll-free into Leesburg via I-75 Exit 329 (no Florida Turnpike).

### The 4 days
| Day | Route | Miles | Hrs | Overnight |
|-----|-------|------:|----:|-----------|
| 1 | Salina → **Oklahoma City** | 290 | 4.5 | OKC (I-40 @ Meridian) |
| 2 | OKC → **Memphis** | 465 | 7 | Memphis EAST (I-40 Exit 16, not downtown) |
| 3 | Memphis → **Montgomery** | 330 | 5 | Montgomery (I-85 EastChase) |
| 4 | Montgomery → **Leesburg** 🏁 | 470 | 7 | home |

---

## 3. Costs (estimates)
- **Fuel (both vehicles): ~$645** — Tacoma towing ~$400 (~15 mpg), Land Cruiser ~$245 (~24.5 mpg). Budget $650–700.
- **Hotels (3 nts × 2 rooms): ~$796** at current default picks.
- **Tolls: $0**
- **Trip total (fuel + hotels): ~$1,441** (food/misc extra)
- Cheapest gas: **Oklahoma ($3.74)** and **Mississippi ($3.81)** — buy big there; top off before TN and FL.

---

## 4. Hotels — status: DEFAULTS SET, not yet booked
All Marriott/Hilton family, ~$120–150, trailer-friendly lots, **bookable on Hotels.com (use your points)**. Current defaults (one per night):

- **Night 1 – Oklahoma City:** Courtyard OKC Airport — $128 *(has bus/horse-trailer parking)*
  - alts: Home2 Suites OKC ($132, all-suite), Fairfield Inn & Suites OKC ($122)
- **Night 2 – Memphis East:** Hilton Garden Inn Wolfchase — $130 *(indoor pool)*
  - alts: Hampton Wolfchase ($130, patrolled lot, free breakfast), Courtyard Germantown ($125)
- **Night 3 – Montgomery:** Hampton Inn & Suites EastChase — $140 *(4.7★, best of trip, free breakfast)*
  - alts: Hilton Garden Inn Montgomery East ($125), Courtyard Carmichael ($120)

**Agreed workflow:** Thomas finalizes the 3 hotels → tells Claude → Claude locks them into all files (spreadsheet pick, atlas card, TripTik, totals). No auto-sync between Excel and the web files (not technically possible without a server).

**⚠️ Important booking notes:** confirm a crib/pack-n-play and trailer parking at each; book the Montgomery EastChase Hampton early (Saturday night).

---

## 5. Files delivered (all in the Movig folder)
1. **Atlas_Route_Map_Salina_to_Leesburg.html** — vintage Rand McNally-style geographic plate. Works **offline** (state shapes baked in). All gas (F) + rest (P) stops plotted & labeled. Tap a town for its index card (3 hotels, gas, food, rest, with Hotels.com links). Tap **D1–D4** to zoom into one day; the bottom totals recalc to that day only.
2. **Live_TripTik_Mockup.html** — spiral-bound TripTik booklet. Black binding rings, 5 stops per page, page-**flip** animation, the flamed **T-bucket** rolling the strip, "Day X of 4 / Stop Y of 16," "▸ X mi to next" on each line, and **📖 Roadside Trivia** tied to the area. FryDay Films stamp at the bottom. *(Simulated GPS — this is the skeleton of the real app.)*
3. **Move_Itinerary_Salina_to_Leesburg_2026.html** — interactive day-by-day itinerary; pick hotels (Hotels.com links), live cost totals.
4. **Move_Itinerary.pdf** — printable 3-page version for the truck.
5. **Move_Cost_Tracker.xlsx** — editable cost model; Hotels tab has clickable Hotels.com hyperlinks and a "Choose" column.
6. **t bucket_transparent.png** — the T-bucket vector with the checkerboard background removed (transparent), reusable anywhere.
7. **Trip_Session_Report.md** — this file.

---

## 6. 🎯 TOMORROW: Build the real GPS TripTik (the plan)
**Goal:** turn Live_TripTik_Mockup.html into a real app on Thomas's iPhone where the T-bucket follows your actual location and checks off stops as you pass them.

**Key facts established:**
- No dev kit / no paid server needed for the web version. (Native App Store app *would* need Xcode + $99/yr Apple Developer — that's a separate, bigger path.)
- iPhones only share GPS over **HTTPS**, so it must be hosted (not opened as a local file). **Free GitHub Pages** gives HTTPS automatically — and Thomas already uses GitHub.

**Build steps for tomorrow:**
1. Create a GitHub repo (e.g. `friday-films-triptik`), add the HTML as `index.html`.
2. Enable **GitHub Pages** → get the HTTPS URL.
3. Swap the simulate loop for **`navigator.geolocation.watchPosition()`**.
4. Convert live lat/lng → "miles along the route": project the GPS point onto the route polyline (we already have all the city lat/lngs in the file). That number drives everything that already works.
5. On iPhone: open the URL in Safari → **Add to Home Screen** → it behaves like an app.
6. (Optional later) cache for offline, wake-lock so the screen stays on, voice cue at each stop.

### 📝 Homework for Thomas (so we start fast)
- [ ] Confirm/sign in to a **GitHub account**; pick a repo name.
- [ ] **Finalize the 3 hotels** (or confirm the defaults) and send them to Claude.
- [ ] Decide: any **more trivia** or roadside spots you want added?
- [ ] Optional: check **trailer tire pressure** habit for July heat (noted for the trip itself).

---

## 6b. Alternate departure: July 3 vs July 10 (comparison only — not built)
Thomas asked how leaving **Fri July 3** instead of **Fri July 10** changes prices. Kept here for reference; not built into the files yet.

- **Dates:** Jul 3 puts you on the road **on July 4th itself** (Saturday) — driving OKC→Memphis and sleeping in Memphis the night of the 4th. Jul 10 is a normal post-holiday weekend.
- **Gas:** essentially a wash — maybe **+$10–25** over the busiest holiday days. Not a deciding factor.
  - ⚠️ Separate flag: current forecasts show **summer 2026 gas running much higher (~$4.50+/gal, summer forecast near $4.80)** than the ~$3.86 we used. Re-verify actual pump prices the week before departure regardless of date.
- **Hotels:** July 3–5 is the Independence Day weekend, and 2026 is the **250th anniversary** (extra demand). Our interstate hotels run roughly **+20–40%**, heaviest on **Sat July 4 (Memphis night)**.
  - Baseline (Jul 10): **~$796** (3 nts × 2 rooms)
  - Holiday (Jul 3): **~$950–$1,100** → about **$150–$320 more**, plus tighter availability (book earlier).
- **Traffic:** AAA forecasts **record July 4th travel (~61–72M)** — heaviest driving days of the year. Towing the trailer + baby through that is the biggest real cost.
- **Bottom line:** Plan B (Jul 3) ≈ **$160–$340 more** (almost all hotels) and a harder tow. Plan A (Jul 10) stays the easier, cheaper call. July 3 is doable if it fits life better — just book hotels sooner.
- **Labeling (if we build it later):** **Plan A · Jul 10 — Baseline** vs **Plan B · Jul 3 — Independence Day Weekend**; add a 2nd column / departure-date toggle in the spreadsheet and a date badge on the atlas + TripTik.

---

## 7. Open / parking lot
- Hotels not yet booked (defaults set).
- Decide departure date: **Jul 10 (baseline)** vs **Jul 3 (July 4th weekend, ~$160–340 more)** — see §6b.
- ✅ Leesburg destination address received & added everywhere: **34407 Shadewood Circle, Leesburg, FL 34788** (Drive-it map links now route to the door).
- "Day X of 4" auto-badge on the TripTik is done; optional auto-scroll polish could come later.
- Possible future: connect the spreadsheet, atlas, and TripTik to one shared data file once hosted (real-app territory).

*Built together, June 2026. One step at a time — you've got this. 🌿 — Claude*
