-- Crear la tabla 'pages'
CREATE TABLE pages (
  name STRING,
  url STRING,
  time_pages STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ',';

-- Cargar los datos en la tabla 'pages' desde un archivo local
LOAD DATA INPATH 's3://hive-moises/files/visits.log'
OVERWRITE INTO TABLE pages;

-- Crear la tabla 'avg_visit' y calcular el promedio de visitas
CREATE TABLE avg_visit AS
SELECT AVG(num_pages) AS average_visits
FROM (
  SELECT name, COUNT(1) AS num_pages
  FROM pages
  GROUP BY name
) np;
