# Photoshoot has Event Name
SELECT event_id, name
FROM tracker_app_photoshoothasgear p
JOIN tracker_app_event e ON p.event_id = e.id