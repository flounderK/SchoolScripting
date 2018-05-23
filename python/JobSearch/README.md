# JobSearch
A repo to hold the code for my personal choice in job searching.

patternscore is just an extention of re and an overload of the list datastructue's add(). patternscore is meant to grade strings based on specific regex patterns that are created by the user. 

JobSearchRegex.txt is where I am storing the regular expression patterns that I would like to search for.

postingDatabase.py is a set of functions meant to help analyze job postings for the future. It is entirely optional to use. 

PAL.py is a test of patternscore, it uses selenium to automate the parsing of job postings on uc.edu/pal

PAL:

Selenium and chromedriver executable will be needed for this script.
https://sites.google.com/a/chromium.org/chromedriver/downloads
*Update* - The chrome_driver_download.py file is an alternate method.

The script requires selenium and bs4, downloadable though pip.

pip install selenium
pip install beautifulsoup4

starts google chrome with selenium. It navigates to the Login page for 
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
	python PAL.py -a

The database stuff in PAL.py is not necessary, it is just being saved for data ananlysis later. 


