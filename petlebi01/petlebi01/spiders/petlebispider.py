import scrapy
import json

 
# petlebi.com dan veri kazıyazak spider
class PetlebispiderSpider(scrapy.Spider):
    name = "petlebispider"
    
    # scraping işlemi yapılacak web sayfası kaynağı linki.
    start_urls = ["https://www.petlebi.com/cok-satanlar"]

    def parse(self, response):
        # ilgili web sayfası kaynağından xpath aracılığıyla istediğim verileri kazıyorum.
        # her data dizi şeklinde kümeli tutuluyor.
        products_names = response.xpath("//div[@class='card-body pb-0 pt-2 pl-3 pr-3']/a/@title").getall()
        products_prices = response.xpath("//div[@class='card-footer pl-3 pr-3 pb-2 pt-2']/p/span[@class='commerce-discounts']/text()").getall()
        products_url = response.xpath("//div[@class='card-body pb-0 pt-2 pl-3 pr-3']/a/@href").getall()
        product_datagram = response.xpath("//div[@class='card-body pb-0 pt-2 pl-3 pr-3']/a/@data-gtm-product").getall()


        # product sayılarının denk olup olmadığını kontrol etmeye çabalama.
        if len(products_names) == len(products_prices):
            lenght = len(products_prices)

            # istene veri dizilerini loop
            for x in range(lenght):
                name = products_names[x]
                price = products_prices[x]
                url = products_url[x]
                datagram_string = product_datagram[x]
                datagram_dic = json.loads(datagram_string)
                brand = datagram_dic["brand"]
                category = datagram_dic["category"]
                product_id = datagram_dic["id"]
                stock = datagram_dic["quantity"]

                # veri setini yaratma
                yield{
                    'product_url' : url,
                    'product_name' : name,
                    'product_price' : price,
                    'product_brand' : brand,
                    'product_category' : category,
                    'product_ID' : product_id,
                    'product_stock' : stock
                }
        else:
            # hatalı veri sayısıyla karşılaşırsak anlaşılır error mesajı olsun.
            yield{
                'error' : 'product info fetched problematicly.'
            }
        
        # next page e gidip veriyi kazımak için kontrol
        next_page = response.xpath("//a[@rel='next']/@href").get()
        if len(next_page) > 1 :
            yield response.follow(next_page, callback=self.parse)







    


