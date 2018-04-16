import urllib2
from bs4 import BeautifulSoup
from random import randint


class AANDA():
    def __init__(self):
        self.root_url = 'https://www.aanda.org'
        self.issues_all_url = self.root_url + '/component/issues/'
        self.issue_url = self.root_url + '/articles/aa/abs/'

    def _parse_list_of_issues(self):
        page_years = urllib2.urlopen(self.issues_all_url)
        page_html = BeautifulSoup(page_years, 'html.parser')

        list_url_years = page_html.findAll('a')
        issues_all = list([])
        for i_u in range(len(list_url_years)):
            url = list_url_years[i_u]
            try:
                if '/articles/aa/abs/' in url.get('href'):
                    link_split = url.get('href').split('/')
                    issues_all.append([link_split[-4], link_split[-3]])
            except:
                pass
        return issues_all

    def _get_random_issue(self):
        issues_all = self._parse_list_of_issues()
        return issues_all[randint(0, len(issues_all)-1)]

    def get_random_from_issue(self, year, vol):
        page_voliss = urllib2.urlopen(self.issue_url + '/' + str(year) + '/' + str(vol) + '/contents/contents.html')
        page_html = BeautifulSoup(page_voliss, 'html.parser')

        articles_url = page_html.findAll('a')
        articles_all = list([])
        for i_u in range(len(articles_url)):
            url = articles_url[i_u]
            try:
                if '/articles/aa/pdf/' in url.get('href'):
                    articles_all.append(self.root_url + url.get('href'))
            except:
                pass

        pdf_download = articles_all[randint(0, len(articles_all)-1)]
        return pdf_download

    def get_random_article(self):
        y, v = self._get_random_issue()
        return self.get_random_from_issue(y, v)


# ----------------------------
# --------- TESTS ------------
# ----------------------------
# d = AANDA()
# y, v = d._get_random_issue()
# print y, v
# pdf = d.get_random_from_issue(y, v)
# print pdf
# print d.get_random_article()