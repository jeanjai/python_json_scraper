# Json Dynamic Web Scraper

## Table of contents
* [Desctription](#description)
* [Features](#features)
* [Requirements](#requirements)
* [Data types](#data-types)

## Description:
This dynamic scraper uses python and selenium to scrape data from a website based on inputs defined in a json file ```config.json```. You can define actions to navigate and gather information from a specified webpage. 

## Features:
* Wide list of export data types
* Ability to scrape multiple websites using 1 json file
* Ability to do actions on the page based on inputs in json file

## Requirements:
* [Python](https://www.python.org/downloads/)
* [Selenium](https://www.seleniumhq.org/download/)
* Requests ```pip install requests```

## How to run a scrape:

### Step 1:

Install the required packages.
* [Python](https://www.python.org/downloads/)
* [Selenium](https://www.seleniumhq.org/download/)
* Requests ```pip install requests```

### Step 2:

In the ```config.json``` file, enter the actions, and start url for your scrape. You can also use the example_config.json file as a sample.

### Step 3:

Make sure you have defined the ```chrome_path``` in the ```commands.py``` file. 

### Step 4:

Run the ```run.py``` file in terminal ```python run.py```

## Config.json file:
```

{
    "example": {
        "url": ["example.com"], #list of urls
        "actions": [
            {
                "type": "enterText",
                "value": "foo",
                "selector": "#search_keyword"
            },
            {
                "type": "enterText",
                "value": "foo",
                "selector": "#search_location"
            },
            {
                "type": "click",
                "selector": "#btn_search",
                "multiple": false
            }
        ]
    },
    "example2": {
      "url": ["exampletwo.com"], #list of urls
        "actions": [ 
            {
                "type": "enterText",
                "value": "bar",
                "selector": "#search_keyword"
            },
            {
                "type": "enterText",
                "value": "foo",
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

## Data types:
* enterText
* getValue
* getAttribute
* click
* getLink
