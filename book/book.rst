.. ----------------------------------------------------------------------------
.. Title:   "从 Python 到 Taichi"
.. Author:  neozhaoliang@github.com
.. Date:    July 2022
.. License: Creative Commons Share-Alike Non-Commercial International 4.0
.. ----------------------------------------------------------------------------

.. meta::
   :description: An introductory book about taichi programming language
   :viewport: width=device-width, initial-scale=1, maximum-scale=1

.. |date| date::  %B %Y

===============================================================================
                             从 Python 到 Taichi
===============================================================================
-------------------------------------------------------------------------------
       Copyright (c) 2022 - Zhao Liang <liangzhao@taichi.graphics>
-------------------------------------------------------------------------------

.. default-role:: code

.. container:: title-logos

   |
   | Latest version - |date|

.. ----------------------------------------------------------------------------
.. container:: title-logos

   .. image:: data/cubes.png
      :width: 100%

.. ----------------------------------------------------------------------------

There are already a fair number of books about Numpy (see Bibliography_) and a
legitimate question is to wonder if another book is really necessary. As you
may have guessed by reading these lines, my personal answer is yes, mostly
because I think there is room for a different approach concentrating on the
migration from Python to Numpy through vectorization. There are a lot of
techniques that you don't find in books and such techniques are mostly learned
through experience. The goal of this book is to explain some of these
techniques and to provide an opportunity for making this experience in the
process.

**Website:** http://www.labri.fr/perso/nrougier/from-python-to-numpy


.. ----------------------------------------------------------------------------
.. contents:: **目录**
   :class: main-content
   :depth: 2


.. ----------------------------------------------------------------------------

.. ----------------------------------------------------------------------------
.. include:: 01-preface.rst
.. include:: 02-introduction.rst
.. include:: 03-anatomy.rst
.. include:: 04-code-vectorization.rst
.. include:: 05-problem-vectorization.rst
.. include:: 06-custom-vectorization.rst
.. include:: 07-beyond-numpy.rst
.. include:: 08-conclusion.rst
.. include:: 09-quick-reference.rst
.. include:: 10-bibliography.rst


.. --- Compilation ------------------------------------------------------------
.. rst2html.py --link-stylesheet --stylesheet=markdown.css book.rst book.html
