# json_scraper
Scrape websites based on json file

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
