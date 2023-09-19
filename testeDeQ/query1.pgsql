select * from xmldata;

SELECT unnest(XPATH('/athletes/atlethe[@name="A Lamusi"]', xml)) FROM xmldata;

SELECT unnest(XPATH('/athletes/atlethe/sex', xml)) FROM xmldata;
SELECT unnest(XPATH('/athletes/atlethe/age', xml)) FROM xmldata;


 WITH athelete_info_name AS (
   SELECT unnest(XPATH('/athletes/atlethe/age', xml)) AS idadeAtleta
    FROM xmldata
), athelete_sex_info AS (
    SELECT unnest(XPATH('/athletes/atlethe/sex', xml)) AS sexoAtleta
     FROM xmldata
) 
SELECT unnest(XPATH('/athletes/atlethe[@name="A Lamusi"]', xml)) AS nomeAtleta
    FROM xmldata;

 SELECT unnest(xpath('/athletes/atlethe[@name="A Lamusi"]', xml)) AS nome,
        unnest(xpath('/athletes/atlethe/sex', xml)) AS sexo,
        unnest(xpath('/athletes/atlethe/age', xml)) AS idade
FROM xmldata;