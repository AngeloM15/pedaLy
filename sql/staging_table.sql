-- Creation of staging table
CREATE TABLE IF NOT EXISTS raw_data
(
    manufacturer VARCHAR,
    made_in varchar,
    fx varchar,
    "type" varchar,
    jacks_mounted_on varchar,
    bypass varchar,
    battery varchar,
    voltage varchar,
    polarity varchar,
    circuit varchar,
    tube_equipped varchar,
    weight_in_kg varchar,
    famous_users varchar,
    width_in_cm varchar,
    height_in_cm varchar,
    depth_in_cm varchar,
    gtin_14 varchar,
    additional_fx varchar,
    based_on_famous_model varchar,
    series varchar,
    video varchar,
    special_features varchar,
    "year" varchar,
    colour varchar,
    serial_number varchar,
    manufacturer_part_number varchar,
    gtin_12 varchar,
    "url" varchar,
    "name" varchar
);
 
-- Fill table
COPY raw_data FROM '/data/results.csv' DELIMITER ',' CSV HEADER;