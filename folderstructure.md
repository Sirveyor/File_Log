File_Log/
│
├── app/
│   ├── watcher/
│   │   ├── __init__.py
│   │   ├── event_listener.py        # Foreground window + Win32 hooks
│   │   ├── process_inspector.py     # psutil/pywin32 file handle scanning
│   │   ├── session_tracker.py       # Start/stop file sessions
│   │   ├── app_registry.py          # Known apps, exe paths, rules
|   |   |── handlers/
|   |       |── notepad_handler.py
|   
│   │
│   ├── db/
│   │   ├── __init__.py
│   │   ├── schema.py                # SQLite table definitions
│   │   ├── connection.py            # DB connection manager
│   │   └── queries.py               # Insert/select helpers
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── app_model.py
│   │   ├── file_model.py
│   │   └── session_model.py
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── time_utils.py
│   │   ├── path_utils.py
│   │   └── logging_utils.py
│   │
│   ├── analytics/
│   │   ├── __init__.py
│   │   ├── daily_report.py
│   │   ├── weekly_report.py
│   │   └── summary_builder.py
│   │
│   ├── tui/
│   │   ├── __init__.py
│   │   ├── dashboard.py             # Your TUI interface
│   │   └── views/
│   │       ├── __init__.py
│   │       ├── today_view.py
│   │       ├── file_history_view.py
│   │       └── app_usage_view.py
│   │
│   └── main.py                      # Entry point for the watcher service
│
├── tests/
│   ├── test_watcher.py
│   ├── test_db.py
│   ├── test_analytics.py
│   └── test_tui.py
│
├── data/
│   ├── file_log.db                  # SQLite database
│   └── logs/                        # Optional runtime logs
│
├── config/
│   ├── settings.toml                # App config (paths, intervals, etc.)
│   └── apps.yaml                    # Rules for detecting file types per app
│
├── scripts/
│   ├── install_deps.ps1
│   ├── reset_db.py
│   └── export_csv.py
│
├── .venv/
│
├── pyproject.toml
├── README.md
└── .gitignore