WITH reviews AS (
  SELECT * 
  FROM {schema_name}.reviews
),

orders AS (
  SELECT * 
  FROM {schema_name}.orders
),

shipments_deliveries AS (
  SELECT * 
  FROM {schema_name}.shipments_deliveries
),

dim_dates AS(
  SELECT * 
  FROM if_common.dim_dates
),

reviews_counts AS (
SELECT 
  product_id,
  COUNT(*) tt_review_points,
  COUNT(review=1 OR NULL) one_star_review,
  COUNT(review=2 OR NULL) two_star_review,
  COUNT(review=3 OR NULL) three_star_review,
  COUNT(review=4 OR NULL) four_star_review,
  COUNT(review=5 OR NULL) five_star_review

FROM reviews
GROUP BY product_id
),
products_reviews AS (
SELECT 
  product_id,
  tt_review_points,
  one_star_review / CAST(tt_review_points AS FLOAT) pct_one_star_review,
  two_star_review / CAST(tt_review_points AS FLOAT) pct_two_star_review,
  three_star_review / CAST(tt_review_points AS FLOAT) pct_three_star_review,
  four_star_review / CAST(tt_review_points AS FLOAT) pct_four_star_review,
  five_star_review / CAST(tt_review_points AS FLOAT) pct_five_star_review
FROM reviews_counts
),

products_orders AS (
  SELECT 
    o.product_id,
    order_date,
    COUNT(*) total_orders,
    COUNT(*) 
      FILTER (
        WHERE shipment_date - order_date>=6 AND delivery_date IS NULL
      )
    AS tt_late_shipments,
    (
      COUNT(*)-
      COUNT(*) 
        FILTER (
          WHERE shipment_date - order_date>=6 AND delivery_date IS NULL
        )
    ) AS tt_early_shipments
  FROM orders o
  JOIN shipments_deliveries sd
  ON sd.order_id = o.order_id 
  GROUP BY
    product_id,
    order_date
)

SELECT DISTINCT
  product_id,
  FIRST_VALUE(order_date) OVER (PARTITION BY product_id ORDER BY total_orders DESC, order_date DESC) AS most_ordered_day,
  SUM(total_orders) OVER (PARTITION BY product_id) AS tt_orders,
  SUM(tt_early_shipments) OVER (PARTITION BY product_id)/ CAST(SUM(total_orders) OVER (PARTITION BY product_id) AS FLOAT) AS pct_early_shipments,
  SUM(tt_late_shipments) OVER (PARTITION BY product_id)/ CAST(SUM(total_orders) OVER (PARTITION BY product_id) AS FLOAT) AS pct_late_shipments

FROM products_orders po

WINDOW
  by_product AS(
    PARTITION BY product_id
  ),
  by_product_orders AS(
    by_product 
    ORDER BY total_orders DESC, order_date DESC
  )



