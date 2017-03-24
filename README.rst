sabat
===========

.. image:: https://img.shields.io/pypi/v/sabat.svg
        :target: https://pypi.python.org/pypi/sabat

.. image:: https://img.shields.io/travis/tonybaloney/sabat.svg
        :target: https://travis-ci.org/tonybaloney/sabat

.. image:: https://readthedocs.org/projects/sabat/badge/?version=latest
        :target: https://readthedocs.org/projects/sabat/?badge=latest
        :alt: Documentation Status


Sabat client library for API management

* Free software: Apache-2 license
* Documentation: https://sabat.readthedocs.org.

Features
--------

* Invitation management using the license API
* User management using the license API
* Team information
* Invite URL generation

Usage
-----

.. code-block:: python

    from sabat.licensing import LicensingAPIClient

    client = LicensingAPIClient(plan, api_key)
    
    invites = client.invites.get_all_invites()
