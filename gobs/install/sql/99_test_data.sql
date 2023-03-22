BEGIN;

-- TABLES
-- actor_category
INSERT INTO gobs.actor_category
(id, ac_label, ac_description)
VALUES
(1, 'Public organizations', 'Public organizations and stakeholders'),
(2, 'Research centers', 'Public or private research centers'),
(3, 'Individuals', 'Persons acting as a single individual')
;

-- actor
INSERT INTO gobs.actor
(id, a_label, a_description, a_email, id_category, a_login)
VALUES
(1, 'IGN', 'French national geographical institute.', 'contact@ign.fr', 1, 'ign'),
(2, 'CIRAD', 'The French agricultural research and international cooperation organization', 'contact@cirad.fr', 2, 'cirad'),
(3, 'DREAL Bretagne', 'Direction régionale de l''environnement, de l''aménagement et du logement.', 'email@dreal.fr', 1, 'dreal'),
(4, 'Al', 'Al A.', 'al@al.al', 3, 'al'),
(5, 'Bob', 'Bob B.', 'bob@bob.bob', 3, 'bob'),
(6, 'John', 'John J.', 'jon@jon.jon', 3, 'john'),
(7, 'Mike', 'Mike M.', 'mik@mik.mik', 3, 'mike'),
(8, 'Phil', 'Phil P.', 'phi@phi.phi', 3, 'phil')
;

-- indicator
INSERT INTO gobs.indicator
(id, id_code, id_label, id_description, id_date_format, id_paths, id_category)
VALUES
(1, 'pluviometry', 'Hourly pluviometry ', 'Hourly rainfall pluviometry in millimetre', 'hour', 'Environment / Water / Data | Physical and chemical conditions / Water ', 'Water'),
(2, 'population', 'Population ', 'Number of inhabitants for city', 'year', 'Socio-eco / Demography / Population ', 'Population'),
(3, 'hiker_position', 'Hikers position', 'Position and altitude of hikers', 'second', 'Hiking / Tracks', 'Tracks'),
(4, 'observation', 'Observations', 'Faunal observations in the field', 'second', 'Environment / Fauna / Species', 'Species')
;

-- dimension
INSERT INTO gobs.dimension
(id, fk_id_indicator, di_code, di_label, di_type, di_unit)
VALUES
(1, 1, 'pluviometry', 'Pluviometry', 'real', 'mm'),
(2, 2, 'population', 'Population', 'integer', 'people'),
(3, 3, 'altitude', 'Altitude', 'integer', 'm'),
(4, 4, 'number', 'Number of individuals', 'integer', 'ind'),
(5, 4, 'species', 'Observed species', 'text', 'sp')
;

-- document
INSERT INTO gobs.document VALUES
(1, '542aa72f-d1de-4810-97bb-208f2388698b', 'Illustration', 'Picture to use as the indicator illustration.', 'preview', 'hiker_position/preview/hiking.jpg', 3, '2022-10-11 08:30:18.012801', '2022-10-11 08:50:01.248526'),
(2, '1a7f7323-6b18-46ed-a9fe-9efbe1f006a2', 'Hiking presentation', 'Presentation of hiking.', 'document', 'hiker_position/document/hiking_doc.txt', 3, '2022-10-11 08:30:18.012801', '2022-10-11 08:50:01.248526')
;

-- protocol
INSERT INTO gobs.protocol
(id, pr_code, pr_label, pr_description)
VALUES
(1, 'pluviometry', 'Pluviometry', 'Measure of rainfall in mm'),
(2, 'population', 'Population', 'Number of inhabitants obtained from census.'),
(3, 'gps-tracking', 'GPS tracking', 'GPS position recorded by a smartphone containing timestamp at second resolution, position and altitude in meters.'),
(4, 'field_observations', 'Field observations on species', 'Go to the field, recognize the observed species and give the number of individuals.')
;

-- spatial_layer
INSERT INTO gobs.spatial_layer
(id, sl_code, sl_label, sl_description, sl_creation_date, fk_id_actor, sl_geometry_type)
VALUES
(1, 'pluviometers', 'Pluviometers', 'Sites equiped with pluviometers to measure rainfalls', '2019-06-26', 3, 'point'),
(2, 'brittany-cities', 'Cities of Brittany , France', 'Cities of Brittany, France', '2019-07-05', 1, 'multipolygon'),
(3, 'gpsposition', 'GPS position', 'Position of GPS trackers', '2020-09-10', 2, 'point'),
(4, 'faunal_observation', 'Position of faunal observations', 'Observations on species (lions, girafes, etc.)', '2022-09-10', 4, 'point')
;

-- series
INSERT INTO gobs.series
(id, fk_id_protocol, fk_id_actor, fk_id_indicator, fk_id_spatial_layer)
VALUES
(1, 1, 2, 1, 1),
(2, 2, 2, 2, 2),
(3, 3, 4, 3, 3),
(4, 3, 5, 3, 3),
(5, 3, 6, 3, 3),
(6, 3, 7, 3, 3),
(7, 3, 8, 3, 3),
(8, 4, 4, 4, 4)
;

-- SEQUENCES
SELECT pg_catalog.setval('gobs.actor_category_id_seq', 3, true);
SELECT pg_catalog.setval('gobs.actor_id_seq', 8, true);
SELECT pg_catalog.setval('gobs.indicator_id_seq', 4, true);
SELECT pg_catalog.setval('gobs.dimension_id_seq', 5, true);
SELECT pg_catalog.setval('gobs.document_id_seq', 2, true);
SELECT pg_catalog.setval('gobs.protocol_id_seq', 4, true);
SELECT pg_catalog.setval('gobs.spatial_layer_id_seq', 4, true);
SELECT pg_catalog.setval('gobs.series_id_seq', 8, true);

COMMIT;
