"""
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


if __name__ == '__main__':
    reverGeo_gaode(province_str="BeiJing")
