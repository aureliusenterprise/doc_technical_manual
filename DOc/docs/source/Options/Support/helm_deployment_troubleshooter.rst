Troubleshooting deployment
==========================
.. _deployment-troubleshooting:

Connection is not safe
----------------------

After many deployment attempts, it can happen that the reflector pod is not restarted automatically.

1. Check if there is a secret called `letsencrypt-secret-aureliusdev` in our namespace:

.. code:: bash

    kubectl -n <namespace> get secrets

2. If it is not there, then find the reflector pod in the default namespace:

.. code:: bash

    kubectl get all

3. Delete reflector pod (A new one will be created automatically):

.. code:: bash

    kubectl -n <namespace> delete pod/<podname>

Flink-jobmanager and taskmanager is not running
-----------------------------------------------

Flink-jobmanager is not running, and Flink-taskmanager keeps restarting, but other pods are fine.

To check if all pods are running:

.. code:: bash

    kubectl -n <namespace> get all

Go into the Atlas pod, and see the error message:

.. code:: bash

    kubectl -n <namespace> exec -it <pod/chart-id-atlas-0> -- bash
    cd opt/apache-atlas-2.2.0/logs
    cat application.log

If you see an error like:
	``org.apache.solr.client.solrj.impl.HttpSolrClient$RemoteSolrException: Error from server at http://10.20.129.33:9838/solr: Can not find the specified config set: vertex_index``

Then the `vertex_index` collection could not be created.

To solve it, we can create it manually in Solr client, then restart the Atlas pod.

1. We forward port 9838, so we can access Solr web client:

.. code:: bash

    kubectl -n demo port-forward <pod/chart-id-atlas-0> 9838:9838

2. Open the web client on `localhost:9838/solr`

3. Go to the `Collections` menu, and add a collection.

	a. Name: vertex_index
	b. Config set: _default
	c. maxShardsPer: -1

4. From another cmd, open the atlas pod again:

.. code:: bash

    kubectl -n <namespace> exec -it <pod/chart-id-atlas-0> -- bash
    cd opt/apache-atlas-2.2.0/
    bin/atlas_stop.py
    nohup bin/atlas_start.py &

5. You can exit it with CTR+C and to check if it is running:

.. code:: bash

    jobs


If an entity are not getting created
------------------------------------

It could be that a flink job has failed.

1. Check whether all flink jobs are running. if not, then restart them:

.. code:: bash

    kubectl -n <namespace> exec -it <pod/flink-jobmanager-pod-name> -- bash

    cd py_libs/m4i-flink-tasks/scripts

    /opt/flink/bin/flink run -d -py <name_of_job>.py

2. Determine if the entity was created within the apache atlas.

3. Determine if the entity was created in the elastic.

PS. Be aware of resource problems
