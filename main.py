import tweepy, openai
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
import time

TWITTER_API_KEY = "3aRq6aPrFfmFlEY46mbJV5bLc"
TWITTER_API_SECRET = "eqaiLbbG9CJv2DjBH7R02LniHkLrxB8ijJEpGVLxmVl6s6sHpj"
TWITTER_ACCESS_TOKEN = "1682950598529015811-SwpPC2tkMg7XEpmIIf55gh70FCkCFI"
TWITTER_ACCESS_TOKEN_SECRET = "junQn4orAXNmLjFJJCVE7jRSrLOxPhnGZwxyotNlV2TwG"
TWITTER_BEARER_TOKEN = r"AAAAAAAAAAAAAAAAAAAAAHHbowEAAAAAjiHxoPY3VOAfbgC1sj6bSCEyF1w%3Ddw7Oeosoxy1MWlJFzcuMQEFhAC9HNr2D6WRjZRmF9Np84eCNeZ"

openai.api_key = "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"

client = tweepy.Client(
    consumer_key=TWITTER_API_KEY,
    consumer_secret=TWITTER_API_SECRET,
    access_token=TWITTER_ACCESS_TOKEN,
    access_token_secret=TWITTER_ACCESS_TOKEN_SECRET
)

class ThoughtfulGPT():
    def __init__(self):
        self.tweet_response_limit = 35 # How many tweets to respond to each time the program wakes up

        # Initialize the language model w/ temperature of .5 to induce some creativity
        self.llm = ChatOpenAI(temperature=.5, openai_api_key=openai.api_key, model_name='gpt-3.5-turbo')
    
    def generate_tweet(self):
        response = openai.Completion.create(engine="text-davinci-001",prompt=
        """
            RESPONSE TONE:

            - Your prediction should be given in an active voice and be opinionated
            - Your tone should be serious
            
            RESPONSE FORMAT:

            - Respond in under 200 characters
            - Respond in two or less short sentences
            - Do respond with emojis
            
            RESPONSE CONTENT:
            - Only tweet quotes that are very motiovation and uplifting
            - If you don't have an answer for the prompt. respond with "None of your Business, Just start you hustle🦁"
        """,max_tokens=200)
        
        return response
bot = ThoughtfulGPT()
response = bot.generate_tweet()

tweet = response.choices[0].text
client.create_tweet(text=tweet)
time.sleep(60 * 20)
print("successfully tweeted")