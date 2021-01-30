# discord-bot
A discord bot built in python which lets user to search on google through discord.

## Description

If the user types **!google *search text***, it replies with top 5 google search links that the user would get when they search ***search text*** on google.com. Also, the bot lets users to see their search history using **!recent *search text***.

## Requirements
Discord Bot uses the following python modules

* [pymongo](https://pypi.org/project/pymongo/) - Python driver for MongoDB 
* [discord.py](https://pypi.org/project/discord.py/) - Python wrapper for the Discord API
* [requests](https://pypi.org/project/requests/) - Python HTTP for Humans.

Other requirements
* [Valid Token](https://discordpy.readthedocs.io/en/latest/discord.html) - A valid discord bot token
* [Google Custom Search Engine](https://www.google.com/cse/) - A custom search engine
* [Google API key](https://console.developers.google.com/apis/dashboard) - A Google Cloud Console "Project" to get API key
* [Mongo Atlas Cluster](https://docs.atlas.mongodb.com/tutorial/create-new-cluster) - A fully-managed cloud database cluster


## Installation

#### Set the following variables in .env file

    DISCORD_TOKEN=<discord bot token>
    GOOGLE_CUSTOM_SEARCH_URI=<google custom search API URI>
    GOOGLE_API_KEY=<google project API key>
    SEARCH_ENGINE_ID=<custom search engine id>
    CLUSTER_URL=<mongo atlas cluster URL>
    MONGO_USER=<mongo user name>
    MONGO_PASSWORD=<mongo user password>
    DB_NAME=<mongo database name>

#### Shell commands

    # install virtualenv
    $ pip3 install virtualenv

    # create a virtual environment for the bot project
    $ python3 -m virtualenv venv

    # activate virtual environment
    $ source venv/bin/activate

    # install project dependencies
    $ pip3 install -r requirements
    
    # to activate the bot
    $ python main.py
    
## Deployment on Heroku

The bot is deployed on Heroku using the following steps:

Add a file named **Procfile** with the following command in it:
`worker: python main.py`

1. To install heroku: `$ brew install heroku/brew/heroku`
2. To create an app on heroku: `$ heroku create`
3. Find the newly created app on heroku dashboard.
4. Go to settings and connect the newly created heroku app to your github repo and branch.
5. Set the config variables.
6. Click on deploy.

## License
MIT