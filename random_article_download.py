import os
import urllib
# articles import
from mnras import *
from aanda import *
from iop import *


def download_pdf(pdf_url, output_pdf=None):
    if output_pdf is None:
        output_pdf = pdf_url.split('/')[-1]
    try:
        urllib.urlretrieve(pdf_url, output_pdf)
    except:
        print 'Problem downloading file: '+str(pdf_url)


output_dir = '~/AAOD'

os.system('mkdir '+output_dir)
os.chdir(os.path.expanduser(output_dir))

# get MNRAS article
print 'Searching for a random MNRAS article'
pdf_mnras = MNRAS().get_random_article()
print ' downloading article: ' + pdf_mnras
download_pdf(pdf_mnras)

# get AANDA article
print 'Searching for a random AANDA article'
pdf_aanda = AANDA().get_random_article()
print ' downloading article: ' + pdf_aanda
download_pdf(pdf_aanda)

# get articles for different journals hosted by IOP SCIENCE
for j_str in ['PASP', 'ApJ', 'ApJL', 'ApJS']:
    print 'Searching for a random '+j_str+' article'
    pdf_iop = IOP_SCIENCE(journal=j_str).get_random_article()
    print ' downloading article: ' + pdf_iop
    output_name = '_'.join(pdf_iop.split('/')[-4:-1])+'.pdf'  # replace generic pdf name
    download_pdf(pdf_iop, output_pdf=output_name)
