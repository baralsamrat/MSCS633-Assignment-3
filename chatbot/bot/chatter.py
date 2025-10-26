from django.conf import settings
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
from pathlib import Path
import yaml

def get_chatbot():
    db_uri = "sqlite:///" + settings.CHATTERBOT_DB_PATH
    return ChatBot(
        "TerminalBot",
        storage_adapter="chatterbot.storage.SQLStorageAdapter",
        database_uri=db_uri,
        logic_adapters=[{
            "import_path": "chatterbot.logic.BestMatch",
            "default_response": "I'm not sure about that yet. Try rephrasing?",
            "maximum_similarity_threshold": 0.90,
        }],
    )

def initial_train(bot):
    corpus_trainer = ChatterBotCorpusTrainer(bot)
    corpus_trainer.train("chatterbot.corpus.english.greetings", "chatterbot.corpus.english.conversations")
    custom = Path(__file__).parent / "corpus" / "custom.yml"
    if custom.exists():
        with open(custom, "r", encoding="utf-8") as fh:
            data = yaml.safe_load(fh) or {}
        convs = data.get("conversations", [])
        trainer = ListTrainer(bot)
        for conv in convs:
            trainer.train(conv)
