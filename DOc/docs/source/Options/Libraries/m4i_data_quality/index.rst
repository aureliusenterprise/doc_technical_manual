.. _m4i_data_quality_index:


Data Quality
============

Is used to determine the quality of various entities already loaded into DMP's governance tool - Apache Atlas. 
It verifies data loaded against various m4i types ( like m4i_data_domain, m4i_data_entity ) on quality measures like completeness, uniqueness etc.

There are two main categories of Data that is generated for each m4i Type entity. 
 
   * Attributes related data
     consists of details about entity attributes where certain quality metrics can be applied like 
       * completeness -- whether we have a value for an attribute
       * uniqueness -- whether values are unique for different entities
       
   * Relationships related data
     consists of details about entity relationships where certain quality metrics can be applied like
       * completeness -- whether we have correct relationships between two entities.
     
These rules are inherited from `m4i_data_management` repository.

Configuring Rules
------------------
An important aspect of Data Quality is the rules that are applied to each entity. 
There are separate rules for attributes and relationships. However, the structure is same and follows as below.


id: id

expressionVersion: version of expression

expression: expression to evaluate `completeness('name')`

qualifiedName: unique name for the rule example:`m4i_data_domain--name`

qualityDimension: Rule Category - explained below

ruleDescription: Description of the rule ex:`name is not None and is not empty`

active: 0 | 1 

type: attribute | relationship


+-----------------+-------------------------------------+
| Rule Category   | Rule Description                    |
+=================+=====================================+
| completeness    | degree to which data is not null    |
+-----------------+-------------------------------------+
| accuracy        | degree to which a column conforms   |
|                 | to a standard                       |
+-----------------+-------------------------------------+
| validity        | degree to which the data comply     |
|                 | with a predefined structure         |
+-----------------+-------------------------------------+
| uniqueness      | degree to which the data has a      |
|                 | unique value                        |
+-----------------+-------------------------------------+
| timeliness      | the data should be up to date       |
+-----------------+-------------------------------------+

Example

id: 1

expressionVersion: 1

expression: completeness('name')

qualifiedName: m4i_data_domain--name

qualityDimension: completeness

ruleDescription: name is not None and is not empty

active: 1

type: attribute

`Rules` are maintained in `rules` directory of the package and can be found for each m4i type.

Running the code
-----------------
We can execute `run.py` file. This will generates 6 files in output folder of the package. Three each for attributes 
and relationships. In addition, generated data is pushed to Elasticsearch indexes. We can configure pre-fix of indexes by updating
`elastic_index_prefix` for both attributes and relationships related data.

* Summary -- gives a summary of the data quality results.
* Complaint Data -- gives information about complaints.
* Non-complaint Data -- gives information about non-complaints.

Dependency
-----------
To Run this package, we need to have below packages installed
* `m4i_atlas_core` -- communicates with Apache Atlas
* `vox-data-management` -- communicates for Quality metric already defined
* `elasticsearch` -- communicates with ElasticSearch

Installation
-------------

Please ensure your `Python` environment is set on version `3.7`. Some dependencies do not work with any later versions of `Python`.
Basically, this is a requirement for underlying package `m4i_data_management`

To install `m4i-atlas-core` and all required dependencies to your active `Python` environment. Activate it using:

`source <venv_name>\bin\activate` or create new `python3.7 -m venv <venv_name>`

Configurations and Credentials
-------------------------------

Please make a copy of `config.sample.py` and `credentials.sample.py` and rename the files to `config.py` and `credentials.py` respectively.
Please set the configuration parameters and credentials for `atlas` and `elastic` as below.

`credentials.py`
Should contain two dictionaries viz `credential_atlas` and `credential_elastic`

+----------------------------------------------+-------------------------------------------------------------------+
| Name                                         | Description                                                       |
+==============================================+===================================================================+
| credential_atlas[atlas.credentials.username] | The Username to be used to access the Atlas Instance.             |
+----------------------------------------------+-------------------------------------------------------------------+
| credential_atlas[atlas.credentials.password] | The Password to be used to access the Atlas Instance must         |
|                                              | correspond to the Username given.                                 |
+----------------------------------------------+-------------------------------------------------------------------+
| credential_elastic[elastic_cloud_id]         | Service URL for Elastic.                                          |
+----------------------------------------------+-------------------------------------------------------------------+
| credential_elastic[elastic_cloud_username]   | The Username to be used to access the Elastic Instance.           |
+----------------------------------------------+-------------------------------------------------------------------+
| credential_elastic[elastic_cloud_password]   | The Password to be used to access the Elastic Instance must       |
|                                              | correspond to the Username given.                                 |
+----------------------------------------------+-------------------------------------------------------------------+





`config.py`
Should contain two dictionaries viz `config_elastic` and `config_atlas`

+------------------------------------------+------------------------------------------------------------------+
| Name                                     | Description                                                      |
+==========================================+==================================================================+
| config_elastic[elastic_index_prefix]     | Define prefix for the elastic Index where data will be pushed to |
+------------------------------------------+------------------------------------------------------------------+
| config_atlas[atlas.server.url]           | The Server URL that Atlas runs on, with `/api/atlas` post fix.   |
+------------------------------------------+------------------------------------------------------------------+
| config_atlas[atlas.credentials.token]    | Add Keycloak access token                                        |
+------------------------------------------+------------------------------------------------------------------+


Execution 
-----------

1. Create the Python Environment. How to do this can be found in this file under `Installation` 
2. Fill in the Configurations and Credentials as indicated in this file under `Configurations and Credentials` 
3. Run `scripts\run.py` to create 6 files in output folder, 3 each for Attributes and Relationships. Same data is also 
pushed to Elastic.  
   1. creates/updates an index for attributes as `<prefix>`_quality_attr_[ summary | complaint | non_complaint]
   2. creates/updates an index for relationships as `<prefix>`_quality_rels_[ summary | complaint | non_complaint]

