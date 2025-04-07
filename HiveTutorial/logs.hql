-- Crear tabla
CREATE TABLE logs (
  user_id STRING,
  time_log STRING,
  query STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
STORED AS TEXTFILE;

-- Cargar datos
LOAD DATA INPATH 's3://hive-moises/files/excite-small.log' 
OVERWRITE INTO TABLE logs;

-- Crear result
CREATE TABLE result AS
SELECT l.user_id, count(1) AS count 
FROM logs AS l 
GROUP BY l.user_id 
ORDER BY l.user_id;