USE programmers_select;

CREATE TABLE ONLINE_SALE (
	ONLINE_SALE_ID INTEGER PRIMARY KEY NOT NULL,
    USER_ID INTEGER NOT NULL,
    PRODUCT_ID INTEGER NOT NULL,
    SALES_AMOUNT INTEGER NOT NULL,
    SALES_DATE DATE NOT NULL
);

INSERT INTO ONLINE_SALE (ONLINE_SALE_ID, USER_ID, PRODUCT_ID, SALES_AMOUNT, SALES_DATE)
VALUES 
    (1, 1, 3, 2, '2022-02-25'),
    (2, 1, 4, 1, '2022-03-01'),
    (3, 1, 3, 3, '2022-03-31'),
    (4, 2, 4, 2, '2022-03-12'),
    (5, 3, 5, 1, '2022-04-03'),
    (6, 2, 4, 1, '2022-04-06'),
    (7, 1, 4, 2, '2022-05-11');

SHOW TABLES;

SELECT * FROM ONLINE_SALE;

SELECT 
    USER_ID, PRODUCT_ID
FROM
    ONLINE_SALE
GROUP BY USER_ID , PRODUCT_ID
HAVING COUNT(USER_ID) > 1
ORDER BY 1 , 2 DESC;