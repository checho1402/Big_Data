-- Crear tabla
CREATE TABLE docs (line STRING)
ROW FORMAT DELIMITED
LINES TERMINATED BY '\n'
STORED AS TEXTFILE;

-- Cargar Datos
LOAD DATA INPATH 's3://hdfs-hadoop-sergio/files/word.txt' 
OVERWRITE INTO TABLE docs;

-- Crear WordCounter
CREATE TABLE word_counts AS
SELECT w.line, count(1) AS count 
FROM docs AS w 
GROUP BY w.line 
ORDER BY w.line;

-- Mostrar Datos
SELECT * FROM word_counts;

-- Guardar Archivo
INSERT OVERWRITE DIRECTORY 's3://hdfs-hadoop-sergio/output/result01hive'
SELECT * FROM word_counts;