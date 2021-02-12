# FE-API
The Unofficial Fire Emblem API.  
  
Entirely with [FastAPI](https://fastapi.tiangolo.com/), using [BeautifulSoup](https://beautiful-soup-4.readthedocs.io/en/latest/) to scrape all content from [Serenes Forest](https://serenesforest.net/).


## Config
The API is currently not hosted anywhere; these are the steps to run the API locally.

1. Clone the repository to your machine

       $ git clone https://github.com/chrisngyn/FE-API.git
       
2. Change into the directory

       $ cd FE-API
       
3. While optional, it's recommended to setup a virtual environment

       $ python3 -m virtualenv env
       $ source env/bin/activate

4. Install dependencies

       $ pip3 install -r requirements.txt
       
5. Change into the `src/` directory

       $ cd src
       
6. Start application

       $ uvicorn main:app --reload


## Miscellanous
- If you are wondering why there are multiple folders labelled `FE6`, `FE7`, `FE8`, etc. with similar named files, read [this pull request](https://github.com/chrisngyn/FE-API/pull/1) as to why it looks like I'm duplicating code unnecessarily.
- Suggestions can be made by opening an issue. Pull requests are always welcomed.
