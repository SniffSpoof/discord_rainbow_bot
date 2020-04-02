import discord
import asyncio
import random

token = 'Njk0NjU3NDU5Nzg4MTg1NjIw.XoS4pA.Mls2fwRw7iAz3curK4j5g_h6qgc' # токен бота
serverid = 676943098143703090# айди сервера
rainbowrolename = "𝕊𝕒𝕥𝕚𝕣𝕖™" # название роли
delay = 5 # интервал


client = discord.Client()
colours = [discord.Color.dark_orange(),discord.Color.orange(),discord.Color.dark_gold(),discord.Color.gold(),discord.Color.dark_magenta(),discord.Color.magenta(),discord.Color.red(),discord.Color.dark_red(),discord.Color.blue(),discord.Color.dark_blue(),discord.Color.teal(),discord.Color.dark_teal(),discord.Color.green(),discord.Color.dark_green(),discord.Color.purple(),discord.Color.dark_purple()]

async def rainbowrole(role):
	for role in client.get_guild(serverid).roles:
		if str(role) == str(rainbowrolename):
			print("detected role")
			i = 0
			while not client.is_closed():
				if i == len(colours):
					i = 0
				try:
					await role.edit(color=colours[i])
				except Exception:
					print("can't edit role, make sure the bot role is above the rainbow role and that is have the perms to edit roles")
					pass
				i += 1
				await asyncio.sleep(delay)
	print('role with the name "' + rainbowrolename +'" not found')
	print("creating the role...")
	try:
		await client.get_guild(serverid).create_role(reason="Created rainbow role", name=rainbowrolename)
		print("role created!")
		await asyncio.sleep(2)
		client.loop.create_task(rainbowrole(rainbowrolename))
	except Exception as e:
		print("couldn't create the role. Make sure the bot have the perms to edit roles")
		print(e)
		pass
		await asyncio.sleep(10)
		client.loop.create_task(rainbowrole(rainbowrolename))

@client.event
async def on_ready():
	client.loop.create_task(rainbowrole(rainbowrolename))
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('Ready.')
	print('------------')

client.run(token)
