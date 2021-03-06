.. _api:

Developer Interface
===================

.. module:: esser

This part of the documentation covers all the interfaces of `esser`.


Entities / Aggregates
-----------------------

.. autoclass:: esser.entities.Entity
    :members:
    :undoc-members:


Repositories
==================

Base Interface
------------------

.. automodule:: esser.repositories.base
    :members:
    :undoc-members:

DynamoDB
-----------------

.. automodule:: esser.repositories.dynamodb
    :members:
    :undoc-members:


Commands
-----------------------

.. autoclass:: esser.commands.BaseCommand
    :members:
    :undoc-members:

.. autoclass:: esser.commands.CreateCommand
    :members:
    :undoc-members:

.. autoclass:: esser.commands.DeleteCommand
    :members:
    :undoc-members:


Event Handlers
---------------------

.. autoclass:: esser.event_handler.BaseEventHandler
    :members:
    :undoc-members:



Exceptions
-----------------------

.. automodule:: esser.exceptions
    :members:
    :undoc-members: