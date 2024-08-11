# Report: Sentiment Analysis of Movie Reviews Using Azure Text Analytics API

## 1. Introduction

The task was to develop a Python program that analyzes the sentiment of movie reviews using the Azure Text Analytics API. Sentiment analysis is a powerful tool that helps in determining the sentiment behind a text, such as whether the sentiment is positive, negative, or neutral. This report describes the implementation and functionality of the Python program, followed by a detailed explanation of the sentiment analysis process.

## 2. Problem Statement

The objective is to analyze the sentiment of movie reviews using the Azure Text Analytics API. The program needs to determine whether a given movie review has a positive, neutral, or negative sentiment, and it should also provide detailed sentiment scores and opinions on specific aspects of the review.

## 3. Program Overview

The Python program was designed to interact with the Azure Text Analytics API, a cloud-based service that uses machine learning to analyze text. The program reads user input (a movie review), sends it to the Azure API, and retrieves the sentiment analysis results.

## 4. Key Components of the Program

- **Environment Variables:** The program requires two environment variables: `LANGUAGE_KEY` and `LANGUAGE_ENDPOINT`. These are necessary to authenticate the API requests.

- **Azure SDKs:** The program utilizes the Azure SDK for Python, particularly the `TextAnalyticsClient` class, which provides methods to interact with the Text Analytics API.

- **Sentiment Analysis with Opinion Mining:** The program doesn't just provide an overall sentiment score; it also includes opinion mining, which breaks down the sentiment of specific aspects or features mentioned in the review.

## 5. Implementation

Here is the Python program used to analyze the sentiment of movie reviews:

```python
import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Load environment variables
language_key = os.getenv('LANGUAGE_KEY')
language_endpoint = os.getenv('LANGUAGE_ENDPOINT')

# Authenticate the client using your key and endpoint
def authenticate_client():
    ta_credential = AzureKeyCredential(language_key)
    text_analytics_client = TextAnalyticsClient(
        endpoint=language_endpoint,
        credential=ta_credential)
    return text_analytics_client

client = authenticate_client()

# Example method for detecting sentiment and opinions in text
def sentiment_analysis_with_opinion_mining_example(client):
    print("*" * 200)
    print("\n")
    print("Welcome To The Movie Review Sentiment Analysis!".center(200))
    print("\n")
    print("*" * 200)
    print("\n")
    print("Enter Your Review Below:".center(200))
    print("\n")

    documents = [input()]

    result = client.analyze_sentiment(documents, show_opinion_mining=True)
    doc_result = [doc for doc in result if not doc.is_error]

    positive_reviews = [doc for doc in doc_result if doc.sentiment == "positive"]
    negative_reviews = [doc for doc in doc_result if doc.sentiment == "negative"]

    for document in doc_result:
        print("Document Sentiment: {}".format(document.sentiment))
        print("Overall scores: positive={0:.2f}; neutral={1:.2f}; negative={2:.2f} \n".format(
            document.confidence_scores.positive,
            document.confidence_scores.neutral,
            document.confidence_scores.negative,
        ))
        for sentence in document.sentences:
            print("Sentence: {}".format(sentence.text))
            print("Sentence sentiment: {}".format(sentence.sentiment))
            print("Sentence score:\nPositive={0:.2f}\nNeutral={1:.2f}\nNegative={2:.2f}\n".format(
                sentence.confidence_scores.positive,
                sentence.confidence_scores.neutral,
                sentence.confidence_scores.negative,
            ))
            for mined_opinion in sentence.mined_opinions:
                target = mined_opinion.target
                print("......'{}' target '{}'".format(target.sentiment, target.text))
                print("......Target score:\n......Positive={0:.2f}\n......Negative={1:.2f}\n".format(
                    target.confidence_scores.positive,
                    target.confidence_scores.negative,
                ))
                for assessment in mined_opinion.assessments:
                    print("......'{}' assessment '{}'".format(assessment.sentiment, assessment.text))
                    print("......Assessment score:\n......Positive={0:.2f}\n......Negative={1:.2f}\n".format(
                        assessment.confidence_scores.positive,
                        assessment.confidence_scores.negative,
                    ))
            print("\n")
        print("\n")

# Run the sentiment analysis function
sentiment_analysis_with_opinion_mining_example(client)
```

## 6. Execution Flow

1. **Authentication:**
   - The program begins by loading the API key and endpoint from environment variables.
   - It then uses these credentials to authenticate with the Azure Text Analytics service.

2. **User Input:**
   - The program prompts the user to input a movie review.

3. **Sentiment Analysis:**
   - The review text is sent to the Azure API for sentiment analysis.
   - The API returns the overall sentiment (positive, negative, or neutral) and provides detailed scores for each sentiment category.

4. **Opinion Mining:**
   - The program also performs opinion mining, which identifies specific targets (e.g., "acting", "plot") mentioned in the review and analyzes the sentiment towards each target.

5. **Output:**
   - The program outputs the overall sentiment and detailed sentiment scores, including any opinions mined from the text.

## 7. Example Output

- ### A. Positive Review:

```
********************************************************************************


                Welcome To The Movie ReView Sentiment Analysis!                 


********************************************************************************


                            Enter Your Review Below:                            


This is simply one of the best films ever made and I know I am not the first to
say that and I certainly won't be the last.


********************************************************************************


                         Review Analysis is as follows:


Document Sentiment: positive
Overall scores: positive=1.00; neutral=0.00; negative=0.00 

Sentence: This is simply one of the best films ever made and I know I am not the
first to say that and I certainly won't be the last.

Sentence sentiment: positive
Sentence score:
Positive=1.00
Neutral=0.00
Negative=0.00

......'positive' target 'films'
......Target score:
......Positive=1.00
......Negative=0.00

......'positive' assessment 'best'
......Assessment score:
......Positive=1.00
......Negative=0.00

```

- ### A. Negative Review:

```
********************************************************************************


                Welcome To The Movie ReView Sentiment Analysis!                 


********************************************************************************


                            Enter Your Review Below:                            


The dialogue was cringeworthy, the pacing was slow, and the whole thing felt like
a cheap imitation of better films.


********************************************************************************


                         Review Analysis is as follows:                         


Document Sentiment: negative
Overall scores: positive=0.00; neutral=0.00; negative=1.00 

Sentence: The dialogue was cringeworthy, the pacing was slow, and the whole thing
felt like a cheap imitation of better films.

Sentence sentiment: negative
Sentence score:
Positive=0.00
Neutral=0.00
Negative=1.00

......'negative' target 'dialogue'
......Target score:
......Positive=0.36
......Negative=0.64

......'negative' assessment 'cringeworthy'
......Assessment score:
......Positive=0.36
......Negative=0.64

......'negative' target 'pacing'
......Target score:
......Positive=0.03
......Negative=0.97

......'negative' assessment 'slow'
......Assessment score:
......Positive=0.03
......Negative=0.97
```

## 8. Conclusion

The Python program successfully utilizes Azure Text Analytics API to analyze the sentiment of movie reviews. It not only determines the overall sentiment of the review but also performs detailed opinion mining to provide insights into specific aspects of the review. This capability can be extremely useful for businesses that wish to analyze customer feedback or product reviews to understand customer sentiment more deeply.