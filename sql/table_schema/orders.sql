CREATE TABLE IF NOT EXISTS {schema_name}.orders (
    order_id INT PRIMARY KEY NOT NULL,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    product_id VARCHAR NOT NULL,
    unit_price INT NOT NULL,
    quantity INT NOT NULL,
    amount INT NOT NULL
    -- Unable to create the foreign key relationship due to constraint error in the if_common schema
    --FOREIGN KEY (product_id) REFERENCES if_common.dim_products(product_id)
    -- ON UPDATE CASCADE ON DELETE CASCADE 
)