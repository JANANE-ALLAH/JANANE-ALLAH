# GitHub Profile Optimization Guide

A senior-developer playbook to restructure your GitHub presence for recruiters, collaborators, and long-term maintainability.

---

## 1\. Repository Organization

### 1.1 Naming Convention

Use **kebab-case**, lowercase, descriptive, and prefix-based names. Prefixes communicate purpose at a glance.

| Prefix | Meaning | Example |
| :---- | :---- | :---- |
| `app-` | Full applications | `app-task-manager` |
| `api-` | Backend / API services | `api-payments-service` |
| `web-` | Frontend / websites | `web-portfolio` |
| `lib-` | Reusable libraries / packages | `lib-react-hooks` |
| `cli-` | Command-line tools | `cli-image-resizer` |
| `lab-` | Experiments / sandboxes | `lab-rust-async` |
| `learn-` | Tutorials / coursework | `learn-systemdesign` |
| `template-` | Starter kits / boilerplates | `template-nextjs-stripe` |
| `docs-` | Documentation-only repos | `docs-architecture-notes` |

**Rules**

- Avoid version numbers in names (`my-app-v2`); use Git tags instead.  
- Avoid personal markers (`john-final-project`); be project-centric.  
- Match the repo name to the package/module name where possible.

### 1.2 Grouping Strategy

Pick **one** primary axis and stick to it. Recommended: **by status**, with **technology** shown via topics/badges.

Primary grouping (status):

   Production-ready  \-\> public, pinned, polished README, releases

   Active / WIP      \-\> public, "Status: WIP" badge, roadmap

   Experimental      \-\> public or private, lab- prefix

   Archived          \-\> archived flag enabled, frozen

   Private / Client  \-\> private, NDA-friendly stub on profile

Use **GitHub Topics** to expose secondary axes (technology, domain): `react`, `typescript`, `machine-learning`, `devops`, `open-source`. Topics are searchable and create a filter UX on your profile.

### 1.3 Pinned Repositories (max 6\)

Choose pins like a portfolio curator, not a historian. The set should answer: *what kind of engineer are you, and what's your range?*

A strong six:

1. **Flagship project** — your most complete app (full stack, deployed, screenshots).  
2. **Strongest backend / systems work** — shows depth.  
3. **Strongest frontend / UX work** — shows polish.  
4. **Open-source contribution or library** — shows you ship for others.  
5. **Domain specialty** — ML, data, devops, security, whatever sets you apart.  
6. **Recent project** — proves you're still building (commit within the last \~3 months).

If you have fewer than six strong projects, pin five — empty pins are better than weak ones.

---

## 2\. Completed Projects Management

### 2.1 How to Identify "Completed"

A project is **completed (production-ready)** when all are true:

- README is professional and current.  
- It builds and runs from a clean clone with documented steps.  
- There's a deployed demo, published package, or release tag.  
- Tests exist for critical paths (or a deliberate note explaining their absence).  
- License file is present.  
- No `TODO`/`FIXME` blocking core functionality.

Anything failing one of those belongs in **Active / WIP** or **Experimental**, not pinned as flagship.

### 2.2 Professional README Template

Save this as `README.md` at repo root.

\# Project Name

One-sentence elevator pitch. What it does, for whom, why it matters.

\[\!\[Build\](https://img.shields.io/github/actions/workflow/status/USER/REPO/ci.yml)\](...)

\[\!\[License\](https://img.shields.io/github/license/USER/REPO)\](LICENSE)

\[\!\[Release\](https://img.shields.io/github/v/release/USER/REPO)\](../../releases)

\[Live Demo\](https://demo.example.com)  ·  \[Documentation\](./docs)  ·  \[Report Bug\](../../issues)

\---

\#\# Screenshots

\!\[Dashboard view\](docs/images/dashboard.png)

\!\[Mobile view\](docs/images/mobile.png)

\#\# Features

\- Feature one — what it does, value to user.

\- Feature two — measurable outcome where possible ("reduces query time by 60%").

\- Feature three.

\#\# Tech Stack

\*\*Frontend:\*\* React, TypeScript, Tailwind CSS

\*\*Backend:\*\* Node.js, Express, PostgreSQL

\*\*Infra:\*\* Docker, GitHub Actions, AWS (ECS, RDS)

\*\*Testing:\*\* Vitest, Playwright

\#\# Architecture

Short paragraph \+ diagram (\`docs/architecture.png\`). Explain the \*why\*, not just the \*what\*.

\#\# Getting Started

\#\#\# Prerequisites

\- Node.js 20+

\- Docker 24+

\- A \`.env\` file (see \`.env.example\`)

\#\#\# Installation

\`\`\`bash

git clone https://github.com/USER/REPO.git

cd REPO

cp .env.example .env

npm install

npm run dev

### Running tests

npm test

npm run test:e2e

## Usage

Minimal example a reader can copy-paste and run.

import { Client } from "project-name";

const client \= new Client({ apiKey: process.env.API\_KEY });

await client.doThing();

## Roadmap

- [x] v1.0 — initial release  
- [ ] v1.1 — multi-tenant support  
- [ ] v2.0 — plugin API

## Contributing

See [CONTRIBUTING.md](http://./CONTRIBUTING.md).

## License

[MIT](http://./LICENSE) © Your Name

\#\#\# 2.3 The Required Sections, Ordered by Recruiter Attention

Recruiters skim top-down for \~15 seconds. Order matters:

1\. Title \+ one-line pitch (above the fold).

2\. Live demo link / screenshot.

3\. Features (bulleted, outcome-focused).

4\. Tech stack (scannable badges or grouped list).

5\. Getting started (proves it actually runs).

6\. Architecture / decisions (proves you think, not just code).

7\. License \+ contact.

\---

\#\# 3\. Folder Structure Inside Repositories

\#\#\# 3.1 Standard Layouts

\*\*Monorepo / full-stack web app\*\*

repo/ ├── apps/ │   ├── web/              \# frontend │   └── api/              \# backend ├── packages/             \# shared code │   ├── ui/ │   └── config/ ├── docs/ │   ├── architecture.md │   └── images/ ├── scripts/              \# dev/ops scripts ├── .github/ │   ├── workflows/        \# CI/CD │   ├── ISSUE\_TEMPLATE/ │   └── PULL\_REQUEST\_TEMPLATE.md ├── .env.example ├── .gitignore ├── CHANGELOG.md ├── CONTRIBUTING.md ├── LICENSE └── README.md

\*\*Library / package\*\*

repo/ ├── src/ ├── tests/ ├── examples/ ├── docs/ ├── .github/workflows/ ├── package.json (or pyproject.toml, Cargo.toml, ...) ├── CHANGELOG.md ├── LICENSE └── README.md

\*\*CLI tool\*\*

repo/ ├── src/ ├── bin/                  \# entrypoint(s) ├── tests/ ├── docs/ ├── .github/workflows/ ├── README.md └── LICENSE

\#\#\# 3.2 Files to Remove or Gitignore

Delete or ignore (do \*\*not\*\* commit):

\- \`node\_modules/\`, \`dist/\`, \`build/\`, \`.next/\`, \`target/\`, \`\_\_pycache\_\_/\`, \`.venv/\`

\- IDE folders: \`.vscode/\` (unless shared settings), \`.idea/\`

\- OS artifacts: \`.DS\_Store\`, \`Thumbs.db\`

\- Secrets: \`.env\`, \`\*.pem\`, \`\*.key\` (commit only \`.env.example\`)

\- Logs: \`\*.log\`, \`npm-debug.log\*\`

\- Dead code, commented-out blocks, scratch files (\`test.js\`, \`temp/\`)

A baseline \`.gitignore\` per ecosystem is at https://github.com/github/gitignore — copy and trim.

\#\#\# 3.3 Maintainability Best Practices

\- \*\*One repo, one purpose.\*\* Don't bundle unrelated experiments.

\- \*\*Document decisions, not just code.\*\* Use lightweight ADRs in \`docs/adr/\`.

\- \*\*Pin dependencies\*\* in lockfiles; commit them.

\- \*\*Add \`CODEOWNERS\`\*\* if you collaborate, even with one collaborator.

\- \*\*Keep PRs small\*\* and reference issues (\`Closes \#42\`).

\---

\#\# 4\. Profile README Optimization

Create a repo named exactly your \*\*GitHub username\*\* (e.g., \`janane/janane\`) with a \`README.md\` — it becomes your profile landing page.

\#\#\# 4.1 Template (modern, minimal)

\`\`\`markdown

\#\#\# Hi, I'm Janane 👋

Software engineer focused on \*\*\[your focus — e.g., full-stack web apps with TypeScript and cloud-native backends\]\*\*. I care about clean architecture, thoughtful UX, and shipping things that work.

\---

\#\#\#\# 🛠 Tech I work with

\*\*Languages:\*\* TypeScript · Python · Go

\*\*Frontend:\*\* React · Next.js · Tailwind

\*\*Backend:\*\* Node.js · FastAPI · PostgreSQL · Redis

\*\*Infra:\*\* Docker · GitHub Actions · AWS

\#\#\#\# 🚀 Featured projects

\- \*\*\[project-one\](https://github.com/janane/project-one)\*\* — One-line description. \*(Live demo)\*

\- \*\*\[project-two\](https://github.com/janane/project-two)\*\* — One-line description.

\- \*\*\[project-three\](https://github.com/janane/project-three)\*\* — One-line description.

\#\#\#\# 📫 Contact

\- Email: mohamedjanane147@gmail.com

\- LinkedIn: \[linkedin.com/in/your-handle\](https://linkedin.com/in/your-handle)

\- Portfolio: \[your-site.com\](https://your-site.com)

### 4.2 What to Avoid on the Profile README

- Walls of badges and trophies — they read as filler.  
- Animated GIFs longer than \~3 seconds.  
- Auto-generated stats blocks repeated three times.  
- Joke quotes that obscure who you are professionally.  
- Listing every language you've ever touched; list what you'd be hired for.

---

## 5\. Archiving & Cleanup

### 5.1 Decision Tree

For each repo, ask in order:

1. **Is it your work and reasonably presentable?** No → delete or make private.  
2. **Is it complete and unlikely to change?** Yes → **Archive** (keeps it visible, marks it frozen).  
3. **Is it actively maintained?** Yes → keep public, ensure README is current.  
4. **Is it a duplicate / earlier version?** Yes → archive the older one, link to the newer.  
5. **Is it half-finished and abandoned?** Be honest — either finish a v0.1 with a real README, or delete.

### 5.2 What to Archive vs. Delete

**Archive** when the project has value as a portfolio artifact (shipped feature, learning milestone, OSS contribution) but you won't maintain it. Add a banner to the README:

\> ⚠️ \*\*Archived.\*\* This project is no longer maintained. Kept for reference.

**Delete** when the repo is:

- A tutorial follow-along with no original work.  
- A failed experiment that doesn't even build.  
- A duplicate fork you never modified.  
- Coursework that doesn't reflect current ability.

### 5.3 Cleanup Checklist

For every repo you keep public:

- [ ] README updated, accurate, has screenshots.  
- [ ] LICENSE file present.  
- [ ] `.gitignore` clean; no secrets in history (use `git filter-repo` if needed).  
- [ ] Default branch is `main`.  
- [ ] Issues/PRs triaged or closed.  
- [ ] Topics added (3–6 relevant tags).  
- [ ] Description and website URL set in repo settings.  
- [ ] CI passing or removed if obsolete.

---

## 6\. Automation & Best Practices

### 6.1 GitHub Actions

Add a minimal CI workflow to every active repo. Example for a Node project:

\# .github/workflows/ci.yml

name: CI

on:

  push:

    branches: \[main\]

  pull\_request:

jobs:

  test:

    runs-on: ubuntu-latest

    steps:

      \- uses: actions/checkout@v4

      \- uses: actions/setup-node@v4

        with:

          node-version: 20

          cache: npm

      \- run: npm ci

      \- run: npm run lint

      \- run: npm test

      \- run: npm run build

Other workflows worth adding:

- **Dependabot** (`.github/dependabot.yml`) for automated dep updates.  
- **CodeQL** for security scanning on default branch.  
- **Release** workflow that publishes on tag push.  
- **Stale issues** bot for archived-track repos.

### 6.2 Versioning

Use **Semantic Versioning** (`MAJOR.MINOR.PATCH`):

- `MAJOR` — breaking changes.  
- `MINOR` — new functionality, backward-compatible.  
- `PATCH` — bug fixes, backward-compatible.

Tag releases (`git tag v1.2.0 && git push --tags`) and publish a GitHub Release with notes generated from `CHANGELOG.md`. Keep a `CHANGELOG.md` in the [Keep a Changelog](https://keepachangelog.com) format.

### 6.3 Commit Message Convention

Adopt **Conventional Commits**. It enables automated changelogs and reads well in `git log`.

\<type\>(\<scope\>): \<short summary\>

\<body — what and why, not how\>

\<footer — refs, breaking changes\>

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `build`, `ci`, `perf`.

Examples:

feat(auth): add Google OAuth provider

fix(api): handle empty pagination cursor

docs(readme): add architecture diagram

refactor(db): extract migration runner

BREAKING CHANGE: removes \`legacyAuth()\` — see MIGRATION.md.

Pair with [`commitlint`](https://commitlint.js.org/) \+ a Husky pre-commit hook to enforce.

### 6.4 Branching

Default to **trunk-based** with short-lived feature branches:

- `main` — always deployable.  
- `feat/<topic>`, `fix/<topic>` — merge via PR with at least one review (or self-review checklist on solo projects).  
- Delete branches after merge.

---

## Action Plan — Do These In Order

1. **Audit** every repo. Tag each as: Production / Active / Experimental / Archive / Delete.  
2. **Delete or archive** the bottom tier first — the cleanup makes everything else easier to evaluate.  
3. **Rename** survivors to the new convention; update remotes locally.  
4. **Standardize structure** in your top 6–10 repos (READMEs, `.gitignore`, LICENSE, CI).  
5. **Write your profile README** using the template in §4.  
6. **Pin** your final six.  
7. **Add CI \+ Dependabot** to every active repo.  
8. **Set a recurring 30-day review** to re-audit (calendar reminder).

When a recruiter lands on your profile, the first scroll should answer: *what does this person build, how well, and is it current?* Everything in this guide ladders up to that single question.  
