===============================
facehugger
===============================

.. image:: https://badge.fury.io/py/facehugger.png
    :target: http://badge.fury.io/py/facehugger
    
.. image:: https://travis-ci.org/dnmellen/facehugger.png?branch=master
        :target: https://travis-ci.org/dnmellen/facehugger

.. image:: https://pypip.in/d/facehugger/badge.png
        :target: https://crate.io/packages/facehugger?version=latest


Extracts faces from an image

* Free software: BSD license
* Documentation: http://facehugger.rtfd.org.

Requirements
------------

* SimpleCV


Features
--------

* Extracts faces and saves the cropped images to a folder
* You can use it in your app as a library


Quickstart
----------

.. code-block :: bash

    $ sudo pip install facehugger
    $ facehugger -i /path/to/image_with_faces.jpg -o /path/to/dir_to_save_faces
