from tapioca_github import Github
from decouple import config
import misaka


class GithubWikiWrapper(object):
    token = config('GITHUB_TOKEN', None)
    organization = 'citi-ufpe'

    def __init__(self):
        super().__init__()
        self.client = self._init_github_client()
        import ipdb; ipdb.set_trace()

    def _init_github_client(self):
        return Github(access_token=self.token)

    def load_repo_data(self, repo=None):
        """ Import the homepage of a Wiki inside a repository """
        if not repo != None:
            raise RuntimeError('You must provide a repository!')
        response = self.client.repo_single(owner=self.organization, repo=repo).get()
        print('{repo} loaded successfully!').format(repo=response().data)
        return response().data

    def import_file_from_repo(self):
        """ Import `.github/WIKI_HOME.md` from the repository
