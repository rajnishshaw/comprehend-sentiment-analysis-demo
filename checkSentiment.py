import json
import boto3


def lambda_handler(event, context):
    #get the user input from event
    body= json.loads(event['body'])
    userInput = body['review']
    #userInput="I am very happy"
    # call comprehend
    comprehend = boto3.client('comprehend') 
    sentiment_data=comprehend.detect_sentiment(Text=userInput, LanguageCode ='en')
    
    # return value
    retVal = "{ Sentiment : " +sentiment_data['Sentiment']+ "}" 
    

    return {
        'statusCode': 200,
        'body': json.dumps(retVal)
    }
