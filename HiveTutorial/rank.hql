-- Desactivar la conversión automática de joins
SET hive.auto.convert.join = false;

-- Crear la tabla 'visits'
CREATE TABLE visits (
  name STRING,
  url STRING,
  time_visits STRING
)ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
STORED AS TEXTFILE;

-- Cargar los datos en la tabla 'visits' desde un archivo local
LOAD DATA  INPATH 's3://hive-moises/files/visits.log'
OVERWRITE INTO TABLE visits;

-- Crear la tabla 'pages'
CREATE TABLE pages (
  url STRING,
  pagerank DECIMAL
)ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
STORED AS TEXTFILE;

-- Cargar los datos en la tabla 'pages' desde un archivo local
LOAD DATA  INPATH 's3://hive-moises/files/pages.log'
OVERWRITE INTO TABLE pages;

-- Crear la tabla 'rank_result' y realizar la consulta
CREATE TABLE rank_result AS
SELECT pr.name
FROM (
  SELECT V.name, AVG(P.pagerank) AS prank
  FROM visits V
  JOIN pages P ON (V.url = P.url)
  GROUP BY V.name
) pr
WHERE pr.prank > 0.5;
