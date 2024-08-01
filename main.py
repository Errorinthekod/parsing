
from bs4 import BeautifulSoup as BS
import requests
from multiprocessing import Pool

def get_html(url):
    headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}
    response = requests.get(url, headers)
    if response.status_code == 200:
        return response.text
    return None


def get_glide_link(html):
    soup = BS(html,'html.parser')
    content = soup.find('div',class_='main-content')
    posts = content.find('div',class_='listings-wrapper')
    post = posts.find_all('div',class_='listing')
    links = []
    for p in post:
        r_info = p.find('div', class_= 'right-info')
        title = r_info.find('p', class_= 'title')
        link = title.find('a').get('href')
        full_link = 'https://www.house.kg/' + link
        links.append(full_link)
        # print(title.text.strip())
        # r_side = r_info.find('div', class_='right-side')
        # print(r_side.text.strip())
        # sep_main = r_side.find('div', class_='sep main')   
        # price = sep_main.find('div', class_='price')  
        # print(price.text.strip())
        # price_addit = sep_main.find('div', class_='price-addition')
        # print(price_addit.text.strip())
        # top_info = r_info.find('div', class_='top-info')
        # print(top_info.text.strip())
        # left_side = top_info.find('div', class_='left-side')
        # print(left_side.text.strip())
        # addres = left_side.find('div', class_='address')
        # print(addres.text.strip())
        # jk = left_side.find('div', class_='title-addition')
        # print(jk)
        # descr = r_info.find('div', class_= 'description')
        # print(descr.text.strip())


    return links



def get_data(html):
    soup = BS(html, 'html.parser')
    # content = soup.find('div', class_='content')
    # pmovie = content.find('div', class_ = 'pmovie__main')
    # title = pmovie.find('header', class_='pmovie__header').find('h1').text.strip()
    # orig_title = pmovie.find('div', class_='pmovie__main-info ws-nowrap').text.strip()
    # raiting = pmovie.find('div',class_ = 'pmovie__anime').find('div', class_='item-slide__ext-rating item-slide__ext-rating--imdb').text.strip()
    
    content = soup.find('div', class_='content-wrapper')
    phone_block = content.find('div', class_='phone-fixable-block')
    user = phone_block.find('a', class_='name').text.strip()
    phone = phone_block.find('div', class_='number').text.strip()
    
    details = content.find('div', class_='details-main')
    left = details.find('div', {'class':'left'})
    label = left.find_all('div', class_='label')
    info = left.find_all('div', class_='info')
    
    for l, i in zip(label, info):
        print(l.text.strip()+':'+ i.text.strip())
        
    details_header = content.find('div', class_='details-header') 
    left = details_header.find('div', class_='left') 
    right_prices_block = details_header.find('div', class_='right prices-block') 
    right = details.find('div', class_='right') 
    sep_main = right_prices_block.find('div', class_='sep main') 
    sep_addit = right_prices_block.find('div', class_='sep addit') 
    name = left.find('h1').text.strip()
    # print(name) 
    c_name = left.find('div', class_='c-name') 
    c_name = c_name.text.strip() if c_name else 'Net ZHK'
    address = left.find('div', class_='address').text.strip()
    # print(address) 
    price_dollar = sep_main.find('div', class_='price-dollar').text.strip()
    
    price_som = sep_main.find('div', class_='price-som').text.strip()
    price_dollar2 = sep_addit.find('div', class_='price-dollar').text.strip()
    
    price_som2 = sep_addit.find('div', class_='price-som').text.strip()
    description = right.find('div', class_='description') 
    description = description.text.strip() if description else 'Net Opisania'
    

    data = {
        'title': name,
        'price': price_som,
        'price_dollar': price_dollar,
        'price_m2': price_som2,
        'price_dollar_m2': price_dollar2,
        'address': address,
        'zhk': c_name,
        'user': user,
        'phone': phone,
        'description': description,
        'INFO' : {l:i}
        
    }



    print('_____________________________________________________________________________')

    return data

def get_data(html):
    soup = BS(html, 'html.parser')
    content = soup.find('div', class_='content-wrapper')
    # phone_block = content.find('div', class_='phone-fixable-block')
    # user = phone_block.find('a', class_='name').text.strip()
    # phone = phone_block.find('div', class_='number').text.strip()
    main_con = content.find('div' , class_='main-content')
    detailsh = main_con.find('div', class_='details-header')
    # try:
    #     left_h = detailsh.find('div', class_='left').text.strip()
    #     print(left_h)
    # except AttributeError:

    r_price = detailsh.find('div', class_= 'right prices-block')
    print(r_price)
    


    sep_main = r_price.find('div', class_='sep main')
    d_price = sep_main.find('div', class_='price-dollar').text.strip()
    print(d_price)
    s_price = sep_main.find('div', class_='price-som').text.strip()
    print(s_price)
    sep_add = r_price.find('div', class_='sep addit')
    d1_price = sep_add.find('div', class_='price-dollar').text.strip()
    print(d1_price)
    s1_price = sep_add.find('div', class_='price-som').text.strip()
    print(s1_price)
    details_main = detailsh.find('div', class_='details-main')
    right = details_main.find('div', class_='right')
    descr = right.find('div', class_='description').text.strip()
    print(descr)
    #hw
    
    


    details = content.find('div' , class_='details-main')
    left = details.find('div' , {'class': 'left'})
    label = left.find_all('div', class_='label')
    info = left.find_all('div', class_='info')

    for l, i in zip(label, info):
        print(l.text.strip() + ':' + i.text.strip())
        
def last_page(html):
    soup = BS(html, 'html.parser')
    page = soup.find('ul', class_='pagination')
    pages = page.find_all('a', class_='page-link')
    last_page = pages[-1].get('data-page')
    return int(last_page)
    
def parsing(page_num):
    URL = 'https://www.house.kg/kupit-kvartiru?'
    page_url = URL + f'page= {page_num}'
    page_html = get_html(page_url)
    links = get_glide_link(page_html)
    for link in links:
            posts_links = get_html(url = link)
            get_data(html = posts_links)


def main():
    URL = 'https://www.house.kg/kupit-kvartiru?'
    html = get_html(url = URL)
    pages = last_page(html=html)
    # links = get_glide_link(html = html)
with Pool(7) as p:
    p.map(parsing, range(1, pages + 1))


        
    
    

# print('hello')
# time.sleep(5)
# print('world')
 
if __name__ == '__main__':
    main()





