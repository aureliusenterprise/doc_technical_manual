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

..

   .. image:: vertopal_5336a9f227114ea882bbba634fc13a92/media/image10.jpeg
      :alt: Diagram Description automatically generated
      :width: 5.786in
      :height: 4.06467in

Integrate in AWS
----------------

AWS
does not seem to have its own data governance solution, thus stand-alone tools.

..
      .. image:: vertopal_5336a9f227114ea882bbba634fc13a92/media/image11.jpeg
  :alt: Graphical user interface, application Description automatically
   generated
   :width: 6.26806in
   :height: 3.13403in

      .. image:: vertopal_5336a9f227114ea882bbba634fc13a92/media/image12.png
   :alt: Diagram Description automatically generated with low confidence
   :width: 3.03472in
   :height: 3.28056in

.. _section-3: