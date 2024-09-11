# AODPlayerCountBot
This is a Discord bot written in Python that fetches and displays the current player count and maximum player capacity for Age of Dino Sandbox (The Isle Legacy).  

How to Use This Discord Bot

This guide will help you set up and run the Discord bot that provides player count information for a game server.
Prerequisites

    Python 3.6 or higher: Ensure Python is installed on your system.
    A Discord Bot Token: You’ll need to create a bot on the Discord Developer Portal to get a token.

Setup Instructions

    Clone the Repository

    First, clone this repository to your local machine:

    bash

git clone https://github.com/yourusername/discord-player-count-bot.git
cd discord-player-count-bot

Create a Virtual Environment (Optional but recommended)

It’s a good practice to use a virtual environment to manage dependencies:

bash

python -m venv venv

Activate the virtual environment:

    Windows:

    bash

venv\Scripts\activate

macOS/Linux:

bash

    source venv/bin/activate

Install Dependencies

Install the required Python packages using pip:

bash

pip install -r requirements.txt

Create a .env File

In the root directory of the project, create a file named .env with the following content:

plaintext

DISCORD_API_TOKEN=YOUR_DISCORD_BOT_TOKEN

Replace YOUR_DISCORD_BOT_TOKEN with the token you obtained from the Discord Developer Portal.

Run the Bot

Execute the script to start the bot:

bash

    python bot.py

    Invite the Bot to Your Server

    To invite the bot to your Discord server, generate an OAuth2 URL from the Discord Developer Portal with the appropriate permissions (usually, Send Messages and Read Messages are sufficient).

Commands

    !aod: Use this command in a Discord channel where the bot is present to get the current player count and the maximum player capacity of the game server.
