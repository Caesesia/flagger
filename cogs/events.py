import discord
from discord.ext import commands
from utils.events import list_events, show_event
from utils.long import split
import json

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def events(self, ctx, number: str, time_start: str, time_stop: str):

        data = list_events(number, time_start, time_stop)

        try:
            user_id = data['id_auteur']
            user_name = data['nom']

            embed = discord.Embed(
                title=f"Utilisateur: {user_name}",
                description=f"🔗 [Lien vers le profil Root-Me](https://www.root-me.org/{user_name})",
                color=discord.Color.red()
            )
            embed.add_field(name="Identifiant", value=user_id, inline=True)
            embed.set_footer(text = "Récupéré depuis l'API CTFtime")

            await ctx.send(embed=embed)
            print("✅ Embed OK")

        except Exception as e:
            await ctx.send(f"Erreur: {e}")
            print(f"❌ Error NON OK: {e}")

    @commands.command()
    async def ctf(self, ctx, event_id: str):

        data = show_event(event_id)

        try:
            user_id = data['id_auteur']
            user_name = data['nom']

            embed = discord.Embed(
                title=f"Utilisateur: {user_name}",
                description=f"🔗 [Lien vers le profil Root-Me](https://www.root-me.org/{user_name})",
                color=discord.Color.red()
            )
            embed.add_field(name="Identifiant", value=user_id, inline=True)
            embed.set_footer(text = "Récupéré depuis l'API CTFtime")

            await ctx.send(embed=embed)
            print("✅ Embed OK")

        except Exception as e:
            await ctx.send(f"Erreur: {e}")
            print(f"❌ Error NON OK: {e}")

async def setup(bot):
    await bot.add_cog(Events(bot))
