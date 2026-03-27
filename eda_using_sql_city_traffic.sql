create database city_traffic_db;
use city_traffic_db;
show tables in city_traffic_db;


-- 1. DATA OVERVIEW

SELECT COUNT(*) AS total_rows
FROM traffic_data;

SELECT *
FROM traffic_data
LIMIT 10;

-- 2. MISSING VALUE CHECK

SELECT
    COUNT(*) - COUNT(lighting) AS lighting_nulls,
    COUNT(*) - COUNT(weather) AS weather_nulls,
    COUNT(*) - COUNT(avg_speed_kmph) AS speed_nulls,
    COUNT(*) - COUNT(vehicle_count_per_hr) AS traffic_nulls,
    COUNT(*) - COUNT(signal_status) AS signal_status_nulls
FROM traffic_data;

-- 3. TARGET VARIABLE DISTRIBUTION

SELECT 
    accident_occurred,
    COUNT(*) AS count,
    COUNT(*) * 1.0 / SUM(COUNT(*)) OVER() AS proportion
FROM traffic_data
GROUP BY accident_occurred;

-- 4. ACCIDENTS BY HOUR OF DAY

SELECT 
    hour_of_day,
    AVG(CASE WHEN accident_occurred = 1 THEN 1 ELSE 0 END) AS accident_rate
FROM traffic_data
GROUP BY hour_of_day
ORDER BY hour_of_day ;


-- 5. ACCIDENTS BY DAY OF WEEK

SELECT
    CASE day_of_week
        WHEN 0 THEN 'Monday'
        WHEN 1 THEN 'Tuesday'
        WHEN 2 THEN 'Wednesday'
        WHEN 3 THEN 'Thursday'
        WHEN 4 THEN 'Friday'
        WHEN 5 THEN 'Saturday'
        WHEN 6 THEN 'Sunday'
    END AS day_name,
    COUNT(*) AS total_cases,
    SUM(CASE WHEN accident_occurred = 1 THEN 1 ELSE 0 END) AS accidents,
    ROUND(AVG(CASE WHEN accident_occurred = 1 THEN 1 ELSE 0 END), 4) AS accident_rate
FROM traffic_data
GROUP BY day_of_week
ORDER BY accident_rate DESC;

-- 6. TRAFFIC DENSITY ANALYSIS

SELECT 
    CASE 
        WHEN vehicle_count_per_hr < 500 THEN 'Low'
        WHEN vehicle_count_per_hr < 1000 THEN 'Medium'
        ELSE 'High'
    END AS traffic_level,
    
    AVG(CASE WHEN accident_occurred = 1 THEN 1 ELSE 0 END) AS accident_rate
FROM traffic_data
GROUP BY traffic_level;


-- 7. SPEED ANALYSIS

SELECT 
    CASE 
        WHEN avg_speed_kmph < 20 THEN 'Low Speed'
        WHEN avg_speed_kmph < 40 THEN 'Medium Speed'
        ELSE 'High Speed'
    END AS speed_group,
    
    AVG(CASE WHEN accident_occurred = 1 THEN 1 ELSE 0 END) AS accident_rate
FROM traffic_data
GROUP BY speed_group;


-- 8. SIGNAL VS ACCIDENTS

SELECT 
    has_signal,
    AVG(CASE WHEN accident_occurred = 1 THEN 1 ELSE 0 END) AS accident_rate
FROM traffic_data
GROUP BY has_signal;


-- 9. WEATHER ANALYSIS
SELECT 
    weather,
    AVG(CASE WHEN accident_occurred = 1 THEN 1 ELSE 0 END) AS accident_rate
FROM traffic_data
GROUP BY weather;


-- 10. LIGHTING ANALYSIS

SELECT 
    lighting,
    AVG(CASE WHEN accident_occurred = 1 THEN 1 ELSE 0 END) AS accident_rate
FROM traffic_data
GROUP BY lighting;


-- 11. BLACKSPOT SCORE ANALYSIS

SELECT 
    accident_occurred,
    ROUND(AVG(blackspot_score),4) AS avg_blackspot_score
FROM traffic_data
GROUP BY accident_occurred;


-- 12. PEAK VS NON-PEAK ANALYSIS

SELECT 
    is_peak,
    AVG(CASE WHEN accident_occurred = 1 THEN 1 ELSE 0 END) AS accident_rate
FROM traffic_data
GROUP BY is_peak;


-- 13. LOCATION-BASED ANALYSIS


SELECT DISTINCT(LATITUDE),LONGITUDE FROM TRAFFIC_DATA;

-- Total accidents per location
SELECT 
    location_id,
    COUNT(*) AS total_accidents
FROM traffic_data
WHERE accident_occurred = 1
GROUP BY location_id
ORDER BY total_accidents DESC;


-- Accident rate per location
SELECT 
    location_id,
    AVG(CASE WHEN accident_occurred = 1 THEN 1 ELSE 0 END) AS accident_rate
FROM traffic_data
GROUP BY location_id
ORDER BY accident_rate DESC;


-- 14. LOCATION + TIME + CAUSE ANALYSIS

SELECT 
    location_id,
    hour_of_day,
    cause,
    COUNT(*) AS accident_count
FROM traffic_data
WHERE accident_occurred = 1
GROUP BY location_id, hour_of_day, cause
ORDER BY accident_count DESC
LIMIT 10;


-- 15. SIGNAL VIOLATIONS ANALYSIS

SELECT 
    ROUND(AVG(violations_count),4) AS avg_violations,
    accident_occurred
FROM traffic_data
GROUP BY accident_occurred;


-- 16. Which day of week has highest accident rate?
-- here we have day_of_week follows the rule as 0-Monday,1-Tuesday,2-Wednesday,3-Thursday,
-- 4-Friday,5-Saturday, 6-Sunday
SELECT 
    day_of_week,
    COUNT(*) AS total_cases,
    SUM(CASE WHEN accident_occurred = 1 THEN 1 ELSE 0 END) AS accidents,
    AVG(CASE WHEN accident_occurred = 1 THEN 1 ELSE 0 END) AS accident_rate
FROM traffic_data
GROUP BY day_of_week
ORDER BY accident_rate DESC;

-- 17. Which weather condition is most dangerous?

SELECT 
    weather,
    COUNT(*) AS total,
    AVG(CASE WHEN accident_occurred = 1 THEN 1 ELSE 0 END) AS accident_rate
FROM traffic_data
GROUP BY weather
ORDER BY accident_rate DESC;



-- 18. Does peak traffic increase accidents?
SELECT 
    is_peak,
    COUNT(*) AS total,
    AVG(CASE WHEN accident_occurred = 1 THEN 1 ELSE 0 END) AS accident_rate
FROM traffic_data
GROUP BY is_peak;

-- 19. Which speed range is most dangerous?

SELECT 
    CASE 
        WHEN avg_speed_kmph < 20 THEN 'Low Speed'
        WHEN avg_speed_kmph < 40 THEN 'Medium Speed'
        ELSE 'High Speed'
    END AS speed_range,
    
    AVG(CASE WHEN accident_occurred = 1 THEN 1 ELSE 0 END) AS accident_rate
FROM traffic_data
GROUP BY speed_range
ORDER BY accident_rate DESC;

-- 20. Which road type has highest accident risk?
SELECT 
    road_type,
    COUNT(*) AS total,
    AVG(CASE WHEN accident_occurred = 1 THEN 1 ELSE 0 END) AS accident_rate
FROM traffic_data
GROUP BY road_type
ORDER BY accident_rate DESC;

-- 21. Do signals reduce or increase accidents?

SELECT 
    has_signal,
    COUNT(*) AS total,
    AVG(CASE WHEN accident_occurred = 1 THEN 1 ELSE 0 END) AS accident_rate
FROM traffic_data
GROUP BY has_signal;


-- 22. Which traffic density level is most risky?

SELECT 
    CASE 
        WHEN vehicle_count_per_hr < 500 THEN 'Low'
        WHEN vehicle_count_per_hr < 1000 THEN 'Medium'
        ELSE 'High'
    END AS traffic_level,
    
    AVG(CASE WHEN accident_occurred = 1 THEN 1 ELSE 0 END) AS accident_rate
FROM traffic_data
GROUP BY traffic_level
ORDER BY accident_rate DESC;


-- season vs accident rate
SELECT
    season,
    COUNT(*) AS total,
    SUM(CASE WHEN accident_occurred = 1 THEN 1 ELSE 0 END) AS accidents,
    ROUND(AVG(CASE WHEN accident_occurred = 1 THEN 1 ELSE 0 END), 4) AS accident_rate
FROM traffic_data
GROUP BY season
ORDER BY accident_rate DESC;

-- enforcement level vs accident rate
SELECT
    enforcement_level,
    COUNT(*) AS total,
    ROUND(AVG(CASE WHEN accident_occurred = 1 THEN 1 ELSE 0 END), 4) AS accident_rate
FROM traffic_data
GROUP BY enforcement_level
ORDER BY accident_rate DESC;


-- cause distribution - overall

SELECT
    cause,
    COUNT(*) AS accident_count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 2) AS percentage
FROM traffic_data
WHERE accident_occurred = 1
GROUP BY cause
ORDER BY accident_count DESC;