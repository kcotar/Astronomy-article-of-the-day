import os
import urllib
# articles import
from mnras import *
from aanda import *


def download_pdf(pdf_url):
    urllib.urlretrieve(pdf_url, pdf_url.split('/')[-1])


output_dir = '~/AAOD'

os.system('mkdir '+output_dir)
os.chdir(os.path.expanduser(output_dir))

# get MNRAS article
print 'Searching for a random MNRAS journal'
pdf_mnras = MNRAS().get_random_article()
print ' downloading article: ' + pdf_mnras
download_pdf(pdf_mnras)

# get AANDA article
print 'Searching for a random AANDA journal'
pdf_aanda = AANDA().get_random_article()
print ' downloading article: ' + pdf_aanda
download_pdf(pdf_aanda)