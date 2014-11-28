.. -*- Mode: rst -*-

.. -*- Mode: rst -*-

..
   |MonitorServerUrl|
   |MonitorServerHomePage|_
   |MonitorServerDoc|_
   |MonitorServer@github|_
   |MonitorServer@readthedocs|_
   |MonitorServer@readthedocs-badge|
   |MonitorServer@pypi|_

.. |ohloh| image:: https://www.openhub.net/accounts/230426/widgets/account_tiny.gif
   :target: https://www.openhub.net/accounts/fabricesalvaire
   :alt: Fabrice Salvaire's Ohloh profile
   :height: 15px
   :width:  80px

.. |MonitorServerUrl| replace:: http://fabricesalvaire.github.io/MonitorServer

.. |MonitorServerHomePage| replace:: MonitorServer Home Page
.. _MonitorServerHomePage: http://fabricesalvaire.github.io/MonitorServer

.. |MonitorServerDoc| replace:: MonitorServer Documentation
.. _MonitorServerDoc: http://monitorserver.readthedocs.org/en/latest

.. |MonitorServer@readthedocs-badge| image:: https://readthedocs.org/projects/monitorserver/badge/?version=latest
   :target: http://monitorserver.readthedocs.org/en/latest

.. |MonitorServer@github| replace:: https://github.com/FabriceSalvaire/MonitorServer
.. .. _MonitorServer@github: https://github.com/FabriceSalvaire/MonitorServer

.. |MonitorServer@readthedocs| replace:: http://monitorserver.readthedocs.org
.. .. _MonitorServer@readthedocs: http://monitorserver.readthedocs.org

.. |MonitorServer@pypi| replace:: https://pypi.python.org/pypi/MonitorServer
.. .. _MonitorServer@pypi: https://pypi.python.org/pypi/MonitorServer

.. |Build Status| image:: https://travis-ci.org/FabriceSalvaire/MonitorServer.svg?branch=master
   :target: https://travis-ci.org/FabriceSalvaire/MonitorServer
   :alt: MonitorServer build status @travis-ci.org

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
 MonitorServer
====================

The official MonitorServer Home Page is located at |MonitorServerUrl|

The latest documentation build from the git repository is available at readthedocs.org |MonitorServer@readthedocs-badge|

Written by `Fabrice Salvaire <http://fabrice-salvaire.pagesperso-orange.fr>`_.

|Build Status|

-----

.. image:: https://raw.github.com/FabriceSalvaire/MonitorServer/master/doc/sphinx/source/images/screenshot1-scaled.png
.. image:: https://raw.github.com/FabriceSalvaire/MonitorServer/master/doc/sphinx/source/images/screenshot2-scaled.png

.. -*- Mode: rst -*-


==============
 Introduction
==============

MonitorServer is a Python module that provides ...

The source code is licensed under GPL V3.

.. End

.. -*- Mode: rst -*-

.. _installation-page:


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

.. End
