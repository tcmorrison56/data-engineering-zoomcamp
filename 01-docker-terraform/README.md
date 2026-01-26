<!-- SQL and SHELL commands for 01-docker-terraform homework -->

# Question 1
docker run -it --rm --entrypoint=bash python:3.13
/# pip --version
pip 25.3 from /usr/local/lib/python3.13/site-packages/pip (python 3.13)


# Question 2
Used docker-compose.yaml file

# Question 3
SELECT
	COUNT(trip_distance)
FROM
	green_taxi_data
WHERE
	trip_distance <= 1;


# Question 4
SELECT
	MAX(trip_distance) AS "max_trip_distance",
	CAST(lpep_pickup_datetime AS DATE) AS "Date"
FROM
	green_taxi_data
WHERE
	trip_distance < 100
GROUP BY
	CAST(lpep_pickup_datetime AS DATE)
ORDER BY "max_trip_distance" DESC;


# Question 5
SELECT
	"Zone",
	COUNT("Zone")
FROM
	zones
JOIN 
	green_taxi_data ON zones."LocationID" = green_taxi_data."PULocationID"
WHERE
	CAST(lpep_pickup_datetime AS DATE) = '2025-11-18'
GROUP BY
	"Zone"
ORDER BY
	COUNT DESC;


# Question 6
SELECT
	zdo."Zone" AS dropoff_zone,
	MAX(tip_amount) AS max_tip
FROM
	green_taxi_data t
JOIN
	zones zpu on t."PULocationID" = zpu."LocationID"
JOIN
	zones zdo on t."DOLocationID" = zdo."LocationID"
WHERE
	zpu."Zone" = 'East Harlem North'
GROUP BY
	zdo."Zone"
ORDER BY
	max_tip DESC
LIMIT 1;