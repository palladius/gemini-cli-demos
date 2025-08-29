# PRD: Click-Tracking Application

## 1. Objective

To create a simple, high-performance web application using Rust to track clicks from workshop participants. The application will issue a unique PIN to each participant based on their click order (first click vs. subsequent clicks from the same IP).

## 2. Target Audience

Participants of the GCP Workshop.

## 3. Core Features

### 3.1. Homepage

*   A minimalist web page will be served at the root URL (`/`).
*   This page will contain a single, prominent button for the user to click.
*   The page will display the PIN received after a click.

### 3.2. Click Tracking

*   When a user clicks the button, the backend will record the following information:
    *   The user's IP address.
    *   The timestamp of the click (in UTC).
    *   The PIN that was generated and given to the user.
*   No user authentication or login is required.

### 3.3. PIN Generation

*   The application will differentiate between the first click and subsequent clicks from the same IP address.
*   **First Click:** A user clicking for the first time will receive a primary, unique PIN.
*   **Subsequent Clicks:** Any subsequent clicks from the same IP address will receive a secondary, different PIN.
*   The generated PIN will be displayed on the homepage after the click action is complete.

### 3.4. Data Storage

*   A lightweight database will be used to persist the click data.
*   The schema will include fields for `ip_address`, `timestamp`, and `pin_given`.

## 4. Technical Stack

*   **Programming Language:** Rust
*   **Web Framework:** `axum` (a modern and ergonomic web framework for Rust)
*   **Database:** `SQLite` (via the `rusqlite` crate for simple, file-based storage)
*   **Async Runtime:** `tokio`

## 5. Out of Scope

*   User accounts or any form of login.
*   An admin dashboard or complex analytics interface.
*   Editing or deleting click records via the UI.
