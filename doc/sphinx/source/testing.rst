.. -*- Mode: rst -*-

.. _testing-page:

=========
 Testing
=========

..
   .. image:: /images/screenshot1.png
     :scale: 50%

Set the terminal environment using::

  source setenv.sh

Setup a *~/.ovh.conf* file, see https://github.com/ovh/python-ovh#configuration.

then run this command to get an API key::

  ovh-api/get-ovh-consumer-key

and launch the applet::

  bin/monitor-server

.. End
