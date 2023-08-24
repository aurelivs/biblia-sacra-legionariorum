import discord
import re
from book_lists.books import at_1, at_2, nt_1, nt_2
from discord.ext import commands
from functions import pegar_versiculo


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents)

@bot.slash_command(
    name="biblia1",
    description='25 primeiros livros do Antigo Testamento'
    )

@discord.option(
        name='livro', 
        description='Selecione um livro do Antigo Testamento', 
        required=True, 
        choices=at_1
    )

@discord.option(
        name='capitulo_e_versiculo', 
        description='Especificar o capítulo e o versículo', 
        required=True
    )

async def biblia1(
        ctx,
        livro,
        capitulo_e_versiculo: str
    ):
    capitulo_e_versiculo = livro + ' ' + capitulo_e_versiculo
    match = re.match(
        r'^(.+) (\d+),(\d+)(-(\d+))?$',
        capitulo_e_versiculo.strip()
    )
    
    print(capitulo_e_versiculo)
    print(match)
    
    if match:
        nome, cap, vers_inicio, _, vers_fim = match.groups()
        
        vers_texto = pegar_versiculo(
            nome, 
            cap, 
            vers_inicio, 
            vers_fim
        )
        
        await ctx.respond(vers_texto)

@bot.slash_command(
        name="biblia2",
        description='21 últimos livros do Antigo Testamento'
    )

@discord.option(
        name='livro',
        description='Selecione um livro do Antigo Testamento', 
        required=True, 
        choices=at_2
    )

@discord.option(
        name    =   'capitulo_e_versiculo', 
        description =   'Especificar o capítulo e o versículo', 
        required    =   True
    )

async def biblia2(
        ctx,
        livro,
        capitulo_e_versiculo: str
    ):
    capitulo_e_versiculo    =   livro + ' ' + capitulo_e_versiculo
    match = re.match    (
        r'^(.+) (\d+),(\d+)(-(\d+))?$',
        capitulo_e_versiculo.strip()
    )
    
    print(capitulo_e_versiculo)
    print(match)
    
    if match:
        nome, cap, vers_inicio, _, vers_fim = match.groups()
        vers_texto = pegar_versiculo(nome, cap, vers_inicio, vers_fim)
        
        await ctx.respond(vers_texto)

@bot.slash_command(
        name="biblia3",
        description='25 primeiros livros do Novo Testamento'
    )

@discord.option(
        name='livro', 
        description='Selecione um livro do Novo Testamento', 
        required=True, 
        choices=nt_1
    )

@discord.option(
        name='capitulo_e_versiculo', 
        description='Especificar o capítulo e o versículo', 
        required=True
    )

async def biblia3(
        ctx,
        livro,
        capitulo_e_versiculo: str
    ):
    capitulo_e_versiculo = livro + ' ' + capitulo_e_versiculo
    match = re.match(r'^(.+) (\d+),(\d+)(-(\d+))?$', capitulo_e_versiculo.strip())
    
    print(capitulo_e_versiculo)
    print(match)
    
    if match:
        nome, cap, vers_inicio, _, vers_fim = match.groups()
        vers_texto = pegar_versiculo(nome, cap, vers_inicio, vers_fim)
        
        await ctx.respond(vers_texto)

@bot.slash_command(
        name="biblia4",
        description='2 últimos livros do Novo Testamento'
    )

@discord.option(
    name='livro', 
    description='Selecione um livro do Novo Testamento', 
    required=True, 
    choices=nt_2
    )

@discord.option(
        name='capitulo_e_versiculo', 
        description='Especificar o capítulo e o versículo', 
        required=True
    )

async def biblia4(
        ctx,
        livro,
        capitulo_e_versiculo: str
    ):
    capitulo_e_versiculo = livro + ' ' + capitulo_e_versiculo
    match = re.match(r'^(.+) (\d+),(\d+)(-(\d+))?$', capitulo_e_versiculo.strip())
    
    print(capitulo_e_versiculo)
    print(match)
    
    if match:
        nome, cap, vers_inicio, _, vers_fim = match.groups()
        vers_texto = pegar_versiculo(nome, cap, vers_inicio, vers_fim)
        await ctx.respond(vers_texto)


bot.run(TOKEN)
