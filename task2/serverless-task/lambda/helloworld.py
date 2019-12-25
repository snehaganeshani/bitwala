#!/usr/bin/python


import logging
import json


logger = logging.getLogger()
logger.setLevel(logging.INFO)



def helloworld(event, context):
   
    return {
    'body' :  json.dumps('Hello World')
            }
    
    
