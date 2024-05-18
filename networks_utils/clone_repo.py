import subprocess
import requests
# import HTTPBasicAuth


def run_git_command(command):
    try:
        res = subprocess.run(command, capture_output=True, text=True, check=True)
        print(res.stdout)
    except subprocess.CalledProcessError as error:
        print(f'Error output is {error}')


run_git_command(['git', 'clone', 'https://github.com/MaxOn14/ticTacToeGame', 'clone_repo'])
run_git_command(['git', '-C',  'clone_repo', 'log', '--decorate', '--graph'])


# def get_commit_history(username, password, owner, repo_slug):
#     url = f'https://api.bitbucket.org/2.0/repositories/{owner}/{repo_slug}/commits'
#     auth = HTTPBasicAuth(username, password)
#     response = requests.get(url, auth=auth)
#
#     if response.status_code == 200:
#         commits = response.json()['values']
#         for commit in commits:
#             sha = commit['sha']
#             author = commit['author']['user']['display_name']
#             message = commit['message']
#             date = commit['date']
#             print(f'Commit {sha}\nAuthor: {author}, \nDate: {date}, \nMessage: {message}')
#     else:
#         print(f'Failed access, status code is {response.status_code}')
#         print(response.json())
#
#
# username = "username"
# password = 'password'
# owner = 'owner'
# repo_slug = 'repo_slug'
#
#
# get_commit_history(username, password, owner, repo_slug)

