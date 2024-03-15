.. role:: raw-html-m2r(raw)
   :format: html


Aurelius Atlas Backup
=====================

Here you will find how to back up Aurelius Atlas for moving instances.

This process will result in zip files of the Apache Atlas data and a Snapshot repository of Elasticsearch indices that can be used for backup and in the case of disaster recover process. 

Apache Atlas backup
===================

Apache Atlas Backup Process Overview
------------------------------------


.. image:: backup-overview.png
   :target: backup-overview.png
   :alt: img_2.png


Acquire access token for Apache Atlas's admin user
--------------------------------------------------

You can use ``oauth.sh`` script from https://github.com/aureliusenterprise/Aurelius-Atlas-helm-chart. Example usage:

.. code-block::

   export ACCESS_TOKEN=$(./oauth.sh --endpoint https://aureliusdev.westeurope.cloudapp.azure.com/demo/auth/realms/m4i/protocol/openid-connect/token \
   --client-id m4i_atlas \
   --access atlas $ATLAS_USER_PASSWD)

Export data from Apache Atlas
-----------------------------

You can use ``export-atlas.py`` script, that wraps Apache Atlas's `Export API <https://atlas.apache.org/index.html#/ExportAPI>`_ to export all data from Atlas. Example Usage:

.. code-block::

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

   :raw-html-m2r:`<img width="560" alt="Zrzut ekranu 2024-03-13 143127" src="https://github.com/aureliusenterprise/Aurelius-Atlas-helm-chart/assets/155443057/a576c8f2-28de-4264-9f7f-43a0cd39af1e">`

#. 
   Create a new storage account :w


   :raw-html-m2r:`<img width="239" alt="Zrzut ekranu 2024-03-13 143220" src="https://github.com/aureliusenterprise/Aurelius-Atlas-helm-chart/assets/155443057/0233f3d5-4bb5-4bb4-ad65-041634000e89">`

#. 
   Set the account name. Optionally adjust the redundancy and access tier 

   :raw-html-m2r:`<img width="477" alt="Zrzut ekranu 2024-03-13 144404" src="https://github.com/aureliusenterprise/Aurelius-Atlas-helm-chart/assets/155443057/660a0904-9471-474b-8022-50e538cb7fe2">`

   :raw-html-m2r:`<img width="483" alt="Zrzut ekranu 2024-03-13 144711" src="https://github.com/aureliusenterprise/Aurelius-Atlas-helm-chart/assets/155443057/a4b51c7a-c400-49ae-916f-8df809a3585d">`

#. 
   Review and create

#. 
   Once the account is created, go to Containers tab 

   :raw-html-m2r:`<img width="140" alt="Zrzut ekranu 2024-03-13 154545" src="https://github.com/aureliusenterprise/Aurelius-Atlas-helm-chart/assets/155443057/97412587-cd83-474a-9375-ea972f3bff93">`

#. 
   Create a new container 

   :raw-html-m2r:`<img width="221" alt="Zrzut ekranu 2024-03-13 170441" src="https://github.com/aureliusenterprise/Aurelius-Atlas-helm-chart/assets/155443057/039674a6-9b13-4ce0-bfcc-4548799fee54">`

   :raw-html-m2r:`<img width="244" alt="Zrzut ekranu 2024-03-13 170607" src="https://github.com/aureliusenterprise/Aurelius-Atlas-helm-chart/assets/155443057/bcf49c1d-b2ec-4471-880a-039da6e6abc5">`

#. 
   Go to Access keys tab 

   :raw-html-m2r:`<img width="136" alt="Zrzut ekranu 2024-03-13 171520" src="https://github.com/aureliusenterprise/Aurelius-Atlas-helm-chart/assets/155443057/c1a0622f-8f69-45e1-9d0e-58bc93138f09">`

Register a repository
^^^^^^^^^^^^^^^^^^^^^


#. Access Elastic's search pod/image, for example:
   .. code-block::

      kubectl -n demo exec -it pod/elastic-search-es-default-0 -- bash

#. 
   Configure Elasticsearch's keystore with values from the Storage account's Access keys tab.

   :raw-html-m2r:`<img width="415" alt="Zrzut ekranu 2024-03-13 172223" src="https://github.com/aureliusenterprise/Aurelius-Atlas-helm-chart/assets/155443057/e6593057-0f38-4840-86f0-9ec9d54a7466">`

   .. code-block::

      bin/elasticsearch-keystore add azure.client.default.account
      bin/elasticsearch-keystore add azure.client.default.key

#. Optionally set a password for the keystore
   .. code-block::

      bin/elasticsearch-keystore passwd

#. Reload secure settings
   .. code-block::

      curl -X POST -u "elastic:$ELASTIC_PASSWORD" "https://aureliusdev.westeurope.cloudapp.azure.com/demo/elastic/_nodes/reload_secure_settings?pretty" -H 'Content-Type: application/json' -d "
      {
          \"secure_settings_password\": \"$ELASTIC_KEYSTORE_PASSWORD\"
      }"

#. Create the repository
   .. code-block::

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
