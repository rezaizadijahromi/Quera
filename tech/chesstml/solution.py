
from bs4 import BeautifulSoup as BS

def process(name):
    # r = requests.get(name)
    # f = codecs.open(name, 'r', 'utf-8')
    # soup = BS(f.read())
    soup = BS(open(name), "html.parser")
    counts = len(soup.find_all("a"))
    # print(counts)
    return counts

# process('htmlsampletest2.html')
# print(process('htmlsampletest2.html'))