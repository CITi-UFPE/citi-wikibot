# CITi's Wikibot
[![codecov](https://codecov.io/gh/CITi-UFPE/citi-wikibot/branch/master/graph/badge.svg)](https://codecov.io/gh/CITi-UFPE/citi-wikibot) [![CircleCI](https://circleci.com/gh/CITi-UFPE/citi-wikibot.svg?style=svg)](https://circleci.com/gh/CITi-UFPE/citi-wikibot)

Python script to easily edit pages on [CITi's Wiki](http://wiki.citi.org.br/) directly from shell or using a Markdown (.md) file. Currently, our Wiki is made using [MediaWiki](https://www.mediawiki.org/).

## Installation
```shell
$ pip install citi-wikibot
```

## Usage
Note: Keep in mind that every command will overwrite the current page content with the one you provide.

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