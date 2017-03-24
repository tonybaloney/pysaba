sabat
===========

.. image:: https://img.shields.io/pypi/v/pysaba.svg
        :target: https://pypi.python.org/pypi/pysaba

.. image:: https://img.shields.io/travis/tonybaloney/pysaba.svg
        :target: https://travis-ci.org/tonybaloney/pysaba

.. image:: https://readthedocs.org/projects/pysaba/badge/?version=latest
        :target: https://readthedocs.org/projects/pysaba/?badge=latest
        :alt: Documentation Status


Saba client library for API management

* Free software: Apache-2 license
* Documentation: https://pysaba.readthedocs.org.

Features
--------

* Certificate authentication

Usage
-----

.. code-block:: python

    from saba.client import SabaClient
    from saba.auth.certificate import CertificateAuthentication
    
    host = 'mycompany-api.sabacloud.com'
    user = 'me'
    password = 'password'
    
    cert = CertificateAuthentication(host, user, password)
    
    client = SabaClient(host, cert)
    
    print(client.courses.all())
