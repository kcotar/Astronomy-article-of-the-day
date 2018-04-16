import urllib2
from bs4 import BeautifulSoup
from random import randint


class MNRAS():
    def __init__(self):
        self.root_url = 'https://academic.oup.com'
        self.issues_all_url = self.root_url + '/mnras/issue-archive'
        self.issue_url = self.root_url + '/mnras/issue'  # '/188/1'

    def _parse_list_of_years(self):
        page_years = urllib2.urlopen(self.issues_all_url)
        page_html = BeautifulSoup(page_years, 'html.parser')

        list_url_years = page_html.findAll('a')
        years_all = list([])
        for i_u in range(len(list_url_years)):
            url = list_url_years[i_u]
            try:
                if '/mnras/issue-archive/' in url.get('href'):
                    years_all.append(url.text).strip()
            except:
                pass
        return years_all

    def _get_random_year(self):
        years_all = self._parse_list_of_years()
        return years_all[randint(0, len(years_all)-1)]

    def _parse_list_of_volumes_and_issues(self, year):
        page_voliss = urllib2.urlopen(self.issues_all_url+'/'+str(year))
        page_html = BeautifulSoup(page_voliss, 'html.parser')

        list_url_vol = page_html.findAll('a')
        vol_iss = list([])
        for i_u in range(len(list_url_vol)):
            url = list_url_vol[i_u]
            try:
                if '/mnras/issue/' in url.get('href'):
                    if url.get('class') is None:
                        link_split = url.get('href').split('/')
                        vol_iss.append([link_split[-2], link_split[-1]])
            except:
                pass
        return vol_iss

    def _get_random_vol_issue(self, year):
        vol_iss_all = self._parse_list_of_volumes_and_issues(year)
        return vol_iss_all[randint(0, len(vol_iss_all)-1)]

    def get_random_from_issue(self, volume, issue):
        page_voliss = urllib2.urlopen(self.issue_url + '/' + str(volume) + '/' + str(issue))
        page_html = BeautifulSoup(page_voliss, 'html.parser')

        articles_url = page_html.findAll('a', attrs={'class':'viewArticleLink'})
        articles_all = list([])
        for i_u in range(len(articles_url)):
            url = articles_url[i_u]
            try:
                if '/mnras/article-abstract/' in url.get('href'):
                    articles_all.append(self.root_url + url.get('href'))
            except:
                pass

        random_article_url = articles_all[randint(0, len(articles_all)-1)]

        page_article = urllib2.urlopen(random_article_url)
        page_html = BeautifulSoup(page_article, 'html.parser')

        pdf_url = page_html.findAll('a', attrs={'class': 'al-link pdf article-pdfLink'})
        pdf_download = self.root_url + pdf_url[0].get('href')  # as more than one link exist on this page

        return pdf_download

    def get_random_article(self):
        y = self._get_random_year()
        v, i = self._get_random_vol_issue(y)
        return self.get_random_from_issue(v, i)


# ----------------------------
# --------- TESTS ------------
# ----------------------------
# d = MNRAS()
# y = d._get_random_year()
# print y
# v, i = d._get_random_vol_issue(y)
# print v, i
# d.get_random_from_issue(v, i)
# print d.get_random_article()
