import requests
import datetime
from time import sleep


def check_connect(url, payload):
    try:
        response = requests.get(url, params=payload)
        timeout = 0.5
        sleep(timeout)
    except requests.exceptions.ConnectionError:
        return None
    if response.status_code == 200:
        return response
    else:
        return None


def get_trending_repositories(data_stream):
    top_repo = []
    for repo in data_stream:
        top_repo.append((repo['html_url'], repo['open_issues_count']))
    return top_repo


def printing_result(top_repo):
    for repo in top_repo:
        print('Url: {0} \t Open issues: {1}'.format(repo[0], repo[1]))


def main():
    weeks = 1
    width = 2
    req_date = datetime.datetime.now() - datetime.timedelta(weeks=weeks)
    payload = {'q': 'created:>2017-' + str(req_date.month).zfill(width) + 
               '-' + str(req_date.day), 
               'sort': 'stars',
               'order': 'desc',
               'page': '1',
               'per_page': '20'}
    url = 'https://api.github.com/search/repositories'
    response = check_connect(url, payload)
    if response:
        top_repo = get_trending_repositories(response.json()['items'])
        printing_result(top_repo)
    else:
        print('You have the problem to connect...')


if __name__ == '__main__':
    main()
