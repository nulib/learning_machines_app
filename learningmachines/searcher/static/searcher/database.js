let database = {
    "NYT_China": {
          "index": "nyt-china",
          "id": "uid",
          "full_text": "text",
          "doc_title": "title",
          "author": "author",
          "date_type": "date",
          "info": [
                "title",
                "author"
          ],
          "max_doc": 80000,
          "rt_params": {
                "a": 0,
                "b": 0,
                "count": 79923,
                "max": 80000
          },
          "year_count": {
                "2008": 6432,
                "2009": 6882,
                "2010": 5820,
                "2011": 5290,
                "2012": 6084,
                "2013": 5320,
                "2014": 5649,
                "2015": 5172,
                "2016": 4899,
                "2017": 4896,
                "2018": 5607,
                "2019": 5904,
                "2020": 6872,
                "2021": 5096
          },
          "site_info": {
                "option": [],
                "site_name": "NYT China"
          }
    },
    "Poetry_Foundation": {
          "index": "poetry-foundation",
          "id": "pmid",
          "full_text": "text",
          "doc_title": "title",
          "author": "author",
          "date_type": "date",
          "info": [
                "title",
                "author"
          ],
          "max_doc": 16000,
          "rt_params": {
                "a": 0,
                "b": 0,
                "count": 15652,
                "max": 15652
          },
          "year_count": {
                "2022": 15652
          },
          "site_info": {
            "option": [],
            "site_name": "Poetry Foundation"
          }
    }
}

console.log(database)