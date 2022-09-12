Integrations
============

Keycloak is very well equipped to connect with other identity providers
like Azure active directory or Gmail or other identity providers you run
in your organization, if you have already keycloak running and you want
to make use of it then that’s also possible it requires some
configuration, all options a configuration.

It’s also possible to run Apache atlas external, elastic external or
Kafka external.

External means that you disable the port in our helm chart and you
configure the remaining components in such a way that they use the
already existing instances of these different applications, this makes
it very dynamic depending on what you already have running and which
infrastructure is already operated in your environment but you are not
providing additional resources and have a separation of your
infrastructure.

Identity providers via Keycloak (AAD, Gmail,…)

External\* Apache Atlas

External \* Elastic

External \* Kafka

Hadoop

Azure

AWS

GCP

Integrate Aurelius Atlas in Hadoop
----------------------------------

-  Apache Atlas is included in Hadoop environment and used for meta data
   management and the access control​

-  Aurelius Atlas can use this Apache Atlas instance.

..image 



Integrate in Azure Environment.
-------------------------------

-  Azure Purview exposes Apache Atlas REST API as well
   as publishes Kafka change events.​

-  Purview replaces Apache Atlas.

..images

Integrate in AWS
----------------

AWS
does not seem to have its own data governance solution, thus stand-alone tools.

..images

.. _section-3: