#py -m install requests
#%pip install requests
import requests

#use this to web scrape
requests.get('http://www.wisdompetmed.com/')

#scrape data from Wisdom Pet Medicine website and save to response variable
response = requests.get('http://www.wisdompetmed.com/')

#this confirms the url
response.url

#this gives us the status code 200 - success
response.status_code

# retrieve headers of Wisdom Pet Medicine website
response.headers

#retrieve content of the Wisdom Pet Medicine website
response.content

#retrieve text of the Wisdom Pet Medicine website
response.text

#install BeautifulSoup package (py -m install bs4)
%pip install bs4

#import BeautifulSoup package
from bs4 import BeautifulSoup

#Bring in the HTML code to BeautifulSoup
soup = BeautifulSoup(response.text)

#Prettify the HMTL code with BeautifulSoup
print(soup.prettify())

#Find where the first title tag occurs in the code for veterinarian business name
soup.find("title")

#find all times the article tag occurs in the code for list of services
soup.find_all('article')

#find the business phone number
print(soup.find("span", class_ = "phone").text)

#find all featured testimonials
featured_testimonial = soup.find_all("div", class_ = "quote")
for testimonial in featured_testimonial:
  print(testimonial.text)
  
#find all staff members
staff = soup.find_all("div", class_="info col-xs-8 col-xs-offset-2 col-sm-7 col-sm-offset-0 col-md-6 col-lg-8")
for s in staff:
    print(s.text)
    
#find all links on the Wisdom Pet Medicine website
links = soup.find_all("a")
for link in links:
  print(link.text, link.get('href'))

# write HTML code we pulled to a text file
with open("wisdom_vet.txt","w") as f:
  f.write(soup.prettify())
