.. -*- Mode: rst -*-

.. -*- Mode: rst -*-

..
   |monitor-serverUrl|
   |monitor-serverHomePage|_
   |monitor-serverDoc|_
   |monitor-server@github|_
   |monitor-server@readthedocs|_
   |monitor-server@readthedocs-badge|
   |monitor-server@pypi|_

.. |ohloh| image:: https://www.openhub.net/accounts/230426/widgets/account_tiny.gif
   :target: https://www.openhub.net/accounts/fabricesalvaire
   :alt: Fabrice Salvaire's Ohloh profile
   :height: 15px
   :width:  80px

.. |monitor-serverUrl| replace:: http://fabricesalvaire.github.io/monitor-server

.. |monitor-serverHomePage| replace:: monitor-server Home Page
.. _monitor-serverHomePage: http://fabricesalvaire.github.io/monitor-server

.. |monitor-serverDoc| replace:: monitor-server Documentation
.. _monitor-serverDoc: http://monitorserver.readthedocs.org/en/latest

.. |monitor-server@readthedocs-badge| image:: https://readthedocs.org/projects/monitorserver/badge/?version=latest
   :target: http://monitorserver.readthedocs.org/en/latest

.. |monitor-server@github| replace:: https://github.com/FabriceSalvaire/monitor-server
.. .. _monitor-server@github: https://github.com/FabriceSalvaire/monitor-server

.. |monitor-server@readthedocs| replace:: http://monitorserver.readthedocs.org
.. .. _monitor-server@readthedocs: http://monitorserver.readthedocs.org

.. |monitor-server@pypi| replace:: https://pypi.python.org/pypi/monitor-server
.. .. _monitor-server@pypi: https://pypi.python.org/pypi/monitor-server

.. |Build Status| image:: https://travis-ci.org/FabriceSalvaire/monitor-server.svg?branch=master
   :target: https://travis-ci.org/FabriceSalvaire/monitor-server
   :alt: monitor-server build status @travis-ci.org

.. End
.. -*- Mode: rst -*-

.. |Python| replace:: Python
.. _Python: http://python.org

.. |PyPI| replace:: PyPI
.. _PyPI: https://pypi.python.org/pypi

.. |Sphinx| replace:: Sphinx
.. _Sphinx: http://sphinx-doc.org

.. End

====================
 Monitor Server
====================

The official monitor-server Home Page is located at |monitor-serverUrl|

The latest documentation build from the git repository is available at readthedocs.org |monitor-server@readthedocs-badge|

Written by `Fabrice Salvaire <http://fabrice-salvaire.pagesperso-orange.fr>`_.

|Build Status|

-----

.. 
  .. image:: https://raw.github.com/FabriceSalvaire/monitor-server/master/doc/sphinx/source/images/screenshot1-scaled.png

.. -*- Mode: rst -*-


==============
 Introduction
==============

PyQt applet to monitor an OVH Virtual Private Server.

It would be nice to reimplement it using Qt5 QML.

The source code is licensed under GPL V3.

.. End

.. -*- Mode: rst -*-

.. _installation-page:


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

.. End
