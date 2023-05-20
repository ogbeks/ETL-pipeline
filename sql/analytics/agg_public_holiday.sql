WITH orders AS (
  SELECT * 
  FROM {schema_name}.orders
),

dim_dates AS(
  SELECT * 
  FROM if_common.dim_dates
),

orders_public_holiday AS(
  SELECT 
    o.order_id,
    o.order_date,
    CAST(DATE_PART('YEAR',o.order_date) AS INT) AS year_num,
    CAST(DATE_PART('MONTH',o.order_date) AS INT) AS month_num
    
  FROM orders AS o 
  JOIN dim_dates cdd 
    ON o.order_date = cdd.calendar_dt 
  WHERE 
    day_of_the_week_num BETWEEN 1 AND 5 
    AND NOT working_day
)

SELECT 
  CURRENT_DATE AS ingestion_date,
  year_num,
  COUNT(month_num=1 OR NULL) tt_order_hol_jan,
  COUNT(month_num=2 OR NULL) tt_order_hol_feb,
  COUNT(month_num=3 OR NULL) tt_order_hol_mar,
  COUNT(month_num=4 OR NULL) tt_order_hol_apr,
  COUNT(month_num=5 OR NULL) tt_order_hol_may,
  COUNT(month_num=6 OR NULL) tt_order_hol_jun,
  COUNT(month_num=7 OR NULL) tt_order_hol_jul,
  COUNT(month_num=8 OR NULL) tt_order_hol_aug,
  COUNT(month_num=9 OR NULL) tt_order_hol_sep,
  COUNT(month_num=10 OR NULL) tt_order_hol_oct,
  COUNT(month_num=11 OR NULL) tt_order_hol_nov,
  COUNT(month_num=12 OR NULL) tt_order_hol_dec

FROM orders_public_holiday oph

GROUP BY
  CURRENT_DATE,
  year_num
