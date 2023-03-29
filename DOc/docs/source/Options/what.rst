What is Aurelius Atlas?
=======================

Welcome to the **Aurelius Atlas solution** powered by Apache Atlas, Aurelius
Atlas is an open-source **Data Governance solution**, based on a selection
of open-source tools to facilitate business users to access governance
information in an easy consumable way and meet the data governance
demands of the distributed data world.

It is a Data Governance solution powered by Apache Atlas for Data in
motion **(in transit)**, Data in rest, Data in use. It manages distributed
data governance over multicloud environment as well as hybrid **(On-Prem)**

Components of Aurelius Atlas Helm:
----------------------------------

-  `Apache Atlas <https://atlas.apache.org/#/>`__

-  `Kafka UI <https://kafka.apache.org/>`__

-  `Apache Flink <https://flink.apache.org/>`__

-  `Elasticsearch <https://www.elastic.co/guide/index.html>`__

-  `Keycloak <https://www.keycloak.org/documentation>`__

-  API services


The deployment of our solution is provided as a helm chart so you can
roll it out in your Kubernetes cluster.

The solution itself consists of Apache Atlas in the core with Apache
Kafka used in HBase, you also publish and make accessible the original
Apache user interface.

.. image:: /Options/imgs/k8s.png

In addition to that we deployed a Keycloack which is our identity
provider it’s open source also, which allows to integrate with all kinds
of other identity providers like in our demo environment which you can
try by `Clicking here <demo>`__.

We connect with Gmail, but you can also connect to an active directory
somewhere, on top of that we have our actual user interface, which is
included in what we call the `Reverse proxy
port <#reverse-proxy>`__\.

This port have a lot of uses for searches and full text search but also
with different facets, for that we are using the Elastic stack, so an
elastic search is and elastic enterprise search and a Kibana just to
manage the environment, we also publish the Kibana interface in this
helm chart, since the synchronization all changes are directly performed
in Apache Atlas but then have to be updated in the elastic environment.

We use Apache Flink and some jobs in there streaming jobs in there to
consume the Kafka events from Apache Atlas and translate that into
changes in the Elastic Enterprise Search environment using these streams
as additional service.

We have rest based services for the data to model and the lineage model
both are related required for the lineage graph generation and we have
the REST API for integrating our solution with infrastructure as code in
an easy way also provided in the image.

Different namespaces on the same cluster for different, independent
deployments.

.. image:: /Options/imgs/namespaces.png


It is possible to deploy the helm chart multiple times in different
namespaces, so in our usual environments we have governance set up for
the dev environment for the user acceptance environment, and for the
production environment, they can all run in the same Kubernetes cluster
underneath the same increased controller, and you will always have the
same URLs except that the namespace becomes part of the URL and
everything will be related there.

So, to understand how these different components work together, click
here to go to the technical documentation

If you want to learn more about all the components that made up Aurelius
Atlas, `Click here <tech>`__


What do I need to run the application? 
--------------------------------------

To be able to deploy Aurelius Atlas a **Kubernetes cluster will be needed**.

These are some of the components that you need to run the application,
be sure that you have them, before running the application.

If you do not have it click on the name to go to the external
documentation to set up.

-  `Apache Atlas <https://atlas.apache.org/#/>`__

-  `Kafka UI <https://kafka.apache.org/>`__

-  `Apache Flink <https://flink.apache.org/>`__

-  `Elasticsearch <https://www.elastic.co/guide/index.html>`__

-  `Keycloak <https://www.keycloak.org/documentation>`__

-  API services

If you already have it, you can go directly to the deploy section by
`Clicking here. <how>`__

Integration Options
-------------------

Aurelius Atlas has different options to integrate here is an overview of
the integration options:

-  Identity providers via Keycloak **(AAD, gmail,…)**

-  `External\* Apache Atlas <https://atlas.apache.org/#/>`__
  
-  `External\* Elastic <https://www.elastic.co/guide/index.html>`__

-  `External\* Kafka <https://kafka.apache.org/20/documentation/>`__

-  `Hadoop <https://hadoop.apache.org/docs/stable/>`__

-  `Azure <https://docs.microsoft.com/en-us/azure/?product=popular>`__

-  `AWS <https://docs.aws.amazon.com/>`__

..
   -  GCP

    (*Write here a brief overview of the integrations options and why you
    would use them*)

`Click here <integration>`__ to know more about the integration
options.

..
    How others have used Aurelius Atlas
   

    (*Write here a brief overview of how others have integrated with it. Such
    as linking it to IaC*),

    provide a link to the page with more details.

How to Deploy Aurelius Atlas
----------------------------

To start using Aurelius Atlas here is a guide to easily learn how to
deploy the application `Click here <how>`__


