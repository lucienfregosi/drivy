SELECT
	d.year,
	d.month,
	COUNT(*) as thirdMonthRentalCount
FROM
(
    SELECT 
        v.car_id,
        v.rental_id,
        Row_Number() Over (Partition By v.car_id) As rental_count,
        v.year,
        v.month
    FROM
    (
        SELECT 
            c2.id as car_id,
            r.id as rental_id,
            c2.city,
            extract (year from r.starts_at) as year,
            extract (month from r.starts_at) as month
        FROM (
            SELECT 
                id, 
                city, 
                CASE WHEN created_at IS NULL THEN (SELECT TO_DATE(created_at,'YYYY-MM-DD') FROM cars WHERE ID < c.ID AND created_at IS NOT NULL ORDER BY id DESC LIMIT 1) ELSE TO_DATE(created_at,'YYYY-MM-DD') END AS created_at
            FROM cars c
        ) c2
        INNER JOIN rentals r ON c2.id = r.car_id
        WHERE c2.created_at < r.starts_at
    ) v
) d
WHERE d.rental_count = 3
GROUP BY d.year, d.month
ORDER BY d.year, d.month