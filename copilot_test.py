def get_data_from_url(url):
    import requests
    r = requests.get(url)
    return r.text

print(get_data_from_url('http://www.google.com'))