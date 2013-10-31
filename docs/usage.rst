========
Usage
========

To use facehugger in a project::

	from facehugger import get_faces

	faces = get_faces('/some/path/to_image.jpg')


To use facehugger from command line:

.. code-block :: bash

    $ sudo pip install facehugger
    $ facehugger -i /path/to/image_with_faces.jpg -o /path/to/dir_to_save_faces


Rescaling resulting face crops
-------------------------------

.. versionadded:: 0.2.1
    Added `--rescale-face-crop` parameter that receives an integer representing percentage to scale up the crop

.. code-block:: bash

	$ facehugger -i /path/to/image_with_faces.jpg -o /path/to/dir_to_save_faces --rescale-face-crop 20
