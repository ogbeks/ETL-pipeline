CREATE TABLE IF NOT EXISTS {schema_name}.agg_public_holiday (
    ingestion_date DATE PRIMARY KEY NOT NULL,
    --year_num INT NOT NULL,
    tt_order_hol_jan INT NOT NULL,
    tt_order_hol_feb INT NOT NULL,
    tt_order_hol_mar INT NOT NULL,
    tt_order_hol_apr INT NOT NULL,
    tt_order_hol_may INT NOT NULL,
    tt_order_hol_jun INT NOT NULL,
    tt_order_hol_jul INT NOT NULL,
    tt_order_hol_aug INT NOT NULL,
    tt_order_hol_sep INT NOT NULL,
    tt_order_hol_oct INT NOT NULL,
    tt_order_hol_nov INT NOT NULL,
    tt_order_hol_dec INT NOT NULL
)
   