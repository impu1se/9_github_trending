import requests
import time

url = 'https://api.github.com/search/repositories?q=created:>2017-06-10&sort=stars&order=desc'

def get_trending_repositories(top_size):
    top_repo = []
    for repo in top_size['items']:
        top_repo.append((repo['html_url'], repo['stargazers_count']))
    return top_repo        


def get_open_issues_amount(repo_owner, repo_name):
    pass


def main():
    r = requests.get(url)
    top = get_trending_repositories(r.json())
    print(top)


if __name__ == '__main__':
	main()
    
