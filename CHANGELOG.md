# Changelog

## Unreleased

## 5.0.1 - 2021-05-31

* Fix some migrations about the API in QGIS 3.16

## 5.0.0 - 2021-04-07

* Add button in the help menu to open the online webpage https://docs.3liz.org/qgis-gobs-plugin
* Raise the QGIS minimum version to 3.16
* Update the documentation website with MkDocs

## 0.4.3 - 2021-04-07

* Actor - Add a new "a_login" column with unique constraint
* Administration - Update QGIS admin project template
* Docs - Update Schemaspy

## 0.4.2 - 2021-03-15

* Import observations - specify the series spatial layer id to match spatial objects: fix some bugs if spatial objects shared the same codes for different spatial layers.
* Import - Spatial layer: add new SQL functions to check related observations
* Admin - Update the QGIS administration project template with the new document layer
* Doc - Update Schemaspy database documentation

## 0.4.1 - 2020-12-02

Admin - Update administration project template
Docs - Update admin guide
Docs - Add Processing documentation
Docs - Update SchemaSpy database structure documentation: https://docs.3liz.org/qgis-gobs-plugin/database/
Docs - Database doc generation: improve compatibility with PG13
Fix some packaging issues about Transifex

## 0.4.0 - 2020-12-02

* Database structure - Add needed tables and fields for G-Event API:
   - indicator: category, created_at and updated_at
   - observation: end timestamp, uid, created_at and updated_at
   - spatial object: start and end of validity dates, uid, created_at and updated_at
   - new table document to store indicator documents
   - new table deleted_data_log to store indicator documents
   - new trigger to calculate created_at and updated_at, and auto-change validity date for spatial objects
* Import - Observation data: manage new field end date (manual or from field)
* Import - Spatial layer objects: allow multiple versions with validity dates
* Test data - Add tracks data & update pluviometers and cities data
* Tests - Add test for the import spatial layer data algorithm
* Docs - Update database documentation
* Continuous Integration - Move from CI to GitHub actions
* Makefile - Add sql command to export & reformat SQL install scripts
* Docs - Improve administration guide

## 0.3.1 - 2020-08-12

* Documentation - Publish documentation to https://3liz.github.io/qgis-gobs-plugin/ (installation, concepts, admin guide, user guide & database)
* Algorithms - New algorithm to create a database local interface for admins as a QGIS project
* Active PostgreSQL connection - Use a QGIS project variable instead of a QGIS global variable to store the connection name used
* Dock - Reorganize buttons, display the chosen database connection on top
* Dock - Replace helps buttons by single online help button

## 0.3.0 - 2020-06-17

* Remove spatial layer data - new algorithm to proceed spatial layer data deletion
* Remove series data - new algorithm to proceed observation data deletion
* QGIS gobs_manager project - change SCR and map extent
* Get observation data - Add option to also get the corresponding geometry
* Publish on GitHub: https://github.com/3liz/qgis-gobs-plugin

## 0.2.11 - 2020-06-05

* Import scripts - Fix bugs related to old use of self.tr instead of tr

## 0.2.10 - 2020-05-28

* Import spatial layer - Fix bug with points & linestrings

## 0.2.9 - 2020-05-27

* Import observation data - Explicitly convert source value to target format and remove useless spaces from source data
* Import spatial layer - Check geometry types compatibility between QGIS layer and target spatial layer
* Demo data - fix encoding for sub-districts layer
* Continuous integration & test - many fixes and improvements

## 0.2.8 - 2020-05-05

* Import spatial layer data - Use ST_Buffer(geom, 0) to remove invalid geometries
* Import spatial layer data - Fix bug when opening form
* Documentation - Describe each algorithm usage and parameters.
* Documentation - Add 2 button to see Concepts and Database schema

## 0.2.7 - 2020-03-12

* Rename name, title, label, code fields into normalized code label
* Import observation data - Adapt alg inputs based on the indicator characteristics

## 0.2.6 - 2020-03-06

* Create db structure - Fix bug when adding test data
* Move comments in specific SQL script file

## 0.2.5 - 2020-02-24

* Database - Update installation scripts & documentation
* QGIS - Fix bug with indicator type values (remove default value)
* Import observation - add constraint to override data only if not yet validated
* Feedback - Use reportError instead of pushInfo when needed
* Import observation - Remove useless series id in the end of series combobox
* Get series data - Fix bug giving wrong vector dimensions && remove useless series id in combo boxes
