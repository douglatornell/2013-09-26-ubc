---
layout: lesson
root: ../..
title: Python? What? Why? How?
---

##Why Python?

*Short answer:* because we need *some* programming language

The concepts of computational thinking and fundamental computational skills that we're teaching here are applicable in most programming languages,
but trying to talk about them in the abstract is hard and inefficient.
So, we'll teach you some Python, but you should be able to use the underlying concepts in R, Matlab, Ruby, or even Fortran.


##The Flavour of Python

[http://python.org/](http://python.org/)

* Created in 1989 by Guido van Rossum, the BDFL
* Clear, readable syntax
* General purpose language
* Well documented, free, and cross-platform
* Expressive
* Dynamic execution
* Very high level, dynamic data types
* Extensive standard libarary, and ecosystem of third-party packages
* Easily extended in C and C++


##Python for Science

[http://www.scipy.org/](http://www.scipy.org/)

Somewhere along the line,
10 or more years ago,
scientists and engineers embraced Python and started creating powerful tools and libraries for it:

* [NumPy][numpy]: N-dimensional arrays
* [SciPy][scipy]: Library of fundamental scientific alogorithms (in many cases just Python wrappers around time-tested implementations in Fortran, C, ...)
* [Matplotlib][matplotlib]: 2D plotting
* The list goes on...

[numpy]: http://numpy.scipy.org/
[scipy]: http://www.scipy.org/scipylib/index.html
[matplotlib]: http://matplotlib.org/

Choosing scientific packages and getting them compiled and installed can be difficult and time-consuming,
and it's not science.
So,
we've recommended [Anaconda][anaconda],
a curated distribution from [Continuum Analytics][continuum].
Another such distribution is [Canopy][canopy] from [Enthough][enthought].

[anaconda]: https://store.continuum.io/cshop/anaconda/
[continuum]: http://continuum.io/
[canopy]: https://www.enthought.com/products/canopy/
[enthought]: https://www.enthought.com/

##How to Run Python

###Python Shell

```
$ python
Python 2.7.5 |Anaconda 1.6.1 (x86_64)| (default, Jun 28 2013, 22:20:13)
[GCC 4.0.1 (Apple Inc. build 5493)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print 'hello, world!'
hello, world!
>>>
```
Use `ctrl-d` to exit.


###From the Command Line

```
$ cat > hello.py
print 'hello, world!'
ctrl-d

$ python hello.py
hello, world!
```

###IPython Shell

```
$ ipython
Python 2.7.5 |Anaconda 1.6.1 (x86_64)| (default, Jun 28 2013, 22:20:13)
Type "copyright", "credits" or "license" for more information.

IPython 1.0.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: print 'hello, world!'
hello, world!

In [2]: run hello.py
hello, world!

In [3]:
```
Use `exit` to return to the command line.

###IPython Notebook

```
$ ipython notebook
```

That should print a bunch of messages in your terminal window that include telling you that:

```
The IPython Notebook is running at: http://127.0.0.1:8888/
```

and

```
Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
```

It should also cause a tab to open in your browser with the URL [http://127.0.0.1:8888/#notebooks](http://127.0.0.1:8888/#notebooks) loaded.

***This is where the awesome starts!***


[Back to Python Intro](index.html)
