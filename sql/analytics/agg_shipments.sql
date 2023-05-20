WITH orders AS (
  SELECT * 
  FROM {schema_name}.orders
),
shipments_deliveries AS (
  SELECT * 
  FROM {schema_name}.shipments_deliveries
),
shipments_orders AS (
  SELECT 
    sd.*,
    o.order_date

  FROM shipments_deliveries sd 

  JOIN orders o

  ON sd.order_id = o.order_id 
)
SELECT 
  CURRENT_DATE AS ingestion_date,
  COUNT(*) 
    FILTER (
      WHERE shipment_date - order_date>=6 AND delivery_date IS NULL
    )
  AS tt_late_shipments,
  COUNT(*)
    FILTER (
      WHERE shipment_date IS NULL AND delivery_date IS NULL AND MAKE_DATE(2022,09,05) - order_date >=15
    )
  AS tt_undelivered_items

FROM shipments_orders


