"""
读取数据库（暂时是excel）并统计省份->国家信息
"""
# 导入requests包
import json

import requests
from countryinfo import CountryInfo

# 替换为您的 ArcGIS REST API 地址
geocode_url = "https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/findAddressCandidates"
reverse_geocode_url = "https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/reverseGeocode"

# 获得国家之间的映射
with open("./static/resources/word.json", 'r', encoding='utf-8') as file:
    # 路径和启动文件所在有关，所以这里是./而不是../
    countryMap = json.loads(file.read())
    en2chn = countryMap['namemap']


def geocode(location):
    params = {
        "SingleLine": location,
        "outFields": "Country",
        "f": "json"
    }
    response = requests.get(geocode_url, params=params).json()

    if "candidates" in response and len(response["candidates"]) > 0:
        predict_ = response["candidates"][0]
        country = predict_["attributes"]["Country"]
        location_ = (predict_['location']['x'], predict_['location']['y'])
        return country, location_

    return None


def abbrev2name(country_code):
    import pycountry
    try:
        country = pycountry.countries.get(alpha_2=country_code)
        if country:
            country_name = country.name
            print(f"{country_code}: {country_name}")
            return country_name
        else:
            return "找不到该国家缩写的全称。"
    except Exception as e:
        return str(e)


# 根据国家缩写获取国家全称
def get_country_name(country_code):
    try:
        country = CountryInfo(country_code)
        country_name = country.info()['name']
        return country_name
    except Exception as e:
        return "找不到该国家缩写的全称。"


if __name__ == '__main__':
    location = "مصر"
    country_, location_ = geocode(location)
    if country_:
        print(f"The country of {location} is {country_}.")
        print(f"The location of {location} is {location_}.")
    else:
        print(f"Could not find the country for {location}.")

    # 测试获取国家缩写对应的全称
    country_code = 'cn'
    country_name = get_country_name(country_code)
    print(f"{country_code}: {country_name}: {en2chn.get(country_name)}")
