ALTER TABLE orders_table
ALTER COLUMN date_uuid TYPE UUID USING CAST(date_uuid as UUID),
ALTER COLUMN user_uuid TYPE UUID USING CAST(date_uuid as UUID),
ALTER COLUMN card_number TYPE VARCHAR(50),
ALTER COLUMN store_code TYPE VARCHAR(50),
ALTER COLUMN product_code TYPE VARCHAR(50),
ALTER COLUMN product_quantity TYPE SMALLINT;


ALTER TABLE dim_users
ALTER COLUMN first_name TYPE VARCHAR(255),
ALTER COLUMN last_name TYPE VARCHAR(255),
ALTER COLUMN date_of_birth TYPE DATE USING CAST(date_of_birth AS DATE),
ALTER COLUMN country_code TYPE VARCHAR(50),
ALTER COLUMN user_uuid TYPE UUID USING CAST(user_uuid as UUID),
ALTER COLUMN join_date TYPE DATE USING CAST(join_date AS DATE);

ALTER TABLE dim_store_details
ALTER COLUMN longitude TYPE FLOAT USING CAST(longitude AS FLOAT),
ALTER COLUMN locality TYPE VARCHAR(255),
ALTER COLUMN store_code TYPE VARCHAR(20),
ALTER COLUMN staff_numbers TYPE SMALLINT,
ALTER COLUMN opening_date TYPE DATE USING CAST(opening_date as DATE),
ALTER COLUMN store_type TYPE VARCHAR(255),
ALTER COLUMN latitude TYPE FLOAT USING CAST(longitude AS FLOAT),
ALTER COLUMN country_code TYPE VARCHAR(20),
ALTER COLUMN continent TYPE VARCHAR(255);


UPDATE dim_products
SET product_price = REPLACE(product_price, '£', '');


ALTER TABLE dim_products 
	ALTER COLUMN weight TYPE FLOAT USING CAST(weight as FLOAT),
	ADD COLUMN weight_class VARCHAR;


UPDATE dim_products
SET weight_class =
	CASE 
		WHEN weight < 2.0 THEN 'Light'
		WHEN weight >= 2 AND weight < 40 THEN 'Mid_Sized'
		WHEN weight >= 40 AND weight <140 THEN 'Heavy'
		WHEN weight >= 140 THEN 'Truck_Required'
	END;


ALTER TABLE dim_products 
	RENAME COLUMN removed to still_available;

ALTER TABLE dim_products
	ALTER COLUMN product_price TYPE FLOAT USING CAST(product_price as FLOAT),
	ALTER COLUMN weight TYPE FLOAT USING CAST(weight as FLOAT),
    ALTER COLUMN "EAN" TYPE VARCHAR(20),
	ALTER COLUMN product_code TYPE VARCHAR(15),
	ALTER COLUMN date_added TYPE DATE USING CAST(date_added as DATE),
	ALTER COLUMN uuid TYPE UUID USING CAST(uuid as UUID),
	ALTER COLUMN still_available TYPE boolean USING (still_available ='Still_available'),
    ALTER COLUMN weight_class TYPE VARCHAR(15);

ALTER TABLE dim_date_times
	ALTER COLUMN month TYPE VARCHAR(2),
    ALTER COLUMN year TYPE VARCHAR(4),
	ALTER COLUMN day TYPE VARCHAR(2),
    ALTER COLUMN time_period TYPE VARCHAR(10),
	ALTER COLUMN date_uuid TYPE UUID USING CAST(date_uuid as UUID);

SELECT max(length(card_number))
FROM dim_card_details
GROUP BY card_number
ORDER BY max(length(card_number)) desc
LIMIT 1;

SELECT max(length(expiry_date))
FROM dim_card_details
GROUP BY expiry_date
ORDER BY max(length(expiry_date)) desc
LIMIT 1;


ALTER TABLE dim_card_details
	ALTER COLUMN card_number TYPE VARCHAR(22),
    ALTER COLUMN expiry_date TYPE VARCHAR(10),
	ALTER COLUMN date_payment_confirmed TYPE DATE USING CAST(date_payment_confirmed as DATE);


ALTER TABLE dim_card_details
	ADD PRIMARY KEY (card_number);
	
ALTER TABLE dim_date_times
	ADD PRIMARY KEY (date_uuid);
	
ALTER TABLE dim_products
	ADD PRIMARY KEY (product_code);
	
ALTER TABLE dim_store_details
	ADD PRIMARY KEY (store_code);

SELECT user_uuid, COUNT(*) AS count
FROM dim_users
GROUP BY user_uuid
HAVING COUNT(*) > 1;

DELETE FROM dim_users
WHERE user_uuid = 'NULL';

ALTER TABLE dim_users
	ADD PRIMARY KEY (user_uuid);


SELECT orders_table.card_number
FROM orders_table
LEFT JOIN dim_card_details
ON orders_table.card_number = dim_card_details.card_number
WHERE dim_card_details.card_number IS NULL;

INSERT INTO dim_card_details (card_number)
SELECT DISTINCT orders_table.card_number
FROM orders_table
WHERE orders_table.card_number NOT IN
	(SELECT dim_card_details.card_number
	FROM dim_card_details);

ALTER TABLE orders_table
	ADD FOREIGN KEY (card_number)
	REFERENCES dim_card_details(card_number);
	
ALTER TABLE orders_table
	ADD FOREIGN KEY (date_uuid)
	REFERENCES dim_date_times(date_uuid);
	
ALTER TABLE orders_table
	ADD FOREIGN KEY (product_code)
	REFERENCES dim_products(product_code);
	
ALTER TABLE orders_table
	ADD FOREIGN KEY (store_code)
	REFERENCES dim_store_details(store_code);
	
ALTER TABLE orders_table
	ADD FOREIGN KEY (user_uuid)
	REFERENCES dim_users(user_uuid);