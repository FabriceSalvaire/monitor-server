.. -*- Mode: rst -*-

.. _installation-page:

.. include:: project-links.txt
.. include:: abbreviation.txt

==============
 Installation
==============

Dependencies
------------

monitor-server requires the following dependencies:

 * Python 2.7
 * PyQt 4.9
 * `acpi_call <https://github.com/mkottman/acpi_call>`_

Installation from PyPi Repository
---------------------------------

monitor-server is made available on the |Pypi|_ repository at |monitor-server@pypi|

Run this command to install the last release:

.. code-block:: sh

  pip install monitor-server

Installation from Source
------------------------

The monitor-server source code is hosted at |monitor-server@github|

To clone the Git repository, run this command in a terminal:

.. code-block:: sh

  git clone git@github.com:FabriceSalvaire/monitor-server.git

Then to build and install monitor-server run these commands:

.. code-block:: sh

  python setup.py build
  python setup.py install

.. End
