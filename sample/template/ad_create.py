# -*- coding: utf-8 -*-
import requests

def get_access_token_from_redis():
    #TODO 从 redis 中获取 access token
    return ""

def get_ad_create(params_list):    
    url = "https://ad.toutiao.com/open_api/2/ad/create/"    
    for idx, params in enumerate(params_list):    
        headers = {"Access-Token": get_access_token_from_redis()}    
        rsp = requests.post(url, json=params, headers=headers)    
        rsp_data = rsp.json()    
        yield "第%d次请求 => %s"%(idx+1, rsp_data)

if __name__ == "__main__":

    data = []

    data.append({
        "advertiser_id": 0,
        "campaign_id": 0,
        "budget_mode": "BUDGET_MODE_DAY",
        "budget": 1234,
        "name": "ad_create",
        "download_url":"xxx",
        "schedule_type": "SCHEDULE_START_END",
        "flow_control_mode": "FLOW_CONTROL_MODE_FAST",
        "start_time":"2017-04-27 00:00",
        "end_time":"2017-04-29 23:59",
        "bid":10,
        "app_type":"APP_ANDROID",
        "package":"info.pkg",
        "pricing": "PRICING_CPM",
        "gender":"GENDER_FEMALE",
        "age":["AGE_BETWEEN_18_23","AGE_ABOVE_50"],
        "ac":"WIFI",
        "android_osv":"4.1",
        "platform":["ANDROID","IOS"],
        "carrier":["UNICOM"],
    })

    req_iter = get_ad_create(data)

    for req in req_iter:
        print(req)
