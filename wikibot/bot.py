import requests

import misaka
from wikibot.github_wrapper import GithubWikiWrapper


class Wikibot(GithubWikiWrapper):
    wiki_root = 'http://wiki.citi.org.br'
    api_root = wiki_root + '/api.php'
    session = requests.Session()

    def __init__(self, username=None, password=None, page=None):
        super().__init__()
        self.username = username
        self.password = password
        self.page = page
        self._log_in()

    @property
    def login_token(self):
        response = self.session.post(self.api_root, data={
            'format': 'json',
            'action': 'login',
            'lgname': self.username
        })
        response.raise_for_status()
        return response.json()['login']['token']

    @property
    def edit_token(self):
        response = self.session.get(self.api_root, params={
            'action': 'query',
            'meta': 'tokens',
            'format': 'json',
            'prop': 'info'
        })
        return response.json()['query']['tokens']['csrftoken']

    def _log_in(self):
        response = self.session.post(self.api_root, data={
            'format': 'json',
            'action': 'login',
            'lgname': self.username,
            'lgpassword': self.password,
            'lgtoken': self.login_token
        })
        if not response.json()['login']['result'] == 'Success':
            raise RuntimeError(response.json()['login']['reason'])
        print('Successfully logged in as {user}!'.format(user=self.username))
        return response

    def edit_page(self, content=None):
        """ Overwrite existing page with the content you provide (supports Wikicode and basic HTML) """
        if not content != None:
            raise RuntimeError('You have not specified a content!')
        warning = input('This will overwrite the page with your content, do you want to continue? [y/N]: ')
        if warning is not 'y':
            return print('Operation canceled by the user.')
        self.session.post(self.api_root, data={
            'action': 'edit',
            'title': self.page,
            'summary': 'Edited directly from citi-wikibot',
            'bot': True,
            'text': content,
            'token': self.edit_token
        })
        print(
            'Your page was succesfully edited! \n' +
            'Check it here: http://wiki.citi.org.br/index.php?title={page}'.format(page=self.page)
        )
        return

    def edit_page_from_file(self, file=None):
        """ Allows you to edit a page using a Markdown (.md) file """
        if file is None:
            raise RuntimeError('You have not specified a file!')

        file = open(file, 'r')
        if not file.name.endswith('.md'):
            raise RuntimeError('You have to pass a Markdown (.md) file!')
        warning = input('This will overwrite the page with your content, do you want to continue? [y/N]: ')
        if warning is not 'y':
            return print('Operation canceled by the user.')
        content = misaka.html(file.read())
        return self.edit_page(content)

    def edit_page_from_github(self, repo=None):
        """ Automatically gets your GitHub wiki homepage and edits on CITi's Wiki """
        content = self.import_file_from_repo(repo)
        print(
            'GitHub\'s wiki homepage from {repo} successfully loaded.'.format(repo=repo))
        self.edit_page(content)
        return
