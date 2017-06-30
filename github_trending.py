import requests
import sys
import datetime


last_week = datetime.datetime.now() - datetime.timedelta(7)
url = 'https://api.github.com/search/repositories?' + \
      'q=created:>2017-0{}-{}&sort=stars&order=desc'.format(last_week.month,
                                                           last_week.day)


def check_connect(url):
    r = requests.get(url)
    if r.status_code == 200:
        return r
    else:
        return sys.exit('You have the problem to connect...')


def get_trending_repositories(top_size):
    top_repo = []
    for repo in top_size['items']:
        top_repo.append((repo['html_url'], repo['open_issues_count']))
    return top_repo[:20]


def printing_result(top_repo):
    for repo in top_repo:
        print('Url: {0} \t Open issues: {1}'.format(repo[0], repo[1]))


def main():
    response = check_connect(url)
    top = get_trending_repositories(response.json())
    printing_result(top)


if __name__ == '__main__':
    main()
