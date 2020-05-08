import asyncio
import datetime
import discord

client = discord.Client()

print("TESTE!")


# ------------ ON_READY EVENT ----------------
# Chamado após o bot inicializar,
# existem rotinas que são chamadas antes desta.
# ---------------------------------------------

@client.event
async def on_ready():
    print("Bot is ready!")
    # Agora que temos o bot ready, vamos alterar alguns parametros  dele no discord.
    # Acedemos ao client e vamos chamar a função change_presence, passando-lhe uma  Actividade personalizada
    return await client.change_presence(activity=discord.Activity(type=1, name="Documentation!",
                                        url='https://twitch.tv/twitch'))

# Ok. Por testar.
# Evento on_member_join é o evento que dá trigger quando um user dá join
# pela primeira vez ao canal de discord, recebendo o objeto membro
@client.event
async def on_member_join(member):
    # Pelo que entendi, o objeto embed é uma forma de encapsularmos os dados antes de or enviar
    # para o canal de discord. Foi construido com o seguinte site : https://leovoel.github.io/embed-visualizer/
    # Dá para gerar o código automaticamente, mas tem que ser levemente alterado.
    embed = discord.Embed(colour=0x95efcc,
                          description=f"Bem vindo sacana {member.name}! És o {len(list(member.guild.members))} membro.")
    embed.set_thumbnail(url="https://www.wallpaperflare.com/static/209/465/114/fantasy-art-dark-person-sitting-wallpaper.jpg")
    embed.set_footer(text="Have Fun!", icon_url=f"{member.guild.icon_url}")
    embed.timestamp = datetime.datetime.utcnow()
    channel = client.get_channel(id=702598443474092054)
    await channel.send(embed=embed)


# Implementação de outro evento. on_member_update, que recebe o membros antes e depois
# De alterar o seu status
# Neste momento apenas dá print de uma msg na consola sempre que um user.
# Muda o status dele de offline para online.
@client.event
async def on_member_update(before, after):
    if str(before.status) == "offline":
        if str(after.status) == "online":
            print(f"{after.name,after.status} HAS COME ONLINE!!!")


@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
        return
    else:
        await message.channel.send("Got that message!")



client.run('NzA4MDQyNDYxMTI1MTQ4NzAz.XrWU5Q.YbsCzj7TcljBsS_HOPvG0iVt3HA')
