 
create table voruflokkar(
	name VARCHAR(250),
	year INT,
	PRIMARY KEY(name)
);

create table einingar(
	id INT,
	tonn INT,
	cif_verd_milljonir_krona INT,
	hlutfall_af_heild INT,
	name VARCHAR(250),
	PRIMARY KEY(id),
	FOREIGN KEY(name) REFERENCES voruflokkar(name)
);