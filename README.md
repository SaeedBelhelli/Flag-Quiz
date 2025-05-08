My first coding project that I made during my CSP course on 4/29/2024
https://studio.code.org/projects/applab/eWD2LXYynDgCPdgjPLsP-eXWScu5jXMIEM_Qz6lG6fY
# Flag Quiz – Code.org App Lab

An interactive browser‑based game that teaches world flags. Built for Code.org’s **App Lab** environment.

---

## Features

| Mode               | What it Does                                                                                                                                              |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Quiz**           | Shows 15 random flags one by one. Select the correct country from a drop‑down. <br>+2 points per correct answer. Instant feedback and final score screen. |
| **Search / Learn** | Type a starting letter, pick a country from a filtered list, and display its flag.                                                                        |

Additional touches:

* Randomised order each play‑through (synchronised shuffle of flags + names)
* Tiered drop‑downs to filter by **tier** (enthusiast / mid‑range … ) and manufacturer (NVIDIA / AMD) – easy to adapt for other datasets
* Fully keyboard‑navigable UI and dark‑theme colours

---

## Running the App

1. Open **App Lab** at [https://code.org/educate/applab](https://code.org/educate/applab) and create a new project.
2. Copy‑paste the contents of `quiz.js` into the **Code tab**.
3. Add a data table named **“Countries and Territories”** with at least two columns:

   * **Country Name** – text
   * **Flag** – image URL
     (The original version uses the public UN dataset of 250+ countries.)
4. Build the screens referenced in code or import the provided screen design JSON.
5. Press **Run**.


---

## Customisation Ideas

* Change `countries.slice(0, 15)` in `shuffleCountriesAndFlags()` to adjust quiz length.
* Swap the data table for any other image‑and‑name pair (e.g. state flags, company logos).
* Replace the 3‑option drop‑down with multiple‑choice buttons or type‑in answer boxes.
* Add a timer, leaderboard, or streak bonus.

---

## License

MIT – use freely for class projects or personal learning.
