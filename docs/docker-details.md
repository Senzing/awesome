# Docker details

## Docker

### Dockerfiles

*Dockerfiles for building docker images.
The clickable [:whale:](https://hub.docker.com/u/senzing) icon means
it's available as a docker image on [hub.docker.com](https://hub.docker.com/u/senzing).*

| Image name with GitHub link                                                                  | Non-root           | Immutable          | DockerHub | Description |
|----------------------------------------------------------------------------------------------|:------------------:|:------------------:|:---------:|-------------|
| [senzing/db2](https://github.com/Senzing/docker-db2)                                         |                    |                    | | Dockerfile for the DB2 Command Line Processor (CLP).
| [senzing/db2express-c](https://github.com/Senzing/docker-db2express-c)                       |                    |                    | | Dockerfile wrapping ibmcom/db2express-c docker image.
| [senzing/entity-search-web-app](https://github.com/Senzing/entity-search-web-app)            |                    |                    | [:whale:](https://hub.docker.com/r/senzing/entity-search-web-app) | Dockerfile wrapping entity-search-web-app.
| [senzing/g2configtool](https://github.com/Senzing/docker-g2configtool)                       |                    |                    | [:whale:](https://github.com/Senzing/docker-g2configtool) | Dockerfile wrapping Senzing's G2ConfigTool.py.
| [senzing/g2command](https://github.com/Senzing/docker-g2command)                             |                    |                    | [:whale:](https://hub.docker.com/r/senzing/g2command) | Dockerfile wrapping Senzing's G2Command.py.
| [senzing/g2command-db2-cluster](https://github.com/Senzing/docker-g2command-db2-cluster)     |                    |                    | | Dockerfile of Senzing's G2Command.py for DB2 cluster.
| [senzing/g2loader](https://github.com/Senzing/docker-g2loader)                               |                    |                    | [:whale:](https://hub.docker.com/r/senzing/g2loader) | Dockerfile wrapping Senzing's G2Loader.py.
| [senzing/g2loader-db2-cluster](https://github.com/Senzing/docker-g2loader-db2-cluster)       |                    |                    | | Dockerfile of Senzing's python G2Loader for DB2 cluster.
| [senzing/jupyter](https://github.com/Senzing/docker-jupyter)                                 |                    |                    | [:whale:](https://hub.docker.com/r/senzing/jupyter) | Dockerfile for running example Senzing Jupyter notebooks.
| [senzing/mock-data-generator](https://github.com/Senzing/mock-data-generator)                |                    |                    | [:whale:](https://hub.docker.com/r/senzing/mock-data-generator)  | Dockerfile wrapping `mock-data-generator.py`.
| [senzing/mysql](https://github.com/Senzing/docker-mysql)                                     |                    |                    | | Dockerfile of MySQL command line interpreter.
| [senzing/mysql-init](https://github.com/Senzing/docker-mysql-init)                           |                    |                    | | Dockerfile for initializing mysql database with a one-time command.
| [senzing/opt-senzing](https://github.com/Senzing/docker-opt-senzing)                         |                    |                    | | Dockerfile containing a "baked-in" /opt/senzing directory.
| [senzing/python-3.6-base](https://github.com/Senzing/docker-python-3.6-base)                 |                    |                    | | Dockerfile for Senzing, MySQL, and python 3.6 base installation.
| [senzing/python-base-complete](https://github.com/Senzing/docker-python-base-complete)       |                    |                    | | Dockerfile for embedded Senzing, MySQL, and python 2.7 base installation.
| [senzing/python-db2-base](https://github.com/Senzing/docker-python-db2-base)                 |                    |                    | | Dockerfile for Senzing, single DB2 instance, and python 2.7.
| [senzing/python-db2-cluster-base](https://github.com/Senzing/docker-python-db2-cluster-base) |                    |                    | | Dockerfile for Senzing, DB2 cluster, and python 2.7.
| [senzing/python-db2-cluster-demo](https://github.com/Senzing/docker-python-db2-cluster-demo) |                    |                    | | Dockerfile demonstrating simple Flask app using Senzing and DB2 cluster.
| [senzing/python-demo](https://github.com/Senzing/docker-python-demo)                         |                    |                    | [:whale:](https://hub.docker.com/r/senzing/python-demo) | Dockerfile demonstrating simple Flask app using Senzing.
| [senzing/python-mysql-base](https://github.com/Senzing/docker-python-mysql-base)             |                    |                    | | Dockerfile for Senzing, MySQL, and python 2.7 base installation.
| [senzing/python-postgresql-base](https://github.com/Senzing/docker-python-postgresql-base)   |                    |                    | | Dockerfile for Senzing, PostgreSQL, and python 2.7 base installation.
| [senzing/senzing-api-server](https://github.com/Senzing/senzing-api-server)                  |                    |                    | [:whale:](https://hub.docker.com/r/senzing/senzing-api-server) | Dockerfile for server of Senzing REST API.
| [senzing/senzing-base](https://github.com/Senzing/docker-senzing-base)                       | :heavy_check_mark: | :heavy_check_mark: | [:whale:](https://hub.docker.com/r/senzing/senzing-base) | Dockerfile used in FROM statements.
| [senzing/senzing-debug](https://github.com/Senzing/docker-senzing-debug)                     | :no_entry_sign:    | :heavy_check_mark: | [:whale:](https://hub.docker.com/r/senzing/senzing-debug) | Dockerfile for debugging Senzing deployments.
| [senzing/senzing-poc-utility](https://github.com/Senzing/docker-senzing-poc-utility)         |                    |                    | [:whale:](https://hub.docker.com/r/senzing/senzing-poc-utility) | Dockerfile wrapping Senzing's POC utility.
| [senzing/stream-loader](https://github.com/Senzing/stream-loader)                            |                    |                    | [:whale:](https://hub.docker.com/r/senzing/stream-loader) | Dockerfile  wrapping `stream-loader.py`.
| [senzing/web-app-demo](https://github.com/Senzing/docker-web-app-demo)                       |                    |                    | [:whale:](https://hub.docker.com/r/senzing/web-app-demo) | Dockerfile wrapping "Entity Search Web App".
| [store/senzing/senzing-package](https://github.com/Senzing/senzing-package)                  |                    |                    | [:whale:](https://hub.docker.com/_/senzing-package) | Dockerfile wrapping `senzing-package.py`. Requires [accepting EULA](https://github.com/Senzing/knowledge-base/blob/master/HOWTO/accept-eula.md#storesenzingsenzing-package-docker-image).
