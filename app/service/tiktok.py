import requests
from bs4 import BeautifulSoup
import json

class Tiktok():
    def following(self, username, limit):
        print(limit)
        cookies = {
            'tt_chain_token': 'RsODu7vcrXyCun9viGKJyw==',
            'tiktok_webapp_theme': 'light',
            'passport_csrf_token': '5902da3cb4ed40b87d520405ffed2261',
            'passport_csrf_token_default': '5902da3cb4ed40b87d520405ffed2261',
            '_ttp': '2bkzLzELiwAXubktic8G817GGyR',
            'd_ticket': 'dbeb65d8b0128d6aee8d9fb43240e81c1e540',
            'multi_sids': '6749780217957532673%3A6574fbb17a1fcd9c7dfa2df381f83736',
            'cmpl_token': 'AgQQAPPdF-RO0o2S5_8jY504_9q4vEdZv4ArYNFfVw',
            'passport_auth_status': '554847a7c512b04417f4ee904e3a385b%2C',
            'passport_auth_status_ss': '554847a7c512b04417f4ee904e3a385b%2C',
            'sid_guard': '6574fbb17a1fcd9c7dfa2df381f83736%7C1709623899%7C15552000%7CSun%2C+01-Sep-2024+07%3A31%3A39+GMT',
            'uid_tt': 'e22de1c80eb4388c48031ad7f387c3177a0b497e257faddcf41580cba8791073',
            'uid_tt_ss': 'e22de1c80eb4388c48031ad7f387c3177a0b497e257faddcf41580cba8791073',
            'sid_tt': '6574fbb17a1fcd9c7dfa2df381f83736',
            'sessionid': '6574fbb17a1fcd9c7dfa2df381f83736',
            'sessionid_ss': '6574fbb17a1fcd9c7dfa2df381f83736',
            'sid_ucp_v1': '1.0.0-KDYwOGM2NTZmYTI2ZDY3NjUyZWQ5NWQwZTBlMTFhZDY2ODU2N2RmYTUKIAiBiMXaiquC1l0Q25SbrwYYswsgDDCEk7DtBTgCQPEHEAMaBm1hbGl2YSIgNjU3NGZiYjE3YTFmY2Q5YzdkZmEyZGYzODFmODM3MzY',
            'ssid_ucp_v1': '1.0.0-KDYwOGM2NTZmYTI2ZDY3NjUyZWQ5NWQwZTBlMTFhZDY2ODU2N2RmYTUKIAiBiMXaiquC1l0Q25SbrwYYswsgDDCEk7DtBTgCQPEHEAMaBm1hbGl2YSIgNjU3NGZiYjE3YTFmY2Q5YzdkZmEyZGYzODFmODM3MzY',
            'store-idc': 'maliva',
            'store-country-code': 'id',
            'store-country-code-src': 'uid',
            'tt-target-idc': 'alisg',
            'tt-target-idc-sign': 'NxBeUNWDj20Xon206PhslbBOhRNyp9D3NLN6HS9leq2nBJatkqIW-eWyknQCuWdkfh38iaKwunxSjBvWEoIN5hn_wiMVpjEcMENxFa4U-UysRbbDSiXdpQccbqEpxDUeO4i6bQm9I5Uj1T0GYMoM36FrV7NMKB-c6sHotPSjszstb0qKXiftL25xJdo06roMaGBe-mZwyh5M2fvr_5eCLu9xXx0b6CxWIauOtKZTaDWVHzIGmOUNteIy643X45x8_bo9v2M0I4_GMfisP7AA2hgT9dT-03tw7oO30v14IVoDQTYpnQ1gms9gOUCgnEpxsZGsoxuQ_utTf_3cosHqrwFxauQW15MBovW690nkjI7cJ2BrgJUeta6ixBdLBAfHkFhDDS1NKIH2x5iBN2xOfY11NFXtCLb3F7Eeznvq_iTrHiE0Z1DTNX5PGVLWc_XFh1kMsbfMo_-te9bQbRvohj9KAimpbNpgT2Fii19enaX_ZvnZQUp5hq78pPnDT8Wb',
            'last_login_method': 'sms_verification',
            'perf_feed_cache': '{%22expireTimestamp%22:1709830800000%2C%22itemIds%22:[%227313519542037171462%22%2C%227334214300615167265%22%2C%227333544490633825541%22]}',
            'tt_csrf_token': 'hm7hpCWb-RloDc24XsRfRmr_zHkuISHJ-cLw',
            'ak_bmsc': 'D9553C11EED7802091BA115772375955~000000000000000000000000000000~YAAQQ+nOFwYhJf+NAQAAAOJoFxf/L8tbHRllAbHU/2uWrBfyloZnXnuJmf+0Qq0Q7klb+be9+amgrmQMn8YgSACOvRoJekrgahvstgrjLXN4cDqsThD0vfwL0l4vlnI3CtejJ/WCyE7qjpcDOfWG8zKrUos5a/AYT8XHweYSsii2NUPh3XGdGpdqUPWYSUNLX5WQYJ6h7MyYYoXLIS5qSgtts5wBjJln9igkQVdxPz8h4O6EXvq2tG2VmAKOLNqtJJNSkPkLkP1ORA6ykUxLtere8Vai/XMxt91lMVJF9LSYdYggIBW+fmQDT0jMCYLwtc+IETGqFf1i9hlFZckB0Y+i/aGK2o7xe6ZStxUdNcO/N2zsQQE2QCsAF5HFDCjJ+ja4qoJmbogIiR9y',
            'passport_fe_beating_status': 'true',
            'ttwid': '1%7CSs-WSXwK_P549vAAUSfYFc_KGNjCrwrNZgUwp62lKwI%7C1709789848%7C1cc9757557b3caef334807200b288bf87e0eb8a139fd640f7574c704a494d3ef',
            'bm_sv': 'AEBF757BEF7A4843CC4AAB240A2BD496~YAAQZ+nOF99KbvmNAQAA4u9qFxeo+BPyNXRXncfu6DE7tgUXZgf89Vtisen+MNxp3yv5fFZaJiZMgguwVnhhGjAUJPkUmNW4acvz1sZEhz9J7QHHqP3tSlJ0PmjW6icDdAJxu/f64XgdDlBRZFAoziI879mVTvUCZ9f8o8lehJB91E4qT5w0ObKqML7jtMmDaZW9qtBXNoI1faBTBwJH1f9oFpmNLF01LYp/sX1zQn6oCw5XPysJQC/kUU7NjTyp~1',
            'odin_tt': '216864a36a1f6f530f30b827bf1835b2c43d9835f871a40fd6a31cc886abff7d1b540016e19668d15c505488bb28eefe5f9cbd6491198bbaa2774f72bfd890bd',
            'msToken': 'dpUxs1zNqibwOftsKnG9i2PfJX8LwhiIuDsokQoZIVa12KamQ-6XKITJV6neMhNpsrcXoz29A31KBUMrZ0GiZbUCcP8JvSybNvGTLf4pTmpMXgIS3vhcib-TtE1QzRBkeTF8qb2_r5iNkVT5',
            'msToken': 'dpUxs1zNqibwOftsKnG9i2PfJX8LwhiIuDsokQoZIVa12KamQ-6XKITJV6neMhNpsrcXoz29A31KBUMrZ0GiZbUCcP8JvSybNvGTLf4pTmpMXgIS3vhcib-TtE1QzRBkeTF8qb2_r5iNkVT5',
        }

        headers = {
            'authority': 'www.tiktok.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            # 'cookie': 'tt_chain_token=RsODu7vcrXyCun9viGKJyw==; tiktok_webapp_theme=light; passport_csrf_token=5902da3cb4ed40b87d520405ffed2261; passport_csrf_token_default=5902da3cb4ed40b87d520405ffed2261; _ttp=2bkzLzELiwAXubktic8G817GGyR; d_ticket=dbeb65d8b0128d6aee8d9fb43240e81c1e540; multi_sids=6749780217957532673%3A6574fbb17a1fcd9c7dfa2df381f83736; cmpl_token=AgQQAPPdF-RO0o2S5_8jY504_9q4vEdZv4ArYNFfVw; passport_auth_status=554847a7c512b04417f4ee904e3a385b%2C; passport_auth_status_ss=554847a7c512b04417f4ee904e3a385b%2C; sid_guard=6574fbb17a1fcd9c7dfa2df381f83736%7C1709623899%7C15552000%7CSun%2C+01-Sep-2024+07%3A31%3A39+GMT; uid_tt=e22de1c80eb4388c48031ad7f387c3177a0b497e257faddcf41580cba8791073; uid_tt_ss=e22de1c80eb4388c48031ad7f387c3177a0b497e257faddcf41580cba8791073; sid_tt=6574fbb17a1fcd9c7dfa2df381f83736; sessionid=6574fbb17a1fcd9c7dfa2df381f83736; sessionid_ss=6574fbb17a1fcd9c7dfa2df381f83736; sid_ucp_v1=1.0.0-KDYwOGM2NTZmYTI2ZDY3NjUyZWQ5NWQwZTBlMTFhZDY2ODU2N2RmYTUKIAiBiMXaiquC1l0Q25SbrwYYswsgDDCEk7DtBTgCQPEHEAMaBm1hbGl2YSIgNjU3NGZiYjE3YTFmY2Q5YzdkZmEyZGYzODFmODM3MzY; ssid_ucp_v1=1.0.0-KDYwOGM2NTZmYTI2ZDY3NjUyZWQ5NWQwZTBlMTFhZDY2ODU2N2RmYTUKIAiBiMXaiquC1l0Q25SbrwYYswsgDDCEk7DtBTgCQPEHEAMaBm1hbGl2YSIgNjU3NGZiYjE3YTFmY2Q5YzdkZmEyZGYzODFmODM3MzY; store-idc=maliva; store-country-code=id; store-country-code-src=uid; tt-target-idc=alisg; tt-target-idc-sign=NxBeUNWDj20Xon206PhslbBOhRNyp9D3NLN6HS9leq2nBJatkqIW-eWyknQCuWdkfh38iaKwunxSjBvWEoIN5hn_wiMVpjEcMENxFa4U-UysRbbDSiXdpQccbqEpxDUeO4i6bQm9I5Uj1T0GYMoM36FrV7NMKB-c6sHotPSjszstb0qKXiftL25xJdo06roMaGBe-mZwyh5M2fvr_5eCLu9xXx0b6CxWIauOtKZTaDWVHzIGmOUNteIy643X45x8_bo9v2M0I4_GMfisP7AA2hgT9dT-03tw7oO30v14IVoDQTYpnQ1gms9gOUCgnEpxsZGsoxuQ_utTf_3cosHqrwFxauQW15MBovW690nkjI7cJ2BrgJUeta6ixBdLBAfHkFhDDS1NKIH2x5iBN2xOfY11NFXtCLb3F7Eeznvq_iTrHiE0Z1DTNX5PGVLWc_XFh1kMsbfMo_-te9bQbRvohj9KAimpbNpgT2Fii19enaX_ZvnZQUp5hq78pPnDT8Wb; last_login_method=sms_verification; perf_feed_cache={%22expireTimestamp%22:1709830800000%2C%22itemIds%22:[%227313519542037171462%22%2C%227334214300615167265%22%2C%227333544490633825541%22]}; tt_csrf_token=hm7hpCWb-RloDc24XsRfRmr_zHkuISHJ-cLw; ak_bmsc=D9553C11EED7802091BA115772375955~000000000000000000000000000000~YAAQQ+nOFwYhJf+NAQAAAOJoFxf/L8tbHRllAbHU/2uWrBfyloZnXnuJmf+0Qq0Q7klb+be9+amgrmQMn8YgSACOvRoJekrgahvstgrjLXN4cDqsThD0vfwL0l4vlnI3CtejJ/WCyE7qjpcDOfWG8zKrUos5a/AYT8XHweYSsii2NUPh3XGdGpdqUPWYSUNLX5WQYJ6h7MyYYoXLIS5qSgtts5wBjJln9igkQVdxPz8h4O6EXvq2tG2VmAKOLNqtJJNSkPkLkP1ORA6ykUxLtere8Vai/XMxt91lMVJF9LSYdYggIBW+fmQDT0jMCYLwtc+IETGqFf1i9hlFZckB0Y+i/aGK2o7xe6ZStxUdNcO/N2zsQQE2QCsAF5HFDCjJ+ja4qoJmbogIiR9y; passport_fe_beating_status=true; ttwid=1%7CSs-WSXwK_P549vAAUSfYFc_KGNjCrwrNZgUwp62lKwI%7C1709789848%7C1cc9757557b3caef334807200b288bf87e0eb8a139fd640f7574c704a494d3ef; bm_sv=AEBF757BEF7A4843CC4AAB240A2BD496~YAAQZ+nOF99KbvmNAQAA4u9qFxeo+BPyNXRXncfu6DE7tgUXZgf89Vtisen+MNxp3yv5fFZaJiZMgguwVnhhGjAUJPkUmNW4acvz1sZEhz9J7QHHqP3tSlJ0PmjW6icDdAJxu/f64XgdDlBRZFAoziI879mVTvUCZ9f8o8lehJB91E4qT5w0ObKqML7jtMmDaZW9qtBXNoI1faBTBwJH1f9oFpmNLF01LYp/sX1zQn6oCw5XPysJQC/kUU7NjTyp~1; odin_tt=216864a36a1f6f530f30b827bf1835b2c43d9835f871a40fd6a31cc886abff7d1b540016e19668d15c505488bb28eefe5f9cbd6491198bbaa2774f72bfd890bd; msToken=dpUxs1zNqibwOftsKnG9i2PfJX8LwhiIuDsokQoZIVa12KamQ-6XKITJV6neMhNpsrcXoz29A31KBUMrZ0GiZbUCcP8JvSybNvGTLf4pTmpMXgIS3vhcib-TtE1QzRBkeTF8qb2_r5iNkVT5; msToken=dpUxs1zNqibwOftsKnG9i2PfJX8LwhiIuDsokQoZIVa12KamQ-6XKITJV6neMhNpsrcXoz29A31KBUMrZ0GiZbUCcP8JvSybNvGTLf4pTmpMXgIS3vhcib-TtE1QzRBkeTF8qb2_r5iNkVT5',
            'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        }

        response = requests.get(f'https://www.tiktok.com/@{username}', cookies=cookies, headers=headers)

        response_text: str = response.text

        from bs4 import BeautifulSoup
        import json

        soup = BeautifulSoup(response_text, 'html.parser')

        script_tag = soup.find('script', id='__UNIVERSAL_DATA_FOR_REHYDRATION__', type='application/json')

        if script_tag:
            json_content = script_tag.string
            parsed_json = json.loads(json_content)

            secUid_value = parsed_json['__DEFAULT_SCOPE__']['webapp.user-detail']
            uid = secUid_value['userInfo']['user']['secUid']

            param = {
                "WebIdLastTime": "1706762654",
                "aid": "1988",
                "app_language": "en",
                "app_name": "tiktok_web",
                "browser_language": "en-US",
                "browser_name": "Mozilla",
                "browser_online": "true",
                "browser_platform": "Linux%20x86_64",
                "browser_version": "5.0%20%28X11%29",
                "channel": "tiktok_web",
                "cookie_enabled": "true",
                "count": "30",
                "device_id": "7330489720444978690",
                "device_platform": "web_pc",
                "focus_state": "true",
                "from_page": "user",
                "history_len": "1",
                "is_fullscreen": "false",
                "is_page_visible": "true",
                "maxCursor": "0",
                "minCursor": "0",
                "os": "linux",
                "priority_region": "ID",
                "referer": "",
                "region": "ID",
                "scene": "21",
                "screen_height": "720",
                "screen_width": "1280",
                "secUid": uid,
                "tz_name": "Asia%2FJakarta",
                "verifyFp": "verify_lte1wpzi_rOiJWMcF_FE5P_4tuW_87AL_uH3N0JBj3071",
                "webcast_language": "en",
                "msToken": "gIj__rxcvG8RGsjizzjMZEnqB1kXojHyqvGB-_T8pYjyEbnioz-R-TlTFSl301h8ieKVEx9NWs3GZT0EHhmQWc7gBcEuPtz_etgB0jhdPR8CIDcuVw_8CDLFLCjwOJDebGk",
                "X-Bogus": "DFSzsIVYhyxANciNtbx6mt9WcBnM",
                "_signature": "_02B4Z6wo00001nT76UgAAIDCdPvpS66Gwnp0-e3AAPjm70"
            }

            header = {
                "content-type": "application/json; charset=utf-8",
                "x-tt-logid": "202403071002595A63EB806CF0A21BCF2F",
                "tt_stable": "1",
                "bd-tt-error-code": "0",
                "strict-transport-security": "max-age=31536000; includeSubDomains",
                "x-tt-trace-host": "0163e01e647099602d6aefb25f49abfe37c3616b1d26077a93bcae613b96d513b25b98e4f12d48d5b724d6a687f65622244cc482d66e4ee84746f4df8540903d84bc09522443688ec6f386d393e32772e5c06f3e39f0bbdcc9bbbb9b71f5573c68",
                "x-tt-trace-id": "00-2403071002595A63EB806CF0A21BCF2F-5B4B369261427FD7-00",
                "server": "TLB",
                "content-encoding": "br",
                "expires": "Thu, 07 Mar 2024 10:03:00 GMT",
                "cache-control": "max-age=0, no-cache, no-store",
                "pragma": "no-cache",
                "date": "Thu, 07 Mar 2024 10:03:00 GMT",
                "x-cache": "TCP_MISS from a23-206-233-82.deploy.akamaitechnologies.com (AkamaiGHost/11.4.2.2-54704533) (-)",
                "x-tt-trace-tag": "id=16;cdn-cache=miss;type=dyn",
                "server-timing": "inner; dur=163, cdn-cache; desc=MISS, edge; dur=2, origin; dur=181",
                "x-origin-response-time": "183, 23.206.233.82",
                "x-akamai-request-id": "3972254",
                "x-firefox-spdy": "h2"
            }

            cookies = {
                'tt_chain_token': 'RsODu7vcrXyCun9viGKJyw==',
                'tiktok_webapp_theme': 'light',
                'passport_csrf_token': '5902da3cb4ed40b87d520405ffed2261',
                'passport_csrf_token_default': '5902da3cb4ed40b87d520405ffed2261',
                '_ttp': '2bkzLzELiwAXubktic8G817GGyR',
                'tt_csrf_token': 'Sx2ron5x-Hi_icZXXNxRiQLj6Vpn_WswhaX8',
                'ak_bmsc': '923C1B7578FF5B211446C491BEAFE787~000000000000000000000000000000~YAAQU+nOF3z8ogKOAQAA+NmFDRc77ZYZ4bNe/la9dXlU7g1d9PU1r2MNVhq8pKRYMNZa7GSsFxxuhzsYJYxkB5+qmG568QLhhkpqgvSfCpc0PTblqGUQVT566EAO44vCzdmROG5xnflsKh1pg1tIXNsD/GIo67wqMp7sRoslJ2l0pe5fXU4HBAjRPqXM0+9LSYHNZH5PPexKcmNQRUKKPS799UaTD9zKT0evzdSLSaI8i4hsexF6MtP3luni8T8Mij5J++d76wgMSuB5ZYMjH9ZCuVuZDmeoTWomIokZMDqxVTOostnelVG6YmIJote4lS8fIwdBW5tJ4D7enNijyvZAP+oRmACxWYUtXyQOZj5xFCuyKm5mByT9Q9SEQU9crhmeVWpYqg8zcjik',
                's_v_web_id': 'verify_lte1wpzi_rOiJWMcF_FE5P_4tuW_87AL_uH3N0JBj3071',
                'd_ticket': 'dbeb65d8b0128d6aee8d9fb43240e81c1e540',
                'multi_sids': '6749780217957532673%3A6574fbb17a1fcd9c7dfa2df381f83736',
                'cmpl_token': 'AgQQAPPdF-RO0o2S5_8jY504_9q4vEdZv4ArYNFfVw',
                'passport_auth_status': '554847a7c512b04417f4ee904e3a385b%2C',
                'passport_auth_status_ss': '554847a7c512b04417f4ee904e3a385b%2C',
                'sid_guard': '6574fbb17a1fcd9c7dfa2df381f83736%7C1709623899%7C15552000%7CSun%2C+01-Sep-2024+07%3A31%3A39+GMT',
                'uid_tt': 'e22de1c80eb4388c48031ad7f387c3177a0b497e257faddcf41580cba8791073',
                'uid_tt_ss': 'e22de1c80eb4388c48031ad7f387c3177a0b497e257faddcf41580cba8791073',
                'sid_tt': '6574fbb17a1fcd9c7dfa2df381f83736',
                'sessionid': '6574fbb17a1fcd9c7dfa2df381f83736',
                'sessionid_ss': '6574fbb17a1fcd9c7dfa2df381f83736',
                'sid_ucp_v1': '1.0.0-KDYwOGM2NTZmYTI2ZDY3NjUyZWQ5NWQwZTBlMTFhZDY2ODU2N2RmYTUKIAiBiMXaiquC1l0Q25SbrwYYswsgDDCEk7DtBTgCQPEHEAMaBm1hbGl2YSIgNjU3NGZiYjE3YTFmY2Q5YzdkZmEyZGYzODFmODM3MzY',
                'ssid_ucp_v1': '1.0.0-KDYwOGM2NTZmYTI2ZDY3NjUyZWQ5NWQwZTBlMTFhZDY2ODU2N2RmYTUKIAiBiMXaiquC1l0Q25SbrwYYswsgDDCEk7DtBTgCQPEHEAMaBm1hbGl2YSIgNjU3NGZiYjE3YTFmY2Q5YzdkZmEyZGYzODFmODM3MzY',
                'store-idc': 'maliva',
                'store-country-code': 'id',
                'store-country-code-src': 'uid',
                'tt-target-idc': 'alisg',
                'tt-target-idc-sign': 'NxBeUNWDj20Xon206PhslbBOhRNyp9D3NLN6HS9leq2nBJatkqIW-eWyknQCuWdkfh38iaKwunxSjBvWEoIN5hn_wiMVpjEcMENxFa4U-UysRbbDSiXdpQccbqEpxDUeO4i6bQm9I5Uj1T0GYMoM36FrV7NMKB-c6sHotPSjszstb0qKXiftL25xJdo06roMaGBe-mZwyh5M2fvr_5eCLu9xXx0b6CxWIauOtKZTaDWVHzIGmOUNteIy643X45x8_bo9v2M0I4_GMfisP7AA2hgT9dT-03tw7oO30v14IVoDQTYpnQ1gms9gOUCgnEpxsZGsoxuQ_utTf_3cosHqrwFxauQW15MBovW690nkjI7cJ2BrgJUeta6ixBdLBAfHkFhDDS1NKIH2x5iBN2xOfY11NFXtCLb3F7Eeznvq_iTrHiE0Z1DTNX5PGVLWc_XFh1kMsbfMo_-te9bQbRvohj9KAimpbNpgT2Fii19enaX_ZvnZQUp5hq78pPnDT8Wb',
                'last_login_method': 'sms_verification',
                'perf_feed_cache': '{%22expireTimestamp%22:1709794800000%2C%22itemIds%22:[%227340766826034433286%22%2C%227319250533057875232%22%2C%227310395793221930258%22]}',
                'msToken': 'UONXlKDIo3AcvpqhctGk8jl7wX0yvC7-CTfIItE6W4xFuRNiw-UlD7zRIVscwR-OGdOTqy_fr5QK6Y0LBcghhUNfvYI2HLVsjlTkQkvl-DRZ3B_u18ec0EyuTSe_wVPJNZ7al-44ZQmpQwda',
                'msToken': 'PF-_8NVAMOakAc_FXTYVpNlGbmgRVSQ-0OhwwB-xtsA5qScGIzZGpf762vhyd9HZworw392yBMTOiGUMOTJpvdgEd6fRq6gPQbUXq3HJC3ySCqi-NZck',
                'bm_sv': '89E14DC19B553326CED48BC00F8472DA~YAAQUunOF06LjgGOAQAA+aSWDRciUQIhdzII7/0Phw187WMuVErerFXv7rzqm/20fQlhkTgwci1uv3VkYL68l3VpO9UfIzB8E/dEY6cFenbqTp70BJy1MWu4zPZ0aMwXnXYbtnC/ov+BLXGGBxctQtfhkW0GNTAA0EM22SMeK75Y/EmKG07hFd6ZtmM4zyES9dvfD63vymCkCZqE+V5kJnNORssTLz6p1Q2wUe5vxwglFXE74160XqnpvujWq4Lv~1',
                'passport_fe_beating_status': 'true',
                'ttwid': '1%7CSs-WSXwK_P549vAAUSfYFc_KGNjCrwrNZgUwp62lKwI%7C1709624963%7Ca9a2bcaf8e81910c061bb7aebb1f20038e326d81efe2e4cade15dc4e89e11e40',
                'odin_tt': '372a293e9c4c551f96b373bf958d5d9fb13da559ae64ccef0341d5f28f0863baa40f7fc4539e003f914a5c146828c7e728645515244bd9d4856b53df6612279958a826eb4f07da9fad1bab0a72670b51',
            }


            users = []
            iteration_count = 0
            while True:
                response = requests.get('https://www.tiktok.com/api/user/list/', params=param, cookies=cookies,headers=header)
                json_data = response.json()
                if json_data['statusCode'] == 0:
                    max_cursor = json_data['maxCursor']
                    min_cursor = json_data['minCursor']
                    try:
                        userlist = json_data['userList']
                        for user in userlist:
                            userid = user['user']['uniqueId']
                            avatar_link = user['user']['avatarLarger']
                            id = user['user']['id']
                            nickname = user['user']['nickname']
                            userid = {
                                'id': id,
                                'userID': userid,
                                'nickname': nickname,
                                'avatar': avatar_link
                            }
                            users.append(userid)
                    except:
                        print('ok')

                    if max_cursor == -1 or min_cursor == -1 or iteration_count >= limit:
                        break
                    param['maxCursor'] = str(max_cursor)
                    param['minCursor'] = str(min_cursor)
                    iteration_count += 1
                if len(users) == 0:
                    users = 'This Account Private Following'
                    break


            return users

    def followers(self, username, limit):
        print(limit)
        cookies = {
            'tt_chain_token': 'RsODu7vcrXyCun9viGKJyw==',
            'tiktok_webapp_theme': 'light',
            'passport_csrf_token': '5902da3cb4ed40b87d520405ffed2261',
            'passport_csrf_token_default': '5902da3cb4ed40b87d520405ffed2261',
            '_ttp': '2bkzLzELiwAXubktic8G817GGyR',
            'd_ticket': 'dbeb65d8b0128d6aee8d9fb43240e81c1e540',
            'multi_sids': '6749780217957532673%3A6574fbb17a1fcd9c7dfa2df381f83736',
            'cmpl_token': 'AgQQAPPdF-RO0o2S5_8jY504_9q4vEdZv4ArYNFfVw',
            'passport_auth_status': '554847a7c512b04417f4ee904e3a385b%2C',
            'passport_auth_status_ss': '554847a7c512b04417f4ee904e3a385b%2C',
            'sid_guard': '6574fbb17a1fcd9c7dfa2df381f83736%7C1709623899%7C15552000%7CSun%2C+01-Sep-2024+07%3A31%3A39+GMT',
            'uid_tt': 'e22de1c80eb4388c48031ad7f387c3177a0b497e257faddcf41580cba8791073',
            'uid_tt_ss': 'e22de1c80eb4388c48031ad7f387c3177a0b497e257faddcf41580cba8791073',
            'sid_tt': '6574fbb17a1fcd9c7dfa2df381f83736',
            'sessionid': '6574fbb17a1fcd9c7dfa2df381f83736',
            'sessionid_ss': '6574fbb17a1fcd9c7dfa2df381f83736',
            'sid_ucp_v1': '1.0.0-KDYwOGM2NTZmYTI2ZDY3NjUyZWQ5NWQwZTBlMTFhZDY2ODU2N2RmYTUKIAiBiMXaiquC1l0Q25SbrwYYswsgDDCEk7DtBTgCQPEHEAMaBm1hbGl2YSIgNjU3NGZiYjE3YTFmY2Q5YzdkZmEyZGYzODFmODM3MzY',
            'ssid_ucp_v1': '1.0.0-KDYwOGM2NTZmYTI2ZDY3NjUyZWQ5NWQwZTBlMTFhZDY2ODU2N2RmYTUKIAiBiMXaiquC1l0Q25SbrwYYswsgDDCEk7DtBTgCQPEHEAMaBm1hbGl2YSIgNjU3NGZiYjE3YTFmY2Q5YzdkZmEyZGYzODFmODM3MzY',
            'store-idc': 'maliva',
            'store-country-code': 'id',
            'store-country-code-src': 'uid',
            'tt-target-idc': 'alisg',
            'tt-target-idc-sign': 'NxBeUNWDj20Xon206PhslbBOhRNyp9D3NLN6HS9leq2nBJatkqIW-eWyknQCuWdkfh38iaKwunxSjBvWEoIN5hn_wiMVpjEcMENxFa4U-UysRbbDSiXdpQccbqEpxDUeO4i6bQm9I5Uj1T0GYMoM36FrV7NMKB-c6sHotPSjszstb0qKXiftL25xJdo06roMaGBe-mZwyh5M2fvr_5eCLu9xXx0b6CxWIauOtKZTaDWVHzIGmOUNteIy643X45x8_bo9v2M0I4_GMfisP7AA2hgT9dT-03tw7oO30v14IVoDQTYpnQ1gms9gOUCgnEpxsZGsoxuQ_utTf_3cosHqrwFxauQW15MBovW690nkjI7cJ2BrgJUeta6ixBdLBAfHkFhDDS1NKIH2x5iBN2xOfY11NFXtCLb3F7Eeznvq_iTrHiE0Z1DTNX5PGVLWc_XFh1kMsbfMo_-te9bQbRvohj9KAimpbNpgT2Fii19enaX_ZvnZQUp5hq78pPnDT8Wb',
            'last_login_method': 'sms_verification',
            'perf_feed_cache': '{%22expireTimestamp%22:1709830800000%2C%22itemIds%22:[%227313519542037171462%22%2C%227334214300615167265%22%2C%227333544490633825541%22]}',
            'tt_csrf_token': 'hm7hpCWb-RloDc24XsRfRmr_zHkuISHJ-cLw',
            'ak_bmsc': 'D9553C11EED7802091BA115772375955~000000000000000000000000000000~YAAQQ+nOFwYhJf+NAQAAAOJoFxf/L8tbHRllAbHU/2uWrBfyloZnXnuJmf+0Qq0Q7klb+be9+amgrmQMn8YgSACOvRoJekrgahvstgrjLXN4cDqsThD0vfwL0l4vlnI3CtejJ/WCyE7qjpcDOfWG8zKrUos5a/AYT8XHweYSsii2NUPh3XGdGpdqUPWYSUNLX5WQYJ6h7MyYYoXLIS5qSgtts5wBjJln9igkQVdxPz8h4O6EXvq2tG2VmAKOLNqtJJNSkPkLkP1ORA6ykUxLtere8Vai/XMxt91lMVJF9LSYdYggIBW+fmQDT0jMCYLwtc+IETGqFf1i9hlFZckB0Y+i/aGK2o7xe6ZStxUdNcO/N2zsQQE2QCsAF5HFDCjJ+ja4qoJmbogIiR9y',
            'passport_fe_beating_status': 'true',
            'ttwid': '1%7CSs-WSXwK_P549vAAUSfYFc_KGNjCrwrNZgUwp62lKwI%7C1709789848%7C1cc9757557b3caef334807200b288bf87e0eb8a139fd640f7574c704a494d3ef',
            'bm_sv': 'AEBF757BEF7A4843CC4AAB240A2BD496~YAAQZ+nOF99KbvmNAQAA4u9qFxeo+BPyNXRXncfu6DE7tgUXZgf89Vtisen+MNxp3yv5fFZaJiZMgguwVnhhGjAUJPkUmNW4acvz1sZEhz9J7QHHqP3tSlJ0PmjW6icDdAJxu/f64XgdDlBRZFAoziI879mVTvUCZ9f8o8lehJB91E4qT5w0ObKqML7jtMmDaZW9qtBXNoI1faBTBwJH1f9oFpmNLF01LYp/sX1zQn6oCw5XPysJQC/kUU7NjTyp~1',
            'odin_tt': '216864a36a1f6f530f30b827bf1835b2c43d9835f871a40fd6a31cc886abff7d1b540016e19668d15c505488bb28eefe5f9cbd6491198bbaa2774f72bfd890bd',
            'msToken': 'dpUxs1zNqibwOftsKnG9i2PfJX8LwhiIuDsokQoZIVa12KamQ-6XKITJV6neMhNpsrcXoz29A31KBUMrZ0GiZbUCcP8JvSybNvGTLf4pTmpMXgIS3vhcib-TtE1QzRBkeTF8qb2_r5iNkVT5',
            'msToken': 'dpUxs1zNqibwOftsKnG9i2PfJX8LwhiIuDsokQoZIVa12KamQ-6XKITJV6neMhNpsrcXoz29A31KBUMrZ0GiZbUCcP8JvSybNvGTLf4pTmpMXgIS3vhcib-TtE1QzRBkeTF8qb2_r5iNkVT5',
        }

        headers = {
            'authority': 'www.tiktok.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            # 'cookie': 'tt_chain_token=RsODu7vcrXyCun9viGKJyw==; tiktok_webapp_theme=light; passport_csrf_token=5902da3cb4ed40b87d520405ffed2261; passport_csrf_token_default=5902da3cb4ed40b87d520405ffed2261; _ttp=2bkzLzELiwAXubktic8G817GGyR; d_ticket=dbeb65d8b0128d6aee8d9fb43240e81c1e540; multi_sids=6749780217957532673%3A6574fbb17a1fcd9c7dfa2df381f83736; cmpl_token=AgQQAPPdF-RO0o2S5_8jY504_9q4vEdZv4ArYNFfVw; passport_auth_status=554847a7c512b04417f4ee904e3a385b%2C; passport_auth_status_ss=554847a7c512b04417f4ee904e3a385b%2C; sid_guard=6574fbb17a1fcd9c7dfa2df381f83736%7C1709623899%7C15552000%7CSun%2C+01-Sep-2024+07%3A31%3A39+GMT; uid_tt=e22de1c80eb4388c48031ad7f387c3177a0b497e257faddcf41580cba8791073; uid_tt_ss=e22de1c80eb4388c48031ad7f387c3177a0b497e257faddcf41580cba8791073; sid_tt=6574fbb17a1fcd9c7dfa2df381f83736; sessionid=6574fbb17a1fcd9c7dfa2df381f83736; sessionid_ss=6574fbb17a1fcd9c7dfa2df381f83736; sid_ucp_v1=1.0.0-KDYwOGM2NTZmYTI2ZDY3NjUyZWQ5NWQwZTBlMTFhZDY2ODU2N2RmYTUKIAiBiMXaiquC1l0Q25SbrwYYswsgDDCEk7DtBTgCQPEHEAMaBm1hbGl2YSIgNjU3NGZiYjE3YTFmY2Q5YzdkZmEyZGYzODFmODM3MzY; ssid_ucp_v1=1.0.0-KDYwOGM2NTZmYTI2ZDY3NjUyZWQ5NWQwZTBlMTFhZDY2ODU2N2RmYTUKIAiBiMXaiquC1l0Q25SbrwYYswsgDDCEk7DtBTgCQPEHEAMaBm1hbGl2YSIgNjU3NGZiYjE3YTFmY2Q5YzdkZmEyZGYzODFmODM3MzY; store-idc=maliva; store-country-code=id; store-country-code-src=uid; tt-target-idc=alisg; tt-target-idc-sign=NxBeUNWDj20Xon206PhslbBOhRNyp9D3NLN6HS9leq2nBJatkqIW-eWyknQCuWdkfh38iaKwunxSjBvWEoIN5hn_wiMVpjEcMENxFa4U-UysRbbDSiXdpQccbqEpxDUeO4i6bQm9I5Uj1T0GYMoM36FrV7NMKB-c6sHotPSjszstb0qKXiftL25xJdo06roMaGBe-mZwyh5M2fvr_5eCLu9xXx0b6CxWIauOtKZTaDWVHzIGmOUNteIy643X45x8_bo9v2M0I4_GMfisP7AA2hgT9dT-03tw7oO30v14IVoDQTYpnQ1gms9gOUCgnEpxsZGsoxuQ_utTf_3cosHqrwFxauQW15MBovW690nkjI7cJ2BrgJUeta6ixBdLBAfHkFhDDS1NKIH2x5iBN2xOfY11NFXtCLb3F7Eeznvq_iTrHiE0Z1DTNX5PGVLWc_XFh1kMsbfMo_-te9bQbRvohj9KAimpbNpgT2Fii19enaX_ZvnZQUp5hq78pPnDT8Wb; last_login_method=sms_verification; perf_feed_cache={%22expireTimestamp%22:1709830800000%2C%22itemIds%22:[%227313519542037171462%22%2C%227334214300615167265%22%2C%227333544490633825541%22]}; tt_csrf_token=hm7hpCWb-RloDc24XsRfRmr_zHkuISHJ-cLw; ak_bmsc=D9553C11EED7802091BA115772375955~000000000000000000000000000000~YAAQQ+nOFwYhJf+NAQAAAOJoFxf/L8tbHRllAbHU/2uWrBfyloZnXnuJmf+0Qq0Q7klb+be9+amgrmQMn8YgSACOvRoJekrgahvstgrjLXN4cDqsThD0vfwL0l4vlnI3CtejJ/WCyE7qjpcDOfWG8zKrUos5a/AYT8XHweYSsii2NUPh3XGdGpdqUPWYSUNLX5WQYJ6h7MyYYoXLIS5qSgtts5wBjJln9igkQVdxPz8h4O6EXvq2tG2VmAKOLNqtJJNSkPkLkP1ORA6ykUxLtere8Vai/XMxt91lMVJF9LSYdYggIBW+fmQDT0jMCYLwtc+IETGqFf1i9hlFZckB0Y+i/aGK2o7xe6ZStxUdNcO/N2zsQQE2QCsAF5HFDCjJ+ja4qoJmbogIiR9y; passport_fe_beating_status=true; ttwid=1%7CSs-WSXwK_P549vAAUSfYFc_KGNjCrwrNZgUwp62lKwI%7C1709789848%7C1cc9757557b3caef334807200b288bf87e0eb8a139fd640f7574c704a494d3ef; bm_sv=AEBF757BEF7A4843CC4AAB240A2BD496~YAAQZ+nOF99KbvmNAQAA4u9qFxeo+BPyNXRXncfu6DE7tgUXZgf89Vtisen+MNxp3yv5fFZaJiZMgguwVnhhGjAUJPkUmNW4acvz1sZEhz9J7QHHqP3tSlJ0PmjW6icDdAJxu/f64XgdDlBRZFAoziI879mVTvUCZ9f8o8lehJB91E4qT5w0ObKqML7jtMmDaZW9qtBXNoI1faBTBwJH1f9oFpmNLF01LYp/sX1zQn6oCw5XPysJQC/kUU7NjTyp~1; odin_tt=216864a36a1f6f530f30b827bf1835b2c43d9835f871a40fd6a31cc886abff7d1b540016e19668d15c505488bb28eefe5f9cbd6491198bbaa2774f72bfd890bd; msToken=dpUxs1zNqibwOftsKnG9i2PfJX8LwhiIuDsokQoZIVa12KamQ-6XKITJV6neMhNpsrcXoz29A31KBUMrZ0GiZbUCcP8JvSybNvGTLf4pTmpMXgIS3vhcib-TtE1QzRBkeTF8qb2_r5iNkVT5; msToken=dpUxs1zNqibwOftsKnG9i2PfJX8LwhiIuDsokQoZIVa12KamQ-6XKITJV6neMhNpsrcXoz29A31KBUMrZ0GiZbUCcP8JvSybNvGTLf4pTmpMXgIS3vhcib-TtE1QzRBkeTF8qb2_r5iNkVT5',
            'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        }

        response = requests.get(f'https://www.tiktok.com/@{username}', cookies=cookies, headers=headers)

        response_text: str = response.text

        from bs4 import BeautifulSoup
        import json

        soup = BeautifulSoup(response_text, 'html.parser')

        script_tag = soup.find('script', id='__UNIVERSAL_DATA_FOR_REHYDRATION__', type='application/json')

        if script_tag:
            json_content = script_tag.string
            parsed_json = json.loads(json_content)

            secUid_value = parsed_json['__DEFAULT_SCOPE__']['webapp.user-detail']
            uid = secUid_value['userInfo']['user']['secUid']

            param = {
                "WebIdLastTime": "1706762654",
                "aid": "1988",
                "app_language": "en",
                "app_name": "tiktok_web",
                "browser_language": "en-US",
                "browser_name": "Mozilla",
                "browser_online": "true",
                "browser_platform": "Linux%20x86_64",
                "browser_version": "5.0%20%28X11%29",
                "channel": "tiktok_web",
                "cookie_enabled": "true",
                "count": "30",
                "device_id": "7330489720444978690",
                "device_platform": "web_pc",
                "focus_state": "true",
                "from_page": "user",
                "history_len": "1",
                "is_fullscreen": "false",
                "is_page_visible": "true",
                "maxCursor": "0",
                "minCursor": "0",
                "os": "linux",
                "priority_region": "ID",
                "referer": "",
                "region": "ID",
                "scene": "67",
                "screen_height": "720",
                "screen_width": "1280",
                "secUid": uid,
                "tz_name": "Asia%2FJakarta",
                "verifyFp": "verify_lte1wpzi_rOiJWMcF_FE5P_4tuW_87AL_uH3N0JBj3071",
                "webcast_language": "en",
                "msToken": "9CWrUd630fO0ABZCReAyeid8SRbZ1WMBAtXYX860ImQ3QKVXwaoMKMp3ihUiuZRPORWW-2MkwdJwKnPNwwZmUxUcw-iKWEJkVT0uxRiznlA68olxNOWG-z-zibFNf7fR1OI",
                "X-Bogus": "DFSzsIVYtc2ANciNtbxIrz9WcBrr",
                "_signature": "_02B4Z6wo000015LD58AAAIDDksPnwouNaa-SweNAAIFhd6"
            }

            header = {
                "content-type": "application/json; charset=utf-8",
                "x-tt-logid": "2024030710104049741742E93DDD15351F",
                "tt_stable": "1",
                "bd-tt-error-code": "0",
                "strict-transport-security": "max-age=31536000; includeSubDomains",
                "x-tt-trace-host": "011d8a954aecc774318e592f7bcc70162a54d69855c26c0befa8080fe52204257b1eb2ec8f46abb42e60aedf548c2ffb2984aa98fc6ac17876bd546960836240e568b1e13e740b1bc743c77590ab5899d599336f2bf4122ebbfd9bead370edd41f",
                "x-tt-trace-id": "00-24030710104049741742E93DDD15351F-793071C66E328B72-00",
                "server": "TLB",
                "content-encoding": "br",
                "expires": "Thu, 07 Mar 2024 10:10:41 GMT",
                "cache-control": "max-age=0, no-cache, no-store",
                "pragma": "no-cache",
                "date": "Thu, 07 Mar 2024 10:10:41 GMT",
                "content-length": "7447",
                "x-cache": "TCP_MISS from a23-206-233-85.deploy.akamaitechnologies.com (AkamaiGHost/11.4.2.2-54704533) (-)",
                "x-tt-trace-tag": "id=16;cdn-cache=miss;type=dyn",
                "server-timing": "inner; dur=200, cdn-cache; desc=MISS, edge; dur=3, origin; dur=221",
                "x-origin-response-time": "222, 23.206.233.85",
                "x-akamai-request-id": "18500690",
                "x-firefox-spdy": "h2"
            }

            cookies = {
                "tt_chain_token": "RsODu7vcrXyCun9viGKJyw==",
                "tiktok_webapp_theme": "light",
                "passport_csrf_token": "5902da3cb4ed40b87d520405ffed2261",
                "passport_csrf_token_default": "5902da3cb4ed40b87d520405ffed2261",
                "_ttp": "2bkzLzELiwAXubktic8G817GGyR",
                "tt_csrf_token": "Sx2ron5x-Hi_icZXXNxRiQLj6Vpn_WswhaX8",
                "ak_bmsc": "923C1B7578FF5B211446C491BEAFE787~000000000000000000000000000000~YAAQU+nOF3z8ogKOAQAA+NmFDRc77ZYZ4bNe/la9dXlU7g1d9PU1r2MNVhq8pKRYMNZa7GSsFxxuhzsYJYxkB5+qmG568QLhhkpqgvSfCpc0PTblqGUQVT566EAO44vCzdmROG5xnflsKh1pg1tIXNsD/GIo67wqMp7sRoslJ2l0pe5fXU4HBAjRPqXM0+9LSYHNZH5PPexKcmNQRUKKPS799UaTD9zKT0evzdSLSaI8i4hsexF6MtP3luni8T8Mij5J++d76wgMSuB5ZYMjH9ZCuVuZDmeoTWomIokZMDqxVTOostnelVG6YmIJote4lS8fIwdBW5tJ4D7enNijyvZAP+oRmACxWYUtXyQOZj5xFCuyKm5mByT9Q9SEQU9crhmeVWpYqg8zcjik",
                "s_v_web_id": "verify_lte1wpzi_rOiJWMcF_FE5P_4tuW_87AL_uH3N0JBj3071",
                "d_ticket": "dbeb65d8b0128d6aee8d9fb43240e81c1e540",
                "multi_sids": "6749780217957532673%3A6574fbb17a1fcd9c7dfa2df381f83736",
                "cmpl_token": "AgQQAPPdF-RO0o2S5_8jY504_9q4vEdZv4ArYNFfVw",
                "passport_auth_status": "554847a7c512b04417f4ee904e3a385b%2C",
                "passport_auth_status_ss": "554847a7c512b04417f4ee904e3a385b%2C",
                "sid_guard": "6574fbb17a1fcd9c7dfa2df381f83736%7C1709623899%7C15552000%7CSun%2C+01-Sep-2024+07%3A31%3A39+GMT",
                "uid_tt": "e22de1c80eb4388c48031ad7f387c3177a0b497e257faddcf41580cba8791073",
                "uid_tt_ss": "e22de1c80eb4388c48031ad7f387c3177a0b497e257faddcf41580cba8791073",
                "sid_tt": "6574fbb17a1fcd9c7dfa2df381f83736",
                "sessionid": "6574fbb17a1fcd9c7dfa2df381f83736",
                "sessionid_ss": "6574fbb17a1fcd9c7dfa2df381f83736",
                "sid_ucp_v1": "1.0.0-KDYwOGM2NTZmYTI2ZDY3NjUyZWQ5NWQwZTBlMTFhZDY2ODU2N2RmYTUKIAiBiMXaiquC1l0Q25SbrwYYswsgDDCEk7DtBTgCQPEHEAMaBm1hbGl2YSIgNjU3NGZiYjE3YTFmY2Q5YzdkZmEyZGYzODFmODM3MzY",
                "ssid_ucp_v1": "1.0.0-KDYwOGM2NTZmYTI2ZDY3NjUyZWQ5NWQwZTBlMTFhZDY2ODU2N2RmYTUKIAiBiMXaiquC1l0Q25SbrwYYswsgDDCEk7DtBTgCQPEHEAMaBm1hbGl2YSIgNjU3NGZiYjE3YTFmY2Q5YzdkZmEyZGYzODFmODM3MzY",
                "store-idc": "maliva",
                "store-country-code": "id",
                "store-country-code-src": "uid",
                "tt-target-idc": "alisg",
                "tt-target-idc-sign": "NxBeUNWDj20Xon206PhslbBOhRNyp9D3NLN6HS9leq2nBJatkqIW-eWyknQCuWdkfh38iaKwunxSjBvWEoIN5hn_wiMVpjEcMENxFa4U-UysRbbDSiXdpQccbqEpxDUeO4i6bQm9I5Uj1T0GYMoM36FrV7NMKB-c6sHotPSjszstb0qKXiftL25xJdo06roMaGBe-mZwyh5M2fvr_5eCLu9xXx0b6CxWIauOtKZTaDWVHzIGmOUNteIy643X45x8_bo9v2M0I4_GMfisP7AA2hgT9dT-03tw7oO30v14IVoDQTYpnQ1gms9gOUCgnEpxsZGsoxuQ_utTf_3cosHqrwFxauQW15MBovW690nkjI7cJ2BrgJUeta6ixBdLBAfHkFhDDS1NKIH2x5iBN2xOfY11NFXtCLb3F7Eeznvq_iTrHiE0Z1DTNX5PGVLWc_XFh1kMsbfMo_-te9bQbRvohj9KAimpbNpgT2Fii19enaX_ZvnZQUp5hq78pPnDT8Wb",
                "last_login_method": "sms_verification",
                "perf_feed_cache": "{%22expireTimestamp%22:1709794800000%2C%22itemIds%22:[%227340766826034433286%22%2C%227319250533057875232%22%2C%227310395793221930258%22]}",
                "msToken": "PF-_8NVAMOakAc_FXTYVpNlGbmgRVSQ-0OhwwB-xtsA5qScGIzZGpf762vhyd9HZworw392yBMTOiGUMOTJpvdgEd6fRq6gPQbUXq3HJC3ySCqi-NZck",
                "bm_sv": "89E14DC19B553326CED48BC00F8472DA~YAAQUunOF06LjgGOAQAA+aSWDRciUQIhdzII7/0Phw187WMuVErerFXv7rzqm/20fQlhkTgwci1uv3VkYL68l3VpO9UfIzB8E/dEY6cFenbqTp70BJy1MWu4zPZ0aMwXnXYbtnC/ov+BLXGGBxctQtfhkW0GNTAA0EM22SMeK75Y/EmKG07hFd6ZtmM4zyES9dvfD63vymCkCZqE+V5kJnNORssTLz6p1Q2wUe5vxwglFXE74160XqnpvujWq4Lv~1",
                "passport_fe_beating_status": "true",
                "ttwid": "1%7CSs-WSXwK_P549vAAUSfYFc_KGNjCrwrNZgUwp62lKwI%7C1709624963%7Ca9a2bcaf8e81910c061bb7aebb1f20038e326d81efe2e4cade15dc4e89e11e40",
                "odin_tt": "372a293e9c4c551f96b373bf958d5d9fb13da559ae64ccef0341d5f28f0863baa40f7fc4539e003f914a5c146828c7e728645515244bd9d4856b53df6612279958a826eb4f07da9fad1bab0a72670b51"
            }
            
            users = []
            iteration_count = 0
            while True:
                response = requests.get('https://www.tiktok.com/api/user/list/', params=param, cookies=cookies,headers=header)
                json_data = response.json()
                                
                
                if json_data['statusCode'] == 0:
                    max_cursor = json_data['maxCursor']
                    min_cursor = json_data['minCursor']
                    try:
                        userlist = json_data['userList']
                        for user in userlist:
                            userid = user['user']['uniqueId']
                            avatar_link = user['user']['avatarLarger']
                            id = user['user']['id']
                            nickname = user['user']['nickname']
                            userid = {
                                'id': id,
                                'userID': userid,
                                'nickname': nickname,
                                'avatar': avatar_link
                            }
                            users.append(userid)
                    except:
                        print('ok')

                    if max_cursor == -1 or min_cursor == -1 or iteration_count >= limit:
                        break
                    param['maxCursor'] = str(max_cursor)
                    param['minCursor'] = str(min_cursor)
                    iteration_count += 1
                if len(users) == 0:
                    users = 'This Account Private Following'
                    break


            return users
