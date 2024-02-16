USE programmers_string_date;

SHOW TABLES;

SELECT * FROM ANIMAL_INS;

SELECT 
    ANIMAL_ID,
    NAME,
    CASE
        WHEN
            SEX_UPON_INTAKE LIKE '%Neutered%'
                OR SEX_UPON_INTAKE LIKE '%Spayed%'
        THEN
            'O'
        ELSE 'X'
    END AS 중성화
FROM
    ANIMAL_INS
ORDER BY 1