import discord
from discord.ext import commands
import os
from os.path import join, dirname
from dotenv import load_dotenv
import random

# Create .env file path.
dotenv_path = join(dirname(__file__), '.env')

# Load file from the path.
load_dotenv(dotenv_path)

# Gets the token from the '.env'-file, in which it is called SECRET_KEY.
token = os.getenv('SECRET_KEY')
bot = commands.Bot(command_prefix='.')


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))  # Prints to console.


@bot.command(name='Ping!', aliases=['Ping', 'ping!', 'ping'],
             help='Responds with the ping-time, in milli-seconds (ms).')
async def ping(ctx):
    await ctx.send(f'Pong! ({round(bot.latency * 1000)} ms)')


@bot.command(name='8-Ball', aliases=['8ball', '8Ball', '8-ball',
                                     'Magic-8-Ball', 'Magic-8-ball', 'magic-8-ball', 'm8b', 'M8B', 'm8B', 'M8b'],
             help='Write the command, followed by the question.')
async def _8ball(ctx, *, question):
    ball_responses = [
        "It is certain",
        "Without a doubt",
        "You may rely on it",
        "Yes definitely",
        "It is decidedly so",
        "As I see it, yes",
        "Most likely",
        "Yes",
        "Outlook good",
        "Signs point to yes",
        "Reply hazy try again",
        "Better not tell you now",
        "Ask again later",
        "Cannot predict now",
        "Concentrate and ask again",
        "Don't count on it",
        "Outlook not so good",
        "My sources say no",
        "Very doubtful",
        "My reply is no"
    ]

    await ctx.send(f'{ctx.message.author.mention} asked: \'{question}\'\nAnswer: {random.choice(ball_responses)}')


@bot.command(name='Office', aliases=['The-Office', 'TO', 'to', 'office', 'the-office', 'The-office', 'the-Office'],
             help='Responds with a random one-liner, from \"The Office\".')
async def office(ctx):
    office_responses = [
        'I just want to lie on the beach and eat hot dogs.',  # Kevin Malone
        'Where are the turtles?!',  # Micheal Scott
        'If I don\'t have some cake soon, I might die.',  # Stanley Hudson
        'Who is Justice Beaver?',  # Dwight Schrute
        'There\'s too many people on this earth, we need a new plague',  # Dwight Schrute
        'I don\'t care what they say about me... I just want to eat.',  # Pam Beesley
        'I am Beyoncé always.',  # Michael Scott
        'I want to be wined, dined, and sixty-nined.',  # Kevin Malone
        'Why are you the way that you are?',  # Michael Scott
        'I hate looking at your face, I wanna smash it.',  # Michael Scott
        'I am better than you have ever been, or ever will be.',  # Dwight Schrute
        (
            'Sometimes when I start a sentence, I don\'t even know where it\'s'
            ' going, I just hope I find it along the way.'  # Michael Scott
        ),
        'Sorry I annoyed you with my friendship',  # Andy Bernard
        'Dwight, you ignorant slut!',  # Michael Scott
        'Well, happy birthday, Jesus. Sorry your party\'s so lame.',  # Michael Scott
        'You don\'t know me; you\'ve just seen my penis.',  # Michael Scott
        'Apart from hitting her with my car, I have been so kind to that woman.',  # Michael Scott
        'That\'s what she said'  # Michael Scott
    ]
    await ctx.send(f'{random.choice(office_responses)}')


# @bot.command()
# async def help(ctx):
#    helpText = (
#        'List of commands in (not) Alphabetical order:'
#        '\n.Ping! - Responds with the ping-time, in milli-seconds (ms).'
#        '\n.8-Ball - Write the command, followed by the question, and let the 8-ball do it\'s magic.'
#        '\n.99! - Responds with a random one-liner, from \"Brooklyn nine-nine\".'
#        '\n.TO - Responds with a random one-liner, from \"The Office\".'
#    )
#    await ctx.send(f'{helpText}')


@bot.command(aliases=['Play', 'play!', 'Play!'], help='Don\'t.')
async def play(ctx, ):
    await ctx.send('Who do you think I am? Fucking Groovy? Fuck off. God, I\'m so tired of you people.')


@bot.command(name='99!', aliases=['99', 'Nine-nine!', 'Nine-Nine!', 'nine-nine!',
                                  'nine-nine', 'Nine-nine', 'Nine-Nine'],
             help='Responds with a random one-liner, from \"Brooklyn nine-nine\".')
async def _99(ctx):
    nine_responses = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
        'Desperate times call for Desperate Housewives',
        'That\'s a nice thought.... for *an idiot* to have.',
        '...Title of your sex tape.',
        'Aw, man. All the orange soda spilled out of my cereal.',
        (
            'I wasn\'t hurt that badly. The doctor said all my bleeding '
            'was internal. That\'s where the blood\'s supposed to be.'
        ),
        'It\'s Gina\'s phone. Leave me a voice-mail. I won\'t check it \'cause it\'s not 1993.',
        (
            'Wait, first, let\'s say a prayer. Dear Beyonce, Solange, Rihanna, someone cool that\'s white, '
            'Cardi B, please bless this flush. \nA-women.'
        ),
        'I also have a hairline fracture in my thumb. Mankind\'s least important finger, am I right?',
        'The only reason I didn\'t tell you is I don\'t value you as people, so why be honest?',
        'Breakups are a cartoony thumbs down. They make people feel face-with-Xs-for-the-eyes.',
    ]
    await ctx.send(f'{random.choice(nine_responses)}')

bot.run(token)
