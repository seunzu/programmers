USE programmers_groupBy;

CREATE TABLE CAR_RENTAL_COMPANY_CAR (
    CAR_ID INTEGER PRIMARY KEY,
    CAR_TYPE VARCHAR(255) NOT NULL,
    DAILY_FEE INTEGER NOT NULL,
    OPTIONS VARCHAR(255) NOT NULL
);

SHOW TABLES;

INSERT INTO CAR_RENTAL_COMPANY_CAR (CAR_ID, CAR_TYPE, DAILY_FEE, OPTIONS)
VALUES
    (1, '세단', 16000, '가죽시트,열선시트,후방카메라'),
    (2, 'SUV', 14000, '스마트키,네비게이션,열선시트'),
    (3, 'SUV', 22000, '주차감지센서,후방카메라'),
    (4, '트럭', 35000, '주차감지센서,네비게이션,열선시트'),
    (5, 'SUV', 16000, '가죽시트,네비게이션,열선시트,후방카메라,주차감지센서');

SELECT * FROM CAR_RENTAL_COMPANY_CAR;

SELECT 
    CAR_TYPE, COUNT(*) AS CARS
FROM
    CAR_RENTAL_COMPANY_CAR
WHERE
    OPTIONS LIKE '%통풍시트%'
        OR OPTIONS LIKE '%열선시트%'
        OR OPTIONS LIKE '%가죽시트%'
GROUP BY 1
ORDER BY 1
