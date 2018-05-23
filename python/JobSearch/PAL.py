# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 13:04:24 2018

@author: Clif
"""
#TODO: make the text finding/parsing stuff into a function, get rid of nested
#ifs in that function. Hint: include panels assignment in function 
#make the posting database with patternscore's grade included. 
#Check if "Apply on our webpage" or any similar statements are present,
#report this to the user

"""
This script starts google chrome with selenium. It navigates to the Login page for 
the PAL site. Once the user has logged into PAL, the script will start navigating the
website and will determine whether or not to apply to available positions based on 
the position descriptions. The console will also output links to the positions that 
were applied to. There is also an option to create a database to store job postings
for future analysis. 

usage:
	#useful as a test of selenium's functionality, just cycles through all of the available job postings
	python PAL.py 

	#Cycle through job postings and create a database with the postings
	python PAL.py -d

	#Applies to positions
	python PAL.py -a"""
import time
from selenium import webdriver
from selenium.webdriver.support import ui
from bs4 import BeautifulSoup
import argparse
from urllib.parse import urljoin
from re import sub, compile, findall
from postingDatabase import create_db, insert_into_db
import patternScore

def main(args):
    def page_is_loaded(driver):
        return driver.find_element_by_tag_name("body") != None

    def page_reached(driver):
        while (driver.current_url != "https://webapps2.uc.edu/elce/Student"):
            time.sleep(20)

    #create driver object
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    driver = webdriver.Chrome(chrome_options=options)
    wait = ui.WebDriverWait(driver, 10)
    driver.get("https://webapps2.uc.edu/elce/Login")

    #wait until body tag is found
    wait.until(page_is_loaded)

    #wait until login is finished. I don't want to mess with credentials more than
    #neccessary.
    page_reached(driver)

    driver.find_element_by_css_selector(".col-md-2 > a:nth-child(7)").click()
    driver.find_element_by_css_selector("#viewRankMenuLink > a:nth-child(1)").click()

    wait.until(page_is_loaded)
    #actual page
    #select show all
    driver.find_element_by_css_selector("#search-results-table_length > label > select > option:nth-child(5)").click()

    #find all of the pages we need to rank
    content = driver.page_source
    soup = BeautifulSoup(content, "lxml")
    table = soup.find("table", id="search-results-table")
    rows = table.find_all("tr", role="row")

    if args.d:
        create_db()

    legend = patternScore.Score_Legend()
    legend.create_from_file("JobSearchRegex.txt")
    
    positions_applied_to = list()
    eol_re = compile("\\n$")
    sub_re = compile("\\n|\\xa0")
    apply_re = compile("(to )*apply( [Oo]n)*")

    for i in range(1, (len(rows)-1)):
        href = rows[i].find("a")['href']
        url = urljoin(driver.current_url, href)
        driver.get(url)
        #wait
        wait.until(page_is_loaded)

        soup = BeautifulSoup(driver.page_source, "lxml")
        panels = soup.find_all("div", class_="panel panel-default")

        text = None
        title = None
        author = None
        note = None
        apply_flag = False
        for k in panels:
            #remove \n and \xa0 with sub
            #Position Name
            tag = k.find("h2")
            if tag is not None:
                if sub(sub_re, "",tag.text) == 'Rank Position':
                    title = sub(eol_re," ",k.find("div", attrs={"class":"row"}).text)
                    title = sub(sub_re, "", title)
            #Position Description
            tag = k.find("div", attrs={"class":"pal-label"})
            if tag is not None:
                if sub(sub_re, "",tag.text) == "Position Description":
                    text = sub(eol_re, " ", k.find("div", attrs={"class":"pal-content"}).text)
                    text = sub(sub_re, "", text)
                    if len(findall(apply_re, text)[0]) > 0:
                        apply_flag = True

            #Organization Name
                if sub(sub_re, "",tag.text) == "Organization Name":
                    author = sub(eol_re, " ", k.find("div", attrs={"class":"pal-content"}).text)
                    author = sub(sub_re, "", author)
            #Notes
                if sub(sub_re, "", tag.text) == "Note From Instructor":
                    note = sub(eol_re, " ", k.find("div", attrs={"class":"pal-content well"}).text)
                    note = sub(sub_re, "", note)
        
        #grade text, author bias, ect.
        doc = patternScore.Document(legend=legend,
                                    text=text,
                                    title=title,
                                    author=author)

        if args.d:
            insert_into_db(text=text, title=title, author=author)

        if args.a:
            if doc.score_total >= 3.25:
                #apply
                soup.find("input",
                          attrs={"data-val":"true",
                                 "id":"PositionRankId_2",
                                 "name":"RankedPosition.PositionRankId",
                                 "type":"radio",
                                 "value":"2"}).click()

                soup.find("button",
                          attrs={"type":"submit",
                                 "value":"save",
                                 "name":"command",
                                 "class":"btn btn-submit pal-margin-right-1",
                                 "id":"saveButton"}).click()
                wait.until(page_is_loaded)
                applied_dict = dict(zip(url, note))
                positions_applied_to.append(applied_dict)
                
        if (not args.a) and (not args.d):
            print("Document title: {:s}".format(str(doc.title)))
            print("Document author: {:s}".format(str(doc.author)))
            print("Document score: {:s}".format(str(doc.score_total)))
            
    driver.close()
    if args.a and (len(positions_applied_to) > 0):
        print("Applied to positions at the following links:")
        for link, note in positions_applied_to:
            print(link)
            print(note)
            print("")

parser = argparse.ArgumentParser()
parser.add_argument("-d",
                    default=False,
                    action='store_true',
                    help="Include database creation and building functions")
parser.add_argument("-a",
                    default=False,
                    action='store_true',
                    help="Enable appllictation process")
args = parser.parse_args()
main(args)
