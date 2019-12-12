# awesome

Curated list of awesome Senzing software and resources.
Inspired by [other awesome sites](#other-awesome-sites).

## Contents

1. [Demonstrations](#demonstrations)
1. Docker
    1. [Dockerfiles](#dockerfiles)
    1. [DockerHub](#dockerhub)
    1. [docker-compose](#docker-compose)
    1. [Kubernetes](#kubernetes)
    1. [Helm Charts](#helm-charts)
1. [Mapper](#mapper)
1. [Proof of Concept](#proof-of-concept)
1. [Resources](#resources)
1. [User Interface](#user-interface)
1. [Utilities](#utilities)
1. [Under construction](#under-construction)
1. [Obsolete](#obsolete)
1. [Other awesome sites](#other-awesome-sites)

## Demonstrations

*Step-by-step instructions demonstrating use of Senzing.*

1. [docker-app-demo](https://github.com/Senzing/docker-app-demo) - Uses `docker-app` to create a docker formation demonstrating Senzing.
1. [docker-compose-demo](https://github.com/Senzing/docker-compose-demo) - Uses `docker-compose` to create a docker formation demonstrating Senzing.
1. [docker-python-demo](https://github.com/Senzing/docker-python-demo) - Dockerfile demonstrating simple Flask app using Senzing.
1. [docker-web-app-demo](https://github.com/Senzing/docker-web-app-demo) - Dockerfile combining Senzing API server and Senzing Entity WebApp.
1. [ibm-openshift-guide](https://github.com/Senzing/ibm-openshift-guide) - Demonstrates OpenShift deployment of Senzing with queue, Db2, and Senzing API server.
1. [kubernetes-demo](https://github.com/Senzing/kubernetes-demo) - Demonstrates Kubernetes deployment of Senzing with queue, database, and Senzing API server.

## Dockerfiles

*Repositories with Dockerfiles.*

1. [docker-adminer](https://github.com/Senzing/docker-adminer) - Dockerfile wrapping `adminer`, a database viewer.
1. [docker-apt](https://github.com/Senzing/docker-apt) - Dockerfile wrapping `apt-get`, a package manager.
1. [docker-aptdownloader](https://github.com/Senzing/docker-aptdownloader) - Dockerfile wrapping `apt-get install --download-only`.
1. [docker-db2-driver-installer](https://github.com/Senzing/docker-db2-driver-installer) - Install DB2 client drivers on mounted volumes.
1. [docker-g2command](https://github.com/Senzing/docker-g2command) - Dockerfile wrapping Senzing's `G2Command.py`.
1. [docker-g2configtool](https://github.com/Senzing/docker-g2configtool) - Dockerfile wrapping Senzing's `G2ConfigTool.py`.
1. [docker-g2loader](https://github.com/Senzing/docker-g2loader) - Dockerfile wrapping Senzing's `G2Loader.py`.
1. [docker-hello-world](https://github.com/Senzing/docker-hello-world) - Dockerfile for testing docker formations.
1. [docker-ibm-db2](https://github.com/Senzing/docker-ibm-db2) - Wrapper for `ibmcom/db2` docker image.
1. [docker-init-container](https://github.com/Senzing/docker-init-container) - Dockerfile used to initialize Senzing artifacts.
1. [docker-jupyter](https://github.com/Senzing/docker-jupyter) - Dockerfile for running example Senzing Jupyter notebooks.
1. [docker-mysql](https://github.com/Senzing/docker-mysql) - Dockerfile wrapping `mysql` command line interpreter.
1. [docker-mysql-init](https://github.com/Senzing/docker-mysql-init) - Dockerfile for initializing mysql database with a one-time command.
1. [docker-python-demo](https://github.com/Senzing/docker-python-demo) - Dockerfile demonstrating simple Flask app using Senzing.
1. [docker-senzing-base](https://github.com/Senzing/docker-senzing-base) - Dockerfile used in FROM statements.
1. [docker-senzing-debug](https://github.com/Senzing/docker-senzing-debug) - Dockerfile for debugging Senzing deployments.
1. [docker-senzing-poc-utility](https://github.com/Senzing/docker-senzing-poc-utility) - Dockerfile wrapping Senzing's POC utility.
1. [docker-web-app-demo](https://github.com/Senzing/docker-web-app-demo) - Dockerfile combining Senzing API server and Senzing Entity WebApp.
1. [docker-yum](https://github.com/Senzing/docker-yum) - Dockerfile wrapping `yum`, a package manager.
1. [docker-yumdownloader](https://github.com/Senzing/docker-yumdownloader) - Dockerfile wrapping `yumdownloader`.
1. [entity-search-web-app](https://github.com/Senzing/entity-search-web-app) - A lightweight http server providing a web UI for entity search through the senzing api server.
1. [mock-data-generator](https://github.com/Senzing/mock-data-generator) - Python tool for generating mock Senzing data and sending it to Kafka, RabbitMQ, or STDOUT.
1. [resolver](https://github.com/Senzing/resolver) - Ephemeral Senzing entity-resolution.
1. [senzing-api-server](https://github.com/Senzing/senzing-api-server) - Server of Senzing REST API.
1. [senzing-package](https://github.com/Senzing/senzing-package) - Python tool for installing Senzing package.
1. [stream-loader](https://github.com/Senzing/stream-loader) - Python tool for loading Senzing G2 from RabbitMQ, Kafka, URL-addressable file, or STDIN.

## DockerHub

*Git repositories with Docker images on DockerHub.*

1. [docker-adminer](https://github.com/Senzing/docker-adminer) - Dockerfile wrapping `adminer`, a database viewer.
1. [docker-apt](https://github.com/Senzing/docker-apt) - Dockerfile wrapping `apt-get`, a package manager.
1. [docker-aptdownloader](https://github.com/Senzing/docker-aptdownloader) - Dockerfile wrapping `apt-get install --download-only`.
1. [docker-db2-driver-installer](https://github.com/Senzing/docker-db2-driver-installer) - Install DB2 client drivers on mounted volumes.
1. [docker-g2command](https://github.com/Senzing/docker-g2command) - Dockerfile wrapping Senzing's `G2Command.py`.
1. [docker-g2configtool](https://github.com/Senzing/docker-g2configtool) - Dockerfile wrapping Senzing's `G2ConfigTool.py`.
1. [docker-g2loader](https://github.com/Senzing/docker-g2loader) - Dockerfile wrapping Senzing's `G2Loader.py`.
1. [docker-hello-world](https://github.com/Senzing/docker-hello-world) - Dockerfile for testing docker formations.
1. [docker-ibm-db2](https://github.com/Senzing/docker-ibm-db2) - Wrapper for `ibmcom/db2` docker image.
1. [docker-init-container](https://github.com/Senzing/docker-init-container) - Dockerfile used to initialize Senzing artifacts.
1. [docker-jupyter](https://github.com/Senzing/docker-jupyter) - Dockerfile for running example Senzing Jupyter notebooks.
1. [docker-python-demo](https://github.com/Senzing/docker-python-demo) - Dockerfile demonstrating simple Flask app using Senzing.
1. [docker-senzing-base](https://github.com/Senzing/docker-senzing-base) - Dockerfile used in FROM statements.
1. [docker-senzing-debug](https://github.com/Senzing/docker-senzing-debug) - Dockerfile for debugging Senzing deployments.
1. [docker-senzing-poc-utility](https://github.com/Senzing/docker-senzing-poc-utility) - Dockerfile wrapping Senzing's POC utility.
1. [docker-test](https://github.com/Senzing/docker-test) - Used in Spikes. Not for production.
1. [docker-web-app-demo](https://github.com/Senzing/docker-web-app-demo) - Dockerfile combining Senzing API server and Senzing Entity WebApp.
1. [docker-yum](https://github.com/Senzing/docker-yum) - Dockerfile wrapping `yum`, a package manager.
1. [docker-yumdownloader](https://github.com/Senzing/docker-yumdownloader) - Dockerfile wrapping `yumdownloader`.
1. [entity-search-web-app](https://github.com/Senzing/entity-search-web-app) - A lightweight http server providing a web UI for entity search through the senzing api server.
1. [mock-data-generator](https://github.com/Senzing/mock-data-generator) - Python tool for generating mock Senzing data and sending it to Kafka, RabbitMQ, or STDOUT.
1. [resolver](https://github.com/Senzing/resolver) - Ephemeral Senzing entity-resolution.
1. [senzing-api-server](https://github.com/Senzing/senzing-api-server) - Server of Senzing REST API.
1. [senzing-package](https://github.com/Senzing/senzing-package) - Python tool for installing Senzing package.
1. [stream-loader](https://github.com/Senzing/stream-loader) - Python tool for loading Senzing G2 from RabbitMQ, Kafka, URL-addressable file, or STDIN.

## docker-compose

*Docker formations using docker-compose.*

1. [docker-compose-demo](https://github.com/Senzing/docker-compose-demo) - Uses `docker-compose` to create a docker formation demonstrating Senzing.

## Kubernetes

*Step-by-step instructions demonstrating use of Senzing on kubernetes-based systems.*

1. [charts](https://github.com/Senzing/charts) - Charts for use with Kubernetes, OpenShift, and Rancher.
1. [kubernetes-demo](https://github.com/Senzing/kubernetes-demo) - Demonstrates Kubernetes deployment of Senzing with queue, database, and Senzing API server.

## Helm Charts

*Git repositories with Helm Charts for Senzing on kubernetes-based systems.*

1. [charts](https://github.com/Senzing/charts) - Charts for use with Kubernetes, OpenShift, and Rancher.
1. [docker-db2-driver-installer](https://github.com/Senzing/docker-db2-driver-installer) - Install DB2 client drivers on mounted volumes.
1. [docker-hello-world](https://github.com/Senzing/docker-hello-world) - Dockerfile for testing docker formations.
1. [docker-ibm-db2](https://github.com/Senzing/docker-ibm-db2) - Wrapper for `ibmcom/db2` docker image.
1. [docker-init-container](https://github.com/Senzing/docker-init-container) - Dockerfile used to initialize Senzing artifacts.
1. [docker-senzing-base](https://github.com/Senzing/docker-senzing-base) - Dockerfile used in FROM statements.
1. [docker-senzing-debug](https://github.com/Senzing/docker-senzing-debug) - Dockerfile for debugging Senzing deployments.
1. [docker-yum](https://github.com/Senzing/docker-yum) - Dockerfile wrapping `yum`, a package manager.
1. [entity-search-web-app](https://github.com/Senzing/entity-search-web-app) - A lightweight http server providing a web UI for entity search through the senzing api server.
1. [mock-data-generator](https://github.com/Senzing/mock-data-generator) - Python tool for generating mock Senzing data and sending it to Kafka, RabbitMQ, or STDOUT.
1. [resolver](https://github.com/Senzing/resolver) - Ephemeral Senzing entity-resolution.
1. [senzing-api-server](https://github.com/Senzing/senzing-api-server) - Server of Senzing REST API.
1. [senzing-package](https://github.com/Senzing/senzing-package) - Python tool for installing Senzing package.
1. [stream-loader](https://github.com/Senzing/stream-loader) - Python tool for loading Senzing G2 from RabbitMQ, Kafka, URL-addressable file, or STDIN.

## Mapper

*Convert industry standard formats to Senzing-ready format.*

1. [mapper-base](https://github.com/Senzing/mapper-base) - Base functions used to map a variety of formats to a Senzing-acceptable format.
1. [mapper-dnb](https://github.com/Senzing/mapper-dnb) - Map DNB format to Senzing format.
1. [mapper-dowjones](https://github.com/Senzing/mapper-dowjones) - Map Dow Jones Watchlist format to Senzing format.
1. [mapper-ijic](https://github.com/Senzing/mapper-ijic) - Map ICIJ format to Senzing format.
1. [mapper-ofac](https://github.com/Senzing/mapper-ofac) - Map OFAC to Senzing format.

## Proof of Concept

*Tools to work with Proof of Concept engagements.*

1. [docker-senzing-poc-utility](https://github.com/Senzing/docker-senzing-poc-utility) - Dockerfile wrapping Senzing's POC utility.
1. [poc-csv-tools](https://github.com/Senzing/poc-csv-tools) - Exemplar artifacts (files) that can be used in other Senzing repositories.
1. [poc-snapshot](https://github.com/Senzing/poc-snapshot) - Snapshot the current state of the records loaded in a Senzing repository.
1. [poc-viewer](https://github.com/Senzing/poc-viewer) - Interactive command line utility that works along with the poc-snapshot utility.

## Resources

*Non-code information.*

1. [awesome](https://github.com/Senzing/awesome) - Curated list of awesome software and resources for Senzing, The First Real-Time AI for Entity Resolution.
1. [knowledge-base](https://github.com/Senzing/knowledge-base) - HOWTOs, tasks, explanations, and more knowledge.
1. [senzing-rest-api](https://github.com/Senzing/senzing-rest-api) - OpenAPI specification of Senzing REST API.
1. [senzing.github.io](https://github.com/Senzing/senzing.github.io) - Organization site at http://senzing.github.io.

## User Interface

*User interfaces for Senzing.*

1. [rest-api-client-ng](https://github.com/Senzing/rest-api-client-ng) - Angular TypeScript interfaces, and classes for interacting with the senzing-api-server.
1. [sdk-components-ng](https://github.com/Senzing/sdk-components-ng) - A collection of UI components to interface with the Senzing Rest API server.
1. [sdk-graph-components](https://github.com/Senzing/sdk-graph-components) - SDK components that can be used in other projects using Angular 7.X.X.

## Utilities

*Tools for working with Senzing.*

1. [docker-adminer](https://github.com/Senzing/docker-adminer) - Dockerfile wrapping `adminer`, a database viewer.
1. [docker-apt](https://github.com/Senzing/docker-apt) - Dockerfile wrapping `apt-get`, a package manager.
1. [docker-aptdownloader](https://github.com/Senzing/docker-aptdownloader) - Dockerfile wrapping `apt-get install --download-only`.
1. [docker-init-container](https://github.com/Senzing/docker-init-container) - Dockerfile used to initialize Senzing artifacts.
1. [docker-mysql](https://github.com/Senzing/docker-mysql) - Dockerfile wrapping `mysql` command line interpreter.
1. [docker-mysql-init](https://github.com/Senzing/docker-mysql-init) - Dockerfile for initializing mysql database with a one-time command.
1. [docker-senzing-debug](https://github.com/Senzing/docker-senzing-debug) - Dockerfile for debugging Senzing deployments.
1. [docker-yum](https://github.com/Senzing/docker-yum) - Dockerfile wrapping `yum`, a package manager.
1. [docker-yumdownloader](https://github.com/Senzing/docker-yumdownloader) - Dockerfile wrapping `yumdownloader`.
1. [entity-search-web-app](https://github.com/Senzing/entity-search-web-app) - A lightweight http server providing a web UI for entity search through the senzing api server.
1. [mock-data-generator](https://github.com/Senzing/mock-data-generator) - Python tool for generating mock Senzing data and sending it to Kafka, RabbitMQ, or STDOUT.
1. [resolver](https://github.com/Senzing/resolver) - Ephemeral Senzing entity-resolution.
1. [senzing-api-server](https://github.com/Senzing/senzing-api-server) - Server of Senzing REST API.
1. [senzing-package](https://github.com/Senzing/senzing-package) - Python tool for installing Senzing package.
1. [stream-loader](https://github.com/Senzing/stream-loader) - Python tool for loading Senzing G2 from RabbitMQ, Kafka, URL-addressable file, or STDIN.

## Under construction

*Being worked on. a.k.a Fresh meat.*

1. [configurator](https://github.com/Senzing/configurator) - :construction: [Under construction] Web service for configuring Senzing.
1. [docker-poc-notebook](https://github.com/Senzing/docker-poc-notebook) - :construction: [Under construction] Jupyter notebook for showing POC results.
1. [elasticsearch](https://github.com/Senzing/elasticsearch) - :construction: [Under construction] Using G2 engine with ElasticSearch indexing engine.
1. [openshift-demo](https://github.com/Senzing/openshift-demo) - :construction: [Under construction] Demonstration using minishift.
1. [packer-senzing-demo-ubuntu-18.04](https://github.com/Senzing/packer-senzing-demo-ubuntu-18.04) - :construction: [Under construction] A packer build of a senzing demo.
1. [stream-configuration](https://github.com/Senzing/stream-configuration) - :construction: [Under construction] Temporary Senzing configuration service.
1. [terraform-senzing-aws-cookbook](https://github.com/Senzing/terraform-senzing-aws-cookbook) - :construction: [Under construction]  A Terraform-based deployment of Senzing on AWS.

## Obsolete

*Although no longer current, may be informative.*

1. [docker-compose-db2-cluster-demo](https://github.com/Senzing/docker-compose-db2-cluster-demo) - :warning: [Obsolete] Demonstrates docker-compose formation of Senzing, DB2 database cluster, and a simple Flask web app.
1. [docker-g2command-db2-cluster](https://github.com/Senzing/docker-g2command-db2-cluster) - :warning: [Obsolete] Dockerfile of Senzing's python G2Command for DB2 cluster.
1. [docker-g2loader-db2-cluster](https://github.com/Senzing/docker-g2loader-db2-cluster) - :warning: [Obsolete] Dockerfile of Senzing's python G2Loader for DB2 cluster.
1. [docker-opt-senzing](https://github.com/Senzing/docker-opt-senzing) - :warning: [Obsolete] Dockerfile containing a "baked-in" /opt/senzing directory.
1. [docker-python-db2-cluster-base](https://github.com/Senzing/docker-python-db2-cluster-base) - :warning: [Obsolete] Dockerfile for Senzing, DB2 cluster, and python 2.7.
1. [docker-python-db2-cluster-demo](https://github.com/Senzing/docker-python-db2-cluster-demo) - :warning: [Obsolete] Dockerfile demonstrating simple Flask app using Senzing and DB2 cluster.
1. [hello-senzing-springboot-java](https://github.com/Senzing/hello-senzing-springboot-java) - :warning: [Obsolete] Demonstrates how to create an HTTP interface to Senzing using SpringBoot.
1. [rancher-demo](https://github.com/Senzing/rancher-demo) - :warning: [Obsolete] Demonstrates Rancher deployment of Senzing with queue, database, and Senzing API server.
1. [webapp-drillthrough-demo](https://github.com/Senzing/webapp-drillthrough-demo) - :warning: [Obsolete] A demonstration of Senzing drill through using Senzing developer toolkit, Node-RED, and Python Flask.

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
