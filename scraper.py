from bs4 import BeautifulSoup
import urllib 

url = urllib.urlopen('https://ses.ent.northwestern.edu/psp/caesar/EMPLOYEE/HRMS/c/SA_LEARNER_SERVICES_2.SSR_SSENRL_CART.GBL?pslnkid=NW_SS_SA_SHOPPING_CART&FolderPath=PORTAL_ROOT_OBJECT.NW_SS_ENROLLMENT.NW_SS_SA_SHOPPING_CART&IsFolder=false&IgnoreParamTempl=FolderPath%2cIsFolder').read()
soup = BeautifulSoup(url, "html.parser")
print type(soup)
print soup.prettify()[0:1000]

