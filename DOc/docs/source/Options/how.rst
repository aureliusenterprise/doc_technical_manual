How to deploy Aurelius Atlas
============================

The deployment of the solution is provided as a helm chart

| Write description on what will be deployed.

If you want, to try our demo environment `Click
here. <#demo-enviroment>`__

This is the frequently asked questions about the deployment,

`Click here <#faqs>`__ to know more.

Requirements
------------

| Write the requirements to deploy.
| Provide links to how to install requirements if applicable

The content for this section is being written on
`aureliusenterprise/helm-governance
(github.com) <https://github.com/aureliusenterprise/helm-governance>`__

Deployment Steps
----------------

The content for this section is being written on `aureliusenterprise/helm-governance (github.com) <https://github.com/aureliusenterprise/helm-governance>`__ 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _section-2:

``NOTE``


The installation assumes that you have a Kubernetes cluster running. If
not, check out `this
section <#what-do-i-need-to-run-the-application>`__.

1. Install Certificate manager:

2. Install Ingress Nginx Controller

3. Install Elastic

4. Deploying first time on cluster

Installation
------------

Configure public hostname

**Elastic:**

To deploy elastic, Elastic Cluster on Kubernetes (ECK) must be in

stalled on the cluster. To install ECK on the cluster, please follow the
instructions provided
on https://www.elastic.co/guide/en/cloud-on-k8s/master/k8s-deploy-eck.html

For more details about this elastic helm chart look at `elastic
readme <https://github.com/aureliusenterprise/helm-governance/blob/main/charts/elastic/README.md>`__

**Flink:**

For more details about this Flink helm chart look at `Flink
readme <https://github.com/aureliusenterprise/helm-governance/blob/main/charts/flink/README.md>`__

Atlas is now accessible via reverse proxy
at https://aureliusdev.westeurope.cloudapp.azure.com/anwo/atlas2/login.jsp

Deployment of Demo Dataset
~~~~~~~~~~~~~~~~~~~~~~~~~~

The content for this section will be written on
`aureliusenterprise/helm-governance
(github.com) <https://github.com/aureliusenterprise/helm-governance>`__

Video instructions
------------------

..image

..Make Video and place here
