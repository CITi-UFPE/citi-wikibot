import requests
from decouple import config

import misaka
from tapioca_github import Github


class GithubWikiWrapper(object):
    token = None
    organization = 'citi-ufpe'

    def __init__(self):
        self.repo = ''

    def _init_github_client(self):
        self.token = config('GITHUB_TOKEN', None)
        return Github(access_token=self.token)

    def _get_repo_data(self):
        self.client = self._init_github_client()
        """ Import the homepage of a Wiki inside a repository """
        if not self.repo:
            raise RuntimeError('You must provide a repository!')
        try:
            response = self.client.repo_single(owner=self.organization, repo=self.repo).get()
        except:
            raise RuntimeError('This repository is not accessible or doesn\'t exist!')
        print('Repository {repo} loaded successfully!'.format(
            repo=response().data['name']))
        return response().data

    @property
    def repo_has_wiki(self):
        data = self._get_repo_data()
        return data['has_wiki'] == True

    def import_file_from_repo(self, repo=None):
        self.client = self._init_github_client()
        """ Import homepage from Wiki from the repository you used on `load_repo_data()` """
        if not repo:
            raise RuntimeError('You must provide a repository!')
        self.repo = repo
        if not self.repo_has_wiki:
            raise RuntimeError('This repository doesn\'t have a Wiki!\n'
                               'Learn how to create one here: '
                               'https://help.github.com/articles/about-github-wikis/')
        url = 'https://raw.githubusercontent.com/wiki/{organization}/{repo}/Home.md'.format(
            organization=self.organization, repo=self.repo
        )
        headers = dict(
            Authorization='token {0}'.format(self.token),
            Accept='application/vnd.github.v3.raw'
        )
        response = requests.get(url, headers=headers)
        if response.status_code is not 200:
            raise RuntimeError('This repository is not accessible or doesn\'t exist!')
        return misaka.html(response.text)
