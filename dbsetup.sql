CREATE TABLE IF NOT EXISTS apps (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    exe_path TEXT NOT NULL,
    UNIQUE(name, exe_path)
);

CREATE TABLE IF NOT EXISTS files (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    path TEXT NOT NULL UNIQUE,
    extension TEXT
);

CREATE TABLE IF NOT EXISTS sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id INTEGER NOT NULL,
    app_id INTEGER NOT NULL,
    opened_at TEXT NOT NULL,
    closed_at TEXT,
    duration_seconds INTEGER,
    FOREIGN KEY (file_id) REFERENCES files(id),
    FOREIGN KEY (app_id) REFERENCES apps(id)
);