import discord,random,os
from discord.ext import commands,tasks
from itertools import cycle
from drive_imports import download



bot = commands.Bot(command_prefix='.',case_insensitive=True)
bot.remove_command('help')



@bot.command()
async def leaderboard(ctx):
    count_table = {}
    with open('quote_book.txt','r',encoding='utf-8') as f:
        for line in f:
            temp = line.split('-')
            name = temp[1].replace('\n','')
            if name in count_table:
                count_table[name] = count_table[name]+1
            else:
                count_table[name] = 1 

    my_keys = sorted(count_table, key=count_table.get, reverse=True)[:3]
    
    await ctx.send(f'```The Most Quoted List\n\n1){my_keys[0]} - {count_table[my_keys[0]]} unique quotes\n\n2){my_keys[1]} - {count_table[my_keys[1]]} unique quotes\n\n3){my_keys[2]} - {count_table[my_keys[2]]} unique quotes\n\nTo get on here, perhaps be funny```')

    


@bot.command()
async def quotebook(ctx):
    quote_arr = []
    with open('quote_book.txt','r',encoding='utf-8') as f:
        quote_arr = f.readlines()
    random_quote = quote_arr[random.randint(0,len(quote_arr)-1)]
    await ctx.send(random_quote)

@bot.command()
async def quote(ctx,args):
    quote_arr = []
    with open('quote_book.txt','r',encoding='utf-8') as f:
        for line in f:
            temp = line.split('-')
            if args.upper() in temp[1].upper():
                quote_arr.append(line)
    try:
        random_quote = quote_arr[random.randint(0,len(quote_arr)-1)]
        await ctx.send(random_quote)
    except:
        await ctx.send(f'{args}, get in the quote book bozo.')

@bot.command()
async def help(ctx):
    await ctx.send('```.leaderboard - Lists the top 3 most commonly quoted people in the quotebook\n\n.quotebook - Gives you a random quote from the boys\n\n.quote (name) - Gives a random quote from a specified person\n\n.help - Lists all available commands```')



if __name__ == '__main__':
    
    os.chdir(r'text')
    try:
        download()
    except:
        print('File Download Failed')

    bot.run('API-KEY-HERE')


            
