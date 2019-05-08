# awesome

Curated list of awesome Senzing software and resources.
Inspired by [other awesome sites](#other-awesome-sites).

## Contents

1. [Docker](#docker)
    1. [Dockerfiles](#dockerfiles)
    1. [docker-compose demonstrations](#docker-compose-demonstrations)
    1. [Kubernetes demonstrations](#kubernetes-demonstrations)
1. [Demonstrations](#demonstrations)
1. [Resources](#resources)
1. [Utilities](#utilities)
1. [Work in progress](#work-in-progress)

## Docker

### Dockerfiles

*Dockerfiles for building docker images.  The clickable :whale: icon means it's available as a docker image on [hub.docker.com](https://hub.docker.com/u/senzing)*

- [Senzing community Dockerfiles](https://github.com/Senzing?q=docker-) - List of all "docker-" repositories on Senzing Community site.
- [senzing/db2](https://github.com/Senzing/docker-db2) - Dockerfile for the DB2 Command Line Processor (CLP).
- [senzing/db2express-c](https://github.com/Senzing/docker-db2express-c) - Dockerfile wrapping ibmcom/db2express-c docker image.
- [senzing/g2command](https://github.com/Senzing/docker-g2command) [:whale:](https://hub.docker.com/r/senzing/g2command) - Dockerfile wrapping Senzing's G2Command.py.
- [senzing/g2command-db2-cluster](https://github.com/Senzing/docker-g2command-db2-cluster) - Dockerfile of Senzing's G2Command.py for DB2 cluster.
- [senzing/g2loader](https://github.com/Senzing/docker-g2loader) [:whale:](https://hub.docker.com/r/senzing/g2loader) - Dockerfile wrapping Senzing's G2Loader.py.
- [senzing/g2loader-db2-cluster](https://github.com/Senzing/docker-g2loader-db2-cluster) - Dockerfile of Senzing's python G2Loader for DB2 cluster.
- [senzing/jupyter](https://github.com/Senzing/docker-jupyter) [:whale:](https://hub.docker.com/r/senzing/jupyter) - Example Senzing Jupyter notebooks.
- [senzing/mock-data-generator](https://github.com/Senzing/mock-data-generator) [:whale:](https://hub.docker.com/r/senzing/mock-data-generator)  - Dockerfile wrapping `mock-data-generator.py`.
- [senzing/mysql](https://github.com/Senzing/docker-mysql) - Dockerfile of MySQL command line interpreter.
- [senzing/mysql-init](https://github.com/Senzing/docker-mysql-init) - Initialize mysql database with a one-time command.
- [senzing/opt-senzing](https://github.com/Senzing/docker-opt-senzing) - Dockerfile containing a "baked-in" /opt/senzing directory.
- [senzing/python-3.6-base](https://github.com/Senzing/docker-python-3.6-base) - Dockerfile for Senzing, MySQL, and python 3.6 base installation.
- [senzing/python-base-complete](https://github.com/Senzing/docker-python-base-complete) - Dockerfile for embedded Senzing, MySQL, and python 2.7 base installation.
- [senzing/python-db2-base](https://github.com/Senzing/docker-python-db2-base) - Dockerfile for Senzing, single DB2 instance, and python 2.7.
- [senzing/python-db2-cluster-base](https://github.com/Senzing/docker-python-db2-cluster-base) - Dockerfile for Senzing, DB2 cluster, and python 2.7.
- [senzing/python-db2-cluster-demo](https://github.com/Senzing/docker-python-db2-cluster-demo) - Dockerfile demonstrating simple Flask app using Senzing and DB2 cluster.
- [senzing/python-demo](https://github.com/Senzing/docker-python-demo) [:whale:](https://hub.docker.com/r/senzing/python-demo) - Dockerfile demonstrating simple Flask app using Senzing.
- [senzing/python-mysql-base](https://github.com/Senzing/docker-python-mysql-base) - Dockerfile for Senzing, MySQL, and python 2.7 base installation.
- [senzing/python-postgresql-base](https://github.com/Senzing/docker-python-postgresql-base) - Dockerfile for Senzing, PostgreSQL, and python 2.7 base installation.
- [senzing/senzing-api-server](https://github.com/Senzing/senzing-api-server) [:whale:](https://hub.docker.com/r/senzing/senzing-api-server) - Dockerfile for server of Senzing REST API.
- [senzing/senzing-base](https://github.com/Senzing/docker-senzing-base) [:whale:](https://hub.docker.com/r/senzing/senzing-base) - Dockerfile used in FROM statements.
- [senzing/senzing-debug](https://github.com/Senzing/docker-senzing-debug) [:whale:](https://hub.docker.com/r/senzing/senzing-debug) - Dockerfile for debugging Senzing deployments.
- [senzing/senzing-package](https://github.com/Senzing/senzing-package) - Dockerfile wrapping `senzing-package.py`.
- [senzing/senzing-poc-utility](https://github.com/Senzing/docker-senzing-poc-utility) [:whale:](https://hub.docker.com/r/senzing/senzing-poc-utility) - Dockerfile wrapping Senzing's POC utility.
- [senzing/stream-loader](https://github.com/Senzing/stream-loader) [:whale:](https://hub.docker.com/r/senzing/stream-loader) - Dockerfile  wrapping `stream-loader.py`.

### docker-compose demonstrations

*Docker formations using docker-compose.*

- [Senzing community docker-compose](https://github.com/Senzing?q=docker-compose-) - List of all "docker-compose" repositories on Senzing Community site.
- [docker-compose-db2-demo](https://github.com/Senzing/docker-compose-db2-demo) - Demonstrates docker-compose formation of Senzing, single DB2 instance, and a simple Flask web app.
- [docker-compose-db2-cluster-demo](https://github.com/Senzing/docker-compose-db2-cluster-demo) - Demonstrates docker-compose formation of Senzing, DB2 database cluster, and a simple Flask web app.
- [docker-compose-demo](https://github.com/Senzing/docker-compose-demo) - Demonstrates docker-compose formation of Senzing with queue, database, and a simple Flask web app.
- [docker-compose-mysql-demo](https://github.com/Senzing/docker-compose-mysql-demo) - Demonstrates docker-compose formation of Senzing, MySQL, phpMyAdmin, and a simple Flask web app.
- [docker-compose-postgresql-demo](https://github.com/Senzing/docker-compose-postgresql-demo) - Demonstrates docker-compose formation of Senzing, PostgreSQL, phpPgAdmin, and a simple Flask web app.

### Kubernetes demonstrations

- [kubernetes-demo](https://github.com/Senzing/kubernetes-demo) - Demonstrates Kubernetes deployment of Senzing with queue, database, and a simple Flask web app.
- [rancher-demo](https://github.com/Senzing/rancher-demo) - A demonstration of Senzing in a Rancher environment.

## Demonstrations

*Step-by-step instructions demonstrating usage of Senzing.*

- [webapp-drillthrough-demo](https://github.com/Senzing/webapp-drillthrough-demo) - A demonstration of Senzing drill through using Senzing developer toolkit, Node-RED, and Python Flask.
- [hello-senzing-springboot-java](https://github.com/Senzing/hello-senzing-springboot-java) - Demonstrates how to create an HTTP interface to Senzing using SpringBoot.

## Resources

*Non-code information.*

- [awesome](https://github.com/Senzing/awesome) - Curated list of awesome Senzing software and resources.
- [charts](https://github.com/Senzing/charts) - Charts for use with Rancher and Kubernetes.
- [knowledge-base](https://github.com/Senzing/knowledge-base) - HOWTOs, tasks, explanations, and more knowledge.
- [senzing-rest-api](https://github.com/Senzing/senzing-rest-api) - OpenAPI specification of Senzing REST API.

## Utilities

*Tools for working with Senzing.*

- [migrate](https://github.com/Senzing/migrate) - Python tool for migrating Senzing configuration to a new release.
- [mock-data-generator.py](https://github.com/Senzing/mock-data-generator) - Python tool for generating mock Senzing data and sending it to Kafka, RabbitMQ, or STDOUT.
- [senzing-api-server](https://github.com/Senzing/senzing-api-server) - Server of Senzing REST API.
- [senzing-package.py](https://github.com/Senzing/senzing-api-server) - Install Senzing TGZ file.
- [stream-loader.py](https://github.com/Senzing/stream-loader) - Python tool for loading Senzing G2 from Kafka, URL-addressable file, or STDIN.

## Work in progress

*Fresh meat.*

- [elastic-search](https://github.com/Senzing/elasticsearch)
- [example-senzing-projects](https://github.com/Senzing/example-senzing-projects)
- [ibm-icp4d-guide](https://github.com/Senzing/ibm-icp4d-guide) - Reference implementation for Senzing on IBM Cloud Private for Data.
- [rest-api-client-ng](https://github.com/Senzing/rest-api-client-ng) - Angular TypeScript interfaces, and classes for interacting with the senzing-api-server.

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
