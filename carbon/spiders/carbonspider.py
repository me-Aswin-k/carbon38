import scrapy

class CarbonSpider(scrapy.Spider):

    name = "carbonspider"

    start_urls = ['https://www.carbon38.com/shop-all-activewear/tops']

    def parse(self,response):

        for links in response.css('a.ProductItem__ImageWrapper::attr(href)'):

            yield response.follow(links.get(), callback=self.parse_products)
            

        next_page = response.css('a.Pagination__NavItem[rel="next"]::attr(href)').get()
        
        if next_page:
            
            yield response.follow(next_page, callback=self.parse)

   

    def parse_products(self,response):

        yield{
            
             "product_title" : response.css('h1.ProductMeta__Title.Heading.u-h3::text').get(),

             "brand_name" : response.css('h2.ProductMeta__Vendor.Heading.u-h1 a::text').get(),

             "product_price" : response.css('span.ProductMeta__Price.Price::text').get(),

             "product_color" : response.css('span.ProductForm__SelectedValue::text').get(),

            "sizes" : response.css('ul.SizeSwatchList li.HorizontalList__Item label.SizeSwatch::text').getall(),

             "image_url" : response.css('div.AspectRatio img::attr(src)').get(),

             "alt_text" : response.css('div.AspectRatio img::attr(alt)').get(),

             "product_description" : response.css('div.Faq__AnswerWrapper div.Faq__Answer p::text').get(),

             "key_features" : response.css('div.Faq__AnswerWrapper div.Faq__Answer div.metaobject-entry div.metaobject-content::text').getall(),

             "fabric_and_care" : response.css('div.Faq__Answer.Rte span.metafield-multi_line_text_field::text').get(),

             "fit_info" : response.css('div.Faq__Answer.Rte p::text').get(),

        } 



