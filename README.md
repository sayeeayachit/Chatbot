# Chatbot
## Setup and installation
If you haven’t installed Rasa NLU and Rasa Core yet, you can do it by navigating to the project directory and running:

``` pip install -r requirements.txt```
You also need to install a spaCy English language model. You can install it by running:

``` python -m spacy download en```

## Files for Rasa NLU model
data/nlu_data.md file contents training data for the NLU model.

nlu_config.yml file contains the configuration of the Rasa NLU pipeline:

``` language: "en" ```

```pipeline: spacy_sklearn```

## Files for Rasa Core model
**data/stories.md** file contains some training stories which represent the conversations between a user and the assistant.

**domain.yml** file describes the domain of the assistant which includes intents, entities, slots, templates and actions the assistant should be aware of.

**actions.py** file contains the code of a custom action which retrieves results of the latest IPL match by making an external API call.

**endpoints.yml** file contains the webhook configuration for custom action.

**policies.yml** file contains the configuration of the training policies for Rasa Core model.

For more information please refer to https://github.com/JustinaPetr/Weatherbot_Tutorial
