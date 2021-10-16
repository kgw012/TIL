SELECT A.id, A.name
FROM subway_stations A
LEFT JOIN line_routes B
ON A.id = B.station_id
    AND (B.line_color = 'red'
        OR B.line_color = 'green')
WHERE B.id is NULL;