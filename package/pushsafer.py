import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen


# https://www.pushsafer.com/dashboard
def alert(message, private_key):
    url = 'https://www.pushsafer.com/api'
    title = "excitare_cito alert"
    post_fields = {
        "t": title,
        "m": message,
        "s": 36,
        "v": 3,
        "i": 47,
        "c": '#0b5394',
        "d": 'a',
        "k": private_key,
    }

    request = Request(url, urlencode(post_fields).encode())
    message_tmp = urlopen(request).read().decode()
    message = json.loads(message_tmp)
    if message['status'] == 1:
        print(f"[+] {message['success'].capitalize()}")
    else:
        print(f"[!] Pushsafer returned: {message}")
    return message
