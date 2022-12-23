Data Quality
==============

Data quality can be measured on the actual data. It describes the percentage e.g. a column in a database table is fulfilling a certain condition, like e.g. to be not empty.
Since actual data is required for this assessment, this analysis can not be done in Aurelius Atlas itself, but is performed on the related data storage system. The quality results however,
can be documented in Aurelius Atlas. This documentation contains the checked rules as well as the actual data quality complaince results.

Data quality results are then propagated along the breadcrumb of the field to datasets, collections and systems on the technical side and to data attributes, data entities and data domains on the business side.

Conceptual view
---------------

Thus, conceptually data quality results can be added in Aurelius Atlas. It consits of 3 parts:

* the actual data quality result
*  an associated data quality Atlas entity
*  a field which is assicated with the quality result 

Data quality result
~~~~~~~~~~~~~~~~~~~

Data quality result consists of multiple fields:

* a unique ID, which can be human readable, but must be unique
* a qualityguid, which is a guid of the actual quality result	
* a data quality result (dqscore), which is a value between 0 and 1, where 0 mean 0% compliance and 1 means 100% compliance

Data quality rule
~~~~~~~~~~~~~~~~~

A data quality rule is described in Aurelius Atlas as type data quality rule. Currently you can not enter this quality rule via the front end.

A data quality rule consists of :

* name of the associated data quality rule
* data quality rule description: explaining the thought behind the data quality rule
* expression, which is constructuced from an expression language on the level of the data quality 
* business rule ID, which is usually just a number used for ordering the rules when presenting in the front end
* data quality rule dimension: 

+----------------+-------------------------------------------------------------+
| Rule Category  | Rule Description                                            |
+================+=============================================================+
| completeness	 | degree to which data is not null                            |
+----------------+-------------------------------------------------------------+
| accuracy       | degree to which a column conforms to a standard             |
+----------------+-------------------------------------------------------------+
| validity       | degree to which the data comply with a predefined structure |
+----------------+-------------------------------------------------------------+
| uniqueness   	 | degree to which the data has a unique value                 |
+----------------+-------------------------------------------------------------+
| timeliness	 | the data should be up to date			       |
+----------------+-------------------------------------------------------------+


Associated field
~~~~~~~~~~~~~~~~~

A field can be used in multiple data quality rules, thus a field may have multiple data quality results of different data quality rule dimensions. A field is referenced by the followign information:

* qualified name of the field used for the assessment
* fieldguid, that is the guid of the referenced field
* qualified field name


Technical view
--------------

Technically, data quality is represented in Aurelius Atlas as Apache Atlas concepts and as data in the metadata store (elastic app search).
The field as well as a description of the data quality rule are entities in Aurleius Atlas, while the data actual data quality result is stored as metadata in elastic app search.

Data quality result
~~~~~~~~~~~~~~~~~~~

The data quality result in elastic app search is stored in the atlas-dev-quality engine. An exmaple of the required documents is shown below. It contains all the conceptual elements explained in the previous section.

..code:: json
	{
		"id": "nl3--nl3plant--nl3plant001--workorderid--8",
		"fields": [{
				"name": "id",
				"value": "nl3--nl3plant--nl3plant001--workorderid--8",
				"type": "enum"
			}, {
				"name": "fieldqualifiedname",
				"value": "nl3--nl3plant--nl3plant001--workorderid",
				"type": "string"
			}, {
				"name": "fieldguid",
				"value": "21f89d8f-4e10-4419-b135-6a84d55ed63f",
				"type": "string"
			}, {
				"name": "qualityguid",
				"value": "61484c0e-89db-49ff-a67a-2e3bb2e9219c",
				"type": "string"
			}, {
				"name": "dataqualityruledescription",
				"value": "This field has to be filled at all times",
				"type": "string"
			}, {
				"name": "expression",
				"value": "Completeness('workorderid')",
				"type": "string"
			}, {
				"name": "dqscore",
				"value": "1.0",
				"type": "float"
			}, {
				"name": "dataqualityruledimension",
				"value": "Completeness",
				"type": "string"
			}, {
				"name": "businessruleid",
				"value": "8.0",
				"type": "float"
			}, {
				"name": "name",
				"value": "Rule 8",
				"type": "string"
			}, {
				"name": "guid",
				"value": "61484c0e-89db-49ff-a67a-2e3bb2e9219c",
				"type": "string"
			}, {
				"name": "qualityqualifiedname",
				"value": "nl3--nl3plant--nl3plant001--workorderid--8",
				"type": "string"
			}, {
				"name": "datadomainname",
				"value": "plant data",
				"type": "string"
			}
		]
	}

Data quality rules
~~~~~~~~~~~~~~~~~~

Data quality rules are Apache Atlas entities, which can not be entered via the Aurelius Atlas frontend at the moment. We are working on it.

The entity contains the required fields as properties, such that they referential integrity between data quality results and the data quality rule entity are guaranteed.
An example of a data quality rule entity in json format as it is stored in Apache Atlas is shown below.

..code:: json
	{
		"referredEntities": {},
		"entity": {
			"typeName": "m4i_data_quality",
			"attributes": {
				"expression": "completeness('HIER_ORG')",
				"qualifiedName": "nl1--nl1hr--nl1hr001--hier_organization--30",
				"displayName": null,
				"description": null,
				"active": true,
				"businessRuleDescription": "",
				"ruleDescription": "This field has to be filled at all times",
				"name": "nl1--nl1hr--nl1hr001--hier_organization--30",
				"filterRequired": true,
				"id": 30,
				"qualityDimension": "Completeness",
				"expressionVersion": "1",
				"fields": [{
						"guid": "0df94338-1afc-455c-b9d5-c3d0e36d1dac",
						"typeName": "m4i_field",
						"uniqueAttributes": {
							"qualifiedName": "nl1--nl1hr--nl1hr001--hier_organization"
						}
					}
				]
			},
			"guid": "3059989c-364d-4404-92ef-c1e719014f00",
			"isIncomplete": false,
			"relationshipAttributes": {
				"fields": [{
						"guid": "0df94338-1afc-455c-b9d5-c3d0e36d1dac",
						"typeName": "m4i_field",
						"entityStatus": "ACTIVE",
						"displayText": "HIER_ORGANIZATION",
						"relationshipType": "m4i_data_quality_field_assignment",
						"relationshipGuid": "35b3502c-38a7-4524-b266-2fd46888e5f2",
						"relationshipStatus": "ACTIVE",
						"relationshipAttributes": {
							"typeName": "m4i_data_quality_field_assignment"
						}
					}
				],
			},
		}
	}

The relationship attribute fields is referencing the related field. The remaining values are local to the entity and some of them are referenced and/or taken over in the data quality result data structure.

Propagation of data quality results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After creating the data quality rule entity in Apache Atlas and data quality results in the metadata store, the data quality is accessible at the field. 
To propagate data quality results through the complete governance tree, currently there is a script required which can be called periodically. 
In a later version of Aurelius Atlas, all changes to data quality or the sovernance structures in Aurelius Atlas will also propagate data quality results.
A description on how to setup the script and how to run it will follow shortly.
