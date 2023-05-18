CREATE TABLE shipments_deliveries (

    shipment_id INT PRIMARY KEY  NOT NULL,
    order_id INT NOT NULL,
    shipment_date DATE NOT NULL,
    delivery_date DATE NOT NULL
    -- Unable to create the foreign key relationship due to constraint error in the if_common schema
    --FOREIGN KEY (product_id) REFERENCES if_common.dim_products(product_id)
    -- ON UPDATE CASCADE ON DELETE CASCADE 
)