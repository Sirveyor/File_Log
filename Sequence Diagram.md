User                Windows API        Watcher Core        Process Inspector       Session Tracker        SQLite DB
 |                       |                   |                     |                     |                   |
 |--- Switch Window ---->|                   |                     |                     |                   |
 |                       |--- Event -------->|                     |                     |                   |
 |                       |  (foreground      |                     |                     |                   |
 |                       |   window changed) |                     |                     |                   |
 |                       |                   |--- Get PID -------->|                     |                   |
 |                       |                   |                     |--- Inspect -------->|                   |
 |                       |                   |                     |   (exe, handles)    |                   |
 |                       |                   |                     |                     |                   |
 |                       |                   |<-- File Info -------|                     |                   |
 |                       |                   |   (file path, app)  |                     |                   |
 |                       |                   |                     |                     |                   |
 |                       |                   |--- Notify --------->|                     |                   |
 |                       |                   |   (active file)     |                     |                   |
 |                       |                   |                     |--- Compare -------->|                   |
 |                       |                   |                     |   (prev vs new)     |                   |
 |                       |                   |                     |                     |                   |
 |                       |                   |                     |--- Close old ------>|--- Update ------->|
 |                       |                   |                     |    session          |   closed_at       |
 |                       |                   |                     |                     |   duration        |
 |                       |                   |                     |                     |<------------------|
 |                       |                   |                     |                     |                   |
 |                       |                   |                     |--- Open new ------->|--- Insert ------->|
 |                       |                   |                     |    session          |   opened_at       |
 |                       |                   |                     |                     |   file_id, app_id |
 |                       |                   |                     |                     |<------------------|
 |                       |                   |                     |                     |                   |