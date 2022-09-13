Technical description
=====================
.. _tech:

Here we explain all the libraries that are public. How components work
together

In the next picture, you can get an idea of how the browsing
of a page on the front end is executed.

.. image:: /Options/imgs/proxy.png

**1)** User request comes into our web server which acts as a reverse proxy.

**2)** The request is redirected through the reverse proxy to the Apache
   Atlas API.

**3)** The Apache Atlas API has been configured to validate the
   authorization header of the request with Apache Keycloak. Apache
   Keycloak can be integrated with other identity providers if so
   configured.

**4)** The request is handled by the Atlas API and the response is fed back
   to the user interface.

**5)** We ask also for additional context information like data quality,
   governance quality, and more information about the context of the
   entity from the elastic enterprise search.

**5a)** In some cases we will also request a lineage graph and in these
cases, it will go viral from the reverse proxy to the lineage model
potentially

**5b)** Get some information from Apache Atlas.

**5a)** Create the lineage graph in this diagram.

Reverse Proxy
-------------

How a user request is processed
-------------------------------

Atlas Core Library
------------------

Python Rest APIs
----------------

Synchronization 
---------------

How create, update, and delete operations are processed in the
environment.


.. image:: /Options/imgs/proxy2.png
   

**1)** User request of a create update or lead operation is managed to the
   user interface the reverse proxy.

**2)** Which then checks first authentication authorization against keycloak
   and potentially subsequent identity providers.

**3)** The next updates are executed in Apache Atlas, so then we are safe
   that all changes are executed properly.

**4)** Next step is to propagate these to make sure that all the context
information in Elastic Enterprise Search is also up to date again.

**4)** We make use of the facility of Apache Atlas to publish changes to
Kafka events, so we have an Apache Kafka where all the changes are
published in a specific topic, the first pipeline, and all pipelines run
in Apache Flink.

   **5)** The lookup entity pipeline, which receives the topic looks up all
   the context information in Apache Atlas and reaches that event and
   publishes this change event in another Kafka topic.

   **6)** Publish state documents the actual change happened, the actual new
   instance of the entity in Elastic search which allows us also later
   to trace which versions we had who made which changes and which time
   series dependency.

   **7)** The determine change uses a previous version of the entity from
   Atlas and the current change event from the Kafka topic it compares
   the two, identifies which relations have been changed, which
   attributes have been changed, and summarizes that consistently so
   that we can see these attributes have changed, these are the old
   values these, are the new values and publishes that in a new topic,
   now whit all the information we have determined which check what
   changes and how it changed and now we can provide pipelines for
   updating the individual context.

   **8)** The propagate entity context is updating elastic enterprise search
   to provide the updated information related to the context so that we
   can do searches properly and that we have these categories available
   for the trade down of the search engine,

   **9)** The propagate quality updates quality information so either the
   data quality or governance quality if a change happens, we must add
   update the context of this quality information.

    