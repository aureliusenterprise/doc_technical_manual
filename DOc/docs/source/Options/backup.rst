.. role:: raw-html-m2r(raw)
   :format: html


Aurelius Atlas Backup
*********************

Here you will find how to back up Aurelius Atlas for moving instances.

This process will result in zip files of the Apache Atlas data and a Snapshot repository of Elasticsearch indices that can be used for backup and in the case of disaster recover process. 

Apache Atlas backup
===================

Apache Atlas Backup Process Overview
------------------------------------


.. image:: .images/backup-overview.png
   :target: .images/backup-overview.png


Acquire access token for Apache Atlas's admin user
--------------------------------------------------

You can use ``oauth.sh`` script from https://github.com/aureliusenterprise/Aurelius-Atlas-helm-chart. Example usage:

.. code-block:: bash

   export ACCESS_TOKEN=$(./oauth.sh --endpoint https://aureliusdev.westeurope.cloudapp.azure.com/demo/auth/realms/m4i/protocol/openid-connect/token \
   --client-id m4i_atlas \
   --access atlas $ATLAS_USER_PASSWD)

Export data from Apache Atlas
-----------------------------

You can use ``export-atlas.py`` script, that wraps Apache Atlas's `Export API <https://atlas.apache.org/index.html#/ExportAPI>`_ to export all data from Atlas. Example Usage:

.. code-block:: bash

   pip install urlpath
   python export-atlas.py --token $ACCESS_TOKEN \
   --base-url https://aureliusdev.westeurope.cloudapp.azure.com/demo/atlas2/ \
   --output out.zip

Import Backup to Atlas Instance
-------------------------------

Apache Atlas exposes an Import API from where data is imported from a zip file.
Admin user need rights are needed to use this api.
This command will import a file response.zip in the current directory to a specified atlas instance.

.. code-block:: bash

   curl -g -X POST -H 'Authorization: Bearer <Bearer-Token>' -H "Content-Type: multipart/form-data" -H "Cache-Control: no-cache" -F data=@response.zip <apache-atlas-url>/api/atlas/admin/import

Elasticsearch backup
====================

For Elasticsearch backup you can use `Snapshot and restore API <https://www.elastic.co/guide/en/elasticsearch/reference/current/snapshot-restore.html>`_.

Create a snapshot repository
----------------------------

Create a storage account and a container in Azure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Go to https://portal.azure.com/

#. Go to storage accounts service 

   .. image:: .images/storage_account_service.png
#. 
   Create a new storage account

   .. image:: .images/storage_account_create.png

#. 
   Set the account name. Optionally adjust the redundancy and access tier 

   .. image:: .images/storage_account_options1.png

   .. image:: .images/storage_account_options2.png

#. 
   Review and create

#. 
   Once the account is created, go to Containers tab 

   .. image:: .images/containers_tab.png

#. 
   Create a new container 

   .. image:: .images/containers_create1.png

   .. image:: .images/containers_create2.png

#. 
   Go to Access keys tab 

   .. image:: .images/access_keys_tab.png

Register a repository
^^^^^^^^^^^^^^^^^^^^^


#. Access Elastic's search pod/image, for example:

   .. code-block:: bash

      kubectl -n demo exec -it pod/elastic-search-es-default-0 -- bash

#. 
   Configure Elasticsearch's keystore with values from the Storage account's Access keys tab.

   .. image:: .images/access_keys_values.png

   .. code-block:: bash

      bin/elasticsearch-keystore add azure.client.default.account
      bin/elasticsearch-keystore add azure.client.default.key

#. Optionally set a password for the keystore

   .. code-block:: bash

      bin/elasticsearch-keystore passwd

#. Reload secure settings

   .. code-block:: bash

      curl -X POST -u "elastic:$ELASTIC_PASSWORD" "https://aureliusdev.westeurope.cloudapp.azure.com/demo/elastic/_nodes/reload_secure_settings?pretty" -H 'Content-Type: application/json' -d "
      {
          \"secure_settings_password\": \"$ELASTIC_KEYSTORE_PASSWORD\"
      }"

#. Create the repository

   .. code-block:: bash

      curl -X PUT -u "elastic:$ELASTIC_PASSWORD" "https://aureliusdev.westeurope.cloudapp.azure.com/demo/elastic/_snapshot/demo_backup?pretty" -H 'Content-Type: application/json' -d "
      {
        \"type\": \"azure\",
        \"settings\": {
          \"container\": \"aurelius-atlas-elastic-backup\",
           \"base_path\": \"backups\",
           \"chunk_size\": \"32MB\",
          \"compress\": true
        }
      }"

Create a snapshot
-----------------

.. code-block:: bash

   curl -X POST -u "elastic:$ELASTIC_PASSWORD" "https://aureliusdev.westeurope.cloudapp.azure.com/demo/elastic/_snapshot/demo_backup/snapshot_2" -H 'Content-Type: application/json' -d '
   {
      "indices": ".ent-search-engine-documents-*"
   }'
