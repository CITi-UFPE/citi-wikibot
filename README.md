# CITi's Wikibot
Easily edit pages on [CITi's Wiki](http://wiki.citi.org.br/) directly from shell or using a Markdown (.md) file.

## Installation
```shell
$ pip install citi-wikibot
```

## Usage
### Editing a page directly from the shell
```shell
$ python
>>> from wikibot.bot import Wikibot
>>> bot = Wikibot(username='insert_username', password='insert_password', page='insert_page')
>>> bot.edit_page('== My title ==\nHello world!')
```
### Editing a page from a Markdown file
> Important: It's recommended that you run the script in the folder your file is located
```shell
$ ls
notes.md
$ python
>>> from wikibot.bot import Wikibot
>>> bot = Wikibot(username='insert_username', password='insert_password', page='insert_page')
>>> bot.edit_page_from_file('notes.md')
```