import scrapy
import re
from ..items import WeatherItem


class WeatherSpiderSpider(scrapy.Spider):
    name = "weather"
    allowed_domains = ["weather.com"]

    def start_requests(self):
        # Weather.com URL for Chennai's weather
        urls = [
            "https://weather.com/en-IN/weather/today/l/2a6f815c8301e1a4200ee16844ffd240e22ebd00d94220145c68dfc898f32e8c"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_url)

    def parse_url(self, response):
        # Extracting city, temperature, air quality and condition from the response using XPath
        city = response.xpath('//h1[contains(@class,"location")]/text()').get()
        temp = response.xpath('//span[@data-testid="TemperatureValue"]/text()').get()
        air_quality = response.xpath('//span[@data-testid="AirQualityCategory"]/text()').get()
        cond = response.xpath('//div[@data-testid="wxPhrase"]/text()').get()

        temp = re.match(r"(\d+)", temp).group(1) + " C"  # Removing the degree symbol and adding C
        city = re.match(r"^(.*)(?: Weather)", city).group(1)  # Removing 'Weather' from location

        # Yielding the extracted data as Item object. You may also extract as Dictionary
        item = WeatherItem()
        item["city"] = city
        item["temp"] = temp
        item["air_quality"] = air_quality
        item["cond"] = cond
        yield item