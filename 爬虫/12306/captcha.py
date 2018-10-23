# coding = utf-8
from urllib.parse import urlencode

import requests
from .settings import username, password, get_answer
session = requests.Session()
#
start_url = "https://kyfw.12306.cn/otn/login/init"
session.get(start_url)
# 2.获取验证码
captcha_url = "https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.11248564942476502"
response = session.get(captcha_url)
with open('captcha.png', 'wb') as fp:
    fp.write(response.content)
# 3.校验验证码
check_captcha_url = "https://kyfw.12306.cn/passport/captcha/captcha-check"
data = {
    "answer": get_answer(),
    "login_site": "E",
    "rand": "sjrand"
}
response = session.post(check_captcha_url, data=data)
print(response.text)
# 4.校验用户名和密码
login_url = "https://kyfw.12306.cn/passport/web/login"
data = {
    "username": username,
    "password": password,
    "appid": "otn"
}
response = session.post(login_url, data=data)
print(response.text)
# 5.查询车票
base_select_url = "https://kyfw.12306.cn/otn/leftTicket/query?"
params = {
    "leftTicketDTO.train_date": "",
    "leftTicketDTO.from_station": "",
    "leftTicketDTO.to_station": "",
    "purpose_codes=ADULT": ""
}
select_url = base_select_url + urlencode(params)
session.get(select_url)
"secretStr=BgGg3ahcOjLqIBDMSHMPMAZRSRIGj%2FKUMlb0d5D6Jf3XcC1FrHl3iW30%2FMelzJ0DX4WhejtUM9yH%0AdmgLn6X6nIC8LWdoTjml6ZuXtQeCDOhBRfhml2ePFiGYHZdZ1m5CzXy9h34OdONVz6K%2FqIBnvkhd%0AGEq0lsFEZ8gd0nEAEEmGeeh3gGQo58Fw%2FRKHAQeVMUtdq9vfM3TJ4exOw9glQh1JgfPJVIo%2FADlh%0Av1d4kUcgRnDZqTCltaGG9GmC9eAF3dyY66VojPI%3D&train_date=2018-08-10&\
back_train_date=2018-07-26&\
tour_flag=dc&purpose_codes=ADULT&\
query_from_station_name=襄阳东&\
query_to_station_name=武汉&\
undefined"