import pprint

def scrape():
    import pandas as pd
    from bs4 import BeautifulSoup as bs
    from splinter import Browser

    from webdriver_manager.chrome import ChromeDriverManager
    exe_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **exe_path, headless=False)

    nasa_url = 'https://mars.nasa.gov/news/'
    browser.visit(nasa_url)
    html = browser.html
    soup = bs(html, 'html.parser')

    top = soup.find("div", class_="list_text")
    news_title = top.find("div", class_= "content_title").text
    news_p = top.find("div", class_="article_teaser_body").text

    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl_url)
    html = browser.html
    soup = bs(html, 'html.parser')

    picture_url = soup.find('a', class_ = 'group cursor-pointer block')['href']

    base_url = 'https://www.jpl.nasa.gov'
    jpl_result = base_url + picture_url

    browser.visit(jpl_result)
    html = browser.html
    soup = bs(html, 'html.parser')

    featured_image_url = soup.find('a', class_ = 'BaseButton text-contrast-none w-full mb-5 -primary -compact inline-block')['href']

    url = "https://space-facts.com/mars/"
    temp_df = pd.read_html(url)
    mars_df = temp_df[0]
    mars_df

    mars_df.columns=["Mars Profile", ""]
    mars_df.set_index("Mars Profile", inplace=True)
    mars_df.to_html("mars_facts.html")

    usgs_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(usgs_url)
    html = browser.html
    soup = bs(html, 'html.parser')

    link_list = []

    for link in soup.find_all('a', class_ = 'itemLink product-item'):
        if link.get('href') not in link_list:
            link_list.append(link.get('href'))

    hemisphere_image_urls = []

    for i in range(len(link_list)):
        browser.visit('https://astrogeology.usgs.gov' + link_list[i])
        html = browser.html
        soup = bs(html, 'html.parser')
        img_url = soup.find('a', text='Sample')['href']
        hemisphere_image_urls.append(
            {'hemisphere':link_list[i].split('/')[5].split('_')[0], 
            "img_url":img_url}
            )

    browser.quit()

    return {
        "nasa_news":{"headline":news_title,
        "teaser":news_p},
        "mars_facts":mars_df.to_json(),
        "JPL_picture_of_the_day":featured_image_url,
        "Hemisphere_data":hemisphere_image_urls
    }
