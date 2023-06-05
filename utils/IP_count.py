"""
读取数据库（暂时是excel）并统计省份->国家信息
"""
# 导入requests包
import requests

# 替换为您的 ArcGIS REST API 地址
geocode_url = "https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/findAddressCandidates"
reverse_geocode_url = "https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/reverseGeocode"


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


if __name__ == '__main__':
    location = "مصر"
    country_, location_ = geocode(location)
    if country_:
        print(f"The country of {location} is {country_}.")
        print(f"The location of {location} is {location_}.")
    else:
        print(f"Could not find the country for {location}.")
