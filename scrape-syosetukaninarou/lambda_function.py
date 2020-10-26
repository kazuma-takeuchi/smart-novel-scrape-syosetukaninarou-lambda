import os
import re
import json
import time
import base64
import requests
import logging

from datetime import datetime

from models import NovelModel, dic_genre

logger = logging.getLogger()
logger.setLevel(logging.INFO)

SITE_NAME = os.getenv('SITE_NAME')
BASE_URL = os.getenv('BASE_URL')
API_ENDPOINT = os.getenv('API_ENDPOINT')


def get_novel_with_api(ncode):
    params = {
        "ncode": ncode,
        "out": "json"
    }
    res = requests.get(API_ENDPOINT, params=params)
    return json.loads(res.content.decode('utf-8'))[1]

        
def create_id(url):
    id_ = SITE_NAME + "-" + url.split('/')[-1]
    return id_


def jst_str2ts_epoch_milli(jst, format="%Y-%m-%d %H:%M:%S"):
    dt = datetime.strptime(jst + "+0900", format + "%z")
    ts = dt.timestamp() * 1000
    return ts


def extract_attributes(novel):
    document = {
        "title": novel["title"],
        "author": novel["writer"],
        "description": re.sub(r"\n", "", novel["story"]),
        "genre": dic_genre[novel["genre"]],
        "tag": novel["keyword"].split(" "),
        "length": novel["length"],
        "created_at": jst_str2ts_epoch_milli(novel["general_firstup"], format="%Y-%m-%d %H:%M:%S"),
        "updated_time": jst_str2ts_epoch_milli(novel["novelupdated_at"], format="%Y-%m-%d %H:%M:%S"),
        "like_count": novel["fav_novel_cnt"]
    }
    return document


def lambda_handler(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    logger.info(event)
    logger.info(f'event {event}')
    url = BASE_URL + event['url']
    novel = get_novel_with_api(event['url'])
    document = extract_attributes(novel)
    id_ = create_id(url)
    document['key'] = id_
    document['url'] = url
    document['site_name'] = SITE_NAME
    document = NovelModel(**document).dict()
    res = {
        "document": document,
        "id": id_
    }
    return res