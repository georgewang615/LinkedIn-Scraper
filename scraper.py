from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import re as re
import time
import pandas as pd
from collections import Counter
import csv

PATH = "C:\\Users\\georg\\Desktop\\chromedriver.exe"
USERNAME = "georgewang615@gmail.com"
PASSWORD = "2572225463Gw"

driver = webdriver.Chrome(PATH)

driver.get("https://www.linkedin.com/uas/login")
time.sleep(3)

email=driver.find_element_by_id("username")
email.send_keys(USERNAME)
password=driver.find_element_by_id("password")
password.send_keys(PASSWORD)
time.sleep(3)
password.send_keys(Keys.RETURN)

contact_links = [
    "https://www.linkedin.com/in/con-koromilas-4b3228a/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/brett-jollie-5495317/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/adviceintelligence/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/matthew-rady-818a3518/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/caitrionawortley/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/elfreda-jonker-67047336/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/andrew-martin-41857352/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/nicole-mahan-63a41137/detail/recent-activity/", #2020 report
    "https://www.linkedin.com/in/simone-newman-43789b10/detail/recent-activity/", #2020 report
    "https://www.linkedin.com/in/rorycunningham/detail/recent-activity/", #white label, nightingale, CRM
    "https://www.linkedin.com/in/andrew-campion/detail/recent-activity/", #white label
    "https://www.linkedin.com/in/hikchadirchi/detail/recent-activity/", #FFR, nightingale, CRM
    "https://www.linkedin.com/in/mark-knight-8733a730/detail/recent-activity/", #FFR, nightingale
    "https://www.linkedin.com/in/andrea-mcgarry-823291167/detail/recent-activity/", #CRM
    "https://www.linkedin.com/in/chris-gosselin/", #advertising, nightingale
    "https://www.linkedin.com/in/shane-hancock-a0484192/detail/recent-activity/", #white label
    "https://www.linkedin.com/in/landjames/detail/recent-activity/", #2018 report
    "https://www.linkedin.com/in/natalie-dolan-97aa03/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/tony-carter-61113a8/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/ilan-israelstam/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/vinnie-w-11477822/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/chris-sakiris-b90643123/detail/recent-activity/", #nightingale, data audit
    "https://www.linkedin.com/in/kathryn-barnes-webley-9641b7b4/detail/recent-activity/", #data audit
    "https://www.linkedin.com/in/chantal-giles-731a6113/detail/recent-activity/", #data audit
    "https://www.linkedin.com/in/davidgrybas/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/jameslanglands/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/waynefaleiro/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/paul-cullen-au/detail/recent-activity/", #advertising
    "https://www.linkedin.com/in/andrew-king-53026927/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/angela-dovitsas-48547130/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/matthewtee/detail/recent-activity/", #nightingale, FFR
    "https://www.linkedin.com/in/steven-bennett-029a7436/detail/recent-activity/", #2018 report
    "https://www.linkedin.com/in/courtney-mcewen-70785846/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/nickohare/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/steve-williams-01380341/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/euansneyd/detail/recent-activity/", #white label
    "https://www.linkedin.com/in/todd-stevenson-42972723/detail/recent-activity/", #white label
    "https://www.linkedin.com/in/gideonlipman/detail/recent-activity/", #2020 report
    "https://www.linkedin.com/in/benjamin-abell-12299275/detail/recent-activity/", #2019 report
    "https://www.linkedin.com/in/peter-chun-43715120/detail/recent-activity/", #nightingale, 2018 report
    "https://www.linkedin.com/in/matthew-roberts-81754094/detail/recent-activity/", #FFR
    "https://www.linkedin.com/in/matthewrowecfp/detail/recent-activity/", #2020 report
    "https://www.linkedin.com/in/grahame-evans-94513215/detail/recent-activity/", #2020 report
    "https://www.linkedin.com/in/lisahamiltonrose/detail/recent-activity/", #FFR
    "https://www.linkedin.com/in/charlie-wapshott-65a7a737/detail/recent-activity/", #2020 report
    "https://www.linkedin.com/in/james-meade-0049922a/detail/recent-activity/", #2020 report
    "https://www.linkedin.com/in/odette-de-souza-16287736/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/annemcdonnell/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/gregory-newman-74213638/detail/recent-activity/", #nightingale, 2019 report
    "https://www.linkedin.com/in/daniel-brammall-advocate-for-the-truly-independent-adviser-210b5014/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/darrensteinhardt/detail/recent-activity/", #2020 report
    "https://www.linkedin.com/in/itsjordankerr/detail/recent-activity/", #2020 report
    "https://www.linkedin.com/in/lesleymamelokintegritylife/detail/recent-activity/", #2020 report
    "https://www.linkedin.com/in/lucy-hill-27864228/detail/recent-activity/", #advertising
    "https://www.linkedin.com/in/fandronaco/detail/recent-activity/", #2020 report
    "https://www.linkedin.com/in/jonathan-tolub-98a741/detail/recent-activity/", #2020 report
    "https://www.linkedin.com/in/peter-ornsby-456b5b12/detail/recent-activity/", #data audit
    "https://www.linkedin.com/in/selin-ertac/detail/recent-activity/", #data audit
    "https://www.linkedin.com/in/david-hallifax-1319992b/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/katie-babatsikos-3249ab32/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/twbaldwin/detail/recent-activity/", #2020 report
    "https://www.linkedin.com/in/sarah-selig-40a37973/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/filip-gudov/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/andrew-kempe-cfa-884ba528/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/eugene-ardino-a209b313/detail/recent-activity/", #licensee compliance manager
    "https://www.linkedin.com/in/rick-steele/detail/recent-activity/", #FFR
    "https://www.linkedin.com/in/robhardysydney/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/amy-vamvoukis-70534873/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/eli-glotzer-604ab779/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/brendan-carrig-71988420/detail/recent-activity/", #2018 report
    "https://www.linkedin.com/in/frank-casarotti-b4566553/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/sharleengarcia/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/stevemelling/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/richardjnunn/detail/recent-activity/", #2019 report
    "https://www.linkedin.com/in/merayelkhoury/detail/recent-activity/", #2019 report
    "https://www.linkedin.com/in/michael-mulholland-3bb03b4/detail/recent-activity/", #2019 report
    "https://www.linkedin.com/in/noel-lord-3592b420/detail/recent-activity/", #2019 report
    "https://www.linkedin.com/in/deborahdalziel/detail/recent-activity/", #2020 report
    "https://www.linkedin.com/in/reganvanberlo/detail/recent-activity/", #nightingale, FFR, CRM
    "https://www.linkedin.com/in/john-paull-6686645/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/connor-hance-muir-bab37210/detail/recent-activity/", #nightingale, CRM
    "https://www.linkedin.com/in/brendan-carmichael-889b0613a/detail/recent-activity/", #nightingale, 2019 report
    "https://www.linkedin.com/in/melissacrawfordmelb/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/gregory-black-7b34542/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/geoff-rogers-40a81556/detail/recent-activity/", #data audit
    "https://www.linkedin.com/in/robyn-packard-1b54b015/detail/recent-activity/", #data audit
    "https://www.linkedin.com/in/victornordberg/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/philipwinter/detail/recent-activity/", #advertising, nightingale
    "https://www.linkedin.com/in/rinchenolthang/detail/recent-activity/", #advertising
    "https://www.linkedin.com/in/tgangemi/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/chris-galloway-cfa-a5821310/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/jamie-wickham-cfa-88832a62/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/peter-mccarthy-9a0801145/detail/recent-activity/", #nightingale, advertising
    "https://www.linkedin.com/in/danedwardpowell/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/melanie-de-cressac-442b8a15/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/matthew-kent-29a73248/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/mattheine/detail/recent-activity/", #2020 report, nightingale
    "https://www.linkedin.com/in/hollanddamian/detail/recent-activity/", #2020 report, nightingale
    "https://www.linkedin.com/in/andrewbraun/detail/recent-activity/", #nightingale, advertising
    "https://www.linkedin.com/in/lindsay-coates-5223a815/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/justinpcarroll/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/michelle-allen-a7b12817/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/tchourilov/detail/recent-activity/", #2020 report
    "https://www.linkedin.com/in/george-chirakis-28397226/detail/recent-activity/", #CRM, nightingale
    "https://www.linkedin.com/in/emily-vella-643294124/detail/recent-activity/", #CRM
    "https://www.linkedin.com/in/tilly-simpson-15567a84/detail/recent-activity/", #FFR
    "https://www.linkedin.com/in/adam-myers-7591751/detail/recent-activity/", #FFR
    "https://www.linkedin.com/in/cesar-farfan-6ab44044/detail/recent-activity/", #nightingale, FFR
    "https://www.linkedin.com/in/adrian-whittingham-681399/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/ramsin-jajoo-9174a510/detail/recent-activity/", #nightingale, CRM, data audit
    "https://www.linkedin.com/in/chelseyvaux/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/deanmclelland/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/chris-groth-887baa27/detail/recent-activity/", #nightingale, 2020 report
    "https://www.linkedin.com/in/reuban-sivarajasingam-2172b036/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/james-poon-a6a405a/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/matthew-young-cima%C2%AE-a3a5b940/detail/recent-activity/", #nightingale, FFR, advertising
    "https://www.linkedin.com/in/katelyn-hynes-6b000b7a/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/nicholas-simpson-80051b22/detail/recent-activity/", #FFR, CRM
    "https://www.linkedin.com/in/craigjameson1/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/james-gyton-54828216/detail/recent-activity/", #data audit
    "https://www.linkedin.com/in/sean-cogman-4ab1119b/detail/recent-activity/", #data audit
    "https://www.linkedin.com/in/anne-fuchs-90504816/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/darren-hall-978b202a/detail/recent-activity/", #nightingale, musical chairs
    "https://www.linkedin.com/in/niall-mcconville-35a67a30/detail/recent-activity/", #2020 report, 2018 report
    "https://www.linkedin.com/in/rhys-cahill-63b49579/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/laceyfonseca/detail/recent-activity/", #advertising, nightingale
    "https://www.linkedin.com/in/megan-isles/detail/recent-activity/", #advertising
    "https://www.linkedin.com/in/luke-williams-898aab31/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/dileepa-diyagama-62187618/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/ingrid-groer-01339b9/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/jon-howie-ab489a26/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/joshua-parisotto/detail/recent-activity/", #2018 report
    "https://www.linkedin.com/in/david-wright-661a466/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/john-nicoll-2344b229/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/kieran-forde-9a1aba1/detail/recent-activity/", #2020 report
    "https://www.linkedin.com/in/phil-gould-40970510/detail/recent-activity/", #nightingale, musical chairs, 2018 report

]

nightingale = [
    "https://www.linkedin.com/in/con-koromilas-4b3228a/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/brett-jollie-5495317/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/adviceintelligence/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/matthew-rady-818a3518/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/caitrionawortley/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/elfreda-jonker-67047336/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/andrew-martin-41857352/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/rorycunningham/detail/recent-activity/", #white label, nightingale, CRM
    "https://www.linkedin.com/in/hikchadirchi/detail/recent-activity/", #FFR, nightingale, CRM
    "https://www.linkedin.com/in/mark-knight-8733a730/detail/recent-activity/", #FFR, nightingale
    "https://www.linkedin.com/in/chris-gosselin/", #advertising, nightingale
    "https://www.linkedin.com/in/natalie-dolan-97aa03/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/tony-carter-61113a8/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/ilan-israelstam/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/vinnie-w-11477822/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/chris-sakiris-b90643123/detail/recent-activity/", #nightingale, data audit
    "https://www.linkedin.com/in/davidgrybas/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/jameslanglands/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/waynefaleiro/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/andrew-king-53026927/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/angela-dovitsas-48547130/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/matthewtee/detail/recent-activity/", #nightingale, FFR
    "https://www.linkedin.com/in/courtney-mcewen-70785846/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/nickohare/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/steve-williams-01380341/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/peter-chun-43715120/detail/recent-activity/", #nightingale, 2018 report
    "https://www.linkedin.com/in/odette-de-souza-16287736/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/annemcdonnell/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/gregory-newman-74213638/detail/recent-activity/", #nightingale, 2019 report
    "https://www.linkedin.com/in/daniel-brammall-advocate-for-the-truly-independent-adviser-210b5014/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/david-hallifax-1319992b/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/katie-babatsikos-3249ab32/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/sarah-selig-40a37973/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/filip-gudov/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/andrew-kempe-cfa-884ba528/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/robhardysydney/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/amy-vamvoukis-70534873/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/eli-glotzer-604ab779/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/frank-casarotti-b4566553/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/sharleengarcia/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/stevemelling/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/reganvanberlo/detail/recent-activity/", #nightingale, FFR, CRM
    "https://www.linkedin.com/in/john-paull-6686645/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/connor-hance-muir-bab37210/detail/recent-activity/", #nightingale, CRM
    "https://www.linkedin.com/in/brendan-carmichael-889b0613a/detail/recent-activity/", #nightingale, 2019 report
    "https://www.linkedin.com/in/melissacrawfordmelb/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/gregory-black-7b34542/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/victornordberg/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/philipwinter/detail/recent-activity/", #advertising, nightingale
    "https://www.linkedin.com/in/tgangemi/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/chris-galloway-cfa-a5821310/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/jamie-wickham-cfa-88832a62/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/peter-mccarthy-9a0801145/detail/recent-activity/", #nightingale, advertising
    "https://www.linkedin.com/in/danedwardpowell/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/melanie-de-cressac-442b8a15/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/matthew-kent-29a73248/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/mattheine/detail/recent-activity/", #2020 report, nightingale
    "https://www.linkedin.com/in/hollanddamian/detail/recent-activity/", #2020 report, nightingale
    "https://www.linkedin.com/in/andrewbraun/detail/recent-activity/", #nightingale, advertising
    "https://www.linkedin.com/in/lindsay-coates-5223a815/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/justinpcarroll/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/michelle-allen-a7b12817/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/george-chirakis-28397226/detail/recent-activity/", #CRM, nightingale
    "https://www.linkedin.com/in/cesar-farfan-6ab44044/detail/recent-activity/", #nightingale, FFR
    "https://www.linkedin.com/in/adrian-whittingham-681399/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/ramsin-jajoo-9174a510/detail/recent-activity/", #nightingale, CRM, data audit
    "https://www.linkedin.com/in/chelseyvaux/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/deanmclelland/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/chris-groth-887baa27/detail/recent-activity/", #nightingale, 2020 report
    "https://www.linkedin.com/in/reuban-sivarajasingam-2172b036/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/james-poon-a6a405a/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/matthew-young-cima%C2%AE-a3a5b940/detail/recent-activity/", #nightingale, FFR, advertising
    "https://www.linkedin.com/in/katelyn-hynes-6b000b7a/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/craigjameson1/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/anne-fuchs-90504816/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/darren-hall-978b202a/detail/recent-activity/", #nightingale, musical chairs
    "https://www.linkedin.com/in/rhys-cahill-63b49579/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/laceyfonseca/detail/recent-activity/", #advertising, nightingale
    "https://www.linkedin.com/in/luke-williams-898aab31/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/dileepa-diyagama-62187618/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/ingrid-groer-01339b9/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/jon-howie-ab489a26/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/david-wright-661a466/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/john-nicoll-2344b229/detail/recent-activity/", #nightingale
    "https://www.linkedin.com/in/phil-gould-40970510/detail/recent-activity/", #nightingale, musical chairs, 2018 report

]

others = [
    "https://www.linkedin.com/in/nicole-mahan-63a41137/detail/recent-activity/", #2020 report
    "https://www.linkedin.com/in/simone-newman-43789b10/detail/recent-activity/", #2020 report
    "https://www.linkedin.com/in/andrew-campion/detail/recent-activity/", #white label
    "https://www.linkedin.com/in/andrea-mcgarry-823291167/detail/recent-activity/", #CRM
    "https://www.linkedin.com/in/shane-hancock-a0484192/detail/recent-activity/", #white label
    "https://www.linkedin.com/in/landjames/detail/recent-activity/", #2018 report
    "https://www.linkedin.com/in/kathryn-barnes-webley-9641b7b4/detail/recent-activity/", #data audit
    "https://www.linkedin.com/in/chantal-giles-731a6113/detail/recent-activity/", #data audit
    "https://www.linkedin.com/in/paul-cullen-au/detail/recent-activity/", #advertising
    "https://www.linkedin.com/in/matthewtee/detail/recent-activity/", #nightingale, FFR
    "https://www.linkedin.com/in/steven-bennett-029a7436/detail/recent-activity/", #2018 report
    "https://www.linkedin.com/in/euansneyd/detail/recent-activity/", #white label
    "https://www.linkedin.com/in/todd-stevenson-42972723/detail/recent-activity/", #white label
    "https://www.linkedin.com/in/gideonlipman/detail/recent-activity/", #2020 report
    "https://www.linkedin.com/in/benjamin-abell-12299275/detail/recent-activity/", #2019 report
    "https://www.linkedin.com/in/matthew-roberts-81754094/detail/recent-activity/", #FFR
    "https://www.linkedin.com/in/matthewrowecfp/detail/recent-activity/", #2020 report
    "https://www.linkedin.com/in/grahame-evans-94513215/detail/recent-activity/", #2020 report
    "https://www.linkedin.com/in/lisahamiltonrose/detail/recent-activity/", #FFR
    "https://www.linkedin.com/in/charlie-wapshott-65a7a737/detail/recent-activity/", #2020 report
    "https://www.linkedin.com/in/james-meade-0049922a/detail/recent-activity/", #2020 report
    "https://www.linkedin.com/in/darrensteinhardt/detail/recent-activity/", #2020 report
    "https://www.linkedin.com/in/itsjordankerr/detail/recent-activity/", #2020 report
    "https://www.linkedin.com/in/lesleymamelokintegritylife/detail/recent-activity/", #2020 report
    "https://www.linkedin.com/in/lucy-hill-27864228/detail/recent-activity/", #advertising
    "https://www.linkedin.com/in/fandronaco/detail/recent-activity/", #2020 report
    "https://www.linkedin.com/in/jonathan-tolub-98a741/detail/recent-activity/", #2020 report
    "https://www.linkedin.com/in/peter-ornsby-456b5b12/detail/recent-activity/", #data audit
    "https://www.linkedin.com/in/selin-ertac/detail/recent-activity/", #data audit
    "https://www.linkedin.com/in/twbaldwin/detail/recent-activity/", #2020 report
    "https://www.linkedin.com/in/eugene-ardino-a209b313/detail/recent-activity/", #licensee compliance manager
    "https://www.linkedin.com/in/rick-steele/detail/recent-activity/", #FFR
    "https://www.linkedin.com/in/brendan-carrig-71988420/detail/recent-activity/", #2018 report
    "https://www.linkedin.com/in/richardjnunn/detail/recent-activity/", #2019 report
    "https://www.linkedin.com/in/merayelkhoury/detail/recent-activity/", #2019 report
    "https://www.linkedin.com/in/michael-mulholland-3bb03b4/detail/recent-activity/", #2019 report
    "https://www.linkedin.com/in/noel-lord-3592b420/detail/recent-activity/", #2019 report
    "https://www.linkedin.com/in/deborahdalziel/detail/recent-activity/", #2020 report
    "https://www.linkedin.com/in/geoff-rogers-40a81556/detail/recent-activity/", #data audit
    "https://www.linkedin.com/in/robyn-packard-1b54b015/detail/recent-activity/", #data audit
    "https://www.linkedin.com/in/rinchenolthang/detail/recent-activity/", #advertising
    "https://www.linkedin.com/in/tchourilov/detail/recent-activity/", #2020 report
    "https://www.linkedin.com/in/george-chirakis-28397226/detail/recent-activity/", #CRM, nightingale
    "https://www.linkedin.com/in/emily-vella-643294124/detail/recent-activity/", #CRM
    "https://www.linkedin.com/in/tilly-simpson-15567a84/detail/recent-activity/", #FFR
    "https://www.linkedin.com/in/adam-myers-7591751/detail/recent-activity/", #FFR
    "https://www.linkedin.com/in/nicholas-simpson-80051b22/detail/recent-activity/", #FFR, CRM
    "https://www.linkedin.com/in/james-gyton-54828216/detail/recent-activity/", #data audit
    "https://www.linkedin.com/in/sean-cogman-4ab1119b/detail/recent-activity/", #data audit
    "https://www.linkedin.com/in/niall-mcconville-35a67a30/detail/recent-activity/", #2020 report, 2018 report
    "https://www.linkedin.com/in/megan-isles/detail/recent-activity/", #advertising
    "https://www.linkedin.com/in/joshua-parisotto/detail/recent-activity/", #2018 report
    "https://www.linkedin.com/in/kieran-forde-9a1aba1/detail/recent-activity/", #2020 report
]


list = []



def scrape(link):
    new = link.strip("/recent-activity/") + "/interests/influencers"
    driver.get(new)
    span_title = driver.find_elements_by_class_name("pv-entity__summary-title-text")
    time.sleep(10)
    for elem in span_title:
        list.append(elem.text)



for i in range(len(nightingale)):
    scrape(nightingale[i])



dict = Counter(list)

sorted_dict = sorted(dict.items(), key = lambda x: x[1], reverse = True)

with open('nightingale_influencers.csv', 'w', encoding = 'UTF8') as f:
    writer = csv.writer(f)
    for i in sorted_dict:
        writer.writerow(i)




driver.close()
