import requests
import sys
import datetime


last_week = datetime.datetime.now() - datetime.timedelta(7)
current_month = str(last_week.month).zfill(2)
current_day = last_week.day
url = 'https://api.github.com/search/repositories?' + \
      'q=created:>2017-{}-{}&sort=stars&order=desc'.format(current_month,
                                                           current_day)


def check_connect(url):
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        return None
    if response.status_code == 200:
        return response
    else:
        return None


def get_trending_repositories(data_stream):
    top_repo = []
    for repo in data_stream['items']:
        top_repo.append((repo['html_url'], repo['open_issues_count']))
    return top_repo[:20]


def printing_result(top_repo):
    for repo in top_repo:
        print('Url: {0} \t Open issues: {1}'.format(repo[0], repo[1]))


def main():
    response = check_connect(url)
    if response:
        top_repo = get_trending_repositories(response.json())
        printing_result(top_repo)
    else:
        print('You have the problem to connect...')


if __name__ == '__main__':
    main()
