import scrapy

# product ın kendi sayfasına gidip verileri kazıyan ve ana spider class ına o verileri dönecek bir yapı yapmaya çalıştım.
class PetlebiProductInfoSpider(scrapy.Spider):
   
   name = "petlebiProductInfoSpider"
   start_urls = ["https://www.petlebi.com/cok-satanlar"] #?

   #def parse(self, response):
      