
CITi's Wikibot
==============


.. image:: https://codecov.io/gh/CITi-UFPE/citi-wikibot/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/CITi-UFPE/citi-wikibot
   :alt: codecov
 
.. image:: https://circleci.com/gh/CITi-UFPE/citi-wikibot.svg?style=svg
   :target: https://circleci.com/gh/CITi-UFPE/citi-wikibot
   :alt: CircleCI
 
.. image:: https://badge.fury.io/py/citi-wikibot.svg
   :target: https://badge.fury.io/py/citi-wikibot
   :alt: PyPI version


Python script to easily edit pages on `CITi's Wiki <http://wiki.citi.org.br/>`_ directly from shell or using a Markdown (.md) file. Currently, our Wiki is made using `MediaWiki <https://www.mediawiki.org/>`_.

Installation
------------

.. code-block:: shell

   $ pip install citi-wikibot

Usage
-----

Note: Keep in mind that every command will overwrite the current page content with the one you provide.

Quickstart
^^^^^^^^^^


#. Just initialize your Wikibot
#. Use one of the commands, it's that simple :sparkles: 

Editing a page directly from the shell
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: shell

   $ python
   >>> from wikibot import Wikibot
   >>> bot = Wikibot('username', 'password', 'page_title')
   >>> bot.edit_page('== My title ==\nHello world!')

Editing a page from a Markdown file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..

   Important: It's recommended that you run the script in the folder your file is located


.. code-block:: shell

   $ ls
   notes.md
   $ python
   >>> from wikibot import Wikibot
   >>> bot = Wikibot('username', 'password', 'page_title')
   >>> bot.edit_page_from_file('notes.md')

Gets the Homepage from GitHub wiki of your repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Automatically gets your GitHub wiki homepage (\ `example <https://github.com/citi-ufpe/in-forma/wiki>`_\ ), parses it and edits the page on CITi Wiki (\ `result <http://wiki.citi.org.br/index.php?title=In_Forma>`_\ ).

You must declare your `personal access token from GitHub <https://github.com/settings/tokens>`_ in a variable called ``GITHUB_TOKEN`` in order to use this command.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

   $ GITHUB_TOKEN="mypersonalaccesstoken123"
   $ python
   >>> from wikibot import Wikibot
   >>> bot = Wikibot('username', 'password', 'page_title')
   >>> bot.edit_page_from_github('my_repository')
   GitHub's wiki homepage from my_repository successfully loaded and edited!
   Check it here: http://wiki.citi.org.br/index.php?title=insert_page

Reference
---------

``edit_page(content)``
^^^^^^^^^^^^^^^^^^^^^^^^^^


* 
  ``content`` (string): The content you want to put in the page. Note that it will overwrite the current one! **It accepts Wikicode (Wikipedia and MediaWiki format).**

    Example:

  .. code-block:: python

       from wikibot import Wikibot

       bot = Wikibot('myusername', '123', 'My_Page')
       bot.edit_page('*Hello* world!')

``edit_page_from_file(file)``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


* 
  ``file`` (string): The file name you want to load. It must be in Markdown format!

    Example:

  .. code-block:: python

       from wikibot import Wikibot

       bot = Wikibot('myusername', '123', 'My_Page')
       bot.edit_page_from_file('notes.md')

``edit_page_from_github(repo)``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


* 
  ``repo`` (string): The name of your repository. It needs to have a Wiki. The script will automatically search in **citi-ufpe's organization**.

  ..

     Remember to declare your ``GITHUB_TOKEN`` environment variable! Instructions above in **Usage**.


    Example:

  .. code-block:: python

       from wikibot import Wikibot

       bot = Wikibot('myusername', '123', 'My_Page')
       bot.edit_page_from_github('my-repo')
