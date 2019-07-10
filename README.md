# json_scraper
## Description:
This dynamic scraper uses a json file input to configer the scrape.

### Key fuctionalities
* Wide list of export data types
* Ability to scrape multiple websites using 1 json file
* Ability to do actions on the page based on inputs in json file

## Requirements:
* Pyton
* Selenium
* Requests (check http request)


### Config.json file:
```

{
    "first test name": {
        "url": ["website.com"], #list of urls
        "actions": [ #Don't change the name
            {
                "type": "enterText",
                "value": "value to input",
                "selector": "#search_keyword"
            },
            {
                "type": "enterText",
                "value": "value to input",
                "selector": "#search_location"
            },
            {
                "type": "click",
                "selector": "#btn_search",
                "multiple": false
            }
        ]
    },
    "second test name": {
      "url": ["website.com"], #list of urls
        "actions": [ #Don't change the name
            {
                "type": "enterText",
                "value": "value to input",
                "selector": "#search_keyword"
            },
            {
                "type": "enterText",
                "value": "value to input",
                "selector": "#search_location"
            },
            {
                "type": "click",
                "selector": "#btn_search",
                "multiple": false
            }
        ]
    }
}
```
