# Projects
This repository indexes the coding projects I've worked on throughout my Computer Engineering studies, alongside sanitized showcase repos for coursework originally hosted in private university/course organizations. Real credentials, private course materials, and graded solution code for assignments that get reused across semesters have been removed or redacted from those showcases — see each repo's README for specifics.

# Index
Projects are listed in reverse chronological order, most recent first. See each project's own README for full details.

## IT Project Management (IIC3113) — Planificador Académico UC
A 7-person group project run under full PMBOK project management practices: an AI-assisted academic planner that extracts evaluation dates from uploaded course PDFs (via LLM), surfaces them on a calendar alongside class schedules, sends email reminders, and offers a conversational study-planning assistant. **My role was Risk Analyst** — I authored the project's risk register (identification, probability/impact scale, prioritization matrix), which correctly flagged the two risks that materialized during execution and were later resolved via formal change requests. The product itself was built by teammates in backend/frontend roles. At close, the project delivered 100% of its (re-scoped) approved scope with a CPI of 1.02 and an SPI of 1.11, six days ahead of schedule and under budget.
- [Frontend showcase](https://github.com/sebastianval22/planificador-uc-frontend-showcase)
- [Backend showcase](https://github.com/sebastianval22/planificador-uc-backend-showcase)

## Software Engineering (IIC2154) — GeriaPOP
A capstone-style group project built in collaboration with healthcare professionals from Red de Salud UC CHRISTUS: an offline-first geriatric screening platform digitizing validated clinical tests (Mini-Cog for cognitive impairment, MNA for nutritional risk, CFS for frailty). The team split into backend, mobile, and frontend; **I focused on the mobile app** (React Native/Expo, WatermelonDB offline-first sync). The backend is included here as system context since the mobile client depends on it directly.
- [Mobile showcase](https://github.com/sebastianval22/geriapop-mobile-showcase) — my primary contribution
- [Backend showcase](https://github.com/sebastianval22/geriapop-backend-showcase)

## Software Architecture (IIC2173)
A group project building a real-time property auction marketplace with a microservices architecture: a Koa/Sequelize API, an independently-deployed JWT auth service with refresh-token rotation, an MQTT-driven real-time layer, WebPay Plus payments, and a serverless (AWS Lambda) PDF receipt generator — plus a React frontend consuming all of it live. Includes CI/CD pipelines, automated testing, and New Relic monitoring.
- [Backend showcase](https://github.com/sebastianval22/arquisis-backend-showcase)
- [Frontend showcase](https://github.com/sebastianval22/arquisis-frontend-showcase)

## Data Mining (IIC2433)
A group project (four members) predicting a footballer's market value from performance, club, and demographic data, using a public ~30,000-player, 400,000-valuation Transfermarkt dataset. Compares a linear regression baseline against Random Forest and KNN models (with PCA and hyperparameter tuning), aiming to support scouting and transfer decisions by surfacing undervalued players.
[Go to showcase](https://github.com/sebastianval22/el-algoritmo-del-gol)

## Data Structures and Algorithms (IIC2133)
Individual assignments from a data structures & algorithms course. Source repositories are private to the course; the links below are sanitized showcases with the graded algorithm implementations redacted (see each repo's README).

### Assignment 0 — Arrays, Pointers & Memory Management
A pet-store inventory simulation in C, focused on designing array-based data structures and managing dynamic memory (`malloc`/`realloc`/`free`) correctly by hand.
[Go to showcase](https://github.com/sebastianval22/iic2133-t0-showcase)

### Assignment 1 — Min-Max Heaps & Linear Sorting
Priority-queue-style event simulation using a Min-Max Heap for O(1) median/min/max access, plus a two-key stable sort built from Counting Sort.
[Go to showcase](https://github.com/sebastianval22/iic2133-t1-showcase)

### Assignment 2 — Search Trees & Hashing
Binary Search Trees and a KD-tree for attribute and 2D geometric range queries, plus a hash table with chaining and dynamic resizing for O(1) average lookups.
[Go to showcase](https://github.com/sebastianval22/iic2133-t2-showcase)

### Assignment 3 — Graph Algorithms
Kruskal's Minimum Spanning Tree with a Disjoint-Set (Union-Find), and a greedy algorithm for a wait-time minimization problem.
[Go to showcase](https://github.com/sebastianval22/iic2133-t3-showcase)

## Detailed Design of Software (IIC2113)
A console-based simulation of *Fire Emblem Heroes*' turn-based tactical combat system in **C#**, focused on applying detailed object-oriented design (Strategy/Factory patterns) to a genuinely complex rules engine of composable unit skills, conditions, and damage effects. Since this course reuses the same project across semesters, the exact numeric formulas behind each skill have been redacted from the public repo — the design itself is intact.
[Go to repository](https://github.com/sebastianval22/Proyecto_Fire-Emblem_DDS)

## Web Development — TicTacGoal
A football-themed reimagining of Tic-Tac-Toe: to claim a square, a player must name a real footballer matching that row's and column's attributes (nationality, club, position). Supports local, bot, and real-time online multiplayer, with user accounts and match history. Source repositories are private to the course; the links below are sanitized showcases (see each repo's README for current live-deployment status).

**Frontend** — React + Vite SPA with Socket.IO client for real-time play, deployed on Netlify.
[Go to showcase](https://github.com/sebastianval22/tictacgoal-frontend-showcase)

**Backend** — Koa.js + Sequelize/PostgreSQL REST + WebSocket API, with a custom scraping pipeline building the football player dataset, deployed on Render.
[Go to showcase](https://github.com/sebastianval22/tictacgoal-backend-showcase)

## Software Engineering — PichangasYa
A full-course group project: a Ruby on Rails platform for organizing and joining pickup football matches, with private groups, real-time chat, and admin permission management. I worked across both backend and frontend. Source repository is private to the course; the link below is a sanitized showcase (see the repo's README for current deployment status).
[Go to showcase](https://github.com/sebastianval22/pichangasya-showcase)

## Databases
A group project modeling a food-delivery platform's relational database (restaurants, dishes, deliveries, clients) in PostgreSQL, plus a Flask web app demonstrating the supported queries. Source repository is private to the course; the link below is a sanitized showcase with the graded SQL redacted (see the repo's README).
[Go to showcase](https://github.com/sebastianval22/food-delivery-db-showcase)

## Advanced Programming
Python projects using object-oriented design, GUIs, and client-server networking.

### Project T0 — Castle Defense Solver
`main.py` models a castle defense puzzle (turtles and bombs with a blast range) using recursive functions, validating and solving boards per a fixed rule set, with a menu-driven CLI for loading and acting on board files.
[Go to code](https://github.com/sebastianval22/school-projects/tree/main/Advanced%20Programming%20Projects/T0)

### Project T1 — DCCavaCava Tournament Simulator
`main.py` simulates a digging tournament through an object-oriented design (`Tournament`, `Arena`, `Item`, `Digger`, with subclasses for item/digger variants), driven by an interactive menu and persisted match records under `Partidas/`.
[Go to code](https://github.com/sebastianval22/school-projects/tree/main/Advanced%20Programming%20Projects/T1)

### Project T2 — Luigi Arcade Game
`main.py` implements an arcade platformer (start/game/timer/end windows) where the player, as Luigi, navigates a map of ghosts, walls, fire, and movable rocks to reach a goal star within a life and time budget; maps can be loaded from file or built via drag-and-drop.
[Go to code](https://github.com/sebastianval22/school-projects/tree/main/Advanced%20Programming%20Projects/T2)

### Project T3 — DCCachos Networked Dice Game
A client-server implementation (`cliente/main_cliente.py`, `servidor/main_servidor.py`) of a turn-based dice game for four players (backed by bots when the room isn't full), with a waiting-room and in-game GUI, turn actions (pass, announce, use power, roll, doubt), and reconnection handling.
[Go to code](https://github.com/sebastianval22/school-projects/tree/main/Advanced%20Programming%20Projects/T3)
