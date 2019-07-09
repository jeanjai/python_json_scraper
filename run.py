from commands import base
import json

browser = base()

with open('example_config.json') as json_file:
    data = json.load(json_file)


for site in data:
    website = data[site]
    actions = website["actions"]

    for url in website['url']:
        
        if browser.isUrlValid(url):
            browser.visit(url)
        else:
            print ('Unable to connect to url: ' + url)
            continue
    
        for action in actions:

            if action["type"] == "enterText":
                browser.write(action["selector"],action["value"])
            
            elif action["type"] == "getValue":
                if action["multiple"]:
                    browser.getValues(action["selector"])
                else:
                    browser.getValue(action["selector"])
            
            elif action["type"] == "getAttribute":
                if action["multiple"]:
                    browser.getAttributes(action["selector"], action["attribute"])
                else:
                    browser.getAttribute(action["selector"], action["attribute"])

            elif action["type"] == "click":
                browser.click(action["selector"])
        
            else:
                print("Please enter a valid type")







browser.end()