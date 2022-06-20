# awesome

Curated list of awesome Senzing software and resources.
Inspired by [other awesome sites](#other-awesome-sites).

## Contents

1. [Senzing's Top Picks](#senzings-top-picks)
1. [Documentation](#documentation)
1. [Demonstrations](#demonstrations)
1. Docker
    1. [Dockerfiles](#dockerfiles)
    1. [DockerHub](#dockerhub)
    1. [docker-compose](#docker-compose)
    1. [Kubernetes](#kubernetes)
    1. [Helm Charts](#helm-charts)
1. Environment
    1. [AWS environment](#aws-environment)
    1. [Azure environment](#azure-environment)
1. [Mapper](#mapper)
1. [Resources](#resources)
1. [User Interface](#user-interface)
1. [Utilities](#utilities)
    1. [G2Tools](#g2tools)
1. [Under construction](#under-construction)
1. [Obsolete](#obsolete)
1. [Features and bugs](#features-and-bugs)
1. [Other awesome sites](#other-awesome-sites)

## Senzing's Top Picks

*Recommended projects from the team at Senzing.*

1. [docker-compose-demo](https://github.com/Senzing/docker-compose-demo) - Demonstrate Senzing stack using `docker-compose`.
1. [entity-search-web-app](https://github.com/Senzing/entity-search-web-app) - A lightweight http server providing a web UI for entity search through the senzing api server.
1. [senzing-api-server](https://github.com/Senzing/senzing-api-server) - Server of Senzing REST API.
1. [senzinggo](https://github.com/Senzing/senzinggo) - Quickly and easily start the Senzing REST API server, demo web app & Swagger in containers.
1. [stream-loader](https://github.com/Senzing/stream-loader) - Python tool for loading Senzing Engine from RabbitMQ, Kafka, or AWS SQS.
1. [stream-producer](https://github.com/Senzing/stream-producer) - Produce a stream from different input formats.

## Documentation

*Documentation on Senzing usage.*

1. [Promoted articles](https://senzing.zendesk.com/hc/en-us) - Promoted articles.
1. [Senzing API for Developers](https://senzing.zendesk.com/hc/en-us/categories/360000120514-Senzing-API-for-Developers-) - Senzing API for Developers.
1. [Tags used in GitHub](https://github.com/Senzing/knowledge-base/blob/main/lists/github-tags-used.md) - GitHub tags for Senzing artifacts.
1. [community-roadmap](https://github.com/Senzing/community-roadmap) - A peek into the future of the Senzing Community.
1. [evaluate](https://github.com/Senzing/evaluate) - Information for evaluating Senzing at http://senzing.com/evaluate
1. [video](https://github.com/Senzing/video) - Videos available at http://senzing.com/video

## Demonstrations

*Step-by-step instructions demonstrating use of Senzing.*

1. [aws-cloudformation-ecs](https://github.com/Senzing/aws-cloudformation-ecs) - Multiple AWS Cloudformations demonstrating Senzing stack variations.
1. [aws-cloudformation-ecs-poc-simple](https://github.com/Senzing/aws-cloudformation-ecs-poc-simple) - Demonstrate Senzing stack using AWS CloudFormation - simplified.
1. [azure-template-aks-poc-simple](https://github.com/Senzing/azure-template-aks-poc-simple) - An Azure ARM template for bringing up Senzing on Kubernetes (AKS)
1. [docker-app-demo](https://github.com/Senzing/docker-app-demo) - Demonstrate Senzing stack using `docker-app`.
1. [docker-compose-demo](https://github.com/Senzing/docker-compose-demo) - Demonstrate Senzing stack using `docker-compose`.
1. [docker-python-demo](https://github.com/Senzing/docker-python-demo) - Dockerfile demonstrating simple Flask app using Senzing.
1. [ibm-openshift-guide](https://github.com/Senzing/ibm-openshift-guide) - Demonstrate Senzing stack using OpenShift and IBM Db2.
1. [kubernetes-demo](https://github.com/Senzing/kubernetes-demo) - Demonstrate Senzing stack using Kubernetes.
1. [openshift-demo](https://github.com/Senzing/openshift-demo) - Demonstrate Senzing stack using `minishift`.

## Dockerfiles

*Repositories with Dockerfiles.*

1. [connector-neo4j](https://github.com/Senzing/connector-neo4j) - Transform Senzing data into Neo4j graph database.
1. [data-encryption-aes256cbc-sample](https://github.com/Senzing/data-encryption-aes256cbc-sample) - This is a sample encryption plugin, for use with the G2 engine to encrypt sensitive data in the data repository. 
1. [docker-adminer](https://github.com/Senzing/docker-adminer) - Dockerfile wrapping `adminer`, a database viewer.
1. [docker-apt](https://github.com/Senzing/docker-apt) - Dockerfile wrapping `apt-get`, a package manager.
1. [docker-aptdownloader](https://github.com/Senzing/docker-aptdownloader) - Dockerfile wrapping `apt-get install --download-only`.
1. [docker-base-image-debian](https://github.com/Senzing/docker-base-image-debian) - A base docker image for Senzing processes built on Debian.
1. [docker-compose-air-gapper](https://github.com/Senzing/docker-compose-air-gapper) - Create a TGZ bundle for air-gapped environments based on docker-compose.yaml
1. [docker-db2-driver-installer](https://github.com/Senzing/docker-db2-driver-installer) - Install DB2 client drivers on mounted volumes.
1. [docker-hello-world](https://github.com/Senzing/docker-hello-world) - Dockerfile for testing docker formations.
1. [docker-ibm-db2](https://github.com/Senzing/docker-ibm-db2) - Dockerfile wrapping `ibmcom/db2` docker image.
1. [docker-init-container](https://github.com/Senzing/docker-init-container) - Dockerfile used to initialize Senzing artifacts.
1. [docker-installer](https://github.com/Senzing/docker-installer) - Dockerfile use to install Senzing in a non-root container.
1. [docker-jupyter](https://github.com/Senzing/docker-jupyter) - Dockerfile for running example Senzing Jupyter notebooks.
1. [docker-mysql](https://github.com/Senzing/docker-mysql) - Dockerfile wrapping `mysql` command line interpreter.
1. [docker-mysql-init](https://github.com/Senzing/docker-mysql-init) - Dockerfile for initializing mysql database with a one-time command.
1. [docker-python-demo](https://github.com/Senzing/docker-python-demo) - Dockerfile demonstrating simple Flask app using Senzing.
1. [docker-senzing-base](https://github.com/Senzing/docker-senzing-base) - Dockerfile used in FROM statements.
1. [docker-senzing-console](https://github.com/Senzing/docker-senzing-console) - Docker-based console enabled for interacting with Senzing programs.
1. [docker-sshd](https://github.com/Senzing/docker-sshd) - Dockerfile wrapping `sshd`.
1. [docker-web-app-demo](https://github.com/Senzing/docker-web-app-demo) - Dockerfile combining Senzing API server and Senzing Entity WebApp.
1. [docker-wrap-image-with-senzing-apt](https://github.com/Senzing/docker-wrap-image-with-senzing-apt) - Wrap an existing docker image with the Senzing package.
1. [docker-wrap-image-with-senzing-data](https://github.com/Senzing/docker-wrap-image-with-senzing-data) - Add /opt/senzing/data to a base image.
1. [docker-xterm](https://github.com/Senzing/docker-xterm) - Web-based X-terminal.
1. [docker-yum](https://github.com/Senzing/docker-yum) - Dockerfile wrapping `yum`, a package manager.
1. [docker-yumdownloader](https://github.com/Senzing/docker-yumdownloader) - Dockerfile wrapping `yumdownloader`.
1. [entity-search-web-app](https://github.com/Senzing/entity-search-web-app) - A lightweight http server providing a web UI for entity search through the senzing api server.
1. [postgresql-client](https://github.com/Senzing/postgresql-client) - A psql client that waits for the database to be ready before uploading SQL file.
1. [redoer](https://github.com/Senzing/redoer) - Perform Senzing Redo operations.
1. [resolver](https://github.com/Senzing/resolver) - Ephemeral Senzing entity-resolution.
1. [risk-score-calculator](https://github.com/Senzing/risk-score-calculator) - Risk scorer.
1. [senzing-api-server](https://github.com/Senzing/senzing-api-server) - Server of Senzing REST API.
1. [senzing-environment](https://github.com/Senzing/senzing-environment) - Create an environment to use Senzing in a project / virtual environment style.
1. [senzing-listener](https://github.com/Senzing/senzing-listener) - Listener framework.
1. [senzing-poc-server](https://github.com/Senzing/senzing-poc-server) - Senzing API Server plus management APIs.
1. [stream-loader](https://github.com/Senzing/stream-loader) - Python tool for loading Senzing Engine from RabbitMQ, Kafka, or AWS SQS.
1. [stream-logger](https://github.com/Senzing/stream-logger) - A utility for dumping the contents of a stream to a log.
1. [stream-producer](https://github.com/Senzing/stream-producer) - Produce a stream from different input formats.

## DockerHub

*Git repositories with Docker images on [DockerHub](https://hub.docker.com/r/senzing/).*

1. [data-encryption-aes256cbc-sample](https://github.com/Senzing/data-encryption-aes256cbc-sample) - This is a sample encryption plugin, for use with the G2 engine to encrypt sensitive data in the data repository. 
1. [docker-adminer](https://github.com/Senzing/docker-adminer) - Dockerfile wrapping `adminer`, a database viewer.
1. [docker-apt](https://github.com/Senzing/docker-apt) - Dockerfile wrapping `apt-get`, a package manager.
1. [docker-aptdownloader](https://github.com/Senzing/docker-aptdownloader) - Dockerfile wrapping `apt-get install --download-only`.
1. [docker-base-image-debian](https://github.com/Senzing/docker-base-image-debian) - A base docker image for Senzing processes built on Debian.
1. [docker-db2-driver-installer](https://github.com/Senzing/docker-db2-driver-installer) - Install DB2 client drivers on mounted volumes.
1. [docker-hello-world](https://github.com/Senzing/docker-hello-world) - Dockerfile for testing docker formations.
1. [docker-ibm-db2](https://github.com/Senzing/docker-ibm-db2) - Dockerfile wrapping `ibmcom/db2` docker image.
1. [docker-init-container](https://github.com/Senzing/docker-init-container) - Dockerfile used to initialize Senzing artifacts.
1. [docker-jupyter](https://github.com/Senzing/docker-jupyter) - Dockerfile for running example Senzing Jupyter notebooks.
1. [docker-python-demo](https://github.com/Senzing/docker-python-demo) - Dockerfile demonstrating simple Flask app using Senzing.
1. [docker-senzing-base](https://github.com/Senzing/docker-senzing-base) - Dockerfile used in FROM statements.
1. [docker-senzing-console](https://github.com/Senzing/docker-senzing-console) - Docker-based console enabled for interacting with Senzing programs.
1. [docker-sshd](https://github.com/Senzing/docker-sshd) - Dockerfile wrapping `sshd`.
1. [docker-test](https://github.com/Senzing/docker-test) - Used in Spikes. Not for production.
1. [docker-web-app-demo](https://github.com/Senzing/docker-web-app-demo) - Dockerfile combining Senzing API server and Senzing Entity WebApp.
1. [docker-xterm](https://github.com/Senzing/docker-xterm) - Web-based X-terminal.
1. [docker-yum](https://github.com/Senzing/docker-yum) - Dockerfile wrapping `yum`, a package manager.
1. [docker-yumdownloader](https://github.com/Senzing/docker-yumdownloader) - Dockerfile wrapping `yumdownloader`.
1. [entity-search-web-app](https://github.com/Senzing/entity-search-web-app) - A lightweight http server providing a web UI for entity search through the senzing api server.
1. [redoer](https://github.com/Senzing/redoer) - Perform Senzing Redo operations.
1. [resolver](https://github.com/Senzing/resolver) - Ephemeral Senzing entity-resolution.
1. [risk-score-calculator](https://github.com/Senzing/risk-score-calculator) - Risk scorer.
1. [senzing-api-server](https://github.com/Senzing/senzing-api-server) - Server of Senzing REST API.
1. [senzing-environment](https://github.com/Senzing/senzing-environment) - Create an environment to use Senzing in a project / virtual environment style.
1. [senzing-listener](https://github.com/Senzing/senzing-listener) - Listener framework.
1. [senzing-poc-server](https://github.com/Senzing/senzing-poc-server) - Senzing API Server plus management APIs.
1. [stream-loader](https://github.com/Senzing/stream-loader) - Python tool for loading Senzing Engine from RabbitMQ, Kafka, or AWS SQS.
1. [stream-logger](https://github.com/Senzing/stream-logger) - A utility for dumping the contents of a stream to a log.
1. [stream-producer](https://github.com/Senzing/stream-producer) - Produce a stream from different input formats.

## docker-compose

*Docker formations using docker-compose.*

1. [docker-compose-air-gapper](https://github.com/Senzing/docker-compose-air-gapper) - Create a TGZ bundle for air-gapped environments based on docker-compose.yaml
1. [docker-compose-demo](https://github.com/Senzing/docker-compose-demo) - Demonstrate Senzing stack using `docker-compose`.

## G2Tools

*G2Tools distributed with Senzing API package.*

1. [compressedfile](https://github.com/Senzing/compressedfile) - Distributed with Senzing API package
1. [dumpstack](https://github.com/Senzing/dumpstack) - Distributed with Senzing API package
1. [g2audit](https://github.com/Senzing/g2audit) - Distributed with Senzing API package
1. [g2command](https://github.com/Senzing/g2command) - Distributed with Senzing API package
1. [g2configtables](https://github.com/Senzing/g2configtables) - Distributed with Senzing API package
1. [g2configtool](https://github.com/Senzing/g2configtool) - Distributed with Senzing API package
1. [g2createproject](https://github.com/Senzing/g2createproject) - Distributed with Senzing API package
1. [g2database](https://github.com/Senzing/g2database) - Distributed with Senzing API package
1. [g2explorer](https://github.com/Senzing/g2explorer) - Distributed with Senzing API package
1. [g2export](https://github.com/Senzing/g2export) - Distributed with Senzing API package
1. [g2loader](https://github.com/Senzing/g2loader) - Distributed with Senzing API package
1. [g2paths](https://github.com/Senzing/g2paths) - Distributed with Senzing API package
1. [g2project](https://github.com/Senzing/g2project) - Distributed with Senzing API package
1. [g2s3](https://github.com/Senzing/g2s3) - Distributed with Senzing API package
1. [g2setupconfig](https://github.com/Senzing/g2setupconfig) - Distributed with Senzing API package
1. [g2snapshot](https://github.com/Senzing/g2snapshot) - Distributed with Senzing API package
1. [g2updateproject](https://github.com/Senzing/g2updateproject) - Distributed with Senzing API package
1. [senzinggo](https://github.com/Senzing/senzinggo) - Quickly and easily start the Senzing REST API server, demo web app & Swagger in containers.
1. [truth-sets](https://github.com/Senzing/truth-sets) - Distributed with Senzing API package

## Kubernetes

*Step-by-step instructions demonstrating use of Senzing on kubernetes-based systems.*

1. [azure-template-aks-poc-simple](https://github.com/Senzing/azure-template-aks-poc-simple) - An Azure ARM template for bringing up Senzing on Kubernetes (AKS)
1. [charts](https://github.com/Senzing/charts) - Helm Charts for use with Kubernetes, OpenShift, and Rancher.
1. [docker-apt](https://github.com/Senzing/docker-apt) - Dockerfile wrapping `apt-get`, a package manager.
1. [docker-init-container](https://github.com/Senzing/docker-init-container) - Dockerfile used to initialize Senzing artifacts.
1. [docker-installer](https://github.com/Senzing/docker-installer) - Dockerfile use to install Senzing in a non-root container.
1. [docker-senzing-console](https://github.com/Senzing/docker-senzing-console) - Docker-based console enabled for interacting with Senzing programs.
1. [entity-search-web-app](https://github.com/Senzing/entity-search-web-app) - A lightweight http server providing a web UI for entity search through the senzing api server.
1. [kubernetes-demo](https://github.com/Senzing/kubernetes-demo) - Demonstrate Senzing stack using Kubernetes.
1. [postgresql-client](https://github.com/Senzing/postgresql-client) - A psql client that waits for the database to be ready before uploading SQL file.
1. [redoer](https://github.com/Senzing/redoer) - Perform Senzing Redo operations.
1. [senzing-api-server](https://github.com/Senzing/senzing-api-server) - Server of Senzing REST API.
1. [stream-loader](https://github.com/Senzing/stream-loader) - Python tool for loading Senzing Engine from RabbitMQ, Kafka, or AWS SQS.
1. [stream-producer](https://github.com/Senzing/stream-producer) - Produce a stream from different input formats.

## Helm Charts

*Git repositories with Helm Charts for Senzing on kubernetes-based systems.*

1. [charts](https://github.com/Senzing/charts) - Helm Charts for use with Kubernetes, OpenShift, and Rancher.
1. [docker-apt](https://github.com/Senzing/docker-apt) - Dockerfile wrapping `apt-get`, a package manager.
1. [docker-db2-driver-installer](https://github.com/Senzing/docker-db2-driver-installer) - Install DB2 client drivers on mounted volumes.
1. [docker-hello-world](https://github.com/Senzing/docker-hello-world) - Dockerfile for testing docker formations.
1. [docker-ibm-db2](https://github.com/Senzing/docker-ibm-db2) - Dockerfile wrapping `ibmcom/db2` docker image.
1. [docker-init-container](https://github.com/Senzing/docker-init-container) - Dockerfile used to initialize Senzing artifacts.
1. [docker-installer](https://github.com/Senzing/docker-installer) - Dockerfile use to install Senzing in a non-root container.
1. [docker-senzing-base](https://github.com/Senzing/docker-senzing-base) - Dockerfile used in FROM statements.
1. [docker-senzing-console](https://github.com/Senzing/docker-senzing-console) - Docker-based console enabled for interacting with Senzing programs.
1. [docker-yum](https://github.com/Senzing/docker-yum) - Dockerfile wrapping `yum`, a package manager.
1. [entity-search-web-app](https://github.com/Senzing/entity-search-web-app) - A lightweight http server providing a web UI for entity search through the senzing api server.
1. [postgresql-client](https://github.com/Senzing/postgresql-client) - A psql client that waits for the database to be ready before uploading SQL file.
1. [redoer](https://github.com/Senzing/redoer) - Perform Senzing Redo operations.
1. [resolver](https://github.com/Senzing/resolver) - Ephemeral Senzing entity-resolution.
1. [senzing-api-server](https://github.com/Senzing/senzing-api-server) - Server of Senzing REST API.
1. [senzing-poc-server](https://github.com/Senzing/senzing-poc-server) - Senzing API Server plus management APIs.
1. [stream-loader](https://github.com/Senzing/stream-loader) - Python tool for loading Senzing Engine from RabbitMQ, Kafka, or AWS SQS.
1. [stream-producer](https://github.com/Senzing/stream-producer) - Produce a stream from different input formats.

## AWS Environment

*Projects specific to Amazon Web Services environment.*

1. [aws-cloudformation-database-cluster](https://github.com/Senzing/aws-cloudformation-database-cluster) - AWS Cloudformation with VPC and Senzing database cluster
1. [aws-cloudformation-dev-rest](https://github.com/Senzing/aws-cloudformation-dev-rest) - AWS Cloudformation for developers using Senzing HTTP REST API
1. [aws-cloudformation-ecs](https://github.com/Senzing/aws-cloudformation-ecs) - Multiple AWS Cloudformations demonstrating Senzing stack variations.
1. [aws-cloudformation-ecs-poc-simple](https://github.com/Senzing/aws-cloudformation-ecs-poc-simple) - Demonstrate Senzing stack using AWS CloudFormation - simplified.
1. [aws-cloudformation-ecs-senzing-stack-basic](https://github.com/Senzing/aws-cloudformation-ecs-senzing-stack-basic) - AWS Cloudformation demonstrating a Senzing stack that can be used with aws-cloudformation-database-cluster.
1. [aws-cloudformation-ecs-senzing-stack-choices](https://github.com/Senzing/aws-cloudformation-ecs-senzing-stack-choices) - AWS Cloudformation with additional configuration options.
1. [aws-marketplace-evaluation](https://github.com/Senzing/aws-marketplace-evaluation) - AWS Marketplace offering.

## Azure Environment

*Projects specific to Microsoft's Azure environment.*

1. [azure-template-aks-poc-simple](https://github.com/Senzing/azure-template-aks-poc-simple) - An Azure ARM template for bringing up Senzing on Kubernetes (AKS)

## Examples

*Code that shows how to perform a task.*

1. [data-encryption-aes256cbc-sample](https://github.com/Senzing/data-encryption-aes256cbc-sample) - This is a sample encryption plugin, for use with the G2 engine to encrypt sensitive data in the data repository. 

## Mapper

*Convert industry standard formats to Senzing-ready format.*

1. [mapper-base](https://github.com/Senzing/mapper-base) - Base functions used to map a variety of formats to a Senzing-acceptable format.
1. [mapper-csv](https://github.com/Senzing/mapper-csv) - Exemplar artifacts (files) that can be used in other Senzing repositories.
1. [mapper-dnb](https://github.com/Senzing/mapper-dnb) - Map DNB format to Senzing format.
1. [mapper-dowjones](https://github.com/Senzing/mapper-dowjones) - Map Dow Jones Watchlist format to Senzing format.
1. [mapper-icij](https://github.com/Senzing/mapper-icij) - Map ICIJ format to Senzing format.
1. [mapper-leie](https://github.com/Senzing/mapper-leie) - Map US HHS LEIE to Senzing format.
1. [mapper-nomino](https://github.com/Senzing/mapper-nomino) -  Map Nomino format to Senzing format.
1. [mapper-npi](https://github.com/Senzing/mapper-npi) - Map NPPES NPI Registry to Senzing format.
1. [mapper-ofac](https://github.com/Senzing/mapper-ofac) - Map OFAC to Senzing format.
1. [mapper-openc](https://github.com/Senzing/mapper-openc) - Map Open Corporate into Senzing format.
1. [mapper-opensanctions](https://github.com/Senzing/mapper-opensanctions) - Map Open Sanctions into Senzing format.
1. [mapper-sayari](https://github.com/Senzing/mapper-sayari) - Map Sayari's global corporate data into Senzing format.

## Resources

*Non-code information.*

1. [awesome](https://github.com/Senzing/awesome) - Curated list of awesome software and resources for Senzing, The First Real-Time AI for Entity Resolution.
1. [knowledge-base](https://github.com/Senzing/knowledge-base) - HOWTOs, tasks, explanations, and more knowledge.
1. [senzing-data-encryption-specification](https://github.com/Senzing/senzing-data-encryption-specification) - This is the interface for creating encryption plugins, to work with the G2 engine to encrypt sensitive data in the data repository.
1. [senzing-entity-specification](https://github.com/Senzing/senzing-entity-specification) - Complete Senzing Entity Specification and Attribute Dictionary.
1. [senzing-rest-api-specification](https://github.com/Senzing/senzing-rest-api-specification) - OpenAPI specification of Senzing REST API.
1. [senzing-sdk-api-specification](https://github.com/Senzing/senzing-sdk-api-specification) - Software Development Kit documentation.
1. [senzing.github.io](https://github.com/Senzing/senzing.github.io) - Organization site at http://hub.senzing.com

## SDKs

*Software development kits for various platforms.*

1. [g2-sdk-java](https://github.com/Senzing/g2-sdk-java) - Java SDK hosted on MvnRepository.
1. [g2-sdk-python](https://github.com/Senzing/g2-sdk-python) - Python SDK hosted on PYPI.
1. [sdk-components-ng](https://github.com/Senzing/sdk-components-ng) - A collection of UI components to interface with the Senzing Rest API server.
1. [sdk-graph-components](https://github.com/Senzing/sdk-graph-components) - SDK components that can be used in other projects using Angular 7.X.X.
1. [senzing-sdk-api-specification](https://github.com/Senzing/senzing-sdk-api-specification) - Software Development Kit documentation.

## User Interface

*User interfaces for Senzing.*

1. [rest-api-client-ng](https://github.com/Senzing/rest-api-client-ng) - Angular TypeScript interfaces, and classes for interacting with the senzing-api-server.
1. [sdk-components-ng](https://github.com/Senzing/sdk-components-ng) - A collection of UI components to interface with the Senzing Rest API server.
1. [sdk-graph-components](https://github.com/Senzing/sdk-graph-components) - SDK components that can be used in other projects using Angular 7.X.X.

## Utilities

*Tools for working with Senzing.*

1. [ansible-playbook-demo](https://github.com/Senzing/ansible-playbook-demo) - Example of Ansible playbook.
1. [ansible-role-senzingapi](https://github.com/Senzing/ansible-role-senzingapi) - Ansible role - senzingapi
1. [ansible-role-stream-producer](https://github.com/Senzing/ansible-role-stream-producer) - Ansible role - Senzing Stream Producer
1. [docker-adminer](https://github.com/Senzing/docker-adminer) - Dockerfile wrapping `adminer`, a database viewer.
1. [docker-apt](https://github.com/Senzing/docker-apt) - Dockerfile wrapping `apt-get`, a package manager.
1. [docker-aptdownloader](https://github.com/Senzing/docker-aptdownloader) - Dockerfile wrapping `apt-get install --download-only`.
1. [docker-compose-air-gapper](https://github.com/Senzing/docker-compose-air-gapper) - Create a TGZ bundle for air-gapped environments based on docker-compose.yaml
1. [docker-init-container](https://github.com/Senzing/docker-init-container) - Dockerfile used to initialize Senzing artifacts.
1. [docker-mysql](https://github.com/Senzing/docker-mysql) - Dockerfile wrapping `mysql` command line interpreter.
1. [docker-mysql-init](https://github.com/Senzing/docker-mysql-init) - Dockerfile for initializing mysql database with a one-time command.
1. [docker-sshd](https://github.com/Senzing/docker-sshd) - Dockerfile wrapping `sshd`.
1. [docker-wrap-image-with-senzing-data](https://github.com/Senzing/docker-wrap-image-with-senzing-data) - Add /opt/senzing/data to a base image.
1. [docker-xterm](https://github.com/Senzing/docker-xterm) - Web-based X-terminal.
1. [docker-yum](https://github.com/Senzing/docker-yum) - Dockerfile wrapping `yum`, a package manager.
1. [docker-yumdownloader](https://github.com/Senzing/docker-yumdownloader) - Dockerfile wrapping `yumdownloader`.
1. [entity-search-web-app](https://github.com/Senzing/entity-search-web-app) - A lightweight http server providing a web UI for entity search through the senzing api server.
1. [g2-python](https://github.com/Senzing/g2-python) - Tools found at g2/python in the SenzingAPI package.
1. [github-util](https://github.com/Senzing/github-util) - Works with GitHub metadata.
1. [governor-postgresql-transaction-id](https://github.com/Senzing/governor-postgresql-transaction-id) - Governor plugin for PostgreSQL transaction IDs.
1. [packer-ansible](https://github.com/Senzing/packer-ansible) - Use Packer to build virtual machines with Ansible.
1. [postgresql-client](https://github.com/Senzing/postgresql-client) - A psql client that waits for the database to be ready before uploading SQL file.
1. [redoer](https://github.com/Senzing/redoer) - Perform Senzing Redo operations.
1. [resolver](https://github.com/Senzing/resolver) - Ephemeral Senzing entity-resolution.
1. [risk-score-calculator](https://github.com/Senzing/risk-score-calculator) - Risk scorer.
1. [senzing-api-server](https://github.com/Senzing/senzing-api-server) - Server of Senzing REST API.
1. [senzing-commons-java](https://github.com/Senzing/senzing-commons-java) - Java classes used in multiple Senzing projects
1. [senzing-environment](https://github.com/Senzing/senzing-environment) - Create an environment to use Senzing in a project / virtual environment style.
1. [senzing-listener](https://github.com/Senzing/senzing-listener) - Listener framework.
1. [senzing-poc-server](https://github.com/Senzing/senzing-poc-server) - Senzing API Server plus management APIs.
1. [senzinggo](https://github.com/Senzing/senzinggo) - Quickly and easily start the Senzing REST API server, demo web app & Swagger in containers.
1. [stream-loader](https://github.com/Senzing/stream-loader) - Python tool for loading Senzing Engine from RabbitMQ, Kafka, or AWS SQS.
1. [stream-logger](https://github.com/Senzing/stream-logger) - A utility for dumping the contents of a stream to a log.
1. [stream-producer](https://github.com/Senzing/stream-producer) - Produce a stream from different input formats.

## Under construction

*Being worked on. a.k.a. Fresh meat.*

1. [configurator](https://github.com/Senzing/configurator) - Web service for configuring Senzing.
1. [data-mart-replicator](https://github.com/Senzing/data-mart-replicator) - Data mart
1. [docker-terraform-aws](https://github.com/Senzing/docker-terraform-aws) - :construction: [Under construction] 
1. [java-g2loader](https://github.com/Senzing/java-g2loader) - :construction: [Under construction] 
1. [packer-senzing-demo-ubuntu-18.04](https://github.com/Senzing/packer-senzing-demo-ubuntu-18.04) - :construction: [Under construction] A packer build of a senzing demo.
1. [rest-api-client-java](https://github.com/Senzing/rest-api-client-java) - :construction: [Under construction] - Client built from OpenAPI specification.
1. [stream-configuration](https://github.com/Senzing/stream-configuration) - :construction: [Under construction] Temporary Senzing configuration service.

## Obsolete

*Although no longer current, may be informative.*

1. [docker-python-db2-cluster-base](https://github.com/Senzing/docker-python-db2-cluster-base) - :warning: [Obsolete] Dockerfile for Senzing, DB2 cluster, and python 2.7.
1. [spike-docker-store-based-images](https://github.com/Senzing/spike-docker-store-based-images) - :warning: [Obsolete] Use docker image in Docker Store.

## Features and bugs

*How to request new features and bug fixes.*

1. [Request bug fix](https://github.com/Senzing/knowledge-base/blob/main/HOWTO/request-bug-fix.md)
1. [Request new feature in existing repository](https://github.com/Senzing/knowledge-base/blob/main/HOWTO/request-new-feature-in-existing-repository.md)
1. [Request new feature](https://github.com/Senzing/knowledge-base/blob/main/HOWTO/request-new-feature.md)

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
