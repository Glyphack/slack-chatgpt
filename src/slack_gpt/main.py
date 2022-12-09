import logging
import os

# Initialize Flask app
from flask import Flask, request
from revChatGPT.revChatGPT import Chatbot
from slack_bolt import App

# SlackRequestHandler translates WSGI requests to Bolt's interface
# and builds WSGI response from Bolt's response.
from slack_bolt.adapter.flask import SlackRequestHandler
from slack_sdk.web import WebClient

# Put chat GPT token here
os.environ["EMAIL"] = ""
os.environ["PASSWORD"] = ""

# Put Slack token here
os.environ["SLACK_BOT_TOKEN"] = ""
os.environ["SLACK_SIGNING_SECRET"] = ""

config = {
    "email": os.environ["EMAIL"],
    "password": os.environ["PASSWORD"],
}

chatbot = Chatbot(config, conversation_id=None)

SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
SLACK_SIGNING_SECRET = os.environ["SLACK_SIGNING_SECRET"]


def generate_reply(message: str) -> str:
    response = chatbot.get_chat_response(message, output="text")
    return response["message"]


logging.basicConfig(level=logging.INFO)


app = App(signing_secret=SLACK_SIGNING_SECRET, token=SLACK_BOT_TOKEN)


app = App(
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET"),
    token=os.environ.get("SLACK_BOT_TOKEN"),
)


# @app.middleware
# def log_request(logger, body, next):
#     logging.debug(body)
#     return next()


# App is completely framework/runtime agnostic
# @app.command("/gpt-reply")
# def hello(body, ack):
#     ack(f"Hi <@{body['user_id']}>!")


@app.event("app_mention")
def event_test(say, body, client: WebClient):
    channel = body["event"]["channel"]
    thread_ts = client.conversations_replies(
        channel=body["event"]["channel"], ts=body["event"]["ts"]
    )["messages"][0]["thread_ts"]
    history = client.conversations_history(
        channel=channel,
        oldest=thread_ts,
        latest=thread_ts,
        limit=1,
        inclusive=True,
    )
    response = generate_reply(history["messages"][0]["text"])

    event = body["event"]
    thread_ts = event.get("thread_ts", None) or event["ts"]
    say(text=response, thread_ts=thread_ts)


flask_app = Flask(__name__)

handler = SlackRequestHandler(app)

# Register routes to Flask app
@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    # handler runs App's dispatch method
    return handler.handle(request)


if __name__ == "__main__":
    logging.info("Starting app")
    flask_app.run(port=8000)
