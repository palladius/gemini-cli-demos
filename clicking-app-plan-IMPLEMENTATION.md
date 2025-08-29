# Implementation Checklist: Click-Tracking Application

This checklist outlines the steps to implement the click-tracking application as defined in the PRD.

## Phase 1: Project Setup

- [ ] Initialize a new Rust project: `cargo new click-tracker`
- [ ] Add dependencies to `Cargo.toml`:
    - `axum`
    - `tokio` (with `full` features)
    - `rusqlite` (with `bundled` feature)
    - `serde` (for potential JSON responses)
    - `tracing` and `tracing-subscriber` (for logging)

## Phase 2: Database Setup

- [ ] Create a module for database interactions (`database.rs`).
- [ ] Implement a function to initialize the SQLite database and create the `clicks` table.
- [ ] Implement a function to record a new click into the database.
- [ ] Implement a function to check if an IP address already exists in the database.

## Phase 3: Web Server Implementation

- [ ] Set up the main application entry point in `main.rs`.
- [ ] Initialize logging and the database connection.
- [ ] Create the `axum` router with a single route for the homepage (`/`).
- [ ] Implement the handler for the homepage:
    - It should handle both `GET` (display page) and `POST` (handle click) requests.
    - On `POST`, it should call the database module to record the click and determine the correct PIN.
    - It should return the homepage template, now including the generated PIN.

## Phase 4: Frontend

- [ ] Create a simple HTML template for the homepage.
- [ ] The template should include a form with a button that sends a `POST` request to the server.
- [ ] The template should have a placeholder to display the PIN returned by the server.

## Phase 5: Finalization & Testing

- [ ] Add comments to the code where necessary.
- [ ] Write unit tests for the database logic.
- [ ] Write integration tests for the web handlers.
- [ ] Run `cargo fmt` to format the code.
- [ ] Run `cargo clippy` to lint the code.
- [ ] Create a `README.md` for the new demo folder with instructions on how to run the application.
