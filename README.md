A simple discord bot that imports a quote book from google drive and generates a random quote from the .txt file on request in discord.

PLEASE SUBMIT TO THE quote_book.txt IN THE FORMAT: > 'insert quote here' - Name of author

Some of the source needs to be edited in order for the code to run, including the discord bot token of your bot in the discord_bot.py file, as well as the corresponding google drive file id of your text file into the drive_imports.py file.

The google drive import function is not necessary, but if it is desired to be used, the client_secert.json and and the token_drive_v3.pickle file are needed in the same WD as the program, which be be obtained via the google drive API.

This bot has 4 main command:

.quote - randomly quotes a person from the quote_book.txt

.quotebook (name) - quotes a selected person from the quotebook, if no quotes exist, returns as such

.leaderboard - returns the top 3 most quoted people

.help - lists all available commands

