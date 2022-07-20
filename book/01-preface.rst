Preface
===============================================================================
.. contents:: **目录**
   :local:



关于本书
---------------

本书写作时使用了 [Nicolas P. Rougier](https://www.labri.fr/perso/nrougier/) 制作的模板，特此致谢。

预备知识
+++++++++++++

This is not a Python beginner guide and you should have an intermediate level in
Python and ideally a beginner level in NumPy. If this is not the case, have
a look at the bibliography_ for a curated list of resources.


Conventions
+++++++++++

We will use usual naming conventions. If not stated explicitly, each script
should import NumPy, scipy and matplotlib as:

.. code-block:: python

   import numpy as np
   import scipy as sp
   import matplotlib.pyplot as plt


We'll use up-to-date versions (at the date of writing, i.e. January, 2017) of the
different packages:

=========== =========
Packages    Version
=========== =========
Python      3.6.0
----------- ---------
NumPy       1.12.0
----------- ---------
Scipy       0.18.1
----------- ---------
Matplotlib  2.0.0
=========== =========

How to contribute
+++++++++++++++++

If you want to contribute to this book, you can:

* Review chapters (please contact me)
* Report issues (https://github.com/rougier/from-python-to-numpy/issues)
* Suggest improvements (https://github.com/rougier/from-python-to-numpy/pulls)
* Correct English (https://github.com/rougier/from-python-to-numpy/issues)
* Design a better and more responsive html template for the book.
* Star the project (https://github.com/rougier/from-python-to-numpy)

Publishing
++++++++++

If you're an editor interested in publishing this book, you can `contact me
<mailto:Nicolas.Rougier@inria.fr>`_ if you agree to have this version and all
subsequent versions open access (i.e. online at `this address
<http://www.labri.fr/perso/nrougier/from-python-to-numpy>`_), you know how to
deal with `restructured text <http://docutils.sourceforge.net/rst.html>`_ (Word
is not an option), you provide a real added-value as well as supporting
services, and more importantly, you have a truly amazing latex book template
(and be warned that I'm a bit picky about typography & design: `Edward Tufte
<https://www.edwardtufte.com/tufte/>`_ is my hero). Still here?


License
--------

**Book**

This work is licensed under a `Creative Commons Attribution-Non Commercial-Share
Alike 4.0 International License <https://creativecommons.org/licenses/by-nc-sa/4.0/>`_. You are free to:

* **Share** — copy and redistribute the material in any medium or format
* **Adapt** — remix, transform, and build upon the material

The licensor cannot revoke these freedoms as long as you follow the license terms.

**Code**

The code is licensed under the `OSI-approved BSD 2-Clause License
<LICENSE-code.txt>`_.


.. --- Links ------------------------------------------------------------------
.. _Nicolas P. Rougier:     http://www.labri.fr/perso/nrougier/
.. _Inria:                  http://www.inria.fr/en
.. _Mnemosyne:              http://www.inria.fr/en/teams/mnemosyne
.. _LaBRI:                  https://www.labri.fr/
.. _CNRS:                   http://www.cnrs.fr/index.php
.. _University of Bordeaux: http://www.u-bordeaux.com/
.. _Institute of Neurodegenerative Diseases:
      http://www.imn-bordeaux.org/en/
.. _Ten Simple Rules for Better Figures:
      http://dx.doi.org/10.1371/journal.pcbi.1003833
.. ----------------------------------------------------------------------------
