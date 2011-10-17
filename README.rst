==========
 Codepadr
==========

codepadr is an interface to upload things to `codepad.org <http://codepad.org>`_.


Installation & Requirements
---------------------------

To install codepadr, simply::

    $ pip install codepadr

or, if you must::

    $ easy_install codepadr

codepadr requires:

* python 2.6+
* requests


Example usage
-------------

codepadr is quite flexible in how you pass it code to upload::

    $ codepad file.txt
    $ codepad < file.txt
    $ cat file.txt | codepad

You can specify that the paste should be private::

    $ echo "psst, this is private" | codepad -p

You can specify the language of the paste (defaults to plain text)::

    $ echo "print 'hello world'" | codepad -l py

If you pass in a file, the language will be inferred from the file extension::

    $ codepad script.rb

You can ask codepad the run the code::

    $ codepad script.py -r

And if you pass in `-`, it will read from stdin::

    $ codepad -l py -r -
    for i in xrange(25):
        print i**i
    ^D


Credits
-------

This project was inspired by Dalton Barreto's `codepad <https://github.com/daltonmatos/codepad>`_.
