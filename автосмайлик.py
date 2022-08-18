import vk_api
import requests
import time
from python_rucaptcha import ImageCaptcha

a = 1
while True:
    try:
        if a<39:
            r = requests.post("https://api.vk.com/method/status.setImage?access_token=(сюда токен)&v=5.103&status_id="+str(a)) ### скобки в токене убрать
            a += 1
            print(r.text)
            time.sleep(0.5)
        else:
            a = 1
    except vk_api.Captcha as e:
                s_id = e.sid
                url = e.url
                answer = ImageCaptcha.ImageCaptcha(service_type="rucaptcha",
                                                   rucaptcha_key='1').captcha_handler(
                    captcha_link=url)
                code = answer.get("captchaSolve")
                print(url, code)

while True:
    main()