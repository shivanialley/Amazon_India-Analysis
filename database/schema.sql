-- =====================================================
-- Amazon India Sales Analytics Database Schema
-- =====================================================

-- -----------------------------
-- 1. Customers Table
-- -----------------------------
CREATE TABLE IF NOT EXISTS customers (
    customer_id        VARCHAR(50) PRIMARY KEY,
    customer_city      VARCHAR(50),
    customer_state     VARCHAR(50),
    customer_tier      VARCHAR(20),   -- Metro / Tier1 / Tier2 / Rural
    is_prime_member    BOOLEAN,
    age_group          VARCHAR(20)
);

-- -----------------------------
-- 2. Products Table
-- -----------------------------
CREATE TABLE IF NOT EXISTS products (
    product_id         VARCHAR(50) PRIMARY KEY,
    product_name       VARCHAR(200),
    category            VARCHAR(100),
    brand               VARCHAR(100),
    original_price_inr  FLOAT
);

-- -----------------------------
-- 3. Time Dimension Table
-- -----------------------------
CREATE TABLE IF NOT EXISTS time_dimension (
    date_id     DATE PRIMARY KEY,
    year        INT,
    month       INT,
    month_name  VARCHAR(15),
    quarter     VARCHAR(2),
    day         INT,
    week        INT
);

-- -----------------------------
-- 4. Transactions Fact Table
-- -----------------------------
CREATE TABLE IF NOT EXISTS transactions (
    transaction_id     VARCHAR(50) PRIMARY KEY,
    order_date         DATE NOT NULL,
    customer_id        VARCHAR(50),
    product_id         VARCHAR(50),
    final_amount_inr   FLOAT,
    discount_percent   FLOAT,
    payment_method     VARCHAR(30),
    is_festival_sale   BOOLEAN,
    delivery_days      INT,
    return_status      VARCHAR(20),

    -- Foreign Keys
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (order_date) REFERENCES time_dimension(date_id)
);

-- -----------------------------
-- 5. Indexes (Performance Boost)
-- -----------------------------
CREATE INDEX idx_order_date ON transactions(order_date);
CREATE INDEX idx_customer ON transactions(customer_id);
CREATE INDEX idx_product ON transactions(product_id);
CREATE INDEX idx_city ON customers(customer_city);
CREATE INDEX idx_category ON products(category);
