.. _m4i_data_dictionary_index:


m4i_data_dictionary_io
-----------------------

This library contains all core functionality for reading Data Dictionary excels and pushing the defined entities in bulk
by type to atlas. Data Dictionary is expected to be in the same format as the template Data Dictionary.

Installation
-------------

Please ensure your `Python` environment is on version `3.9`. Some dependencies do not work with any previous versions
of `Python`.

To install `m4i-data-dictionary-io` and all required dependencies to your active `Python` environment, please run the
following command from the project root folder:

```
pip install -e .
```

Configurations and Credentials
-------------------------------

In the `scripts` directory. Please make a copy of `config.sample.py` and `credentials.sample.py` and rename the files
to `config.py` and `credentials.py` respectively. Please set the configuration parameters and credentials for `atlas`.

| Name | Required | Description | 
|---|---|---|
| atlas.server.url | True |  The Server Url that Atlas runs on, with '/api/atlas' post fix. | 
| validate_qualified_name | False | If to validate the qualified Names given. This is default to True, however, if the entities provided in the data dictionary do not follow the qualified Name schema, the validation can be turned off by setting this configuration to False. |
| data.dictionary.path | True |  The Path to the Data Dictionary to be loaded.| 
| atlas.credentials.username | True |  The Username to be used to access the Atlas Instance. | 
| atlas.credentials.password | True | The Password to be used to access the Atlas Instance must correspond to the Username given. | 

Execution
----------

1. Create the Python Environment. How to do this can be found in this file under `Installation`
2. Fill in the Configurations and Credentials as indicated in this file under `Configurations and Credentials`
3. Run `main.py` in the terminal to load the definitions.

Testing
--------

This project uses `pytest` as its unit testing framework. To run the unit tests, please install `pytest` and then
execute the `pytest` command from the project root folder.

Unit tests are grouped per module. Unit test modules are located in the same folder as their respective covered modules.
They can be recognized by the `test__` module name prefix, followed by the name of the covered module.





