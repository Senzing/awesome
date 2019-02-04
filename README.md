# awesome

Curated list of awesome Senzing software and resources.
Inspired by [other awesome sites](#other-awesome-sites).

## Contents

1. [Demonstrations](#demonstrations)
    1. [docker-compose demonstrations](#docker-compose-demonstrations)
1. [Dockerfiles](#dockerfiles)
1. [Resources](#resources)
1. [Utilities](#utilities)

## Demonstrations

*Step-by-step instructions demonstrating usage of Senzing.*

- [hello-senzing-springboot-java](https://github.com/Senzing/hello-senzing-springboot-java) - Demonstrates how to create an HTTP interface to Senzing using SpringBoot.
- [webapp-drillthrough-demo](https://github.com/Senzing/webapp-drillthrough-demo) - A demonstration of Senzing drill through using Senzing developer toolkit, Node-RED, and Python Flask.

### docker-compose demonstrations

*Docker formations using docker-compose.*

- [Senzing community docker-compose](https://github.com/Senzing?q=docker-compose-) - List of all "docker-compose" repositories on Senzing Community site.
- [docker-compose-db2-demo](https://github.com/Senzing/docker-compose-db2-demo) - Demonstrates docker-compose formation of Senzing, single DB2 instance, and a simple Flask web app.
- [docker-compose-db2-cluster-demo](https://github.com/Senzing/docker-compose-db2-cluster-demo) - Demonstrates docker-compose formation of Senzing, DB2 database cluster, and a simple Flask web app.
- [docker-compose-mysql-demo](https://github.com/Senzing/docker-compose-mysql-demo) - Demonstrates docker-compose formation of Senzing, MySQL, phpMyAdmin, and a simple Flask web app.
- [docker-compose-stream-loader-kafka-demo](https://github.com/Senzing/docker-compose-stream-loader-kafka-demo) - Demonstrates docker-compose formation for loading Senzing G2 via Kafka.

## Dockerfiles

*Dockerfiles for building docker images.*

- [Senzing community Dockerfiles](https://github.com/Senzing?q=docker-) - List of all "docker-" repositories on Senzing Community site.
- [senzing/db2](https://github.com/Senzing/docker-db2) - Dockerfile for the DB2 Command Line Processor (CLP).
- [senzing/db2express-c](https://github.com/Senzing/docker-db2express-c) - Dockerfile wrapping ibmcom/db2express-c docker image.
- [senzing/g2command-db2-cluster](https://github.com/Senzing/docker-g2command-db2-cluster) - Dockerfile of Senzing's G2Command.py for DB2 cluster.
- [senzing/g2command-db2](https://github.com/Senzing/docker-g2command-db2) - Dockerfile of Senzing's G2Command.py for single DB2 database.
- [senzing/g2command](https://github.com/Senzing/docker-g2command) - Dockerfile of Senzing's G2Command.py for MySQL.
- [senzing/g2loader-db2-cluster](https://github.com/Senzing/docker-g2loader-db2-cluster) - Dockerfile of Senzing's python G2Loader for DB2 cluster.
- [senzing/g2loader-db2](https://github.com/Senzing/docker-g2loader-db2)- Dockerfile of Senzing's G2Loader.py for single DB2 database.
- [senzing/g2loader](https://github.com/Senzing/docker-g2loader) - Dockerfile of Senzing's G2Loader.py for MySQL.
- [senzing/jupyter](https://github.com/Senzing/docker-jupyter) - Example Senzing Jupyter notebooks.
- [senzing/mock-data-generator](https://github.com/Senzing/mock-data-generator) - Dockerfile wrapping `mock-data-generator.py`.
- [senzing/mysql](https://github.com/Senzing/docker-mysql) - Dockerfile of MySQL command line interpreter.
- [senzing/mysql-init](https://github.com/Senzing/docker-mysql-init) - Initialize mysql database with a one-time command.
- [senzing/python-3.6-base](https://github.com/Senzing/docker-python-3.6-base) - Dockerfile for Senzing, MySQL, and python 3.6 base installation.
- [senzing/python-base](https://github.com/Senzing/docker-python-base) - Dockerfile for Senzing, MySQL, and python 2.7 base installation.
- [senzing/python-base-complete](https://github.com/Senzing/docker-python-base-complete) - Dockerfile for embedded Senzing, MySQL, and python 2.7 base installation.
- [senzing/python-db2-base](https://github.com/Senzing/docker-python-db2-base) - Dockerfile for Senzing, single DB2 instance, and python 2.7.
- [senzing/python-db2-cluster-base](https://github.com/Senzing/docker-python-db2-cluster-base) - Dockerfile for Senzing, DB2 cluster, and python 2.7.
- [senzing/python-db2-cluster-demo](https://github.com/Senzing/docker-python-db2-cluster-demo) - Dockerfile demonstrating simple Flask app using Senzing and DB2 cluster.
- [senzing/python-db2-demo](https://github.com/Senzing/docker-python-db2-demo) - Dockerfile demonstrating simple Flask app using Senzing and single DB2 instance.
- [senzing/python-demo](https://github.com/Senzing/docker-python-demo) - Dockerfile demonstrating simple Flask app using Senzing and MySQL.
- [senzing/stream-loader](https://github.com/Senzing/stream-loader) - Dockerfile  wrapping `stream-loader.py`.

## Resources

*Non-code information.*

- [awesome](https://github.com/Senzing/awesome) - Curated list of awesome Senzing software and resources.
- [knowledge-base](https://github.com/Senzing/knowledge-base) - HOWTOs, tasks, explanations, and more knowledge.
- [senzing-rest-api](https://github.com/Senzing/senzing-rest-api) - OpenAPI specification of Senzing REST API.

## Utilities

*Tools for managing Senzing.*

- [migrate](https://github.com/Senzing/migrate) - Python tool for migrating Senzing configuration to a new release.
- [mock-data-generator](https://github.com/Senzing/mock-data-generator) - Python tool for generating mock Senzing data and sending it to Kafka or STDOUT.
- [stream-loader](https://github.com/Senzing/stream-loader) - Python tool for loading Senzing G2 from Kafka, URL-addressable file, or STDIN.

## Work in progress

*Fresh meat.*

- [elastic-search](https://github.com/Senzing/elasticsearch)
- [example-senzing-projects](https://github.com/Senzing/example-senzing-projects)
- [relationship-graph-examples](https://github.com/Senzing/relationship-graph-examples)
- [rest-api-client-ng](https://github.com/Senzing/rest-api-client-ng)
- [sdk-components-examples](https://github.com/Senzing/sdk-components-examples)
- [sdk-components-ng](https://github.com/Senzing/sdk-components-ng)
- [sdk-components-web](https://github.com/Senzing/sdk-components-web)
- [senzing-api-server](https://github.com/Senzing/senzing-api-server)

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
