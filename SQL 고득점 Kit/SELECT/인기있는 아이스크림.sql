USE programmers_select;

CREATE TABLE FIRST_HALF (
	SHIPMENT_ID INT(20) PRIMARY KEY NOT NULL,
    FLAVOR VARCHAR(50) NOT NULL,
    TOTAL_ORDER INT(20) NOT NULL
);

SHOW TABLES;

INSERT INTO FIRST_HALF (SHIPMENT_ID, FLAVOR, TOTAL_ORDER) 
VALUES
(101, 'chocolate', 3200),
(102, 'vanilla', 2800),
(103, 'mint_chocolate', 1700),
(104, 'caramel', 2600),
(105, 'white_chocolate', 3100),
(106, 'peach', 2450),
(107, 'watermelon', 2150),
(108, 'mango', 2900),
(109, 'strawberry', 3100),
(110, 'melon', 3150),
(111, 'orange', 2900),
(112, 'pineapple', 2900);

SELECT * FROM FIRST_HALF;

SELECT 
    FLAVOR
FROM
    FIRST_HALF
ORDER BY TOTAL_ORDER DESC , SHIPMENT_ID ASC;