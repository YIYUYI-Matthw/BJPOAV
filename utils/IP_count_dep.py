"""
该文件已被弃用
读取数据库（暂时是excel）并统计省份->国家信息
"""
import openpyxl
import pycountry
from geopy.geocoders import Nominatim
# 导入requests包
import requests


def _getLocationByProvince(province_str):
    geolocator = Nominatim(user_agent="my-app")

    location = geolocator.geocode(province_str)

    if location:
        latitude = location.latitude
        longitude = location.longitude
        print(province_str + f"的经纬度坐标为: ({latitude}, {longitude})")
        return location
    else:
        print("无法找到北京的经纬度坐标")
        return None


def getCountryByProvince_dep(province_str=""):
    location = _getLocationByProvince(province_str)
    if location is None:
        print("无法找到对应国家的信息")
        return None
    country = pycountry.countries.search(latitude=location.latitude, longitude=location.longitude)

    if country:
        country_name = country[0].name
        print(f"北京所在的国家是: {country_name}")
        return country_name
    else:
        print("无法找到北京所在的国家")
        return None


def reverGeo_gaode(province_str=""):
    url = "https://restapi.amap.com/v3/geocode/geo"
    parameters = {"address": province_str,
                  "output": "JSON",
                  "key": "c93f574233412333a6b3779b2fe789e7"}
    res = eval(requests.get(url=url, params=parameters).text)
    if res.get("status") is "0":
        print("查询无果")
        return None
    print(res.get("geocodes")[0])
    print(res.get("geocodes")[0].get("country"))


def getProvinces():
    # TODO：待续：等找到合适的SDK再来做
    origin_book_path = "../static/resources/docs/userInfo.xlsx"
    work_book = openpyxl.load_workbook(origin_book_path)
    sheet_instance = work_book["Sheet1"]
    comment_idxes, comments = sheet_instance['C']
    pass


def gaode_remap(location):
    # 高德地图开发者密钥
    api_key = 'c93f574233412333a6b3779b2fe789e7'
    # 地理编码 API
    geocode_url = f"https://restapi.amap.com/v3/geocode/geo?address={location}&key={api_key}"
    response = requests.get(geocode_url).json()

    if response["status"] == "1" and response["count"] != "0":
        # 提取经纬度坐标
        coordinates = response["geocodes"][0]["location"]

        # 逆地理编码 API（添加 extensions 参数）
        regeocode_url = f"https://restapi.amap.com/v3/geocode/regeo?location={coordinates}&key={api_key}&extensions=all"
        reponse = requests.get(regeocode_url).json()

        if reponse["status"] == "1":
            # 提取国家信息
            country = reponse["regeocode"]["addressComponent"]["country"]
            return country

    return None


def baidu_remap(address):
    ak = "TzBKUpn0kBvyScbFFvhSWbRSXCInHWaG"
    # 解析
    url_name2location = "https://api.map.baidu.com/geocoding/v3"
    # 逆地理编码
    url_regeo = "https://api.map.baidu.com/reverse_geocoding/v3"
    # 地理解析
    params_name2location = {
        "address": address,
        "output": "json",
        "ak": ak,
    }
    response = requests.get(url=url_name2location, params=params_name2location).json()
    location = response['result']['location']
    print("坐标：" + str(location))
    # 逆地理编码
    re_params = {
        "ak": ak,
        "output": "json",
        "coordtype": "wgs84ll",
        "extensions_poi": "0",
        # "location": "31.225696563611,121.49884033194",
        "location": str(location['lat']) + "," + str(location['lng']),
    }
    response = requests.get(url=url_regeo, params=re_params).json()
    if response:
        print("结果：", end='')
        print(response)
        return response

        # if response["status"] == 0 and response["result"]:
        # 提取经纬度坐标
        # coordinates = f"{response['result']['location']['lng']},{response['result']['location']['lat']}"

        """
        regeocode_url = f"http://api.map.baidu.com/reverse_geocoding/v3/?location={coordinates}&output=json&ak={ak}"
        response = requests.get(regeocode_url).json()

        if response["status"] == 0 and response["result"]:
            # 提取国家信息
            country = response["result"]["addressComponent"]["country"]
            return country

    return None
        """


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
        location = (predict_['location']['x'], predict_['location']['y'])
        return country, location

    return None


def reverse_geocode(lat, lon):
    params = {
        "location": f"{lon},{lat}",
        "outFields": "Country",
        "f": "json"
    }
    response = requests.get(reverse_geocode_url, params=params).json()

    if "address" in response and "CountryCode" in response["address"]:
        country = response["address"]["CountryCode"]
        return country

    return None


if __name__ == '__main__':

    # 示例用法
    location = "北京"
    country_, location_ = geocode(location)
    if country_:
        print(f"The country of {location} is {country_}.")
        print(f"The location of {location} is {location_}.")
    else:
        print(f"Could not find the country for {location}.")

    """
    lat = 40.7128
    lon = -74.0060
    country = reverse_geocode(lat, lon)
    if country:
        print(f"The country at coordinates ({lat}, {lon}) is {country}.")
    else:
        print(f"Could not find the country at coordinates ({lat}, {lon}).")
    """
    """
    location = "纽约"
    response = baidu_remap(location)
    if response:
        print(f"The country of {location} is {response['result']['addressComponent']['country']}.")
    else:
        print(f"Could not find the country for {location}.")
    """

"""
{'status': 0, 'result': {'location': {'lng': 116.4260559234063, 'lat': 39.91850710095061},
                            'formatted_address': '北京市东城区外交部街甲46-6号', 'edz': {'name': ''}, 'business': '东单,建国门,王府井',
                            'addressComponent': {'country': '中国', 'country_code': 0, 'country_code_iso': 'CHN',
                                                 'country_code_iso2': 'CN', 'province': '北京市', 'city': '北京市',
                                                 'city_level': 2, 'district': '东城区', 'town': '建国门街道',
                                                 'town_code': '110101008', 'distance': '32', 'direction': '附近',
                                                 'adcode': '110101', 'street': '外交部街', 'street_number': '甲46-6号'},
                            'pois': [], 'roads': [], 'poiRegions': [], 'sematic_description': '',
                            'formatted_address_poi': '', 'cityCode': 131}}
"""
