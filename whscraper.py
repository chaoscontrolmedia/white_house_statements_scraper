from bs4 import BeautifulSoup
import requests

test = requests.get('https://www.whitehouse.gov/briefing-room/').text
soup = BeautifulSoup(test, 'lxml')

headlines = soup.find_all('article')
#print(headlines)

for x in headlines:
    title = x.find('h2').text.strip()
    name = x.find('a').text.strip()  #alt
    date = x.find('time').text.strip()
    type = x.find('span', class_='tax-links cat-links').text.strip()

    #alt way wih more data cleanup
    newsitem = x.find('div').text.strip()
    a = newsitem.split()#turns newsitem into list form
    b = a[0:3]
    c = a[4:]
    e = (" ".join(b))#cleans up b
    f = (" ".join(c))#cleans up c

    g = f'{e}, {f}'# joining e and f

    cleaned_data = f'{title} \n{date}, {type}'


    print(cleaned_data)








    #print(title)



    '''
    b = a[0] + a[1] + a[2]

    c = a[4] + a[5]
    
  
    '''


   
  
    #print(b)


'''

date = soup.find_all('span', class_='tax-links cat-links')
for x in date:
    y = x.text.strip()
    #print(y)

'''





'''
print(f"{title}, {date}, {y}")

'''




    

#print(test)


