# Bharat Impact Lab

### Nine focused products for everyday challenges across India

Bharat Impact Lab is a community-first portfolio of nine independent web apps. Each app starts with an everyday challenge and helps people take a practical next step: report water interruptions, understand air observations, compare farm sales, practice maths, organize care follow-ups, explore work pathways, plan for safety, trace waste handoffs, and prepare questions about public benefits.

The apps share an API and deployment foundation while keeping separate purpose, interface, workflow, API route, and SQLite collection. The long-term vision is a multilingual, low-bandwidth network helping communities and accountable local partners move from a clear report to a verified response.

> **Status:** Working prototypes for local exploration and small partner-led pilots. They are not production public services and do not connect to live government, health, employer, sensor, market, or emergency systems.

## The nine projects

| Project | What it helps with |
|---|---|
| **JalRakshak** | Captures water interruptions and local follow-up. A report is not a water quality test. |
| **SaansMap** | Records community air observations separately from official readings and partner sensors. |
| **KisanSetu** | Compares individual and pooled farm sale estimates after entered costs. |
| **SeekhoSaath** | Offers short foundational maths practice with immediate feedback. |
| **SwasthyaSetu** | Organizes anonymous clinic and refill follow-ups; it does not give clinical advice. |
| **KaamNirmaan** | Captures work pathway preferences; it does not show live verified vacancies. |
| **SurakshaSaathi** | Provides a discreet safety planning workflow; it does not contact anyone or dispatch help. |
| **SwachhChain** | Records sample waste handoffs; this is not proof of safe processing. |
| **HaqSaathi** | Prepares questions about public benefits; it does not determine eligibility. |

## Run locally

Install Python 3.9 or newer. On Windows, double-click `Start-Projects.bat`. On other platforms, run from the repository root:

```bash
python backend/app.py
```

Open `http://127.0.0.1:8000`. The prototype uses Python's standard library and SQLite; no database server or API key is needed. Each project has a separate SQLite file created under `backend/data/` when first used.

## Architecture

- `site/` contains the portfolio and nine distinct project experiences.
- `backend/app.py` serves the site and project API routes.
- `backend/schemas.py` validates each project's records.
- `netlify/functions/api-proxy.mjs` forwards same-origin requests to the hosted API.
- `netlify.toml` configures the static site; `render.yaml` configures the API and persistent disk.
- `docs/` contains the product vision, architecture, and pilot roadmap.

API routes use `GET /api/{project}/records` and `POST /api/{project}/records`. See `backend/README.md`, `docs/ARCHITECTURE.md`, and `docs/PILOT-ROADMAP.md`.

## Deploy

1. Deploy the API to Render using `render.yaml`.
2. Deploy the repository to Netlify using `netlify.toml`.
3. Set Netlify's `BACKEND_URL` to the Render service URL without a trailing slash, then redeploy.

Before a real pilot, add authentication, abuse controls, security and privacy review, backups, data retention and deletion policies, monitoring, and a named operator. Health and safety workflows need specialist governance and trusted local partners.

## Future direction

Build a network of small tools with reviewed local-language access, low-bandwidth and offline capture, clear evidence labels, accountable partner work queues, traceable status updates, and carefully de-identified community insights. Measure outcomes with communities: time to confirmed water repair, completed follow-ups, farm returns after costs, verified job placement, and safe material destinations.

AI may assist with reviewed translation or summaries of non-sensitive reports. It must not diagnose illness, declare water safe, invent benefit rules, certify employers, issue emergency alerts, or decide anyone's rights or access to services.

## Data and safety

Use fictional or non-sensitive details. There are no user accounts or encryption at rest; health and safety entries are stored as plain text. Do not enter patient details, safety plans, phone numbers, exact addresses, or identity documents. Delete the relevant local database file to remove demo records. Prototype observations and estimates are not independently verified.

## Contributing and license

See `CONTRIBUTING.md`. Released under the MIT License; see `LICENSE`.
