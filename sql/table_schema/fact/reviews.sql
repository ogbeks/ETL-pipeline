CREATE TABLE IF NOT EXISTS  {schema_name}.reviews (
    review INT NOT NULL,
    product_id INT NOT NULL
    -- Unable to create the foreign key relationship due to constraint error in the if_common schema
    --FOREIGN KEY (product_id) REFERENCES if_common.dim_products(product_id)
    --ON UPDATE CASCADE ON DELETE CASCADE 
)
