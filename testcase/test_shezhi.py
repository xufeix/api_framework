# /usr/bin/env python3.8
# coding:utf-8

"""
@file: test_shezhi.py
@time: 2021/5/12 4:01 下午
@author:XF
"""
import unittest
from lib.public import postRequest


class TestDemo(unittest.TestCase):
    def test_shezhi(self):
        #  构造参数
        param = {
            "list": [{
                "action": "open",
                "otype": "app",
                "src": "app",
                "cur_page": "other",
                "from_page": "other",
                "data": {
                    "dur": 22410,
                    "st": 1620801857628,
                    "use_mode": "hot",
                    "c_ver": "1.1.0.3",
                    "source": "icon",
                    "et": 1620801880038,
                    "log_id": "1620801880039_4"
                }
            }],
            "h_av": "1.1.0.3",
            "h_dt": 0,
            "h_mf": "OPPO",
            "h_ch": "google",
            "h_model": "CPH1923",
            "h_nt": 1,
            "h_os": 28,
            "h_ts": 1620801882662,
            "h_app": "maga",
            "h_pkg": "us",
            "h_lang": "en",
            "gps_adid": "08986914-6eed-45ba-8e4a-be94e0e98708",
            "h_did": "60811c09dfe1fd5f75ec6557",
            "h_aid": "6081158b8e218b641a1d372e",
            "token": "T4K6N1uBL0OIEVYOvq6Omskyx6NxFjyhZHuVwor2EjpCm1Aya1q1gBoRVDnUJRVT3Wvthu-zdeellmGmqUKull6Jq5Ng0dDmHEJ_FBQ6iTgnumJPyHABAPXvBkCbO5yGS3D0r",
            "h_m": 503540135
        }
        #  发送点击设置的请求，并获取返回
        req = postRequest('/stat/action', param)
        self.assertEqual(req.json()['ret'], 1)

