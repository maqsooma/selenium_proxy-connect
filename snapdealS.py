import os
import zipfile
import time

from selenium import webdriver

def initiate(proxy):
    proxy = proxy.replace("http://", "").replace("https://", "")
    PROXY_HOST = proxy.split("@")[1].split(":")[0]          #host
    PROXY_PORT = int(proxy.split("@")[1].split(":")[1])     #port
    PROXY_USER = proxy.split("@")[0].split(":")[0]          #username
    PROXY_PASS = proxy.split("@")[0].split(":")[1]          #password

    manifest_json = """
    {
        "version": "1.0.0",
        "manifest_version": 2,
        "name": "Chrome Proxy",
        "permissions": [
            "proxy",
            "tabs",
            "unlimitedStorage",
            "storage",
            "<all_urls>",
            "webRequest",
            "webRequestBlocking"
        ],
        "background": {
            "scripts": ["background.js"]
        },
        "minimum_chrome_version":"22.0.0"
    }
    """

    background_js = """
    var config = {
            mode: "fixed_servers",
            rules: {
            singleProxy: {
                scheme: "http",
                host: "%s",
                port: parseInt(%s)
            },
            bypassList: ["localhost"]
            }
        };

    chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

    function callbackFn(details) {
        return {
            authCredentials: {
                username: "%s",
                password: "%s"
            }
        };
    }

    chrome.webRequest.onAuthRequired.addListener(
                callbackFn,
                {urls: ["<all_urls>"]},
                ['blocking']
    );
    """ % (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)

    path = os.path.dirname(os.path.abspath(__file__))
    chrome_options = webdriver.ChromeOptions()
    pluginfile = 'proxy_auth_plugin.zip'
    chrome_options.add_extension(pluginfile)
    os.path.join(path, 'chromedriver'),
    chrome_options=chrome_options
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def main():
    driver = initiate("http://youparcel:Proxy2022!@us-fl.proxymesh.com:31280")
    #driver.get('https://www.google.com/search?q=my+ip+address')
    driver.get(' https://www.snapdeal.com/products/computers?sort=plrty')
    time.sleep(15)

if __name__ == '__main__':
    main()