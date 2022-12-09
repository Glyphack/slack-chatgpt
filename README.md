# slack-gpt

[![PyPI](https://img.shields.io/pypi/v/slack-gpt?style=flat-square)](https://pypi.python.org/pypi/slack-gpt/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/slack-gpt?style=flat-square)](https://pypi.python.org/pypi/slack-gpt/)
[![PyPI - License](https://img.shields.io/pypi/l/slack-gpt?style=flat-square)](https://pypi.python.org/pypi/slack-gpt/)
[![Coookiecutter - Wolt](https://img.shields.io/badge/cookiecutter-Wolt-00c2e8?style=flat-square&logo=cookiecutter&logoColor=D4AA00&link=https://github.com/woltapp/wolt-python-package-cookiecutter)](https://github.com/woltapp/wolt-python-package-cookiecutter)

---

**Documentation**: [https://Glyphack.github.io/slack-gpt](https://Glyphack.github.io/slack-gpt)

**Source Code**: [https://github.com/Glyphack/slack-gpt](https://github.com/Glyphack/slack-gpt)

**PyPI**: [https://pypi.org/project/slack-gpt/](https://pypi.org/project/slack-gpt/)

---

Reply to slack message without thinking with GPT3

## Usage

### Step 1. Create an slack bot

1. Goto <https://api.slack.com/apps> and create new app
2. Enable Events for the bot and subscribe to event `app_mention` and set the callback to "yourdomain.com/slack/events"
3. Add permission in Oauth & Permissions tab add the following permissions

```
app_mentions:read
channels:history
chat:write
chat:write.public
commands
groups:history
im:history
incoming-webhook
mpim:history
```

4. Copy the Bot User OAuth Token
5. Copy the Signing Secret

### Step 2. Register in chatGPT

<https://chat.openai.com/chat>

### Step 3. Fill the secrets

Open `src/slack_gpt/main.py` and fill the env values from secrets above.

### Step 4

...

### Step 5

Profit

## Development

- Clone this repository
- Requirements:
  - [Poetry](https://python-poetry.org/)
  - Python 3.7+
- Create a virtual environment and install the dependencies

```sh
poetry install
```

- Activate the virtual environment

```sh
poetry shell
```

### Testing

```sh
pytest
```
