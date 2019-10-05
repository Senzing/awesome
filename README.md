# awesome

Curated list of awesome Senzing software and resources.
Inspired by [other awesome sites](#other-awesome-sites).

## Contents

1. [Docker](#docker)
1. [Demonstrations](#demonstrations)
1. [Dockerfiles](#dockerfiles)
1. [docker-compose](#docker-compose)
1. [Kubernetes](#kubernetes)
1. [Mapper](#mapper)
1. [Proof of Concept](#proof-of-concept)
1. [Resources](#resources)
1. [Utilities](#utilities)
1. [Work in progress](#work-in-progress)
1. [Other awesome sites](#other-awesome-sites)

## Docker

**Legend:**
The following icons are clickable:

- [:whale:](https://hub.docker.com/u/senzing) - Available as a docker image on [hub.docker.com](https://hub.docker.com/u/senzing).
- [:gear:](https://github.com/Senzing/charts/tree/master/charts) - Available as a Helm Chart on [https://github.com/Senzing/charts](https://github.com/Senzing/charts)

| Image name with GitHub link |      |      | Description |
|-----------------------------|:----:|:----:|-------------|
| [senzing/db2](https://github.com/Senzing/docker-db2) | | | Dockerfile for the DB2 Command Line Processor (CLP).
| [senzing/db2express-c](https://github.com/Senzing/docker-db2express-c) | | | Dockerfile wrapping ibmcom/db2express-c docker image.
| [senzing/entity-search-web-app](https://github.com/Senzing/entity-search-web-app) | [:whale:](https://hub.docker.com/r/senzing/entity-search-web-app) | [:gear:](https://github.com/Senzing/charts/tree/master/charts/senzing-entity-search-web-app) | Dockerfile wrapping entity-search-web-app.
| [senzing/g2configtool](https://github.com/Senzing/docker-g2configtool) | [:whale:](https://github.com/Senzing/docker-g2configtool) | | Dockerfile wrapping Senzing's G2ConfigTool.py.
| [senzing/g2command](https://github.com/Senzing/docker-g2command) | [:whale:](https://hub.docker.com/r/senzing/g2command) | | Dockerfile wrapping Senzing's G2Command.py.
| [senzing/g2command-db2-cluster](https://github.com/Senzing/docker-g2command-db2-cluster) | | | Dockerfile of Senzing's G2Command.py for DB2 cluster.
| [senzing/g2loader](https://github.com/Senzing/docker-g2loader) | [:whale:](https://hub.docker.com/r/senzing/g2loader) | | Dockerfile wrapping Senzing's G2Loader.py.
| [senzing/g2loader-db2-cluster](https://github.com/Senzing/docker-g2loader-db2-cluster) | | | Dockerfile of Senzing's python G2Loader for DB2 cluster.
| [senzing/jupyter](https://github.com/Senzing/docker-jupyter) | [:whale:](https://hub.docker.com/r/senzing/jupyter) | | Dockerfile for running example Senzing Jupyter notebooks.
| [senzing/mock-data-generator](https://github.com/Senzing/mock-data-generator) | [:whale:](https://hub.docker.com/r/senzing/mock-data-generator) | | Dockerfile wrapping `mock-data-generator.py`.
| [senzing/mysql](https://github.com/Senzing/docker-mysql) | | | Dockerfile of MySQL command line interpreter.
| [senzing/mysql-init](https://github.com/Senzing/docker-mysql-init) | | | Dockerfile for initializing mysql database with a one-time command.
| [senzing/opt-senzing](https://github.com/Senzing/docker-opt-senzing) | | | Dockerfile containing a "baked-in" /opt/senzing directory.
| [senzing/python-base-complete](https://github.com/Senzing/docker-python-base-complete) | | | Dockerfile for embedded Senzing, MySQL, and python 3.7 base installation.
| [senzing/python-db2-base](https://github.com/Senzing/docker-python-db2-base) | | | Dockerfile for Senzing, single DB2 instance, and python 3.7.
| [senzing/python-db2-cluster-base](https://github.com/Senzing/docker-python-db2-cluster-base) | | | Dockerfile for Senzing, DB2 cluster, and python 3.7.
| [senzing/python-db2-cluster-demo](https://github.com/Senzing/docker-python-db2-cluster-demo) | | | Dockerfile demonstrating simple Flask app using Senzing and DB2 cluster.
| [senzing/python-demo](https://github.com/Senzing/docker-python-demo) | [:whale:](https://hub.docker.com/r/senzing/python-demo) | | Dockerfile demonstrating simple Flask app using Senzing.
| [senzing/python-postgresql-base](https://github.com/Senzing/docker-python-postgresql-base) | | | Dockerfile for Senzing, PostgreSQL, and python 3.7 base installation.
| [senzing/senzing-api-server](https://github.com/Senzing/senzing-api-server) | [:whale:](https://hub.docker.com/r/senzing/senzing-api-server) | | Dockerfile for server of Senzing REST API.
| [senzing/senzing-base](https://github.com/Senzing/docker-senzing-base) | [:whale:](https://hub.docker.com/r/senzing/senzing-base) | | Dockerfile used in FROM statements.
| [senzing/senzing-debug](https://github.com/Senzing/docker-senzing-debug) | [:whale:](https://hub.docker.com/r/senzing/senzing-debug) | | Dockerfile for debugging Senzing deployments.
| [senzing/senzing-poc-utility](https://github.com/Senzing/docker-senzing-poc-utility) | [:whale:](https://hub.docker.com/r/senzing/senzing-poc-utility) | | Dockerfile wrapping Senzing's POC utility.
| [senzing/stream-loader](https://github.com/Senzing/stream-loader) | [:whale:](https://hub.docker.com/r/senzing/stream-loader) | | Dockerfile  wrapping `stream-loader.py`.
| [senzing/web-app-demo](https://github.com/Senzing/docker-web-app-demo) | [:whale:](https://hub.docker.com/r/senzing/web-app-demo) | | Dockerfile wrapping "Entity Search Web App".
| [store/senzing/senzing-package](https://github.com/Senzing/senzing-package) | [:whale:](https://hub.docker.com/_/senzing-package) | | Dockerfile wrapping `senzing-package.py`. Requires [accepting EULA](https://github.com/Senzing/knowledge-base/blob/master/HOWTO/accept-eula.md#storesenzingsenzing-package-docker-image).

## Demonstrations

*Step-by-step instructions demonstrating use of Senzing.*

1. [docker-app-demo](https://github.com/Senzing/docker-app-demo) - Use "docker-app" to create a docker formation.
1. [docker-compose-db2-cluster-demo](https://github.com/Senzing/docker-compose-db2-cluster-demo) - Demonstrates docker-compose formation of Senzing, DB2 database cluster, and a simple Flask web app.
1. [docker-compose-demo](https://github.com/Senzing/docker-compose-demo) - Demonstrates docker-compose formation of Senzing with queue, database, and the Senzing Entity Search WebApp.
1. [docker-web-app-demo](https://github.com/Senzing/docker-web-app-demo) - Senzing API server and Senzing Entity WebApp combo.
1. [hello-senzing-springboot-java](https://github.com/Senzing/hello-senzing-springboot-java) - Demonstrates how to create an HTTP interface to Senzing using SpringBoot.
1. [ibm-openshift-guide](https://github.com/Senzing/ibm-openshift-guide) - Create a docker formation using minishift.
1. [kubernetes-demo](https://github.com/Senzing/kubernetes-demo) - Demonstrates Kubernetes deployment of Senzing with queue, database, and Senzing API server.
1. [rancher-demo](https://github.com/Senzing/rancher-demo) - Demonstrates Rancher deployment of Senzing with queue, database, and Senzing API server.
1. [webapp-drillthrough-demo](https://github.com/Senzing/webapp-drillthrough-demo) - A demonstration of Senzing drill through using Senzing developer toolkit, Node-RED, and Python Flask.

## Dockerfiles

*Repositories with Dockerfiles.*

1. [configurator](https://github.com/Senzing/configurator) - Web service for configuring Senzing.
1. [docker-db2](https://github.com/Senzing/docker-db2) - Dockerfile for the DB2 Command Line Processor (CLP).
1. [docker-db2-driver-installer](https://github.com/Senzing/docker-db2-driver-installer) - Install DB2 client drivers on mounted volumes.
1. [docker-g2command](https://github.com/Senzing/docker-g2command) - Dockerfile wrapping Senzing's G2Command.py.
1. [docker-g2configtool](https://github.com/Senzing/docker-g2configtool) - Dockerfile wratpping G2ConfigTool.
1. [docker-g2loader](https://github.com/Senzing/docker-g2loader) - Dockerfile wrapping Senzing's G2Loader.py.
1. [docker-hello-world](https://github.com/Senzing/docker-hello-world) - Dockerfile for testing docker formations.
1. [docker-ibm-db2](https://github.com/Senzing/docker-ibm-db2) - Wrapper for `ibmcom/db2`.
1. [docker-init-container](https://github.com/Senzing/docker-init-container) - Dockerfile used to initialize Senzing artifacts.
1. [docker-jupyter](https://github.com/Senzing/docker-jupyter) - Dockerfile for running example Senzing Jupyter notebooks.
1. [docker-mysql-init](https://github.com/Senzing/docker-mysql-init) - Dockerfile for initializing mysql database with a one-time command.
1. [docker-poc-notebook](https://github.com/Senzing/docker-poc-notebook) - Jupyter notebook for showing POC results.
1. [docker-python-demo](https://github.com/Senzing/docker-python-demo) - Dockerfile demonstrating simple Flask app using Senzing.
1. [docker-senzing-base](https://github.com/Senzing/docker-senzing-base) - Dockerfile used in FROM statements.
1. [docker-senzing-debug](https://github.com/Senzing/docker-senzing-debug) - Dockerfile for debugging Senzing deployments.
1. [docker-senzing-poc-utility](https://github.com/Senzing/docker-senzing-poc-utility) - Dockerfile wrapping Senzing's POC utility.
1. [docker-yum](https://github.com/Senzing/docker-yum) - A dockerized version of yum.
1. [docker-yumdownloader](https://github.com/Senzing/docker-yumdownloader) - A docker wrapper over yumdownloader.
1. [entity-search-web-app](https://github.com/Senzing/entity-search-web-app) - A lightweight http server providing a web UI for entity search through the senzing api server.
1. [mock-data-generator](https://github.com/Senzing/mock-data-generator) - Python tool for generating mock Senzing data and sending it to Kafka, RabbitMQ, or STDOUT.
1. [resolver](https://github.com/Senzing/resolver) - Ephemeral Senzing entity-resolution.
1. [senzing-api-server](https://github.com/Senzing/senzing-api-server) - Server of Senzing REST API.
1. [senzing-package](https://github.com/Senzing/senzing-package) - Python tool for installing Senzing TGZ file.
1. [stream-loader](https://github.com/Senzing/stream-loader) - Python tool for loading Senzing G2 from RabbitMQ, Kafka, URL-addressable file, or STDIN.

## docker-compose

*Docker formations using docker-compose.*

1. [docker-compose-demo](https://github.com/Senzing/docker-compose-demo) - Demonstrates docker-compose formation of Senzing with queue, database, and the Senzing Entity Search WebApp.

## Kubernetes

*Step-by-step instructions demonstrating use of Senzing on kubernetes-based systems.*

1. [charts](https://github.com/Senzing/charts) - Charts for use with Rancher and Kubernetes.
1. [kubernetes-demo](https://github.com/Senzing/kubernetes-demo) - Demonstrates Kubernetes deployment of Senzing with queue, database, and Senzing API server.

## Helm Charts

*Helm Charts for Senzing on kubernetes-based systems.*

1. [charts](https://github.com/Senzing/charts) - Charts for use with Rancher and Kubernetes.
1. [configurator](https://github.com/Senzing/configurator) - Web service for configuring Senzing.
1. [docker-db2-driver-installer](https://github.com/Senzing/docker-db2-driver-installer) - Install DB2 client drivers on mounted volumes.
1. [docker-hello-world](https://github.com/Senzing/docker-hello-world) - Dockerfile for testing docker formations.
1. [docker-ibm-db2](https://github.com/Senzing/docker-ibm-db2) - Wrapper for `ibmcom/db2`.
1. [docker-init-container](https://github.com/Senzing/docker-init-container) - Dockerfile used to initialize Senzing artifacts.
1. [docker-senzing-base](https://github.com/Senzing/docker-senzing-base) - Dockerfile used in FROM statements.
1. [docker-senzing-debug](https://github.com/Senzing/docker-senzing-debug) - Dockerfile for debugging Senzing deployments.
1. [docker-yum](https://github.com/Senzing/docker-yum) - A dockerized version of yum.
1. [entity-search-web-app](https://github.com/Senzing/entity-search-web-app) - A lightweight http server providing a web UI for entity search through the senzing api server.
1. [mock-data-generator](https://github.com/Senzing/mock-data-generator) - Python tool for generating mock Senzing data and sending it to Kafka, RabbitMQ, or STDOUT.
1. [resolver](https://github.com/Senzing/resolver) - Ephemeral Senzing entity-resolution.
1. [senzing-api-server](https://github.com/Senzing/senzing-api-server) - Server of Senzing REST API.
1. [senzing-package](https://github.com/Senzing/senzing-package) - Python tool for installing Senzing TGZ file.
1. [stream-loader](https://github.com/Senzing/stream-loader) - Python tool for loading Senzing G2 from RabbitMQ, Kafka, URL-addressable file, or STDIN.

## Mapper

*Convert industry standard formats to Senzing-ready format.*

1. [mapper-base](https://github.com/Senzing/mapper-base) - Base functions used to map a variety of formats to a Senzing-acceptable format.
1. [mapper-dnb](https://github.com/Senzing/mapper-dnb) - Map DNB format to Senzing format.
1. [mapper-dowjones](https://github.com/Senzing/mapper-dowjones) - Map Dow Jones Watchlist format to Senzing format.
1. [mapper-ijic](https://github.com/Senzing/mapper-ijic) - Map ICIJ format to Senzing format.
1. [mapper-ofac](https://github.com/Senzing/mapper-ofac) - OFAC to JSON mapper.

## Proof of Concept

*Tools to work with Proof of Concept engagements.*

1. [docker-poc-notebook](https://github.com/Senzing/docker-poc-notebook) - Jupyter notebook for showing POC results.
1. [docker-senzing-poc-utility](https://github.com/Senzing/docker-senzing-poc-utility) - Dockerfile wrapping Senzing's POC utility.
1. [poc-csv-tools](https://github.com/Senzing/poc-csv-tools) - Exemplar artifacts (files) that can be used in other Senzing repositories.
1. [poc-snapshot](https://github.com/Senzing/poc-snapshot) - Snapshot the current state of the records loaded in a Senzing repository.
1. [poc-viewer](https://github.com/Senzing/poc-viewer) - Interactive command line utility that works along with the poc-snapshot utility.

## Resources

*Non-code information.*

1. [awesome](https://github.com/Senzing/awesome) - Curated list of awesome software and resources for Senzing, The First Real-Time AI for Entity Resolution.
1. [charts](https://github.com/Senzing/charts) - Charts for use with Rancher and Kubernetes.
1. [knowledge-base](https://github.com/Senzing/knowledge-base) - HOWTOs, tasks, explanations, and more knowledge.
1. [senzing-rest-api](https://github.com/Senzing/senzing-rest-api) - OpenAPI specification of Senzing REST API.
1. [senzing.github.io](https://github.com/Senzing/senzing.github.io) - Organization site at http://senzing.github.io.

## Utilities

*Tools for working with Senzing.*

1. [configurator](https://github.com/Senzing/configurator) - Web service for configuring Senzing.
1. [docker-init-container](https://github.com/Senzing/docker-init-container) - Dockerfile used to initialize Senzing artifacts.
1. [entity-search-web-app](https://github.com/Senzing/entity-search-web-app) - A lightweight http server providing a web UI for entity search through the senzing api server.
1. [migrate](https://github.com/Senzing/migrate) - Python tool for migrating Senzing configuration to a new release.
1. [mock-data-generator](https://github.com/Senzing/mock-data-generator) - Python tool for generating mock Senzing data and sending it to Kafka, RabbitMQ, or STDOUT.
1. [resolver](https://github.com/Senzing/resolver) - Ephemeral Senzing entity-resolution.
1. [senzing-api-server](https://github.com/Senzing/senzing-api-server) - Server of Senzing REST API.
1. [senzing-package](https://github.com/Senzing/senzing-package) - Python tool for installing Senzing TGZ file.
1. [stream-loader](https://github.com/Senzing/stream-loader) - Python tool for loading Senzing G2 from RabbitMQ, Kafka, URL-addressable file, or STDIN.

## Work in progress

*Fresh meat.*

1. [elasticsearch](https://github.com/Senzing/elasticsearch) - Using G2 engine with ElasticSearch indexing engine.
1. [ibm-icp4d-guide](https://github.com/Senzing/ibm-icp4d-guide) - Reference implementation for Senzing on IBM Cloud Private for Data.
1. [openshift-demo](https://github.com/Senzing/openshift-demo) - Demonstration using minishift.
1. [stream-configuration](https://github.com/Senzing/stream-configuration) - :construction: [Under construction] Temporary Senzing configuration service.
1. [terraform-senzing-aws-cookbook](https://github.com/Senzing/terraform-senzing-aws-cookbook) - :construction: [Under construction]  A Terraform-based deployment of Senzing on AWS.

## Other awesome sites

*Our thanks to those who blazed the 'awesome' trail before us.*

- General:
  [sindresorhus/awesome](https://github.com/sindresorhus/awesome),
- GoLang:
  [avelino/awesome-go](https://github.com/avelino/awesome-go)
- Java:
  [java-lang/awesome-java](https://github.com/java-lang/awesome-java),
  [akullpp/awesome-java](https://github.com/akullpp/awesome-java),
  [awesome-java](https://github.com/uhub/awesome-java)
- JavaScript:
  [sorrycc/awesome-javascript](https://github.com/sorrycc/awesome-javascript),
  [uhub/awesome-javascript](https://github.com/uhub/awesome-javascript)
- PHP:
  [https://github.com/uhub/awesome-php](https://github.com/uhub/awesome-php),
  [ziadoz/awesome-php](https://github.com/ziadoz/awesome-php)
- Python:
  [vinta/awesome-python](https://github.com/vinta/awesome-python)
