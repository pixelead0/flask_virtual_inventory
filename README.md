# Python Flask Test

This project implements an inventory system using flask-restful

# Entities
```
Product
   - sku
   - name
   - description
   - (timestamp_mixin)

Store
   - name
   - description
   - (address_mixin)
   - (timestamp_mixin)

Inventory
   - product_id
   - store_id
   - qty

```
Two mixins were created
    `TimestampMixin` fields to know if a record is active and when it was created or modified
    `AddressMixin` fields for use in other tables e.g. for deliveries


1. Crear una API Rest con Flask que implemente un sistema de inventario de productos con estas características ​ mínimas​:

   a. Una entidad ​ Tienda ​ que almacene la información básica asociada a la misma (ie. nombre, irección, etc.)

   b. Una entidad ​ Producto ​ que almacene la información básica asociada a la misma (ie. SKU, etc.)

   c. Poder agregar/asociar inventario a una tienda

   d. Poder determinar si hay suficiente stock de un producto en la tienda

   e. Interactuar con el sistema de inventario de forma asíncrona

   f. ​ NO ​ usar frameworks (ie. Django, etc.), con la excepción de Flask/Flask-RestPlus/etc. y Psycopg2/etc. (capas de presentación y base de datos), lo demás debe ser lo mas “​vanilla” posible

2. Hacer uso de una BD Postgres

3. Improvisar cualquier información que no haya sido suministrada o que se considere complementaria lo requerido, indicando la razón de dicha decisión.

## Requirements:

- [Docker](https://docs.docker.com/engine/installation/).
- [Docker-compose](https://docs.docker.com/compose/install).

## Technologies

- `Python 3.8`
- `Flask 1.1.2 `
- `Docker`
- `Redis`
- `PostgreSQL 11`


## COLLABORATIVE WORKFLOW

1. Before beginning any work, always pull latest version of `dev`
   branch.
2. Create a new branch from `master`. There are two formats for branch names:
   1. `github_username/description_of_feature/trello_id`
      Use this format when an associated Trello ticket exists for this
      particular feature that you are working on.
   2. `github_username/description_of_feature`
      Use this format where there is not an associated Trello ticket
      for the particular feature that you are working on.
      Some example branch names:
   - `pixelead0/changes-button-colors`
   - `pixelead0/fixes-login-error/xeuoiu37893`
3. Do your work in the new feature branch that you made.
4. When the branch is ready, rebase all your changes into one commit.
   - Make sure commit has a descriptive title in all title case.
     For example:
     `Changes Button Colors`
   - Add the bottom of each commit message, if there is a trello ticket,
     post the ticket url like this:
     `Reference: https://trello.com/blah/blah/113873`
5. Push your branch up to Github
6. Make a new Pull Request from your feature branch to the `master` branch.
   Never push directly into the `master` branch.
   1. In the PR, add `pixelead0` as a reviewer
7. Notify `pixelead0` that PR is ready for review.

## INITIAL IDE SETUP

You will probably need to build some files for your IDE.  These
will only be accessed by the IDE.  These are not used by the actual app server.  The app server uses the files which are inside the docker container.

On your host machine, setup python environment:

```shell
# FROM HOST
rm -fr ./venv
virtualenv -p python3.8 ./venv
./venv/bin/pip3 install -r ./api/requirements.txt
```

## Install:

**Clone the repository**

```shell
git clone git@github.com:pixelead0/project.git
```

**Copy the configuration files.**

```shell
sh config-init.sh
```

**Run docker-compose to start the containers:**

```shell
docker-compose up
```

**Reset own files user**

```shell
sudo chown -R $USER
```

---
# Docker commands

## Delete all containers
```
docker-compose rm -fsa
```

## Containers init
```
docker-compose up
```

## Restart only python container
```
docker-compose restart api
```


# References

Flask Tuturial:
https://realpython.com/python-web-applications-with-flask-part-i/
https://realpython.com/python-web-applications-with-flask-part-ii/
https://realpython.com/python-web-applications-with-flask-part-iii/

Functional structure:
http://exploreflask.com/en/latest/blueprints.html#functional-structure

How to structure a Flask-RESTPlus web service for production builds
https://www.freecodecamp.org/news/structuring-a-flask-restplus-web-service-for-production-builds-c2ec676de563/

Flask restful example:
https://github.com/kuankitng/flask-restful-api
