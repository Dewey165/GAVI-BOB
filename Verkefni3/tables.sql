 
CREATE TABLE catagories (
catagory_id SERIAL,
name VARCHAR(250)
PRIMARY KEY(catagory_id)
);

CREATE TABLE units (
unit_id SERIAL,
catagory_id INT REFERENCES catagories(catagory_id),
unit_ton NUMERIC,
unit_cost NUMERIC,
unit_total NUMERIC,
year INT
PRIMARY KEY(unit_id)
);