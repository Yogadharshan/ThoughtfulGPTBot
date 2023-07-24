import tweepy, openai
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
import time
import schedule

TWITTER_API_KEY = ""
TWITTER_API_SECRET = ""
TWITTER_ACCESS_TOKEN = ""
TWITTER_ACCESS_TOKEN_SECRET = ""
TWITTER_BEARER_TOKEN = ""

openai.api_key = ""

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
            - Only tweet quotes that are very motivation and uplifting
            - If you don't have an answer for the prompt. respond with "None of your Business, Just start you hustle🦁"
        """,max_tokens=200)
        
        return response
def geeks():
    bot = ThoughtfulGPT()
    response = bot.generate_tweet()
    tweet = response.choices[0].text
    client.create_tweet(text=tweet)
    print("successfully tweeted")
    time.sleep(60 * 20) 
    
schedule.every(10).minutes.do(geeks)
