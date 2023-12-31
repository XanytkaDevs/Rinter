import disnake
from disnake.ext import commands

class MemberInteractions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        await channel.send(f"Вечер в хату, **<@{member.id}>**!")
        await member.send("Привет, бро!")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = member.guild.system_channel
        await channel.send(f"**<@{member.id}>** покинул наш уголок!")
    
def setup(bot):
    bot.add_cog(MemberInteractions(bot))