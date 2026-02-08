# Homework 03 Data Warehouses 

### Create external table from parquet files in Google Cloud Storage by running the following query:

```sql
CREATE OR REPLACE EXTERNAL TABLE dtc-de-course-485518.nytaxi.yellow_taxi_data
OPTIONS(
  format= 'PARQUET',
  uris = ['gs://dtc-de-course-485518-03-bigquery/*.parquet']
);
```

### Create a native table using the following query:

```sql
CREATE OR REPLACE TABLE dtc-de-course-485518.nytaxi.yellow_taxi_data_native AS
SELECT * FROM dtc-de-course-485518.nytaxi.yellow_taxi_data;
```

## Question 1.
What is the count of records for the 2024 Yellow Taxi data? (January through June)

```sql
SELECT
  count(*) as total_rows
FROM
  dtc-de-course-485518.nytaxi.yellow_taxi_data;
```

Result = 20332093

## Question 2.
Write queries to count the destinct number of PULocationIDs for the entire dataset on both tables. What is the estimated amount of data that will be read when this query is executed on each table.

### External Table
```sql
SELECT
  count(DISTINCT(PULocationID)) FROM dtc-de-course-485518.nytaxi.yellow_taxi_data;
  ```
  Result = 0 MB

### Native Table
```sql
SELECT
  count(DISTINCT(PULocationID)) FROM dtc-de-course-485518.nytaxi.yellow_taxi_data_native;
  ```
  Result = 155.12 MB

## Question 3.
Write a query to retrieve the PULocationID from the table (not the external table) in BigQuery. Now write a query to retrieve the PULocationID and DOLocationID on the same table.

```sql
SELECT PULocationID FROM nytaxi.yellow_taxi_data_native;

SELECT
  PULocationID,
  DOLocationID
FROM nytaxi.yellow_taxi_data_native;
```

## Question 4.
How many records have a fare_amount of 0?

```sql
SELECT 
  count(*)
FROM
  `nytaxi.yellow_taxi_data_native`
WHERE
  fare_amount = 0;
```
  Result = 8333

## Question 5.
Create an optimized table in Big Query where you always filter based on tpep_dropoff_datetime and order results by VendorID

```sql
CREATE OR REPLACE TABLE dtc-de-course-485518.nytaxi.yellow_taxi_data_partitioned
PARTITION BY DATE(tpep_dropoff_datetime)
CLUSTER BY VendorID
AS 
SELECT * FROM dtc-de-course-485518.nytaxi.yellow_taxi_data;
```

## Question 6.
Write a query to retrieve the distinct VendorIDs between tpep_dropoff_datetime 2024-03-01 and 2024-03-15 (inclusive)

Use the materialized table you created earlier in your from clause and note the estimated bytes. Now change the table in the from clause to the partitioned table you created for question 5 and note the estimated bytes processed. What are these values?

### Non-partitioned Table
```sql
SELECT DISTINCT
  VendorID
FROM 
  `nytaxi.yellow_taxi_data_native`
WHERE 
  DATE(tpep_dropoff_datetime) BETWEEN '2024-03-01' AND '2024-03-15';
```
Result = 31-.24 MB

### Partitioned Table
```sql
SELECT DISTINCT
  VendorID
FROM 
  `nytaxi.yellow_taxi_data_partitioned`
WHERE 
  DATE(tpep_dropoff_datetime) BETWEEN '2024-03-01' AND '2024-03-15';
  ```
Result = 26.84 MB

