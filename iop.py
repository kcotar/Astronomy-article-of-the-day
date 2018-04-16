import urllib2
from bs4 import BeautifulSoup
from random import randint


class IOP_SCIENCE():
    def __init__(self, journal='PASP'):

        if journal is 'PASP':
            self.j_id = '1538-3873'
        elif journal is 'ApJ':
            self.j_id = '0004-637X'
        elif journal is 'ApJL':
            self.j_id = '2041-8205'
        elif journal is 'AJ':
            self.j_id = '1538-3881'
        elif journal is 'ApJS':
            self.j_id = '0067-0049'

        self.root_url = 'http://iopscience.iop.org'
        self.issues_all_url = self.root_url + '/journal/' + self.j_id
        self.volume_url = self.root_url + '/volume/' + self.j_id
        self.issue_url = self.root_url + '/issue/' + self.j_id

    def _parse_list_of_volumes(self):
        page_years = urllib2.urlopen(self.issues_all_url)
        page_html = BeautifulSoup(page_years, 'html.parser')

        list_url_years = page_html.findAll('option')
        years_all = list([])
        for i_u in range(len(list_url_years)):
            url = list_url_years[i_u]
            try:
                if '/volume/' in url.get('value') and 'Vol' in url.text and self.j_id in url.get('value'):  # j_id was observed to change between volumes
                    vol = url.get('value').split('/')[-1]
                    years_all.append(vol)
            except:
                pass
        return years_all

    def _get_random_volume(self):
        years_all = self._parse_list_of_volumes()
        return years_all[randint(0, len(years_all)-1)]

    def _parse_list_of_issues(self, volume):
        print self.volume_url+'/'+str(volume)
        page_voliss = urllib2.urlopen(self.volume_url+'/'+str(volume))
        page_html = BeautifulSoup(page_voliss, 'html.parser')

        list_url_vol = page_html.findAll('a')
        vol_iss = list([])
        for i_u in range(len(list_url_vol)):
            url = list_url_vol[i_u]
            try:
                if '/issue/' in url.get('href'):
                    if url.get('class') is None:
                        link_split = url.get('href').split('/')
                        vol_iss.append(link_split[-1])
            except:
                pass
        return vol_iss

    def _get_random_issue(self, volume):
        vol_iss_all = self._parse_list_of_issues(volume)
        return vol_iss_all[randint(0, len(vol_iss_all)-1)]

    def get_random_from_issue(self, volume, issue):
        page_voliss = urllib2.urlopen(self.issue_url + '/' + str(volume) + '/' + str(issue))
        page_html = BeautifulSoup(page_voliss, 'html.parser')

        articles_url = page_html.findAll('a')
        articles_all = list([])
        for i_u in range(len(articles_url)):
            url = articles_url[i_u]
            try:
                if '/article/' in url.get('href') and '/pdf' in url.get('href'):
                    articles_all.append(self.root_url + url.get('href'))
            except:
                pass

        pdf_download = articles_all[randint(0, len(articles_all)-1)]

        # page_article = urllib2.urlopen(random_article_url)
        # page_html = BeautifulSoup(page_article, 'html.parser')
        #
        # pdf_url = page_html.findAll('a', attrs={'class': 'al-link pdf article-pdfLink'})
        # pdf_download = self.root_url + pdf_url[0].get('href')  # as more than one link exist on this page

        return pdf_download

    def get_random_article(self):
        v = self._get_random_volume()
        i = self._get_random_issue(v)
        return self.get_random_from_issue(v, i)


# ----------------------------
# --------- TESTS ------------
# ----------------------------
# d = IOP_SCIENCE(journal='PASP')
# v = d._get_random_volume()
# print v
# i = d._get_random_issue(v)
# print v, i
# pdf = d.get_random_from_issue(v, i)
# print pdf
# print d.get_random_article()
