import os
import urllib
# articles import
from mnras import *

output_dir = '~/AAOD'

os.system('mkdir '+output_dir)
os.chdir(os.path.expanduser(output_dir))

# get MNRAS article
print 'Searching for a random MNRAS journal'
pdf_mnras = MNRAS().get_random_article()
print ' downloading article: ' + pdf_mnras
urllib.urlretrieve(pdf_mnras, pdf_mnras.split('/')[-1])