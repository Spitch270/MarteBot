#Author : CUNY Félicien
#Language : FR - French
#Date : 03/12/2020
#Copyright : This code can be use for every member working on 'Marte Bot' discord bot only. If you want to work on it, please contact me : felicien.cuny@outlook.fr

import discord #importation des modules discord
import os #pour les cogs si besoin
from discord.ext import commands, tasks#importation des fonctions pour discord bot

martebot = commands.Bot(command_prefix = '$') #prefixe à utiliser pour intéragir avec le bot

@martebot.event #Déclarer à chaque fois que l'on veut une action du bot
async def on_ready(): #lancement du bot en ligne
    await martebot.change_presence(status=discord.Status.idle, activity=discord.Game('Scroll sur TikTok')) #change le "jeu" auquel joue le bot
    print('Le bot est pret') #indique que le bot est lancé.

@martebot.command() #Déclarer à chaque fois que l'on veut utiliser le bot
async def ping(ctx): #ping = nom de la commande; exemple $ping pourra être utiliser sur discord pour trigger le bot
    await ctx.send("Pong !")

@martebot.command()


martebot.run('Token')
