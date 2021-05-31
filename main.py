from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import discord
from pypresence import Presence
import requests
import imdb
#import wikipediaapi

client = commands.Bot(command_prefix = "." , intents = discord.Intents.all())

#
#
#bot init
@client.event
async def on_ready():
    print("BOT is up and Running")
    await client.change_presence(status=discord.Status.idle,activity=discord.Game("watching something cool"))

#
#
#error handling
@client.event
async def on_command_error(ctx,error):
    await ctx.send(error)

#
#
#main block
@client.command(aliases=['search','movie_search','imdb'])
async def movie(ctx,*,movie:str):

    async with ctx.typing():
        moviesDB = imdb.IMDb()
        searched_movies = moviesDB.search_movie_advanced(movie,adult=True)
        movie_id = searched_movies[0].getID()
        movie_result = moviesDB.get_movie(movie_id)

        title = movie_result['title']
        description=movie_result['plot'][0]
        year = movie_result['year']
        rating = movie_result['rating']
        directors = movie_result['directors']
        movie_directors=' '.join(map(str,directors))
        genre= movie_result['genres']
        movie_genre=', '.join(map(str,genre))
        movie_image=movie_result['cover url']

        embed = discord.Embed(
            title = title,
            description=description,
            colour = discord.Colour.blue()
        )

        embed.set_footer(text='By IMDB')
        embed.set_image(url=movie_image)
        #embed.set_thumbnail(url=movie_image)
        embed.set_author(name='Movie Search',icon_url='https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/IMDB_Logo_2016.svg/1200px-IMDB_Logo_2016.svg.png')
        embed.add_field(name='Year',value=year , inline=False)
        embed.add_field(name='Rating',value=rating , inline=False)
        embed.add_field(name='Director',value=movie_directors , inline=False)
        embed.add_field(name="Genre",value=movie_genre,inline=False)

        await ctx.send(embed=embed)


# @client.command()
# async def cast(ctx,*,cast_name:str):
#     moviesDB = imdb.IMDb()
#     cast_search = imdb.search_person(cast_name)
#     cast_id = cast_search[0].getID()
#     cast_search = moviesDB.get_person(cast_id)
    
#     title = cast_search['name']
#     dob = cast_search['birth date']
#     awards = cast_search['awards']
#     description = cast_search['biography']
#     age = cast_search['age']

#     embed = discord.Embed(
#         title = title,
#         description=description,
#         colour = discord.Colour.dark_orange()
#     )

#     embed.set_footer(text='By IMDB')
#     embed.set_image(url=movie_image)
#     #embed.set_thumbnail(url=movie_image)
#     embed.set_author(name='Movie Search',icon_url='https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/IMDB_Logo_2016.svg/1200px-IMDB_Logo_2016.svg.png')
#     embed.add_field(name='Year',value=year , inline=False)
#     embed.add_field(name='Rating',value=rating , inline=False)
#     embed.add_field(name='Director',value=movie_directors , inline=False)
#     embed.add_field(name="Genre",value=movie_genre,inline=False)

#     await ctx.send(embed=embed)



client.run("NzQzMTU0MjMwMjY4OTE5ODY4.XzQiTw.RXVJWUG8k0OJHRzaTpawbJVtOxs")
