#LIF BOT
from itertools import cycle
import discord
from discord.ext import commands, tasks
import time
import platform
import random
import asyncio

intents = discord.Intents.default()
intents.members = True
intents.guilds = True

description = "BOT feito exclusivo para a LIF, por: RickDB17. Uso somente da Staff. \nDigite `/help` para ver seus comandos!"

client = commands.Bot(
    command_prefix=commands.when_mentioned_or('/'), 
    case_insensitive = True, 
    description = description, 
    hidden=False, 
    intents=intents
    )

invite = discord.Invite
TOKEN = 'TOKEN'
version = '0.1.0'


entrada_ch = 766669343165120553
entrada_r = 'entrada'
login_ch = 766672957698474004
suporte_ch = 766673399409016862
staff = 'staff'
adm = 'General'
ativo = 'ativos'
contas_ch = 766673746181619752
log_ch = 766696332005081168
warn_log = 766674053439553537

########################################################################

# START
@client.event
async def on_ready():
    print('----------------------------------------------------')
    print(f'Entrou como {client.user}')
    print(f'bot_id: {client.user.id}')
    print(f"discord.py version: {discord.__version__}")
    print('----------------------------------------------------')
    print('     ███ ]▄▄▄▄▄▃  / Bora Tropa! LIF no comando!')
    print('  ▂▄▅█████▅▄▃▂         \ __|_  /           __  _')
    print('[███████████████]    - /    \ -        __/  \|')
    print('__◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤__/\__,--|_____|,---_____/')
    print('      ___                   ___           ')
    print('     /\__\      ___        /\  \          ')
    print('    /:/  /     /\  \      /::\  \         ')
    print('   /:/  /      \:\  \    /:/\:\  \        ')
    print('  /:/  /       /::\__\  /::\~\:\  \       ')
    print(' /:/__/     __/:/\/__/ /:/\:\ \:\__\      ')
    print(' \:\  \    /\/:/  /    \/__\:\ \/__/      ')
    print('  \:\  \   \::/__/          \:\__\        ')
    print('   \:\  \   \:\__\           \/__/        ')
    print('    \:\__\   \/__/                        ')
    print('     \/__/                                ')
    print('      ___           ___           ___     ')
    print('    /::\  \       /::\  \        \:\  \   ')
    print('   /:/\:\  \     /:/\:\  \        \:\  \  ')
    print('  /::\~\:\__\   /:/  \:\  \       /::\  \ ')
    print(' /:/\:\ \:|__| /:/__/ \:\__\     /:/\:\__\ ')
    print(' \:\~\:\/:/  / \:\  \ /:/  /    /:/  \/__/')
    print('  \:\ \::/  /   \:\  /:/  /    /:/  /     ')
    print('   \:\/:/  /     \:\/:/  /     \/__/      ')
    print('    \::/__/       \::/  /                 ')
    print('                   \/__/                  ')
    
    game = discord.Game("/help")
    stream = discord.Streaming(name='/help', url='https://ifunny.co')
    await client.change_presence(status=discord.Status.idle, activity=game)


async def change_presece():
    await client.wait_until_ready()

    statuses = ['Pai tá on B) \n RickDB17', 'Use /liberar_dm, no: #comandos-do-bot para liberar a DM.','Use /help | LIFBOT \n ', 'Use /help | LIFBOT \n RickDB17']

    while not client.is_closed():
        status = random.choice(statuses)
        await client.change_presence(status=discord.Status.idle, activity=discord.Game(status))

        await asyncio.sleep(30)
client.loop.create_task(change_presece())


########################################################################


## LIBERAR DEPOIS DOS TESTES
# Falta de argumento ou permissão
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Por favor preencha  todos os requerimentos, veja o /help <cmd>. :rolling_eyes:.')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Sem permissões, configure o canal. :angry:")



# Quando um membro entrar, o bot vai dar cargo de 'etapa1' e vai mandar msg na dm.
@client.event
async def on_member_join(member: discord.Member):

    # EMBED - welcome
    aviso = discord.Embed(title=f"Bem-vindo, {member.name}!",
                    description=f"```Seja bem vindo À LIF, siga as instruções de login e leia as regras```",
                    color=0xffdd00)
    aviso.set_thumbnail(url="https://cdn.discordapp.com/icons/696132213598584942/a_ba5909ec4dbad809bf85db696ee97f04.gif")
    # Chat de login
    aviso.add_field(name="Teleporte: ",
        value=f"<#{login_ch}>",
        inline=False)
    aviso.add_field(name='Como logar:',
                    value=f'Vá no chat indicado, digite `/login`, leia as regras, aceite na reação e mande seu link de usuário do ifunny. Caso o bot não mande uma confirmação de login, repita o procedimento, se persistir, chame por @General, @Coronel ou @Capitão no <#{suporte_ch}>.',
                    inline=False)
    
    # Canal de entrada
    ch = client.get_channel(entrada_ch)
    # Cargo de entrada
    role = discord.utils.get(member.guild.roles, name = entrada_r)

    await member.add_roles(role)
    await ch.send(f"{member.mention}")
    await ch.send(embed=discord.Embed(
        title=f"Olá, {member.name}",
        description=f"{member.mention}Vá em configurações, privacidade e segurança, e então ative: 'Permitir mensagens diretas de membros do servidor' para um melhor funcionamento do server e do Bot.\n \
Ou Use /liberar_dm no <#696132812989792296>. Até lá, vá em <#{login_ch}>, mande `/login` e siga as instruções.",
        color=0xffdd00)
        )
    
    await member.send(embed=aviso)


# Login
@client.command()
@commands.has_any_role(adm, entrada_r)
async def login(ctx):
    try:
        ch = client.get_channel(login_ch)
        if ctx.channel == ch:

            # EMBED
            # mandar as regras
            embed=discord.Embed(title="Regras",
                                url="https://br.ifunny.co",
                                description="```A proposta desse grupo é incentivar os iFunnyers a criar memes originais, conhecer sobre as regras do iFunny, se unir e fazer novas amizades, impedir que posts impróprios continuem a poluir nosso coletivo, divulgar memes e perfis legais e, o mais importante, se divertir...```",
                                color=0xffdd00)
            embed.set_thumbnail(url="https://cdn.discordapp.com/icons/696132213598584942/a_ba5909ec4dbad809bf85db696ee97f04.gif")
            embed.add_field(name="São proibidos:",
                            value="...",
                            inline=False)
            embed.add_field(name="1. Porn",
                            value="É proibido compartilhar conteúdos pornográficos no server;", inline=False)
            embed.add_field(name="2. Discussões",
                            value="É proibido discussões de cunho religioso ou político! só se for zoeira, aí pode hehe;",
                            inline=False)
            embed.add_field(name="3. Toxidade",
                            value="É proibido humilhar amiguinhos; Respeito é sempre bom, então evite brigas;",
                            inline=False)
            embed.add_field(name="4. Dados pessoais",
                            value="É proibido divulgar dados pessoais de outros usuários no grupo. Caso alguém queira compartilhar as suas informações pessoais fica por conta e risco, mas não é recomendado;", inline=False)
            embed.add_field(name="5. Respeito à hierarquia",
                            value="Respeite o seu superior. Pode zoar mas com moderação hehehe;",
                            inline=False)
            embed.add_field(name="6. Zoeira e piada",
                            value="Permitido zoeiras de humor negro, no entanto aprecie essa regra com moderação;",
                            inline=False)
            embed.add_field(name="7. Cumprir as regras do iFunny",
                            value="Qualquer iFunnyer que for pego postando conteúdos impróprios ou kibes será intimado a remover o post. Caso se recuse a fazer o solicitado o iFunnyer será banido do grupo e pode levar um banimento no próprio iFunny (lembrando que temos moderadores no grupo); Para mais, veja: <#696133741369622538>",
                            inline=False)
            embed.add_field(name="8. Novos membros",
                            value=" É permitido qualquer membro no grupo que respeite as regras do iFunny, no entanto somente membros de patente alta possui permissão para add novos membros;", inline=False)
            embed.add_field(name="9. Promoções",
                            value="As graduações de cargo serão fornecidas de acordo com a produtividade do iFunnyer no grupo e no iFunny, principalmente conteúdos de memes criados e postados. Usuários que postam memes de outras plataformas não serão promovidos mas podem permanecer no grupo;",
                            inline=False)
            embed.add_field(name="10. Chats",
                            value="Usem os chats de forma organizada, cada um tem uma função, respeitem isso;",
                            inline=False)
            embed.add_field(name="Aceitar Permissões",
                            value="Para aceitar as permissões reaja com :white_check_mark:.\n Agora mande seu link de usuário o ifunny.\nSe não aparecer a mensagem 'Loggado!' você deve repetir o comando '/login' e as etapas da forma correta.",
                            inline=False)
            embed.set_footer(text="By: Adiministração")

            # envio + emoji
            msg = await ctx.send(embed=embed)
            #emj = client.get_emoji(762142621002104853)
            await msg.add_reaction('\N{WHITE HEAVY CHECK MARK}') 

            @client.event 
            async def on_reaction_add(reaction, member):
                print(reaction, member)
                @client.event
                async def on_message(message):

                    if message.content.startswith('https://br.ifunny.co/user/') or message.content.startswith('https://ifunny.co/user/'):
                        role1 = discord.utils.get(member.guild.roles, name = entrada_r)
                        role2 = discord.utils.get(member.guild.roles, name = 'Recruta')
                        role3 = discord.utils.get(member.guild.roles, name = ativo)

                        # EMBED
                        loggado=discord.Embed(title="Loggado!",
                                url=f"{message.content}",
                                description="```Parabéns, usuário. Seu login foi feito com sucesso!\nSiga as regras da LIF.```",
                                color=0xffdd00)
                        loggado.set_thumbnail(url="https://cdn.discordapp.com/icons/696132213598584942/a_ba5909ec4dbad809bf85db696ee97f04.gif")
                        loggado.add_field(name="Vá para:", value=f'<#{696132778483253269}>')

                        await message.add_reaction('\N{WHITE HEAVY CHECK MARK}') 
                        await ctx.send(embed= discord.Embed(title="Concluído!", color=0xffdd00))

                        # EMBED
                        dm_req = discord.Embed(title="Sucesso!",
                        url="https://br.ifunny.co",
                        description=f"{ctx.author.mention} se não chegar nenhuma mensagem na dm, configure seu usuário para receber mensagem de membros do server. Veja mais com liberar_dm.",
                        color=0xffdd00)


                        await ctx.send(embed=dm_req)
                        await ctx.author.add_roles(role3)
                        await ctx.author.add_roles(role2)
                        await ctx.author.remove_roles(role1)

                        print(message)

                        channel = client.get_channel(contas_ch)

                        # EMBED
                        login_sucesso = discord.Embed(title="Novo usuário loggado!",
                                url=f"{message.content}",
                                description=f"```Um novo usuário entrou no grupo, segue suas informações:```",
                                color=0xffdd00)
                        login_sucesso.set_thumbnail(url="https://cdn.discordapp.com/icons/696132213598584942/a_ba5909ec4dbad809bf85db696ee97f04.gif")
                        login_sucesso.add_field(name="Usuário:",
                            value=f"<@{message.author.id}>",
                            inline=False)
                        login_sucesso.add_field(name="ID do Discord:",
                            value=f"{message.author.id}",
                            inline=False)
                        login_sucesso.add_field(name="Link do iFunny:",
                            value=f"{message.content}",
                            inline=False)

                        await channel.send(f'Use `Ctrl` + `F` >> `mentions:` + `<user name>` para pesquisar.\n /checkpoint: <@{message.author.id}>')
                        await channel.send(embed=login_sucesso)
                        time.sleep(30)
                        await ctx.author.send(embed=loggado)

    except discord.Forbidden:
        error = discord.Embed(title="ERRO!",
                    description = f"{ctx.author.mention} você tem a `DM` bloqueada, favor, desbloquear, como mencionado na <#758714947261169685>.",
                    color=0xffdd00)
        c = client.get_channel({log_ch})
        return await c.send(embed=error)
        await c.send(f'{ctx.author.mention}')



# Regras
@client.command(name='rules', aliases=['regras'])
@commands.has_any_role('General')
async def rules(ctx):
    embed=discord.Embed(title="Regras",
                        url="https://br.ifunny.co",
                        description="```A proposta desse grupo é incentivar os iFunnyers a criar memes originais, conhecer sobre as regras do iFunny, se unir e fazer novas amizades, impedir que posts impróprios continuem a poluir nosso coletivo, divulgar memes e perfis legais e, o mais importante, se divertir...```",
                        color=0xffdd00)
    embed.set_thumbnail(url="https://cdn.discordapp.com/icons/696132213598584942/a_ba5909ec4dbad809bf85db696ee97f04.gif")
    embed.add_field(name="São proibidos:",
                    value="...",
                    inline=False)
    embed.add_field(name="1. Porn",
                    value="É proibido compartilhar conteúdos pornográficos no server;", inline=False)
    embed.add_field(name="2. Discussões",
                    value="É proibido discussões de cunho religioso ou político! só se for zoeira, aí pode hehe;",
                    inline=False)
    embed.add_field(name="3. Toxidade",
                    value="É proibido humilhar amiguinhos; Respeito é sempre bom, então evite brigas;",
                    inline=False)
    embed.add_field(name="4. Dados pessoais",
                    value="É proibido divulgar dados pessoais de outros usuários no grupo. Caso alguém queira compartilhar as suas informações pessoais fica por conta e risco, mas não é recomendado;", inline=False)
    embed.add_field(name="5. Respeito à hierarquia",
                    value="Respeite o seu superior. Pode zoar mas com moderação hehehe;",
                    inline=False)
    embed.add_field(name="6. Zoeira e piada",
                    value="Permitido zoeiras de humor negro, no entanto aprecie essa regra com moderação;",
                    inline=False)
    embed.add_field(name="7. Cumprir as regras do iFunny",
                    value="Qualquer iFunnyer que for pego postando conteúdos impróprios ou kibes será intimado a remover o post. Caso se recuse a fazer o solicitado o iFunnyer será banido do grupo e pode levar um banimento no próprio iFunny (lembrando que temos moderadores no grupo); Para mais, veja: <#696133741369622538>",
                    inline=False)
    embed.add_field(name="8. Novos membros",
                    value=" É permitido qualquer membro no grupo que respeite as regras do iFunny, no entanto somente membros de patente alta possui permissão para add novos membros;", inline=False)
    embed.add_field(name="9. Promoções",
                    value="As graduações de cargo serão fornecidas de acordo com a produtividade do iFunnyer no grupo e no iFunny, principalmente conteúdos de memes criados e postados. Usuários que postam memes de outras plataformas não serão promovidos mas podem permanecer no grupo;",
                    inline=False)
    embed.add_field(name="10. Chats",
                    value="Usem os chats de forma organizada, cada um tem uma função, respeitem isso;",
                    inline=False)
    embed.set_footer(text="By: Adiministração")

    # envio
    msg = await ctx.send(embed=embed)

 

@client.command(name='addall', aliases=['aa', 'adicionartodos'])
@commands.has_any_role(adm)
async def addall(ctx, role:discord.Role):
    for m in ctx.guild.members:
        await m.add_roles(role)
    await ctx.send(embed=discord.Embed(title='AVISO!',
                                        description=f'@everyone, parabéns, agora todos são {role.mention}',
                                        color=0xffdd00))

@client.command(name='removeall', aliases=['ra','removertodos'])
@commands.has_any_role(adm)
async def removeall(ctx, role:discord.Role):
    for m in ctx.guild.members:
        await m.remove_roles(role)
        await ctx.send(embed=discord.Embed(title='AVISO!',
                                        description=f'<@{m.id}>, perdeu {role.mention}',
                                        color=0xffdd00))

@client.command()
@commands.has_any_role(adm)
async def role(ctx, arg, member: discord.Member, role: discord.Role):

    if arg == 'add':
        add = discord.Embed(title="Cargo Adicionado!",
                                description=f"{role} foi adicionado à/ao {member.mention}",
                                color=0xffdd00)
        add.set_author(name=f"{ctx.author.name}",
                    icon_url=f"{ctx.author.avatar_url}")
        add.set_thumbnail(url=f"{member.avatar_url}")
        
        await member.add_roles(role)
        await ctx.send(embed=add)
    elif arg == 'remove':
        remove = discord.Embed(title="Cargo Adicionado!",
                            description=f"{role} foi removido da/do {member.mention}",
                            color=0xffdd00)
        remove.set_author(name=f"{ctx.author.name}",
                icon_url=f"{ctx.author.avatar_url}")
        remove.set_thumbnail(url=f"{member.avatar_url}")
    else:
        return await ctx.send(embed= discord.Embed(
            title = 'AVISO!',
            description = "Use `add` ou `remove` como argumentos.",
            color=0xffdd00
        ))
    
    await member.remove_roles(role)
    await ctx.send(embed=remove)



@client.command(name='piada')
@commands.has_any_role('ativos')
async def piada(ctx):
    messages = [
    'Você está caindo de rank mais que o world trade center',
    'Os cachorros sempre lambem o pinto deles, mas quando eu faço isso eles ficam: Ainn solta meu cachorro',
    'Mano, uma vez eu estava no mercado, ai eu vi uma mulher sem os braços levando as compras, ai uma hora ela caiu e tudo caiu no chão, ai eu fui ajudar, cheguei lá e perguntei: Posso te dar uma mão? E ELA SAIU PUTA, porra mulher é foda, a gente da a mão e ela quer o braço',
    'Perguntei pro cadeirante quanto ele calçava ele disse aro 20',
    'Qual o alimento que tem a melhor bunda de todas?  A better raba',
    'Um cara que viu sua mulher o traindo decide se jogar de um prédio, e a mulher fala: "te dei um par de chifres, não um par de asas!"',
    'Garoto islâmico mata irmãs gêmeas',
    'Malhar pra pegar mulher kkkk claro q n malhar pra bater em qm compra fifa todo ano',
    'Piu\nPiu piu\nPiadas acima',
    'Se diz hétero mas ouvi que fica sentado em um tal de sofá',
    'Só tem aids quem faz o exame',
    'Namorar uma solteira é igual a fazer um gol sem goleiro\nNÃO TEM GRAÇA',
    'Um cara estava comendo um bife na cozinha e chegou sua prima e disse:\n-Espero que esteja gostando da carne assassino.\nEntão o cara respondeu:\n-Eu já pedi desculpas por ter matado sua mãe, me deixe em paz'
    ]
    msg = random.choice(messages)
    await ctx.channel.send(embed=discord.Embed(name=f'Piada',
    description = f'{msg}',
    color=0xffdd00))    

@client.group(name='pedir')
@commands.has_any_role(ativo)
async def pedir(ctx):

    solicitação = 766114727100285038
    pedido_ch = 766116146902204416

    if ctx.channel == client.get_channel(solicitação):

        # EMBED
        aviso = discord.Embed(title="AVISO!",
                        description=f"```Erro no comando, faltam argumentos.```",
                        color=0xffdd00)
        aviso.set_thumbnail(url="https://cdn.discordapp.com/icons/696132213598584942/a_ba5909ec4dbad809bf85db696ee97f04.gif")
        aviso.add_field(name="Para pedir um banner, use:",
            value=f"`/pedir banner [descrição]`",
            inline=False)
        aviso.add_field(name="Para pedir um selo, use:",
            value=f"`/pedir selo [descrição]`",
            inline=False)
        aviso.add_field(name="Para pedir uma base, use:",
            value=f"`/pedir base [descrição]`",
            inline=False)

        await ctx.send(embed=aviso)

@pedir.command(name='banner', aliases = ['capa', 'cover'])
async def banner(ctx, *, descrição):
    await ctx.channel.purge(limit=1)
    solicitação = 766114727100285038
    pedido_ch = 766116146902204416
    r = 'EditorDeBanners'
    h_ = int(ctx.message.created_at.hour)
    if h_ == 0:
        h = 21
    elif h_ == 1:
        h = 22
    elif h_ == 2:
        h = 23
    elif h_ == 3:
        h = 0
    else:
        h = h_ - 3

    if  descrição == None:

        # EMBED
        aviso1 = discord.Embed(title="AVISO!",
            description=f"```Erro no comando, descrição não determinada.```\nUse: `/pedir banner [descrição]`",
            color=0xffdd00)
        aviso1.set_thumbnail(url="https://cdn.discordapp.com/icons/696132213598584942/a_ba5909ec4dbad809bf85db696ee97f04.gif")
        
        await ctx.send(embed=aviso1)
        return

    elif descrição != None:
        role = discord.utils.get(ctx.guild.roles, name = r)
        ch = client.get_channel(pedido_ch)

        await ctx.message.add_reaction('\N{WHITE HEAVY CHECK MARK}')

        # EMBED
        sucesso = discord.Embed(title="Sucesso!",
            description=f"{ctx.author.mention} seu pedido foi enviado, logo um dos editores deve te chamar na dm.",
            color=0xffdd00)
        sucesso.set_thumbnail(url="https://cdn.discordapp.com/icons/696132213598584942/a_ba5909ec4dbad809bf85db696ee97f04.gif")
        
        # EMBED
        pedido = discord.Embed(title="Novo pedido!",
            description=f"```Um usuário quer um banner.```",
            color=0xffdd00)
        pedido.set_thumbnail(url="https://cdn.discordapp.com/icons/696132213598584942/a_ba5909ec4dbad809bf85db696ee97f04.gif")
        pedido.add_field(name="Usuário:",
            value=f"<@{ctx.author.id}>",
            inline=False)
        pedido.add_field(name="Enviado:",
            value=f"```({h}:{ctx.message.created_at.minute}) {ctx.message.created_at.day}/{ctx.message.created_at.month}/{ctx.message.created_at.year}```",
            inline=False)
        pedido.add_field(name="Descrição:",
            value=f"```{descrição}```",
            inline=False)
        pedido.set_footer(text="Não se esqueça de adicionar o :white_check_mark: quando aceitar, para que não ocorram conflitos.")


        await ctx.send(f'{ctx.author.mention}')
        await ctx.send(embed=sucesso)
        await ch.send(f'{role.mention}')
        await ch.send(embed=pedido)

@pedir.command(name='selo', aliases = ['marca', 'antikibe', 'logo'])
async def selo(ctx, *, descrição):  
    await ctx.channel.purge(limit=1)
    solicitação = 766114727100285038
    pedido_ch = 766116146902204416
    r = 'EditorDeSelos'
    h_ = int(ctx.message.created_at.hour)
    if h_ == 0:
        h = 21
    elif h_ == 1:
        h = 22
    elif h_ == 2:
        h = 23
    elif h_ == 3:
        h = 0
    else:
        h = h_ - 3


    if descrição == None:

        # EMBED
        aviso1 = discord.Embed(title="AVISO!",
            description=f"```Erro no comando, descrição não determinada.```\nUse: `/pedir selo [descrição]`",
            color=0xffdd00)
        aviso1.set_thumbnail(url="https://cdn.discordapp.com/icons/696132213598584942/a_ba5909ec4dbad809bf85db696ee97f04.gif")
        
        await ctx.send(embed=aviso1)
        return

    elif descrição != None:

        role = discord.utils.get(ctx.guild.roles, name = r)
        ch = client.get_channel(pedido_ch)

        await ctx.message.add_reaction('\N{WHITE HEAVY CHECK MARK}')

        # EMBED
        sucesso = discord.Embed(title="Sucesso!",
            description=f"{ctx.author.mention} seu pedido foi enviado, logo um dos editores deve te chamar na dm.",
            color=0xffdd00)
        sucesso.set_thumbnail(url="https://cdn.discordapp.com/icons/696132213598584942/a_ba5909ec4dbad809bf85db696ee97f04.gif")
        
        # EMBED
        pedido = discord.Embed(title="Novo pedido!",
            description=f"```Um usuário quer um selo.```",
            color=0xffdd00)
        pedido.set_thumbnail(url="https://cdn.discordapp.com/icons/696132213598584942/a_ba5909ec4dbad809bf85db696ee97f04.gif")
        pedido.add_field(name="Usuário:",
            value=f"<@{ctx.author.id}>",
            inline=False)
        pedido.add_field(name="Enviado:",
            value=f"```({h}:{ctx.message.created_at.minute}) {ctx.message.created_at.day}/{ctx.message.created_at.month}/{ctx.message.created_at.year}",
            inline=False)
        pedido.add_field(name="Descrição:",
            value=f"```{descrição}```",
            inline=False)
        pedido.set_footer(text="Não se esqueça de adicionar o :white_check_mark: quando aceitar, para que não ocorram conflitos.")

        await ctx.send(f'{ctx.author.mention}')
        await ctx.send(embed=sucesso)
        await ch.send(f'{role.mention}')
        await ch.send(embed=pedido)

@pedir.command(name='base', aliases = ['template'])
async def base(ctx, *, descrição):  
    await ctx.channel.purge(limit=1)
    solicitação = 766114727100285038
    pedido_ch = 766116146902204416
    r = 'CaçadoresDeBases'
    h_ = int(ctx.message.created_at.hour)
    if h_ == 0:
        h = 21
    elif h_ == 1:
        h = 22
    elif h_ == 2:
        h = 23
    elif h_ == 3:
        h = 0
    else:
        h = h_ - 3

    if descrição == None:

        # EMBED
        aviso1 = discord.Embed(title="AVISO!",
            description=f"```Erro no comando, descrição não determinada.```\nUse: `/pedir base [descrição]`",
            color=0xffdd00)
        aviso1.set_thumbnail(url="https://cdn.discordapp.com/icons/696132213598584942/a_ba5909ec4dbad809bf85db696ee97f04.gif")
        
        await ctx.send(embed=aviso1)
        return

    elif descrição != None:
        role = discord.utils.get(ctx.guild.roles, name = r)
        ch = client.get_channel(pedido_ch)

        await ctx.message.add_reaction('\N{WHITE HEAVY CHECK MARK}')

        # EMBED
        sucesso = discord.Embed(title="Sucesso!",
            description=f"{ctx.author.mention} seu pedido foi enviado, logo um dos caçadores deve te mandar no <#727639370265395241>.\n \
            ```Caso não seja enviado em 48h, é porque seu pedido não foi encontrado.```",
            color=0xffdd00)
        sucesso.set_thumbnail(url="https://cdn.discordapp.com/icons/696132213598584942/a_ba5909ec4dbad809bf85db696ee97f04.gif")
        
        # EMBED
        pedido = discord.Embed(title="Novo pedido!",
            description=f"```Um usuário quer uma base.```",
            color=0xffdd00)
        pedido.set_thumbnail(url="https://cdn.discordapp.com/icons/696132213598584942/a_ba5909ec4dbad809bf85db696ee97f04.gif")
        pedido.add_field(name="Usuário:",
            value=f"<@{ctx.author.id}>",
            inline=False)
        pedido.add_field(name="Enviado:",
            value=f"```({h}:{ctx.message.created_at.minute}) {ctx.message.created_at.day}/{ctx.message.created_at.month}/{ctx.message.created_at.year}",
            inline=False)
        pedido.add_field(name="Descrição:",
            value=f"```{descrição}```",
            inline=False)
        pedido.set_footer(text="Não se esqueça de adicionar o :white_check_mark: quando encontrar e enviar, para que não ocorram conflitos.")

        await ctx.send(f'{ctx.author.mention}')
        await ctx.send(embed=sucesso)
        await ch.send(f'{role.mention}')
        await ch.send(embed=pedido)



# Ping
@client.command(aliases = ['resposta', 'latencia', 'latências', 'lat', 'ms'], description = 'Dá o tempo de resposta do Bot com o servidor em ms' )
@commands.has_any_role(staff)
async def ping(ctx):
    pong = discord.Embed(title="Pong!",
                    description=f"```Você está vendo o meu tempo de resposta em milisegundos.```",
                    color=0xffdd00)
    pong.set_thumbnail(url="https://cdn.discordapp.com/icons/696132213598584942/a_ba5909ec4dbad809bf85db696ee97f04.gif")
    pong.add_field(name="Ping:",
        value=f"{round(client.latency*1000)}ms.",
        inline=False)
    pong.set_footer(text='Para mais informações, use /info.')

    await ctx.send(embed=pong)



#Clear
@client.command(aliases = ['c', 'limpar'], description = 'Limpa o chat, digite uma variável(int); padrão e limite = 100')
@commands.has_any_role(adm)
async def clear(ctx, amount = 100):

    await ctx.channel.purge(limit = amount + 1)
    limpar = discord.Embed(title="Chat Limpo!",
                    color=0xffdd00)
    limpar.set_thumbnail(url="https://cdn.discordapp.com/icons/696132213598584942/a_ba5909ec4dbad809bf85db696ee97f04.gif")
    limpar.add_field(name="Mensagens apagadas:",
        value=f"{amount} mensagens.",
        inline=False)
    limpar.set_footer(text='(Em 20 segundos esse mensagem desaparecerá.)')

    await ctx.send(embed=limpar, delete_after = 20)
    await ctx.send(f'```Chat limpo! {amount} mensagens apagadas.\n(Em 20 segundos esse mensagem desaparecerá.)```', delete_after = 20)



# Carta
@client.group(name='carta', aliases = ['say', 'mandar', 'dizer'])
@commands.has_any_role(staff)
async def carta(ctx):
    msg = discord.Embed(title=f'Escrever Carta',
                        description=f'Para escrever, use:',
                        color=0xffdd00)
    msg.add_field(name='DM',
                  value='/[carta|say|mandar|dizer] [dm|privado|usuário|user|member|membro] [@user(citação)] [mensagem]')
    msg.add_field(name='GUILD',
                  value='/[carta|say|mandar|dizer][guild|server|channel|servidor|canal] [#channel(citação)] [mensagem]')

    msg.set_footer(text=f'{ctx.author.name}')
    await ctx.send(embed=msg)

@carta.command(name='dm', aliases=['privado','usuário','usuario','user','member','membro'])
async def dm_subcmd(ctx, victim:discord.User, message):
    await ctx.channel.purge(limit=1)
    try:
        msg = discord.Embed(title=f'{ctx.guild.name}, {ctx.message.created_at.day}/{ctx.message.created_at.month}/{ctx.message.created_at.year}',
                            description=f'```{message}```',
                            color=0xffdd00)
        msg.set_author(name=f'{ctx.author}',
                       icon_url=f'{ctx.author.avatar_url}')
        msg.set_footer(text=f'{ctx.author.name}')
        await victim.send(embed=msg)
        await ctx.message.add_reaction('\N{WHITE HEAVY CHECK MARK}')
    except discord.Forbidden:
        error = discord.Embed(title="ERRO!",
                description = f"{victim.mention} tem a `DM` bloqueada!",
                color=0xffdd00)
        return await ctx.send(embed=error)

@carta.command(name='guild', aliases=['server','servidor','canal','channel'])
async def dm_subcmd(ctx, channel:discord.TextChannel, message):
    await ctx.channel.purge(limit=1)
    msg = discord.Embed(title=f'{ctx.guild.name}, {ctx.message.created_at.day}/{ctx.message.created_at.month}/{ctx.message.created_at.year}',
                        description=f'```{message}```',
                        color=0xffdd00)
    msg.set_author(name=f'{ctx.author}',
                   icon_url=f'{ctx.author.avatar_url}')
    msg.set_footer(text=f'{ctx.author.name}')
    await channel.send(embed=msg)
    await ctx.message.add_reaction('\N{WHITE HEAVY CHECK MARK}')



# Convites
@client.command(alias = ['convite'])
@commands.has_any_role(staff)
async def invite(ctx, amount=1):

    _amount = int(amount)
    convite = discord.Embed(title="Convite para a Guild da LIF:",
                          description='```Segue o link de convite para o nosso servidor:```',
                          color=0xffdd00)
    convite.add_field(name="Quantidade de usos:",
                    value=f"{amount}")
    convite.add_field(name="Tempo de duração:",
                    value=f"24h")

    ch = client.get_channel(entrada_ch)

    link = await ch.create_invite(max_age = 86400, max_uses = _amount)
    await ctx.send(embed=convite)
    await ctx.send(f"╒                 Convite                 ╕\n\
 {link}\n\
╘      Loucademia IFunny      ╛\n\
.        ███ ]▄▄▄▄▄▃\n\
▂▄▅█████▅▄▃▂\n\
[███████████████]\n\
_◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤\n")



@client.group(name='warn', aliases=['punir'])
@commands.has_any_role(staff)
async def warn(ctx):
    aviso = discord.Embed(title='WARN',
            description='Punir um usuário:',
            color=0xffdd00)
    aviso.add_field(name= 'BANIR', value= '/warn ban @user motivo')
    aviso.add_field(name= 'DESBANIR', value= '/warn ban @user motivo')
    aviso.add_field(name= 'KICK', value= '/warn kick @user motivo')
    aviso.add_field(name= 'DETER', value= '/warn det @user motivo')
    aviso.add_field(name= 'LIBERTAR', value= '/warn desdet @user motivo')
    await ctx.send(embed=aviso)


# Ban - só no canal: #Ban-list, id = 758765312748814377
@warn.command(name = 'ban', aliases = ['banir','b', 'expulsar'], description = 'Na reason, escreva no infinitivo.')
async def ban(ctx, member: discord.User = None, *, reason = None):

    await ctx.channel.purge(limit=1)

    try:
        if reason == None:
            aviso = discord.Embed(title='Falta um motivo!',
            description='Você não pode se banir ninguém sem dar um motivo.',
            color=0xffdd00)
            await ctx.send(embed=aviso)
            return

        if member == None or member == ctx.message.author:
            aviso = discord.Embed(title='Você não pode se banir!',
            description='Você não pode se banir por questões de segurança, tente um usuário.',
            color=0xffdd00)
            await ctx.send(embed=aviso)
            return

        # EMBEDS - BAN

        h_ = int(ctx.message.created_at.hour)
        if h_ == 0:
            h = 21
        elif h_ == 1:
            h = 22
        elif h_ == 2:
            h = 23
        elif h_ == 3:
            h = 0
        else:
            h = h_ - 3
        
        ban = discord.Embed(title="Anotação de Warn.",
                        description=f"```Um usuário foi banido.```",
                        color=0xffdd00)
        ban.set_author(name=f"{ctx.author.name}",
            icon_url=f"{ctx.author.avatar_url}")
        ban.set_thumbnail(url="https://cdn.discordapp.com/icons/696132213598584942/a_ba5909ec4dbad809bf85db696ee97f04.gif")
        ban.add_field(name="Usuário:",
            value=f"<@{member.id}>",
            inline=False)
        ban.add_field(name="ID:",
            value=f"```{member.id}```",
            inline=True)
        ban.add_field(name="Penalidade:",
            value=f"```Banimento```",
            inline=False)
        ban.add_field(name="Motivo:",
            value=f"```{reason}```",
            inline=False)
        ban.add_field(name="Responsável:",
            value=f"{ctx.author.mention}",
            inline=False)
        ban.add_field(name="Data:",
            value=f"```({h}:{ctx.message.created_at.minute}){ctx.message.created_at.day}/{ctx.message.created_at.month}/{ctx.message.created_at.year}```",
            inline=True)
        ban.set_footer(text="Para desbanir, use /unban")

        # EMBEDS - CAUSE
        cause = discord.Embed(title="Usuário banido!",
                        description=f"Veja <#{warn_log}> para mais info.",
                        color=0xffdd00)

        # EMBEDS - DM
        dm = discord.Embed(title="Você foi banido!",
                        description=f"Você não é mais um membro da Loucademia Ifunny.",
                        color=0xffdd00)
        dm.add_field(name='Motivo:',
                     value=f'{reason}.')

        ch = client.get_channel(warn_log)
        await ctx.guild.ban(member, reason = reason)
        await ch.send(f'/checkpoint: <@{member.id}>')
        await ch.send(embed=ban)
        await ctx.send(embed=cause)
        await member.send(embed=dm)
    except discord.Forbidden:
        error = discord.Embed(title="ERRO!",
        description = f"<@{member.id}> tem a `DM` bloqueada!",
        color=0xffdd00)
        return await ctx.send(embed=error)




# Kick
@warn.command(name = 'kick', aliases = ['chutar','k', 'remover'], description = 'Na reason, escreva no infinitivo.')
async def kick(ctx, member: discord.Member = None, *, reason = None):

    await ctx.channel.purge(limit=1)
    
    try:

        if member == None or member == ctx.message.author:
            aviso = discord.Embed(title='Você não pode se remover!',
            description='Você não pode se remover por questões de segurança, tente um usuário.',
            color=0xffdd00)
            await ctx.send(embed=aviso)
            return
        
        if reason == None:
            reason = 'Agir de forma imprudente!'

        # EMBEDS - KICK

        h_ = int(ctx.message.created_at.hour)
        if h_ == 0:
            h = 21
        elif h_ == 1:
            h = 22
        elif h_ == 2:
            h = 23
        elif h_ == 3:
            h = 0
        else:
            h = h_ - 3
        
        kick = discord.Embed(title="Anotação de Warn.",
                        description=f"```Um usuário foi chutado.```",
                        color=0xffdd00)
        kick.set_author(name=f"{ctx.author.name}",
            icon_url=f"{ctx.author.avatar_url}")
        kick.set_thumbnail(url="https://cdn.discordapp.com/icons/696132213598584942/a_ba5909ec4dbad809bf85db696ee97f04.gif")
        kick.add_field(name="Usuário:",
            value=f"<@{member.id}>",
            inline=False)
        kick.add_field(name="ID:",
            value=f"```{member.id}```",
            inline=True)
        kick.add_field(name="Penalidade:",
            value=f"```Remoção```",
            inline=False)
        kick.add_field(name="Motivo:",
            value=f"```{reason}```",
            inline=False)
        kick.add_field(name="Responsável:",
            value=f"{ctx.author.mention}",
            inline=False)
        kick.add_field(name="Data:",
            value=f"```({h}:{ctx.message.created_at.minute}){ctx.message.created_at.day}/{ctx.message.created_at.month}/{ctx.message.created_at.year}```",
            inline=True)
        kick.set_footer(text="Para trazê-lo de volta, use /invite e mande-o o convite.")

        # EMBEDS - CAUSE
        cause = discord.Embed(title="Usuário removido!",
                        description=f"Veja <#{warn_log}> para mais info.",
                        color=0xffdd00)

        # EMBEDS - DM
        dm = discord.Embed(title="Você foi removido!",
                        description=f"Você não é mais um membro da Loucademia Ifunny.",
                        color=0xffdd00)
        dm.add_field(name='Motivo:',
                     value=f'{reason}.')
        
        ch = client.get_channel(warn_log)
        await ctx.guild.kick(member, reason = reason)
        await ch.send(embed=ban)
        await ctx.channel.send(embed=cause)
        await member.send(embed=dm)   
    except discord.Forbidden:
        error = discord.Embed(title="ERRO!",
        description = f"<@{member.id}> tem a `DM` bloqueada!",
        color=0xffdd00)
        return await ctx.send(embed=error)

# UNBan
@warn.command(name = 'unban', aliases = ['desbanir','unb', 'desexpulsar'], description = 'Na reason, escreva no infinitivo.')
async def unban(ctx, *, member):

    await ctx.channel.purge(limit=1)

    if member == None or member == ctx.message.author:
        await ctx.send(embed=discord.Embed(title="Você não pode se desbanir.",
                        description=f"```É para a sua segurança.```",
                        color=0xffdd00))
        return

    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator == member_name, member_discriminator):

            # EMBEDS - UNBAN
            h_ = int(ctx.message.created_at.hour)
            if h_ == 0:
                h = 21
            elif h_ == 1:
                h = 22
            elif h_ == 2:
                h = 23
            elif h_ == 3:
                h = 0
            else:
                h = h_ - 3
              
            unban = discord.Embed(title="Anotação de DesWarn.",
                            description=f"```Um usuário foi desbanido.```",
                            color=0xffdd00)
            unban.set_author(name=f"{ctx.author.name}",
                icon_url=f"{ctx.author.avatar_url}")
            unban.set_thumbnail(url="https://cdn.discordapp.com/icons/696132213598584942/a_ba5909ec4dbad809bf85db696ee97f04.gif")
            unban.add_field(name="Usuário:",
                value=f"<@{user.id}>",
                inline=False)
            unban.add_field(name="ID:",
                value=f"```{user.id}```",
                inline=True)
            unban.add_field(name="Penalidade:",
                value=f"```Desbanido.```",
                inline=False)
            unban.add_field(name="Motivo do ban:",
                value=f"Ver em: <#758765312748814377>.",
                inline=False)
            unban.add_field(name="Responsável:",
                value=f"{ctx.author.mention}",
                inline=False)
            unban.add_field(name="Data:",
                value=f"```({h}:{ctx.message.created_at.minute}){ctx.message.created_at.day}/{ctx.message.created_at.month}/{ctx.message.created_at.year}```",
                inline=True)
            unban.set_footer(text="Para trazê-lo de volta, use /invite e mande-o o convite.")

            # EMBEDS - CAUSE
            cause = discord.Embed(title="Usuário desbanido!",
                        description=f"Veja <#{warn_log}> para mais info.",
                        color=0xffdd00)

            ch = client.get_channel(warn_log)
            await ctx.guild.unban(user)
            await ch.send(embed=unban)
            await ctx.channel.send(embed=cause)



# Detentos

@warn.command(name = 'det', aliases = ['deter'])
async def det(ctx, member: discord.Member, role: discord.Role, *, reason):

    await ctx.channel.purge(limit=1)

    # roles = [r.name for r in member.roles]

    r_ativos = discord.utils.get(member.guild.roles, name = 'ativos')
    r_elite = discord.utils.get(member.guild.roles, name = 'Membro Elite')
    r_reserva = discord.utils.get(member.guild.roles, name = 'Reservistas')
    r_da = discord.utils.get(member.guild.roles, name = 'Detento 001')
    r_db = discord.utils.get(member.guild.roles, name = 'Detento 002')
    r_dc = discord.utils.get(member.guild.roles, name = 'Detento 003')
    r_dd = discord.utils.get(member.guild.roles, name = 'Detento 004')

    # EMBED - log

    h_ = int(ctx.message.created_at.hour)
    if h_ == 0:
        h = 21
    elif h_ == 1:
        h = 22
    elif h_ == 2:
        h = 23
    elif h_ == 3:
        h = 0
    else:
        h = h_ - 3
                
    log = discord.Embed(title="Anotação de Warn.",
                            description=f"```Um usuário foi detido.```",
                            color=0xffdd00)
    log.set_author(name=f"{ctx.author.name}",
        icon_url=f"{ctx.author.avatar_url}")
    log.set_thumbnail(url=f'{member.avatar_url}')
    log.add_field(name="Usuário:",
        value=f"<@{member.id}>",
        inline=False)
    log.add_field(name="ID:",
        value=f"```{member.id}```",
        inline=True)
    log.add_field(name="Penalidade:",
        value=f"```Detido.```",
        inline=False)
    log.add_field(name="Motivo da detenção:",
        value=f"{reason}.",
        inline=False)
    # log.add_field(name="Cargos:",
        #value=f"```diff\n{member.roles}```",
        #inline=False)
    log.add_field(name="Responsável:",
        value=f"{ctx.author.mention}",
        inline=False)
    log.add_field(name="Data:",
        value=f"```({h}:{ctx.message.created_at.minute}){ctx.message.created_at.day}/{ctx.message.created_at.month}/{ctx.message.created_at.year}```",
        inline=False)
    
    if r_ativos in member.roles:
        await ctx.send(f"{member} tinha {r_testadores}")
        await member.remove_roles(r_testadores)
        log.add_field(name="Cargo removido:",
        value=f"{r_testadores.mention}",
        inline=True)
    if r_da in member.roles:
        await ctx.send(f"{member} tinha {r_da}")
        await member.remove_roles(r_da)
        log.add_field(name="Cargo removido:",
        value=f"{r_da.mention}",
        inline=True)
    if r_db in member.roles:
        await ctx.send(f"{member} tinha {r_db}")
        await member.remove_roles(r_db)
        log.add_field(name="Cargo removido:",
        value=f"{r_db.mention}",
        inline=True)
    if r_dc in member.roles:
        await ctx.send(f"{member} tinha {r_dc}")
        await member.remove_roles(r_dc)
        log.add_field(name="Cargo removido:",
        value=f"{r_dc.mention}",
        inline=True)
    if r_dd in member.roles:
        await ctx.send(f"{member} tinha {r_dd}")
        await member.remove_roles(r_dd)
        log.add_field(name="Cargo removido:",
        value=f"{r_dd.mention}",
        inline=True)
    if r_reserva in member.roles:
        await ctx.send(f"{member} tinha {r_dd}")
        await member.remove_roles(r_dd)
        log.add_field(name="Cargo removido:",
        value=f"{r_dd.mention}",
        inline=True)
    if r_elite in member.roles:
        await ctx.send(f"{member} tinha {r_dd}")
        await member.remove_roles(r_dd)
        log.add_field(name="Cargo removido:",
        value=f"{r_dd.mention}",
        inline=True)

    
    log.set_footer(text="Indique o tempo, adicionando uma reação numeral, como: :one:, :two:, :three:, :four:, :five: ...")

    ch = client.get_channel(warn_log)
    await member.add_roles(role)
    await ctx.send(embed=discord.Embed(title="Em detenção!",
                            description=f"<@{member.id}> foi detido. Veja mais em <#{warn_log}>",
                            color=0xffdd00))
    await ch.send(embed=log)

# DesDET

@client.command(name = 'desdet', aliases= ['liberar', 'libertar', 'soltar'])
async def desdet(ctx, member: discord.Member, role1: discord.Role = None, role2: discord.Role = None, role3: discord.Role = None, role4: discord.Role = None, role5: discord.Role = None, role6: discord.Role = None, role7: discord.Role = None, role8: discord.Role = None):

    await ctx.channel.purge(limit=1)

    # roles = [r.name for r in member.roles]

    r_da = discord.utils.get(member.guild.roles, name = 'Detento 001')
    r_db = discord.utils.get(member.guild.roles, name = 'Detento 002')
    r_dc = discord.utils.get(member.guild.roles, name = 'Detento 003')
    r_dd = discord.utils.get(member.guild.roles, name = 'Detento 004')

    # EMBED - log

    h_ = int(ctx.message.created_at.hour)
    if h_ == 0:
        h = 21
    elif h_ == 1:
        h = 22
    elif h_ == 2:
        h = 23
    elif h_ == 3:
        h = 0
    else:
        h = h_ - 3
                
    log = discord.Embed(title="Anotação de DesWarn.",
                            description=f"```Um usuário foi liberado.```",
                            color=0xffdd00)
    log.set_author(name=f"{ctx.author.name}",
        icon_url=f"{ctx.author.avatar_url}")
    log.set_thumbnail(url=f'{member.avatar_url}')
    log.add_field(name="Usuário:",
        value=f"<@{member.id}>",
        inline=False)
    log.add_field(name="ID:",
        value=f"```{member.id}```",
        inline=True)
    log.add_field(name="Penalidade:",
        value=f"```Remoção de Pena.```",
        inline=False)
    log.add_field(name="Motivo da detenção:",
        value=f"Veja <#{warn_log}> para mais info.",
        inline=False)
    # log.add_field(name="Cargos:",
        #value=f"```diff\n{member.roles}```",
        #inline=False)
    log.add_field(name="Responsável:",
        value=f"{ctx.author.mention}",
        inline=False)
    log.add_field(name="Data:",
        value=f"```({h}:{ctx.message.created_at.minute}){ctx.message.created_at.day}/{ctx.message.created_at.month}/{ctx.message.created_at.year}```",
        inline=False)
    
    if r_da in member.roles:
        await ctx.send(f"{member} tinha {r_da}")
        await member.remove_roles(r_da)
        log.add_field(name="Cargo de detento removido:",
        value=f"{r_da.mention}",
        inline=True)
    if r_db in member.roles:
        await ctx.send(f"{member} tinha {r_db}")
        await member.remove_roles(r_db)
        log.add_field(name="Cargo de detento removido:",
        value=f"{r_db.mention}",
        inline=True)
    if r_dc in member.roles:
        await ctx.send(f"{member} tinha {r_dc}")
        await member.remove_roles(r_dc)
        log.add_field(name="Cargo de detento removido:",
        value=f"{r_dc.mention}",
        inline=True)
    if r_dd in member.roles:
        await ctx.send(f"{member} tinha {r_dd}")
        await member.remove_roles(r_dd)
        log.add_field(name="Cargo de detento removido:",
        value=f"{r_dd.mention}",
        inline=True)

    if role1 == None:
        await ctx.send(embed=discord.Embed(
            title = 'Adicione um cargo!',
            description = f'Você, obrigatoriamente, deve adicionar um cargo para devolver\n \
                para saber qual cargo deve adicionar, pesquise em <#{warn_log}>, em menções, para saber os cargos do detento.',
            color = 0xffdd00
        ))
        return

    elif role1 != None:
        await member.add_roles(role1)
        log.add_field(name="Cargo devolvido:",
        value=f"{role1.mention}",
        inline=True)
        if role2 != None:
            await member.add_roles(role2)
            log.add_field(name="Cargo devolvido:",
            value=f"{role2.mention}",
            inline=True)
            if role2 != None:
                await member.add_roles(role3)
                log.add_field(name="Cargo devolvido:",
                value=f"{role3.mention}",
                inline=True)
                if role2 != None:
                    await member.add_roles(role4)
                    log.add_field(name="Cargo devolvido:",
                    value=f"{role4.mention}",
                    inline=True)
                    if role2 != None:
                        await member.add_roles(role5)
                        log.add_field(name="Cargo devolvido:",
                        value=f"{role5.mention}",
                        inline=True)
                        if role2 != None:
                            await member.add_roles(role6)
                            log.add_field(name="Cargo devolvido:",
                            value=f"{role6.mention}",
                            inline=True)
                            if role2 != None:
                                await member.add_roles(role7)
                                log.add_field(name="Cargo devolvido:",
                                value=f"{role7.mention}",
                                inline=True)
                                if role2 != None:
                                    await member.add_roles(role8)
                                    log.add_field(name="Cargo devolvido:",
                                    value=f"{role8.mention}",
                                    inline=True)


    
    log.set_footer(text=f"Pesquise pelo usuário em <#{warn_log}> para mais info. ")

    ch = client.get_channel(warn_log)
    # await member.add_roles(role)
    await ctx.send(embed=discord.Embed(title="Em processo de soltura!",
                            description=f"<@{member.id}> foi liberado. Veja mais em <#{warn_log}>",
                            color=0xffdd00))
    await ch.send(embed=log)



# Info
    #ADM

@client.group(name='info')
@commands.has_any_role(staff)
async def info(ctx):
    c = client.get_channel(766674597466210305)
    if ctx.channel == c:
        inf=discord.Embed(
                title="Info",
                description=f"```Use '/info + argumentos'.\nOs argumentos devem ser os seguintes:```",
                color=0xffdd00)
        inf.set_thumbnail(
            url=f"https://cdn.discordapp.com/icons/696132213598584942/a_ba5909ec4dbad809bf85db696ee97f04.gif"
            )
        inf.add_field(
            name=f"Guild:",
            value=f"/info [guild|server|lif|servidor] [1-10]",
            inline=False)
        inf.add_field(
            name=f"LIFBot:",
            value=f"/info [lifbot|bot|lb]",
            inline=False)
        inf.add_field(
            name=f"Membro:",
            value=f"/info [membro|member|usuário|user] [membro (citação)]",
            inline=False)
        inf.add_field(
            name=f"Eu:",
            value=f"/info [eu|me]",
            inline=False)
        inf.add_field(
            name=f"Canal:",
            value=f"/info [canal|channel|ch|chat] [chat (citação)] [1-2 (número)]",
            inline=False)
        inf.add_field(
            name=f"Cargo:",
            value=f"/info [cargol|role|patente] [cargo (citação)] [1-3 (número)]",
            inline=False)
        inf.add_field(
            name=f"Convites:",
            value=f"/info [convites|invites|invs] ",
            inline=False)
        inf.set_footer(
            text=f"[] = argumento obrigatório; <> = argumento opcional; () = especificação; [x-y] = de um ponto ao outro; | = alternância")
        msg = await ctx.send(embed=inf)

@info.command(name='guild', aliases=['lif','servidor','server'])
async def guild_subcommand(ctx, pg = '1'):

    await ctx.channel.purge(limit=1)
    if pg == None or pg =='1':
        guild1=discord.Embed(
            title="Guild Info - LIF",
            description=f"```Informações da {ctx.guild.name}```",
            color=0xffdd00)
        guild1.set_thumbnail(
            url=f"https://cdn.discordapp.com/icons/696132213598584942/a_ba5909ec4dbad809bf85db696ee97f04.gif"
            )
        guild1.set_author(
            name=f"{ctx.author.name}",
            icon_url=f"{ctx.author.avatar_url}"
            )
        guild1.add_field(
            name=f"Nome:",
            value=f"```{ctx.guild.name}```",
            inline=False)
        guild1.add_field(
            name=f"Descrição:",
            value=f"```{ctx.guild.description}```",
            inline=False)
        guild1.add_field(
            name=f"ID:",
            value=f"```{ctx.guild.id}```",
            inline=False)
        guild1.add_field(
            name=f"Dono e Administrador master:",
            value=f"{ctx.guild.owner.mention}",
            inline=False)
        guild1.add_field(
            name=f"Nível de verificação:",
            value=f"```{ctx.guild.verification_level}```",
            inline=False)
        guild1.add_field(
            name=f"Nível de autentificação:",
            value=f"```{ctx.guild.mfa_level}```",
            inline=False)                 
        region = str(ctx.guild.region).capitalize()
        guild1.add_field(
            name=f"Região:",
            value=f"```{region}```",
            inline=False)
        guild1.add_field(
            name=f"---------------------------------------\nPáginas:",
            value=f"**Principal**|Members|Cargos|Canais|Emojis|Premium|Bans|Integrations|Convites|Outros",
            inline=False)
        guild1.set_footer(
            text=f"Principal - pg. 1 (use /info guild <num>)")
        await ctx.send(embed=guild1)

    elif pg == '2':
        guild2=discord.Embed(
            title="Guild Info - MEMBROS",
            description=f"```Informações da {ctx.guild.name}\n>>> Membros e maior cargo:```",
            color=0xffdd00)
        guild2.set_thumbnail(
            url=f"https://cdn.discordapp.com/icons/696132213598584942/a_ba5909ec4dbad809bf85db696ee97f04.gif"
            )
        guild2.set_author(
            name=f"{ctx.author.name}",
            icon_url=f"{ctx.author.avatar_url}"
            )
        guild2.add_field(
            name=f"Membros:",
            value=f"`...",
            inline=False)
        for m in ctx.guild.members:
            guild2.add_field(
                name=f"Membro:",
                value=f"<@{m.id}>\nTop: {m.top_role.mention}",
                inline=True)
        guild2.add_field(
            name=f"---------------------------------------\nPáginas:",
            value=f"Principal|**Membros**|Cargos|Canais|Emojis|Premium|Bans|Integrations|Convites|Outros",
            inline=False)
        guild2.set_footer(
            text=f"Membros - pg. 2 (use /info guild <num>)")
        await ctx.send(embed = guild2)

    elif pg == '3':
        guild3=discord.Embed(
            title="Guild Info - CARGOS",
            description=f"```Informações da {ctx.guild.name}\n>>> Cargos:```",
            color=0xffdd00)
        guild3.set_thumbnail(
            url=f"https://cdn.discordapp.com/icons/696132213598584942/a_ba5909ec4dbad809bf85db696ee97f04.gif"
            )
        guild3.set_author(
            name=f"{ctx.author.name}",
            icon_url=f"{ctx.author.avatar_url}"
            )
        guild3.add_field(
            name=f"Cargos:",
            value=f"...",
            inline=False)
        for r in ctx.guild.roles:
            guild3.add_field(
                name=f"Cargo:",
                value=f"<@&{r.id}>\n**Pos.:** `{r.position}`",
                inline=True)
        guild3.add_field(
            name=f"---------------------------------------\nPáginas:",
            value=f"Principal|Members|**Cargos**|Canais|Emojis|Premium|Bans|Integrations|Convites|Outros",
            inline=False)
        guild3.set_footer(
            text=f"Cargos - pg. 3 (use /info guild <num>)")
        await ctx.send(embed = guild3)        
                                     
    elif pg == '4':
        guild4=discord.Embed(
            title="Guild Info - CANAIS",
            description=f"```Informações da {ctx.guild.name}\n>>> Canais:```",
            color=0xffdd00)
        guild4.set_thumbnail(
            url=f"https://cdn.discordapp.com/icons/696132213598584942/a_ba5909ec4dbad809bf85db696ee97f04.gif"
            )
        guild4.set_author(
            name=f"{ctx.author.name}",
            icon_url=f"{ctx.author.avatar_url}"
            )
        guild4.add_field(
            name=f"Canais:",
            value=f"...",
            inline=False)
        for c in ctx.guild.text_channels:
            cat = f"{c.category}".capitalize()
            cat = f"'{cat}'"
            if c.category == None:
                cat = ''
            guild4.add_field(
            name=f"Canal:",
            value=f"<#{c.id}>",
            inline=False)
        guild4.add_field(
            name=f"---------------------------------------\nPáginas:",
            value=f"Principal|Members|Cargos|**Canais**|Emojis|Premium|Bans|Integrations|Convites|Outros",
            inline=False)
        guild4.set_footer(
            text=f"Canais - pg. 4 (use /info guild <num>)")
        await ctx.send(embed = guild4)    

    elif pg == '5':
        guild5=discord.Embed(
            title="Guild Info - EMOJIS",
            description=f"```Informações da {ctx.guild.name}\n>>> Emojis:```",
            color=0xffdd00)
        guild5.set_thumbnail(
            url=f"https://cdn.discordapp.com/icons/696132213598584942/a_ba5909ec4dbad809bf85db696ee97f04.gif"
            )
        guild5.set_author(
            name=f"{ctx.author.name}",
            icon_url=f"{ctx.author.avatar_url}"
            )
        guild5.add_field(
            name=f"Emojis:",
            value=f"...",
            inline=False)
        for e in ctx.guild.emojis:
            guild5.add_field(
            name=f"**Emoji: {e}**",
            value=f"**nome:** `:{e.name}:`\n```id:{e.id}```",
            inline=False)
        guild5.add_field(
            name=f"---------------------------------------\nPáginas:",
            value=f"Principal|Members|Cargos|Canais|**Emojis**|Premium|Bans|Integrations|Convites|Outros",
            inline=False)
        guild5.set_footer(
            text=f"Emojis - pg. 5 (use /info guild <num>)")            
        await ctx.send(embed = guild5)  


    elif pg == '6':
        guild6=discord.Embed(
            title="Guild Info - PREMIUM",
            description=f"```Informações da {ctx.guild.name}\n>>> Premium:```",
            color=0xffdd00)
        guild6.set_thumbnail(
            url=f"https://cdn.discordapp.com/icons/696132213598584942/a_ba5909ec4dbad809bf85db696ee97f04.gif"
            )
        guild6.set_author(
            name=f"{ctx.author.name}",
            icon_url=f"{ctx.author.avatar_url}"
            )
        guild6.add_field(
            name=f"Membros Premium (Apoiadores do exército):",
            value=f"...",
            inline=False)
        guild6.add_field(
            name=f"Server Boost Nível:",
            value=f"```{ctx.guild.premium_subscription_count}```",
            inline=False)      
        for p in ctx.guild.premium_subscribers:
            guild6.add_field(
            name=f"Apoiador:",
            value=f"nome: `:{p.name}:`\nid:<#{p.id}>",
            inline=False)
        guild6.add_field(
            name=f"---------------------------------------\nPáginas:",
            value=f"Principal|Members|Cargos|Canais|Emojis|**Premium**|Bans|Integrations|Convites|Outros",
            inline=False)
        guild6.set_footer(
            text=f"Premium - pg. 6 (use /info guild <num>)")            
        await ctx.send(embed = guild6)  

    elif pg == '7':
        guild7=discord.Embed(
            title="Guild Info - BANS",
            description=f"```Informações da {ctx.guild.name}\n>>> Bans:```",
            color=0xffdd00)
        guild7.set_thumbnail(
            url=f"https://cdn.discordapp.com/icons/696132213598584942/a_ba5909ec4dbad809bf85db696ee97f04.gif"
            )
        guild7.set_author(
            name=f"{ctx.author.name}",
            icon_url=f"{ctx.author.avatar_url}"
            )
        guild7.add_field(
            name=f"Lista de membros banidos:",
            value=f"...",
            inline=False)
        banlist = await ctx.guild.bans()
        for b in banlist:
            guild7.add_field(
            name=f"{b.user.name}#{b.user.discriminator}\n",
            value=f"**ID:** `{b.user.id}`\n```Razão: {b.reason}```",
            inline=False)
        guild7.add_field(
            name=f"---------------------------------------\nPáginas:",
            value=f"Principal|Members|Cargos|Canais|Emojis|Premium|**Bans**|Integrations|Convites|Outros",
            inline=False)
        guild7.set_footer(
            text=f"Bans - pg. 7 (use /info guild <num>)")            
        await ctx.send(embed = guild7)  

    elif pg == '8':
        guild8=discord.Embed(
            title="Guild Info - INTERGRATIONS",
            description=f"```Informações da {ctx.guild.name}\n>>> Integrations:```",
            color=0xffdd00)
        guild8.set_thumbnail(
            url=f"https://cdn.discordapp.com/icons/696132213598584942/a_ba5909ec4dbad809bf85db696ee97f04.gif"
            )
        guild8.set_author(
            name=f"{ctx.author.name}",
            icon_url=f"{ctx.author.avatar_url}"
            )
        guild8.add_field(
            name=f"Lista de Inetegrações:",
            value=f"...",
            inline=False)
        integ = await ctx.guild.integrations()
        web = await ctx.guild.webhooks()
        for i in integ:
            guild8.add_field(
            name=f"{i.name}",
            value=f"**ID:** `{i.id}`\n**Tipo:** `{b.type}`",
            inline=False)
        for w in web:
            guild8.add_field(
            name=f"{w.name}",
            value=f"**ID:** `{w.id}`\n**Tipo:** `{w.type}`\n**Token:** `{w.token}`\n**URL:** *{w.url}*\n---------------------------------------",
            inline=False)            
        guild8.add_field(
            name=f"---------------------------------------\nPáginas:",
            value=f"Principal|Members|Cargos|Canais|Emojis|Premium|Bans|**Integrations**|Convites|Outros",
            inline=False)
        guild8.set_footer(
            text=f"Integrations - pg. 8 (use /info guild <num>)")            
        await ctx.send(embed = guild8)  

    elif pg == '9':
        guild9=discord.Embed(
            title="Guild Info - CONVITES",
            description=f"```Informações da {ctx.guild.name}\n>>> Convites:```",
            color=0xffdd00)
        guild9.set_thumbnail(
            url=f"https://cdn.discordapp.com/icons/696132213598584942/a_ba5909ec4dbad809bf85db696ee97f04.gif"
            )
        guild9.set_author(
            name=f"{ctx.author.name}",
            icon_url=f"{ctx.author.avatar_url}"
            )
        guild9.add_field(
            name=f"Lista de Convites:",
            value=f"...",
            inline=False)
        inv = await ctx.guild.invites()
        for i in inv:
            guild9.add_field(
            name=f"**Código:** `{i.code}`",
            value=f"**Criação:** `({i.created_at.hour}:{i.created_at.minute}) - {i.created_at.day}/{i.created_at.month }/{i.created_at.year}`, **tempo de vida:** `{i.max_age}`\n\
**Temporário:** *{i.temporary}*\n**Usos:** `{i.uses}/{i.max_uses}`\n\
**Por:** <@{i.inviter.id}>\n**URL:** *{i.url}*\n---------------------------------------",
            inline=False)
        guild9.add_field(
            name=f"---------------------------------------\nPáginas:",
            value=f"Principal|Members|Cargos|Canais|Emojis|Premium|Bans|Integrations|**Convites**|Outros",
            inline=False)
        guild9.set_footer(
            text=f"Convites - pg. 9 (use /info guild <num>)")            
        await ctx.send(embed = guild9)  
        
    elif pg == '10':
        guild10=discord.Embed(
            title="Guild Info - OUTROS",
            description=f"```Informações da {ctx.guild.name}\n>>> Outros:```",
            color=0xffdd00)
        guild10.set_thumbnail(
            url=f"https://cdn.discordapp.com/icons/696132213598584942/a_ba5909ec4dbad809bf85db696ee97f04.gif"
            )
        guild10.set_author(
            name=f"{ctx.author.name}",
            icon_url=f"{ctx.author.avatar_url}"
            )
        guild10.add_field(
            name=f"Quantidade de canais:",
            value=f"{ctx.guild.large}",
            inline=False) 
        guild10.add_field(
            name=f"Canal do Sistema:",
            value=f"<#{ctx.guild.system_channel.id}>",
            inline=False)
        br = str(int(ctx.guild.bitrate_limit)/1000) + 'Kbps'
        guild10.add_field(
            name=f"Quantias:",
            value=f"Membros: {ctx.guild.member_count}\nEmojis: {ctx.guild.emoji_limit}\nBitrate: {br}\nArquivos: {ctx.guild.filesize_limit}",
            inline=False)            
        guild10.add_field(
            name=f"Criação:",
            value=f"Data: {ctx.guild.created_at.day}/{ctx.guild.created_at.month }/{ctx.guild.created_at.year}",
            inline=False)   
        guild10.add_field(
            name=f"URL de imagens:",
            value=f"Ícone: {ctx.guild.icon_url}\nBanner: {ctx.guild.banner_url}",
            inline=False)                
        guild10.add_field(
            name=f"---------------------------------------\nPáginas:",
            value=f"Principal|Members|Cargos|Canais|Emojis|Premium|Bans|**Integrations**|Convites|Outros",
            inline=False)
        guild10.set_footer(
            text=f"Outros - pg. 10 (use /info guild <num>)")            
        await ctx.send(embed = guild10)


@info.command(name='bot', aliases=['lifbot','lb'])
async def bot_subcommand(ctx):

    await ctx.channel.purge(limit=1)

    bot_id = ctx.me.id
    profile = ctx.me.avatar_url
    status = ':radio_button: Online'

    bot_emb=discord.Embed(
        title="LIF BOT Info",
        description=f"```Informações do {ctx.me.name}:```",
        color=0xffdd00)
    bot_emb.set_thumbnail(
        url=f"{profile}"
        )
    bot_emb.set_author(
        name=f"{ctx.author.name}",
        icon_url=f"{ctx.author.avatar_url}"
        )
    bot_emb.add_field(
        name=f"Nome:",
        value=f"<@{bot_id}> <:bot:765236492577931265>",
        inline=False)  
    bot_emb.add_field(
        name=f"ID:",
        value=f"{bot_id}",
        inline=False)
    bot_emb.add_field(
        name=f"Avatar_URL:",
        value=f"{ctx.me.avatar_url}",
        inline=False)    
    bot_emb.add_field(
        name=f"Status:",
        value=f"{status}",
        inline=False)  
    bot_emb.add_field(
        name=f"Latência:",
        value=f"{round(client.latency*1000)}ms.",
        inline=False)                           
    bot_emb.add_field(
        name=f"Criação:",
        value=f"Data: {ctx.me.created_at.day}/{ctx.me.created_at.month }/{ctx.me.created_at.year}",
        inline=False)
    bot_emb.add_field(
        name=f"Versão do LIFBOT:",
        value=f"v. {version}",
        inline=False)   
    bot_emb.add_field(
        name=f"Versão do Discord.py:",
        value=f"v. {discord.__version__}",
        inline=False)                 
    bot_emb.set_footer(
        text=f"LIF BOT - (use /info bot)")            
    await ctx.send(embed = bot_emb) 


@info.command(name='membro', aliases=['member','user', 'usuário', 'usuario', 'participante', 'integrante'])
async def bot_subcommand(ctx, member: discord.Member = None):

    await ctx.channel.purge(limit=1)
    if member == None:
        await ctx.send(    bot_emb=discord.Embed(
        title="Erro!",
        description=f"```Escolha um membro: '/info membro @menção'```",
        color=0xffdd00))

    entrou = f'{member.joined_at.day}/{member.joined_at.month}/{member.joined_at.year}'
    nome = member.nick
    cargo_top = member.top_role
    profile = member.avatar_url
    is_a_bot = member.bot
    criado = f'{member.created_at.day}/{member.created_at.month}/{member.created_at.year}'
    m_id = member.id


    m_emb=discord.Embed(
        title="Membro Info",
        description=f"```Informações do {member.name}:```",
        color=0xffdd00)
    m_emb.set_thumbnail(
        url=f"{profile}"
        )
    m_emb.set_author(
        name=f"{member.name}",
        icon_url=f"{profile}"
        )
    if is_a_bot == True:
        m_emb.add_field(
            name=f"Nome:",
            value=f"<@{m_id}> <:bot:765236492577931265>",
            inline=False) 
    elif is_a_bot == False:
       m_emb.add_field(
            name=f"Nome:",
            value=f"<@{m_id}>",
            inline=False)          
    m_emb.add_field(
        name=f"ID:",
        value=f"{m_id}",
        inline=False)
    m_emb.add_field(
        name=f"Apelido:",
        value=f"{nome}",
        inline=False)         
    m_emb.add_field(
        name=f"Avatar_URL:",
        value=f"{profile}",
        inline=False)
    m_emb.add_field(
        name=f"Entrou no servidor:",
        value=f"Data: {entrou}",
        inline=False)                            
    m_emb.add_field(
        name=f"Criação:",
        value=f"Data: {criado}",
        inline=False)
    for cargos in member.roles:
        m_emb.add_field(
        name=f"Cargo:",
        value=f"{cargos.mention}",
        inline=True)
  
    m_emb.set_footer(
        text=f"Membro - (use /info membro)")            
    await ctx.send(embed = m_emb) 

@info.command(name='eu', aliases=['me'])
async def bot_subcommand(ctx):

    await ctx.channel.purge(limit=1)

    entrou = f'{ctx.author.joined_at.day}/{ctx.author.joined_at.month}/{ctx.author.joined_at.year}'
    nome = ctx.author.nick
    cargo_top = ctx.author.top_role
    profile = ctx.author.avatar_url
    is_a_bot = ctx.author.bot
    criado = f'{ctx.author.created_at.day}/{ctx.author.created_at.month}/{ctx.author.created_at.year}'
    m_id = ctx.author.id


    m_emb=discord.Embed(
        title="Autor Info",
        description=f"```Informações do {ctx.author.name}:```",
        color=0xffdd00)
    m_emb.set_thumbnail(
        url=f"{profile}"
        )
    m_emb.set_author(
        name=f"{ctx.author.name}",
        icon_url=f"{profile}"
        )
    if is_a_bot == True:
        m_emb.add_field(
            name=f"Nome:",
            value=f"<@{m_id}> <:bot:765236492577931265>",
            inline=False) 
    elif is_a_bot == False:
       m_emb.add_field(
            name=f"Nome:",
            value=f"<@{m_id}>",
            inline=False)          
    m_emb.add_field(
        name=f"ID:",
        value=f"{m_id}",
        inline=False)
    m_emb.add_field(
        name=f"Apelido:",
        value=f"{nome}",
        inline=False)         
    m_emb.add_field(
        name=f"Avatar_URL:",
        value=f"{profile}",
        inline=False)
    m_emb.add_field(
        name=f"Entrou no servidor:",
        value=f"Data: {entrou}",
        inline=False)                            
    m_emb.add_field(
        name=f"Criação:",
        value=f"Data: {criado}",
        inline=False)
    for cargos in ctx.author.roles:
        m_emb.add_field(
        name=f"Cargo:",
        value=f"{cargos.mention}",
        inline=True)
  
    m_emb.set_footer(
        text=f"Autor - (use /info me)")            
    await ctx.send(embed = m_emb) 


@info.command(name='canal', aliases=['chat', 'channel', 'conversa', 'ch'])
async def bot_subcommand(ctx, channel: discord.TextChannel, pg = '1'):

    await ctx.channel.purge(limit=1)

    profile = ctx.author.avatar_url
    c_id = channel.id
    categoria = f'{channel.category} | `{channel.category_id}` '
    pos = channel.position
    topico = channel.topic
    criacao = f'({channel.created_at.hour}:{channel.created_at.minute}) - {channel.created_at.day}/{channel.created_at.month}/{channel.created_at.year}'
    sincronizado = channel.permissions_synced
    nsfw = channel.is_nsfw()
    news = channel.is_news()

    if pg == '1':
        m_emb=discord.Embed(
            title="Channel Info",
            description=f"```Informações do {channel.name}:```",
            color=0xffdd00)
        m_emb.set_thumbnail(
            url=f"https://cdn.discordapp.com/icons/696132213598584942/a_ba5909ec4dbad809bf85db696ee97f04.gif"
            )
        m_emb.set_author(
            name=f"{ctx.author.name}",
            icon_url=f"{profile}"
            )
        m_emb.add_field(
            name=f"Nome:",
            value=f"<#{c_id}>",
            inline=False) 
        m_emb.add_field(
            name=f"ID:",
            value=f"```{c_id}```",
            inline=False)  
        m_emb.add_field(
            name=f"Regras:",
            value=f"```{topico}```",
            inline=False)   
        m_emb.add_field(
            name=f"Posição:",
            value=f"{pos}",
            inline=False)  
        m_emb.add_field(
            name=f"Categoria:",
            value=f"{categoria}",
            inline=False)       
        m_emb.add_field(
            name=f"Características:",
            value=f"**Sincronizado:** `{sincronizado}`\n**Nsfw:** `{nsfw}`\n**News:** `{news}` ",
            inline=False)     
        m_emb.add_field(
            name=f"Criação::",
            value=f"{criacao} ",
            inline=False)   
        m_emb.add_field(
            name=f"---------------------------------------\nPáginas:",
            value=f"**Principal**|Membros",
            inline=False)
        m_emb.set_footer(
            text=f"Principal - pg. 1 (use /info channel <num>)")            
        await ctx.send(embed = m_emb)    

    if pg == '2':
        m_emb=discord.Embed(
            title="Channel Info - Membros",
            description=f"```Quem pode ver o {channel.name}:```",
            color=0xffdd00)
        m_emb.set_thumbnail(
            url=f"https://cdn.discordapp.com/icons/696132213598584942/a_ba5909ec4dbad809bf85db696ee97f04.gif"
            )
        m_emb.set_author(
            name=f"{ctx.author.name}",
            icon_url=f"{profile}"
            )
        for m in channel.members:
            m_emb.add_field(
                name=f"Membro:",
                value=f"<@{m.id}> | <@&{m.top_role.id}>",
                inline=True) 
        m_emb.add_field(
            name=f"---------------------------------------\nPáginas:",
            value=f"Principal|**Membros**",
            inline=False)
        m_emb.set_footer(
            text=f"Membros - pg. 2 (use /info channel <num>)")            
        await ctx.send(embed = m_emb)   


@info.command(name='cargo', aliases=['role', 'patente'])
async def bot_subcommand(ctx, role: discord.Role, pg = '1'):

    await ctx.channel.purge(limit=1)

    profile = ctx.author.avatar_url
    r_id = role.id
    pos = role.position
    criacao = f'({role.created_at.hour}:{role.created_at.minute}) - {role.created_at.day}/{role.created_at.month}/{role.created_at.year}'
    cor = f'{role.color} | {role.colour}'

    if pg == '1':
        m_emb=discord.Embed(
            title="Cargos Info",
            description=f"```Informações do {role.name}:```",
            color=0xffdd00)
        m_emb.set_thumbnail(
            url=f"https://cdn.discordapp.com/icons/696132213598584942/a_ba5909ec4dbad809bf85db696ee97f04.gif"
            )
        m_emb.set_author(
            name=f"{ctx.author.name}",
            icon_url=f"{profile}"
            )
        m_emb.add_field(
            name=f"Nome:",
            value=f"<@&{r_id}>",
            inline=False) 
        m_emb.add_field(
            name=f"ID:",
            value=f"```{r_id}```",
            inline=False)  
        m_emb.add_field(
            name=f"Posição:",
            value=f"{pos}",
            inline=False)  
        m_emb.add_field(
            name=f"Cor:",
            value=f"{cor}",
            inline=False)          
        m_emb.add_field(
            name=f"Criação::",
            value=f"{criacao} ",
            inline=False)   
        m_emb.add_field(
            name=f"---------------------------------------\nPáginas:",
            value=f"**Principal**|Membros|Permissões",
            inline=False)
        m_emb.set_footer(
            text=f"Principal - pg. 1 (use /info channel <num>)")            
        await ctx.send(embed = m_emb)    

    if pg == '2':
        m_emb=discord.Embed(
            title="Cargos Info - Membros",
            description=f"```Quem tem o {role.name}:```",
            color=0xffdd00)
        m_emb.set_thumbnail(
            url=f"https://cdn.discordapp.com/icons/696132213598584942/a_ba5909ec4dbad809bf85db696ee97f04.gif"
            )
        m_emb.set_author(
            name=f"{ctx.author.name}",
            icon_url=f"{profile}"
            )
        for m in role.members:
            m_emb.add_field(
                name=f"Membro:",
                value=f"<@{m.id}>",
                inline=True) 
        m_emb.add_field(
            name=f"---------------------------------------\nPáginas:",
            value=f"Principal|**Membros**|Permissões",
            inline=False)
        m_emb.set_footer(
            text=f"Membros - pg. 2 (use /info channel <num>)")            
        await ctx.send(embed = m_emb)  

    if pg == '3':
        m_emb=discord.Embed(
            title="Cargos Info - Permissão",
            description=f"```Permissões do {role.name}:```",
            color=0xffdd00)
        m_emb.set_thumbnail(
            url=f"https://cdn.discordapp.com/icons/696132213598584942/a_ba5909ec4dbad809bf85db696ee97f04.gif"
            )
        m_emb.set_author(
            name=f"{ctx.author.name}",
            icon_url=f"{profile}"
            )
        for p in role.permissions:
            m_emb.add_field(
                name=f"Permissão:",
                value=f"{p}",
                inline=True) 
        m_emb.add_field(
            name=f"---------------------------------------\nPáginas:",
            value=f"Principal|Membros|**Permissões**",
            inline=False)
        m_emb.set_footer(
            text=f"Permissões - pg. 3 (use /info channel <num>)")            
        await ctx.send(embed = m_emb)  
                   

@info.command(name='convites', aliases=['invites'])
async def bot_subcommand(ctx):

    await ctx.channel.purge(limit=1)  



    guild9=discord.Embed(
        title="Convites Info ",
        description=f"```Informações da {ctx.guild.name}\n>>> Convites:```",
        color=0xffdd00)
    guild9.set_thumbnail(
        url=f"https://cdn.discordapp.com/icons/696132213598584942/a_ba5909ec4dbad809bf85db696ee97f04.gif"
        )
    guild9.set_author(
        name=f"{ctx.author.name}",
        icon_url=f"{ctx.author.avatar_url}"
        )
    guild9.add_field(
        name=f"Lista de Convites:",
        value=f"...",
        inline=False)
    inv = await ctx.guild.invites()
    for i in inv:
        h_ = int(i.created_at.hour)
        if h_ == 0:
            h = 21
        elif h_ == 1:
            h = 22
        elif h_ == 2:
            h = 23
        elif h_ == 3:
            h = 0
        else:
            h = h_ - 3
        guild9.add_field(
        name=f"**Código:** `{i.code}`",
        value=f"**Criação:** `({h}:{i.created_at.minute}) - {i.created_at.day}/{i.created_at.month }/{i.created_at.year}`, **tempo de vida:** `{i.max_age}`\n\
**Temporário:** *{i.temporary}*\n**Usos:** `{i.uses}/{i.max_uses}`\n\
**Por:** <@{i.inviter.id}>\n**URL:** *{i.url}*\n---------------------------------------",
        inline=False)

    guild9.set_footer(
        text=f"Convites - pg. 1 (use /info convites)")            
    await ctx.send(embed = guild9)                  
                           
@client.command()
@commands.has_any_role('testadores')
async def liberar_dm(ctx):

    await ctx.send('https://imgur.com/a/5APfCqd')
    await asyncio.sleep(2)
    await ctx.send('https://imgur.com/a/GSxDMjY')



# SEC
@client.event
async def on_command(ctx):
    ch = client.get_channel(log_ch)

    # EMBED
    h_ = int(ctx.message.created_at.hour)
    if h_ == 0:
        h = 21
    elif h_ == 1:
        h = 22
    elif h_ == 2:
        h = 23
    elif h_ == 3:
        h = 0
    else:
        h = h_ - 3

    embed = discord.Embed(
        title='Comando usado!',
        description='```Um comando está sendo usado, somente adms podem ver esse canal.```',
        color=0xffdd00
    )
    embed.set_thumbnail(
        url=f'{ctx.author.avatar_url}'
    )
    embed.add_field(
        name='Autor:',
        value=f'<@{ctx.author.id}>',
        inline=False
    )
    embed.add_field(
        name='Comando:',
        value=f'{ctx.message.content}',
        inline=False
    )
    embed.add_field(
        name='Canal:',
        value=f'<#{ctx.message.channel.id}>',
        inline=False
    )
    embed.add_field(
        name='Data:',
        value=f"```({h}:{ctx.message.created_at.minute}){ctx.message.created_at.day}/{ctx.message.created_at.month}/{ctx.message.created_at.year}```",
        inline=False
    )

    await ch.send(embed=embed)



# Deliga o bot
@client.command(aliases = ['off', 'turnoff', 'shutdown', 'desliga', 'desligar'], description = 'Desliga o Bot.')
@commands.has_any_role('General')
async def close(ctx):

    status = 'Bot desligado!'
    await client.change_presence(status)
    await ctx.send('Tchau!')
    await client.close()
    print("Bot Closed")
    






# RUN
client.run(TOKEN)
