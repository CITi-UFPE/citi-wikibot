import requests
import misaka

class Wikibot(object):
    api_root = 'http://wiki.citi.org.br/api.php'
    session = requests.Session()

    def __init__(self, username=None, password=None, page=None):
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
        return response

    def edit_page(self, content=None):
        if not content != None:
            raise RuntimeError('You have not specified a content!')
        response = self.session.post(self.api_root, data={
            'action': 'edit',
            'title': self.page,
            'summary': 'Editing directly from CTWB',
            'bot': True,
            'text': content,
            'token': self.edit_token
        })

    def edit_page_from_file(self, file=None):
        """ Allows you to edit a page using a Markdown (.md) file """
        if not file != None:
            raise RuntimeError('You have not specified a file!')

        file = open(file, 'r')
        if not file.name.endswith('.md'):
            raise RuntimeError('You have to pass a Markdown (.md) file!')

        content = misaka.html(file.read())
        return self.edit_page(content)
