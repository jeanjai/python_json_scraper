from commands import base
import json

browser = base()

with open('example_config.json') as json_file:
    jsonData = json.load(json_file)


def runTypes(action):
    if action["type"] == "enterText":
        browser.write(action["selector"],action["value"])
            
    elif action["type"] == "getValue":
        if action["multiple"]:
            return browser.getValues(action["selector"])
        else:
            return browser.getValue(action["selector"])
            
    elif action["type"] == "getAttribute":
        if action["multiple"]:
            return browser.getAttributes(action["selector"], action["attribute"])
        else:
            return browser.getAttribute(action["selector"], action["attribute"])
    
    elif action["type"] == "click":
        browser.click(action["selector"])

    elif action["type"] == "getLink":
        if action["multiple"]:
            return browser.getLinks(action["selector"])
        else:
            return browser.getLink(action["selector"])

    else:
        print("Please enter a valid type")


def addColumn(data):
    #This is where the data will be exported. For now it's just logging the results
    print ("exporting " + str(data))


for site in jsonData:
    website = jsonData[site]
    actions = website["actions"]

    for url in website['url']:
        
        if browser.isUrlValid(url):
            browser.visit(url)
        else:
            print ('Unable to connect to url: ' + url)
            continue
    
        for action in actions:

            data = runTypes(action)
            
            if data:
                addColumn(data)

browser.end()