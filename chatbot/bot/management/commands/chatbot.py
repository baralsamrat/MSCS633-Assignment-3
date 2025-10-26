from django.core.management.base import BaseCommand
from django.conf import settings
from pathlib import Path
import os
from bot.chatter import get_chatbot, initial_train

class Command(BaseCommand):
    help = "Run a terminal chat session with ChatterBot"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Booting TerminalBot..."))
        bot = get_chatbot()
        if not Path(settings.CHATTERBOT_DB_PATH).exists():
            self.stdout.write("Training new bot...")
            initial_train(bot)
        self.stdout.write("Type :quit to exit.")

        while True:
            user_input = input("user: ").strip()
            if user_input.lower() in {":quit", ":exit"}:
                print("bot: Goodbye!")
                break
            elif user_input.lower() == ":reset":
                os.remove(settings.CHATTERBOT_DB_PATH)
                initial_train(bot)
                continue
            response = bot.get_response(user_input)
            print(f"bot: {response}")
