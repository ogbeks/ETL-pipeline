CREATE TABLE IF NOT EXISTS  chukogbe1619_staging.shipments_deliveries (

    shipment_id INT PRIMARY KEY  NOT NULL,
    order_id INT NOT NULL,
    shipment_date DATE NULL,
    delivery_date DATE NULL
    -- Unable to create the foreign key relationship due to constraint error in the if_common schema
    --FOREIGN KEY (product_id) REFERENCES if_common.dim_products(product_id)
    -- ON UPDATE CASCADE ON DELETE CASCADE 
)