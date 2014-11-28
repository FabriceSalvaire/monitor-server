.. -*- Mode: rst -*-

.. _installation-page:

.. include:: project-links.txt
.. include:: abbreviation.txt

==============
 Installation
==============

Dependencies
------------

MonitorServer requires the following dependencies:

 * Python 2.7
 * PyQt 4.9
 * `acpi_call <https://github.com/mkottman/acpi_call>`_

Installation from PyPi Repository
---------------------------------

MonitorServer is made available on the |Pypi|_ repository at |MonitorServer@pypi|

Run this command to install the last release:

.. code-block:: sh

  pip install MonitorServer

Installation from Source
------------------------

The MonitorServer source code is hosted at |MonitorServer@github|

To clone the Git repository, run this command in a terminal:

.. code-block:: sh

  git clone git@github.com:FabriceSalvaire/MonitorServer.git

Then to build and install MonitorServer run these commands:

.. code-block:: sh

  python setup.py build
  python setup.py install

.. End
