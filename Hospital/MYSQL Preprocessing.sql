create database Hospital;
use Hospital;
CREATE TABLE hospital_clean AS
SELECT DISTINCT * FROM Hospital_1;

CREATE TABLE departments_clean AS
SELECT DISTINCT * FROM departments;

CREATE TABLE physicians_clean AS
SELECT DISTINCT * FROM physicians;

CREATE TABLE skus_clean AS
SELECT DISTINCT * FROM skus;

CREATE TABLE vendors_clean AS
SELECT DISTINCT * FROM vendors;

CREATE TABLE inventory_clean AS
SELECT DISTINCT * FROM inventory;

CREATE TABLE patients_clean AS
SELECT DISTINCT * FROM patients;

CREATE TABLE purchase_orders_clean AS
SELECT DISTINCT * FROM purchase;

CREATE TABLE deliveries_clean AS
SELECT DISTINCT * FROM delivery;

CREATE TABLE transactions_clean AS
SELECT DISTINCT * FROM transactions;

CREATE TABLE Analytics_clean AS
SELECT DISTINCT * FROM Analytics;

CREATE TABLE inventory_clean AS
SELECT DISTINCT * FROM inventory;

------------------------------------------------------
-- 3. Handle Missing Values
------------------------------------------------------

-- Example: Replace NULL department names with 'Unknown'
UPDATE departments_clean
SET dept_name = 'Unknown'
WHERE dept_name IS NULL;

-- Example: Replace NULL physician specialties with 'General'
UPDATE physicians_clean
SET specialty = 'General'
WHERE specialty IS NULL;

-- Example: Replace missing vendor names
UPDATE vendors_clean
SET vendor_name = 'Unknown Vendor'
WHERE vendor_name IS NULL;

-- Example: Fill missing patient gender with 'Not Specified'
UPDATE patients_clean
SET age_group = 'Not Specified'
WHERE age_group IS NULL;

UPDATE patients_clean
SET admission_date = STR_TO_DATE(admission_date, '%d-%m-%Y')
WHERE admission_date IS NOT NULL;

UPDATE transactions_clean
SET transaction_date = STR_TO_DATE(transaction_date, '%d-%m-%Y')
WHERE transaction_date IS NOT NULL;

UPDATE deliveries_clean
SET delivery_date = STR_TO_DATE(delivery_date, '%d-%m-%Y')
WHERE delivery_date IS NOT NULL;

UPDATE purchase_orders_clean 
SET po_date = STR_TO_DATE(po_date, '%d-%m-%Y')
WHERE po_date IS NOT NULL;

------------------------------------------------------
-- 4. Standardize Data Types
------------------------------------------------------

-- Convert date columns to DATE type
ALTER TABLE patients_clean 
MODIFY admission_date DATE;

ALTER TABLE transactions_clean 
MODIFY transaction_date DATE;

ALTER TABLE deliveries_clean 
MODIFY delivery_date DATE;

ALTER TABLE purchase_orders_clean 
MODIFY po_date DATE;

-- Ensure numeric columns are numeric
ALTER TABLE inventory_clean 
MODIFY current_stock INT,
MODIFY stock_value DECIMAL(10,2);

ALTER TABLE transactions_clean 
MODIFY quantity_consumed INT,
MODIFY unit_cost DECIMAL(10,2);

------------------------------------------------------
-- 5. Apply Data Quality Rules
------------------------------------------------------

-- Remove rows with negative costs
DELETE FROM transactions_clean
WHERE unit_cost < 0;

DELETE FROM inventory_clean
WHERE stock_value < 0 OR current_stock < 0;

-- Ensure patient age is reasonable (0–120 years)
DELETE FROM patients_clean
WHERE TIMESTAMPDIFF(YEAR, admission_date, CURDATE()) NOT BETWEEN 0 AND 120;

-- Drop rows with empty strings in key fields (example: patient_id, sku_id)
DELETE FROM patients_clean WHERE patient_id = '' OR patient_id IS NULL;
DELETE FROM skus_clean WHERE sku_id = '' OR sku_id IS NULL;
DELETE FROM transactions_clean WHERE transaction_id = '' OR transaction_id IS NULL;

------------------------------------------------------
-- 6. Final Clean Verification
------------------------------------------------------

-- Count after cleaning
SELECT 'hospital_clean', COUNT(*) FROM hospital_clean
UNION ALL
SELECT 'departments_clean', COUNT(*) FROM departments_clean
UNION ALL
SELECT 'physicians_clean', COUNT(*) FROM physicians_clean
UNION ALL
SELECT 'skus_clean', COUNT(*) FROM skus_clean
UNION ALL
SELECT 'vendors_clean', COUNT(*) FROM vendors_clean
UNION ALL
SELECT 'inventory_clean', COUNT(*) FROM inventory_clean
UNION ALL
SELECT 'patients_clean', COUNT(*) FROM patients_clean
UNION ALL
SELECT 'purchase_orders_clean', COUNT(*) FROM purchase_orders_clean
UNION ALL
SELECT 'deliveries_clean', COUNT(*) FROM deliveries_clean
UNION ALL
SELECT 'transactions_clean', COUNT(*) FROM transactions_clean
UNION ALL
SELECT 'analytics_clean', COUNT(*) FROM analytics_clean;

