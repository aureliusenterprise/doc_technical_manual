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
*  a field which is associated with the quality result 

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
| timeliness	 | the data should be up to date			                   |
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
The field as well as a description of the data quality rule are entities in Aurelius Atlas, while the data actual data quality result is stored as metadata in elastic app search.

Data quality result
~~~~~~~~~~~~~~~~~~~

The data quality result in elastic app search is stored in the atlas-dev-quality engine. An example of the required documents is shown below. It contains all the conceptual elements explained in the previous section.

.. code-block:: javascript

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

.. code-block:: javascript

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
In a later version of Aurelius Atlas, all changes to data quality or the governance structures in Aurelius Atlas will also propagate data quality results.
A description on how to setup the script and how to run it will follow shortly.



The Data quality rules
~~~~~~~~~~~~~~~~~~~~~~

They are located at the m4i-data-management repository https://gitlab.com/m4i/m4i-data-management/-/tree/master/m4i_data_management/core/quality/rules
on gitlab. In the rules file you can find all the data quality rules, that you can apply on a dataset. They are explanations of each rule and examples on how to use them.
These are they data quality rules that are applied on a dataset.

Below is a brief description of each rule. (This file is found in the rules folder of m4i-data-management). The reason we provide this information is to give
some insight for a first time user.


  

+------------------+-----------------------------------------------------------------+
| Rule             | Description                                                     |
+==================+=================================================================+
|                  |                                                                 |
| Biijacency       | Checks whether or not the values in the given `column_a` and    |
|                  | `column_b` only occur as a unique combination.                  |
+------------------+-----------------------------------------------------------------+
|                  |                                                                 |
| Compare first    | Checks whether the first 'number_of_characters' values in       |
| characters       | `first_column_name` and `second_column_name` are similar, and if|
|                  | the values are None or NaN.                                     |
+------------------+-----------------------------------------------------------------+
|                  |                                                                 |           
| Compare first    | Checks whether the first 'number_of_characters' values starting |
| characters       | without in `first_column_name` and `second_column_name` are     |
| starting without | similar, and if `column_name` does not start with any of the    |
|                  | given `prefixes`, and if the values are None or NaN.            |
+------------------+-----------------------------------------------------------------+
|                  |                                                                 |
| Completeness     | Checks whether the values in the column with the given          |
|                  | `column_name` are None or NaN.                                  |
+------------------+-----------------------------------------------------------------+
|                  |                                                                 |
| Conditional      | Checks whether or not the values in the given `value_column`    |
| completeness     | are `None` or `NaN`.                                            |
+------------------+-----------------------------------------------------------------+
|                  |                                                                 |
| Conditional      | Checks if values in the column with the given `value_column`    |
| unallowed text   | contain a specific unallowed `text`.                            |
+------------------+-----------------------------------------------------------------+
|                  |                                                                 |
| Conditional value| Checks whether the values in the given `value_column` match     |
|                  | (one of) the expected value(s) for a given key in the           |
|                  | `key_column`.                                                   |
+------------------+-----------------------------------------------------------------+
|                  |                                                                 |
| Contains         | Checks how many times the values in the column with the given   |
| character        | `column_name` contain a specific character.                     |
+------------------+-----------------------------------------------------------------+
|                  |                                                                 |
| Formatting       | Checks whether or not the values in the column with the given   |
|                  | `column_name` match the given `pattern`.                        |
+------------------+-----------------------------------------------------------------+
|                  |                                                                 |
| Invalidity       | Checks whether or not the values in the column with the given   |
|                  | `column_name` does not exist in the given list of `values`.     |
+------------------+-----------------------------------------------------------------+
|                  |                                                                 |
| Length           | Checks if the number of characters of the values in the column  |
|                  | with the given `column_name` are equal to the `required_length`.|
+------------------+-----------------------------------------------------------------+
|                  |                                                                 |
| Range            | Checks whether or not the values in the column with the given   |
|                  | `column_name` are:                                              |
|                  | - Greater than or equal to the given `lower_bound`.             |
|                  | - Less than or equal to the given `upper_bound`.                |
+------------------+-----------------------------------------------------------------+
|                  |                                                                 |
| Starts with      | Checks whether or not the values in the column with the given   |
|                  | `column_name` start with any of the given `prefixes`.           |
+------------------+-----------------------------------------------------------------+
|                  |                                                                 |
| Unallowed text   | Checks if values in the column with the given `column_name`     |
+------------------+-----------------------------------------------------------------+
|                  |                                                                 |
| Uniqueness       | Checks whether the values in the column with the given          |
|                  | `column_name` are unique (duplicate value check).               |
+------------------+-----------------------------------------------------------------+
|                  |                                                                 |
| Validity         | Checks whether or not the values in the column with the given   |
|                  | `column_name` exist in the given list of `values`.              |
+------------------+-----------------------------------------------------------------+
|                  |                                                                 |
| Cross-Column     | Checks whether or not the combination of values in the given    |
| Validity         | `first_column_name` and `second_column_name` exist in the given |
|                  | list of valid `value_combinations`.                             |
+------------------+-----------------------------------------------------------------+                 





Data Quality Rules Examples With Code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


1. Bijacency

In our example,we are providing a dummy dataset and we are comparing the columns "id" and "name".

    

We provide a dummy data set in the code
We first run a test to see if the columns are bijacent. We are comparing "id" and "name".
    
    
       data = DataFrame([
        {
            "id": 1234,
            "name": "John Doe",
            "function": "Developer",
            "from": "01-01-2021"
        },
        {
            "id": 1234,
            "name": "John Doe",
            "function": "Senior developer",
            "from": "01-01-2022"
        }
    ])


This is the function that we are using: bijacency(data, "id", "name"). The inputs are the dataset and the column names.
We have same id and name in this example, which means they are bijacent. We will get an output 1.




2. Compare First characters


Checks whether the first 'number_of_characters 'values in `first_column_name` and `second_column_name` are similar, and if the values are None or NaN.

We provide this dummy data and we will compare the first two characters of the id and name.

 data = DataFrame([
        {
            "id": "NL.xxx",
            "name": "NL.xxx",

        }

This is the function that we are using: compare_first_characters(data, "id", "name", 2). The inputs are the dataset,the column names and the number of characters we want to compare.
Because they are the same the ouput will be 1.


   
      


3. Check First Characters using Prefix


This rule does three checks. It checks if the first characters are the same, if the have same prefix and if the values are Nan or none.


1) In are first example we provide a dummy dataset with two columns, id and name

   data = DataFrame([
        {
            "id": "BE.xxx",
            "name": "BE.xxx",

        }
    ])

We use as a prefix BE and we use the function: 
	compare_first_characters_starting_without(data, "id", "name", 2, 'BE')

we provide the dataset we are using, the column names, the number of characters we want to compare and the prefix.
The output will be 1, because the charaters are the same and have the prefix too.
    


4. Check Completeness

Checks whether the values in the column with the given `column_name` are None or NaN. 
    
    
We provide a data dummy test in the unit test and we want to check if the column 'name' has a value or not. If it has a value the
function will return 1, otherwise it will return 0
    
    data = DataFrame([
        {
            "id": 1234,
            "name": NaN,
            "function": "Developer",
            "from": "01-01-2021"
        }

 This is the function tha we will use. The inputs are data and the name of the column we want to check.
     
	 completeness(data, "name")
 
 The output here will be 0, because the column 'name' has no value in it.


5. Check Conditional Completeness


We are checking that the columns "value" and "conditional" are 'None' or 'NaN'. But before we do that we filter out the rows
where the value of the 'key_column', in not a substring of the given value in the function. In ths example the key column in "conditional"
and we are seeing if it has a substring of the list values.

  values = ['.TMP', '.FREE']
 ['.TMP', '.FREE']
    data = DataFrame([
        {
            "value": "Something",
            "conditional": "xx.FREE.eur"
        }
    ])

This is the function we are using. The inputs are data, the name of the columns and the list of given values.

conditional_completeness(data, "conditional", "value", values)

The output here will be 1, because they are no empty values in the columns and the column "conditional" has substrings of the given 
values= ['.TMP', '.FREE']






6. Check Unallowed Text


We are checking if there is unalllowed text in the columns of the dummy dataframe. 


     values = ['.TMP', '.FREE']

    unallowed_text_item = "("

    data = DataFrame([
        {
            "value": "Something",
            "conditional": "xx.FREE.eur"
        }
    ])

This is the function we are using. The inputs are is the dataframe, the name of the two columns, the values of the substrings and the unallowed text.

    conditional_unallowed_text(data, "conditional", "value", values, unallowed_text_item)

The output will be 1 because it containf substrings in the 'conditional'  column and doesn't contain the unalloed text in column "Value". If it did the output would be 0.




7. Check Conditional Value


We are checking the 'value' and 'conditional' column to see if it contains the expected values of the 'key' values object.

    values = {"xx.TMP": "XX No Grade"}    (this is dictionary with it's key and value)

    data = DataFrame([                    (this is our dummy dataset)
        {
            "value": "XX No Grade",
            "conditional": "xx.TMP"
        }
    ])

this is the function we ae using. The inputs are data of the dummy dataset, the names of the columns which are "value" and "conditional" and the values, that are the substrings we want to check.
    
    result = conditional_value(data, "conditional", "value", values) 
The output here will 1, because "value" column, contains an expecetd value. Otherwise it would be 0.



8. Check Character Count


 Checks how many times the values in the column with the given `column_name` contain a specific character. 


We provide a dummy dataframe with one column called "id". 

  data = DataFrame([
        {
            "id": "12.12"
        }
    ])

This is the function that we use. The inputs are data, name of the column, the character we want to check and 1 is the expected count
    
    contains_character(data, "id", ".", 1)  


We want to check if the the id contains "." . The output will be 1 because the "id" column contains "."


9. Check Matching Pattern


In this example we are checking if the values in the column `name` match the given `pattern`.

We provide a dummy dataset

data = DataFrame([
        {
            "name": 'ExampleText'
        }
    ])


This is the function that we are using. The inputs are the dataset we are using,the column "name" and the pattern we want to see match 

formatting(data, "name", r'^[a-zA-Z]+$')


The ouput will be 1 in this example, because 'ExampleText' matches the pattern.



10. Check Invalidity


In this example we are checking if the values  in the column with the given name `value` does not exist in the given list of `exampleValues`.

We provide a list of the example values and a dummy dataframe.

  exampleValues = ['x', 'X', 'TBD', 'Name']

    data = DataFrame([
        {
            "value": "X"
        }
    ])

The funtion we are using is called invalidity. The inputs are data, column name and the list of values we want to check.

    invalidity(data, "value", exampleValues)

The output here will be 1 , becaue "X" is in the list of values.


11. Check Length

In this example we are checking if the number of characters of the values in the column `id` are equal to the `required_length`. 


We provide a dummy dataframe with column name "id"

 data = DataFrame([
        {
            "id": "1234"
        }
    ])

We are using this function length. The inputs are data, column name and the length of required characters.
    
    length(data, "id", 4)

The output will be 1 because the length of id is 4.


12. Check Range


In this example we checking if the values in the column  `column_name` are greater than or equal to the given `lower_bound` or less than or equal to the given `upper_bound`.

We provide a dummy dataframe for this example with column name "value"

 
 data = DataFrame([
        {
            "value": 0.1
        }
    ])


We are using this function. Th inputs are the dataframe, the column name and the range (The upper and lower bound)

    range(data, "value", 0, 1)


The output will be 1 because o,1 is between 0 and 1.


13. Check Prefix


In this example we are checking if the values in the column `column_name` start with any of the given `prefixes`.


 data = DataFrame([
        {
            "id": 1234
        }
    ])



This is the function we are using. The inputs are the data the column name and the prefix.

    starts_with(data, "id", "1")

The output wil be 1, because "1" is in the value of the id column.



14. Check Unallowed Text


In this example we are checking if the values in the column `Organisation` contain a specific unallowed `text`.

We provide a dummy dataset.



     data = DataFrame([
        {
            "Organisation": "Something Else"
        }
    ])


This is the function we are using. The inputs are data, the column name and the unallowed text

    unallowed_text(data, "Organisation", "BG Van Oord")

The output will be 1 because "BG Van Oord" is not in the "Something Else" of the "Organisation" column.


15. Check Uniqueness


In this example we are checking if the values in the column `id` are unique. We are looking for duplicate values

We provide a dummy dataset

 data = DataFrame([
        {
            "id": "1234"
        },
        {
            "id": "1234"
        },
        {
            "id": "2345"
        }
    ])


This is the function we are using. The inputs are the dataset and the name of the column.
    
    uniqueness(data, "id")

The output will be 0, because the "id" column conatins duplicate values



16. Check Validity

In this example we are checking if the values in the column `value` exist in the list of exampleValues.

We provide the values in the example list and a dummy dataset

exampleValues = ['Definite Contract', 'Indefinite Contract']

    data = DataFrame([
        {
            "value": "Definite Contract"
        }
    ])

This is the function we are using. The inputs are data, the column name and the list of example values.
    
    result = validity(data, "value", exampleValues)

The output will 1, because the value of the column exists in the example list.



Apply Data Quality results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~


1. First we want to upload a file, where we define the rules that we want to apply to the data. We push this file to atlas.

2. Then we get the data quality rules from atlas and see our data quality results. Our quality results have a data quality score. 1 is compiant and 0 is non-compliant

3. Finally we want to push our data quality results to kafka.


    


