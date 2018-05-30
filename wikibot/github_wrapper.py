import requests
from decouple import config

import misaka
from tapioca_github import Github


class GithubWikiWrapper(object):
    token = config('GITHUB_TOKEN', None)
    organization = 'citi-ufpe'

    def __init__(self, repo=None):
        self.client = self._init_github_client()

    def _init_github_client(self):
        return Github(access_token=self.token)

    def _get_repo_data(self):
        """ Import the homepage of a Wiki inside a repository """
        if not self.repo:
            raise RuntimeError('You must provide a repository!')
        response = self.client.repo_single(owner=self.organization, repo=self.repo).get()
        print('Repository {repo} loaded successfully!'.format(
            repo=response().data['name']))
        return response().data

    def import_file_from_repo(self, repo=None):
        """ Import homepage from Wiki from the repository you used on `load_repo_data()` """
        if not repo:
            raise RuntimeError('You must provide a repository!')
        url = 'https://raw.githubusercontent.com/wiki/{organization}/{repo}/Home.md'.format(
            organization=self.organization, repo=repo
        )
        headers = dict(
            Authorization='token {0}'.format(self.token),
            Accept='application/vnd.github.v3.raw'
        )
        response = requests.get(url, headers=headers)
        return misaka.html(response.text)
