# 🚛 FryDay Films Road Atlas — Salina → Leesburg

An interactive moving-trip kit: a vintage road atlas, a spiral-bound "TripTik," and a full day-by-day itinerary for a 4-day / 3-night move from **Salina, KS** to **34407 Shadewood Circle, Leesburg, FL 34788**, towing a 2,300 lb T-bucket roadster.

**Route:** I-135 → I-35 → I-40 → I-22 → I-65 → US-231 → I-10 → I-75 (Exit 329) · ~1,555 mi · ~23.5 hrs · $0 tolls · chosen for easiest towing (avoids Monteagle Mountain & Atlanta).

## What's inside
| File | What it is |
|------|-----------|
| `index.html` | Landing page linking everything |
| `atlas.html` | Offline geographic route map — tap towns, zoom by day |
| `triptik.html` | Spiral-bound page-flipping drive guide with the T-bucket & roadside trivia |
| `itinerary.html` | Day-by-day plan, 3 hotels/night (Hotels.com links), gas, food, rest |
| `itinerary.pdf` | Printable version |
| `cost-tracker.xlsx` | Editable cost model (fuel + hotels), Hotels.com hyperlinks |
| `t-bucket.png` | The T-bucket vector (transparent) |
| `session-report.md` | Full plan, costs, July 3 vs July 10 comparison, GPS build plan |

## Everything runs in a browser — no install
All the HTML files are self-contained and work offline (the atlas even has the state shapes baked in). Just open `index.html`.

## Coming next: live GPS TripTik
`triptik.html` currently runs on a simulated drive. The plan is to swap the simulator for `navigator.geolocation` so the T-bucket follows your real position — hosted here on GitHub Pages (which provides the HTTPS that phones require for location). See `session-report.md` for the build steps.

---
*Built with Claude · FryDay Films Road Atlas Series · 2026*
