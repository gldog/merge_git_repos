import unittest

from src import concurrent_git_merge as main


class Test01(unittest.TestCase):

    def test_1_repo_with_minimal_parts(self):
        default_source_branch = 'default-source-branch'
        default_dest_branch = 'default-dest-branch'

        repos_data_parameters = ['repo-a']
        repos_metadata = main.make_repos_metadata(repos_data_parameters, default_source_branch, default_dest_branch)
        expected = [
            {'repo_data_from_parameter': 'repo-a', 'repo_local_name': 'repo-a',
             'source_branch': default_source_branch, 'dest_branch': default_dest_branch}
        ]
        self.assertEquals(expected, repos_metadata)

        repos_data_parameters = ['repo-a:']
        repos_metadata = main.make_repos_metadata(repos_data_parameters, default_source_branch, default_dest_branch)
        expected = [
            {'repo_data_from_parameter': 'repo-a:', 'repo_local_name': 'repo-a',
             'source_branch': default_source_branch, 'dest_branch': default_dest_branch}
        ]
        self.assertEquals(expected, repos_metadata)

        repos_data_parameters = ['repo-a:::']
        repos_metadata = main.make_repos_metadata(repos_data_parameters, default_source_branch, default_dest_branch)
        expected = [
            {'repo_data_from_parameter': 'repo-a:::', 'repo_local_name': 'repo-a',
             'source_branch': default_source_branch, 'dest_branch': default_dest_branch}
        ]
        self.assertEquals(expected, repos_metadata)

        repos_data_parameters = ['repo-a:my-source-branch:']
        repos_metadata = main.make_repos_metadata(repos_data_parameters, default_source_branch, default_dest_branch)
        expected = [
            {'repo_data_from_parameter': 'repo-a:my-source-branch:', 'repo_local_name': 'repo-a',
             'source_branch': 'my-source-branch', 'dest_branch': default_dest_branch, }
        ]
        self.assertEquals(expected, repos_metadata)

        repos_data_parameters = ['repo-a::my-dest-branch']
        repos_metadata = main.make_repos_metadata(repos_data_parameters, default_source_branch, default_dest_branch)
        expected = [
            {'repo_data_from_parameter': 'repo-a::my-dest-branch', 'repo_local_name': 'repo-a',
             'source_branch': default_source_branch, 'dest_branch': 'my-dest-branch'}
        ]
        self.assertEquals(expected, repos_metadata)

        repos_data_parameters = ['repo-a:my-source-branch:my-dest-branch']
        repos_metadata = main.make_repos_metadata(repos_data_parameters, default_source_branch, default_dest_branch)
        expected = [
            {'repo_data_from_parameter': 'repo-a:my-source-branch:my-dest-branch', 'repo_local_name': 'repo-a',
             'source_branch': 'my-source-branch', 'dest_branch': 'my-dest-branch'}
        ]
        self.assertEquals(expected, repos_metadata)

    def test_5_repos_with_minimal_parts(self):
        default_source_branch = 'default-source-branch'
        default_dest_branch = 'default-dest-branch'

        repos = ['repo-a', 'repo-b::',
                 'repo-c:my-source-branch:', 'repo-d::my-dest-branch',
                 'repo-e:my-source-branch:my-dest-branch']
        repos_data = main.make_repos_metadata(repos, default_source_branch, default_dest_branch)
        expected = [
            {'repo_data_from_parameter': 'repo-a', 'repo_local_name': 'repo-a',
             'source_branch': default_source_branch, 'dest_branch': default_dest_branch},
            {'repo_data_from_parameter': 'repo-b::', 'repo_local_name': 'repo-b',
             'source_branch': default_source_branch, 'dest_branch': default_dest_branch},
            {'repo_data_from_parameter': 'repo-c:my-source-branch:', 'repo_local_name': 'repo-c',
             'source_branch': 'my-source-branch', 'dest_branch': default_dest_branch},
            {'repo_data_from_parameter': 'repo-d::my-dest-branch', 'repo_local_name': 'repo-d',
             'source_branch': default_source_branch, 'dest_branch': 'my-dest-branch'},
            {'repo_data_from_parameter': 'repo-e:my-source-branch:my-dest-branch', 'repo_local_name': 'repo-e',
             'source_branch': 'my-source-branch', 'dest_branch': 'my-dest-branch'}
        ]
        self.assertEquals(expected, repos_data)
