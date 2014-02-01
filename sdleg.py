from mechanize import Browser
from bs4 import *
from time import *
import re
import datetime

mech = Browser()

mech.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

mech.set_handle_robots(False)

today = str(datetime.date.today().strftime("%m-%d-%Y"))

f = open('bills-as-of-' + today + '.txt','wb')

f.write("bill_num\tsummary\tsponsor\taddress\tsponsor_url\tbill_url\t\n")

legdata = { "Anderson": "29177 477th Avenue Hudson, SD 57304", "Bartling": "28921 US Hwy. 18 Gregory, SD 57533", "Begalka": "18254 SD Highway 15 Clear Lake, SD 57226-5401", "Bolin": "403 West 11th Street Canton, SD 57013-2418", "Bradford": "PO Box 690 Pine Ridge, SD 57770-0690", "Brown": "316 S Potter Street Gettysburg, SD 57442-1549", "Buhl O'Donnell": "521 N. Prairie Sioux Falls, SD 57104", "Cammack": "PO Box 100 Union Center, SD 57787-0100", "Campbell": "3480 Colvin Street Rapid City, SD 57703", "Carson": "PO Box 1112 Mitchell, SD 57301-7112", "Conzet": "1523 West Blvd Rapid City, SD 57701-4551", "Craig": "8556 Heather Drive Rapid City, SD 57702-7710", "Cronin": "300 E Blaine Avenue Gettysburg, SD 57442-0042", "Curd": "810 E. 23rd St. Sioux Falls, SD 57105", "Dryden": "2902 Tomahawk Drive Rapid City, SD 57702-4250", "Duvall": "PO Box 453 Pierre, SD 57501", "Ecklund": "48217 265th Street Brandon, SD 57005", "Erickson": "PO Box 88045 Sioux Falls, SD 57109", "Ewing": "PO Box 607 Spearfish, SD 57783", "Feickert": "38485 129th St Aberdeen, SD 57401-8386", "Feinstein": "3205 E Marson Drive Sioux Falls, SD 57103", "Frerichs": "13507 465th Avenue Wilmot, SD 57279", "Gibson": "1010 Valley View Court Huron, SD 57350-4221", "Gosch": "312 Alta Vista Drive Rapid City, SD 57701-2337", "Greenfield": "507 N Smith Street Clark, SD 57225-1250", "Haggar (Jenna)": "PO Box 763 Sioux Falls, SD 57101", "Haggar (Don)": "PO Box 1532 Sioux Falls, SD 57101", "Hajek": "PO Box 1779 Sioux Falls, SD 57101", "Hawks": "405 S. Tessa Ave. Hartford, SD 57033", "Hawley": "1215 W. 8th St. South Brookings, SD 57006-2972", "Heineman (Phyllis)": "2005 S. Phillips Sioux Falls, SD 57105-2939", "Heinemann (Leslie)": "47962 228th St. Flandreau, SD 57028-6701", "Heinert": "PO Box 634 Mission, SD 57555-0634", "Hickey": "4501 N. Ellis Road Sioux Falls, SD 57107", "Hoffman": "34328 106th Street Eureka, SD 57437-5302", "Holien": "1315 11th Avenue NE Watertown, SD 57201-1607", "Hunhoff (Bernie)": "PO Box 175 Yankton, SD 57078-0175", "Hunhoff (Jean)": "2511 Mulligan Dr Yankton, SD 57078", "Jensen": "10215 Pioneer Ave Rapid City, SD 57702", "Johns": "203 W. Main St. Lead, SD 57754", "Jones (Chuck)": "713 W. 3rd Avenue Flandreau, SD 57028-0326", "Jones (Tom)": "117 N. Kemper Street Viborg, SD 57070", "Kaiser": "1415 Nicklaus Dr. Aberdeen, SD 57401-8822", "Killer": "PO Box 322 Pine Ridge, SD 57770-0322", "Kirkeby": "315 East Philadelphia Street Rapid City, SD 57701-1559", "Kirschman": "901 N Duluth Ave #1 Sioux Falls, SD 57104-2321", "Kopp": "1618 Downing St. Rapid City, SD 57701", "Krebs": "25740 Packard Lane Renner, SD 57055", "Langer": "600 W. 7th Street Dell Rapids, SD 57002-2117", "Latterell": "PO Box 801 Tea, SD 57064", "Lederman": "725 Indian Wells Ct. Dakota Dunes, SD 57049", "Lucas": "PO Box 182 Mission, SD 57555-0182", "Lust": "4269 Rosemary Lane Rapid City, SD 57702", "Magstadt": "1625 Northridge Drive Unit 107 Watertown, SD 57201-8667", "Maher": "PO Box 237 Isabel, SD 57633-0237", "May": "20261 BIA 2 Kyle, SD 57752-7400", "Mickelson": "101 N Main Ave., Suite 321 Sioux Falls, SD 57105", "Monroe": "127 W. Dakota Avenue Pierre, SD 57501", "Munsterman": "1133 West 8th St, South Brookings, SD 57006", "Nelson": "24739 420th Avenue Fulton, SD 57340", "Novstrup (David)": "1008 S. Wells Street Aberdeen, SD 57401-7373", "Novstrup (Al)": "1705 Northview Lane Aberdeen, SD 57401-2268", "Olson (Betty)": "11919 SD Highway 79 Prairie City, SD 57649", "Omdahl": "P.O. Box 88235 Sioux Falls, SD 57109-8235", "Otten (Ernie)": "46787 273rd St. Tea, SD 57064-8024", "Otten (Herman)": "PO Box 326 Tea, SD 57064-0325", "Parsley": "103 N. Liberty Madison, SD 57042-2706", "Peters": "705 N Sagehorn Drive Hartford, SD 57033-2380", "Peterson": "16952 482nd Avenue Revillo, SD 57259-5208", "Qualm": "27507 John Qualm Road Platte, SD 57369", "Rampelberg": "13948 Lariat Road Rapid City, SD 57702-7315", "Rasmussen": "28639 458th Avenue Hurley, SD 57036-6410", "Rave": "46923 250th St Baltic, SD 57003", "Rhoden": "PO Box 12 Union Center, SD 57787-0012", "Ring": "607 Sterling Street Vermillion, SD 57069-3453", "Romkema": "240 Fairway Drive Spearfish, SD 57783-3110", "Rounds": "513 North Van Buren Pierre, SD 57501", "Rozum": "87 S. Harmon Drive Mitchell, SD 57301", "Russell": "1938 Lincoln Ave Hot Springs, SD 57747", "Schaefer": "23026 SD Highway 273 Kennebec, SD 57544-5201", "Schoenfish": "42472 Maxwell Road Scotland, SD 57059-7106", "Schrempp": "1999 Trailsend Lantry, SD 57636-1999", "Sly": "22560 Potter Road Rapid City, SD 57702-6132", "Soholt": "PO Box 1146 Sioux Falls, SD 57101-1146", "Soli": "810 W. 6th Street Sioux Falls, SD 57104-2904", "Solum": "1333 Mayfair Drive Watertown, SD 57201-1155", "Stalzer": "5909 W. Bristol Drive Sioux Falls, SD 57106-0660", "Steele": "3220 W Zephyr Place #1 Sioux Falls, SD 57108-5009", "Stevens": "214 Marina Dell Yankton , SD 57078", "Sutton": "919 Franklin Street Burke, SD 57523", "Tidemann": "251 Indian Hills Rd Brookings, SD 57006-3650", "Tieszen": "3416 Brookside Drive Rapid City, SD 57702-8118", "Tulson": "44975 SD Highway 28 Lake Norden, SD 57248", "Tyler": "48170 144th St. Big Stone City, SD 57216-5520", "Van Gerpen": "1304 S. Laurel Street Tyndall, SD 57066", "Vehle": "132 N Harmon Drive Mitchell, SD 57301", "Verchio": "143 Rainbow Ridge Ct. Hill City, SD 57745-6621", "Welke": "PO Box 166 Warner, SD 57479-0166", "Werner": "1505 McDonald Drive Huron, SD 57350-3474", "Westra": "508 E. Meadowlark Trail Sioux Falls, SD 57108-2885", "White": "1145 Beach Circle NE Huron, SD 57350-4700", "Wick": "3009 W. Donahue Dr. Sioux Falls, SD 57105-0153", "Wink": "PO Box 137 Howes, SD 57748-0137", "Wismer": "PO Box 147 Britton, SD 57430-0147" }

baseurl = "http://legis.sd.gov/Legislative_Session/Bills/default.aspx?Session=2014"

page = mech.open(baseurl)
html = page.read()
soup = BeautifulSoup(html)

bill_links = []
sponsors = []
sponsorlinks = []

for link in mech.links(url_regex='Bill.aspx\?Bill='):
    bill_links.append(link.url)

print "Looping through detail pages."

for url in bill_links:
    counter = 0
    while counter < 5:
        try:
            page = mech.open(url)
            counter = 6
        except:
            print "The page didn't open on try No. " + str(counter+1) +". Feel bad."
            counter += 1
            sleep(30)
        
        html = page.read()
        soup = BeautifulSoup(html)

        try:
            billnum = soup.findAll('div', id=re.compile("divBillNumber"))[0].get_text(strip=True)
        except:
            billnum = ''
        print billnum

        try:
            sponsorgroup = soup.findAll('td', id=re.compile("tdSponsors"))
            for p in sponsorgroup:
                for v in p.findAll('a'):
                    sponslink = ('http://legis.sd.gov' + v['href']).replace('MemberBills.aspx','MemberDetail.aspx')
                    sponsorlinks.append(sponslink)
                    spons = v.get_text(strip=True)
                    sponsors.append(spons)
        except:
            pass

        try:
            billsumm = soup.findAll('td', id=re.compile("tdTitle"))[0].get_text()
        except:
            billsumm = ''
            
        try:
            vers = soup.findAll('table', id=re.compile("tblBillVersions"))
            for cell in vers:
                x = cell.findAll('td')[2].a
                billurl = 'http://legis.sd.gov/Legislative_Session/Bills/' + x['href']
        except:
            billurl = ''
        
        count = 0
        for name in sponsors:
            try:
                addy = legdata[name]
            except KeyError:
                addy = ''
            fullrecord = (billnum, billsumm, name, addy, sponsorlinks[count], billurl, '\n')
            f.write("\t".join(fullrecord))
            count += 1

    del sponsors[:]
    del sponsorlinks[:]
    mech.back()
    sleep(1)
f.flush()
f.close()

"""
# get list of urls for legislator mugs

j = open('sd-leg-mugs.txt','wb')

legurl = "http://legis.sd.gov/Legislators/Legislators/default.aspx?Session=2014"

page = mech.open(legurl)
html = page.read()
soup = BeautifulSoup(html)

house = soup.find('div', {'id': 'ContentPlaceHolder1_mlHouse_divMembers' })
senate = soup.find('div', {'id': 'ContentPlaceHolder1_mlSenate_divMembers' })

houselist = house.findAll('a')
senatelist = senate.findAll('a')
full_list = houselist + senatelist

cow = 0
for link in full_list:
    try:
        page = mech.open(link['href'])
        cow = 6
    except:
        print "The page didn't open on try No. " + str(cow+1) +". Feel bad."
        cow += 1
        sleep(30)
    html = page.read()
    soup = BeautifulSoup(html)
    name = soup.find('h3', {'id':'ContentPlaceHolder1_hdMember'}).get_text(strip=True).replace("  "," ").replace("Representative", "Rep.").replace("Senator", "Sen.")
    print name
    district = soup.find('span', {'id': 'ContentPlaceHolder1_spanDistrict'}).get_text(strip=True)
    
    pic = soup.findAll('img', {'id': 'ContentPlaceHolder1_imgMember'})
    for m in pic:
        mug = 'http://legis.sd.gov' + m['src']
    rec = (name,"|",mug,'\n')
    j.write(rec)
    mech.back()
    sleep(1)

j.flush()
j.close()
"""