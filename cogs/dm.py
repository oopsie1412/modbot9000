import discord
from discord.ext import commands
import datetime


class Dm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        reportchannel = self.bot.get_channel(875562790528647189)

        def check(m):
            return m.author == message.author

        if not message.content.startswith('?'):

            if not message.guild and not message.author.bot:

                exclude = ['Y', 'y', 'N', 'n', '1', '2']

                if message.content not in exclude:
                    await message.channel.send("Hey there! You're about to file the previous message as a report to the mods. **Type `Y` to continue and `N` to exit**")
                    report = message.content

                confirm = await self.bot.wait_for('message', check=check)
                confirmcontent = confirm.content

                if confirmcontent == "Y" or confirmcontent == "y":
                    await message.channel.send("Sounds good! Would you like to file your report anonymously **(`1`)** or not **(`2`)**? *If not, only server mods will know who you are.* This lets them reach out to you in the future!")

                    anon = await self.bot.wait_for('message', check=check)
                    anoncontent = anon.content

                    if anoncontent == "1":
                        user = "Anonymous"

                        embed = discord.Embed(color=0xED4245) #Red
                        embed.add_field(name=user + ' has filed a report!', value=report, inline=True)
                        embed.set_footer(text='Filed on ' + str(datetime.datetime.now()))
                        await reportchannel.send(embed=embed)
                        await reportchannel.send("<@&731214145101496390>")

                        
                        await message.channel.send("Anonymous report sent!")

                    if anoncontent == "2":
                        user = message.author.display_name + '#' + message.author.discriminator

                        embed = discord.Embed(color=0xED4245) #Red
                        embed.add_field(name=user + ' has filed a report!', value=report, inline=True)
                        embed.set_footer(text='Filed on ' + str(datetime.datetime.now()))
                        await reportchannel.send(embed=embed)
                        await reportchannel.send("<@&731214145101496390>")

                        await message.channel.send("Report sent!")

                if confirmcontent == "N" or confirmcontent == "n":
                    await message.channel.send("Your report has been *cancelled*!")


def setup(bot):
    bot.add_cog(Dm(bot))