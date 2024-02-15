USE programmers_select;

CREATE TABLE ICECREAM_INFO (
	FLAVOR VARCHAR(50) NOT NULL,
    INGREDIENT_TYPE VARCHAR(50) NOT NULL
);

SHOW TABLES;

INSERT INTO ICECREAM_INFO (FLAVOR, INGREDIENT_TYPE) 
VALUES
('chocolate', 'sugar_based'),
('vanilla', 'sugar_based'),
('mint_chocolate', 'sugar_based'),
('caramel', 'sugar_based'),
('white_chocolate', 'sugar_based'),
('peach', 'fruit_based'),
('watermelon', 'fruit_based'),
('mango', 'fruit_based'),
('strawberry', 'fruit_based'),
('melon', 'fruit_based'),
('orange', 'fruit_based'),
('pineapple', 'fruit_based');

SELECT 
    A.FLAVOR
FROM
    FIRST_HALF A
        LEFT JOIN
    ICECREAM_INFO B ON A.FLAVOR = B.FLAVOR
WHERE
    TOTAL_ORDER > 3000
        AND INGREDIENT_TYPE = 'fruit_based'
ORDER BY TOTAL_ORDER DESC