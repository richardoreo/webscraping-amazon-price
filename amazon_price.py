# Step 1: Import modules and libraries
from bs4 import BeautifulSoup
import requests
 
# Step 2: Define Headers. This is needed because Amazon has protections against webscraping.
# We need to trick the website to thinking that we're an actual human browsing the page.
HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                'Accept-Language': 'en-US, en;q=0.5'})
 
# Step 3: Define the webpage URL that we're trying to convert into a BeautifulSoup object
# that we can then manipulate
URL = "https://www.amazon.com/Automate-Boring-Stuff-Python-2nd-dp-1593279922/dp/1593279922/ref=dp_ob_title_bk"
 
# Step 4: Create the HTTP Request
webpage = requests.get(URL, headers=HEADERS) # goes to the website using the headers
 
# Step 5: Create a Soup Object by extracting the websites and putting the lxml into the Soup Object
soup = BeautifulSoup(webpage.content, "lxml")
 
# Step 6 (Optional): Run this if you're having trouble with errors. This should print out the webpage
# into whichever command prompt you're using. Just delete the hashtags
# if this doesn't print out, then you know you have an issue prior to this step.
# prettify_webpage = soup.prettify()
# print(prettify_webpage)
 
# Step 7: We create another price variable/object (not sure what this would be called)
# that contains the parameters we're looking for which is price.
# then the .string.strip() creates a string that we can then pass into the print() function
price = soup.find("span", attrs={'id':'price'}).string.strip()
 
# Step 8: Print out price
print("Product Price =", price)
