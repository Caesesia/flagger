import discord
from discord.ext import commands
from utils.events import list_events, show_event
from utils.long import split
import json
from datetime import datetime

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def events(self, ctx, number: int, time_start: int, time_stop: int):

        data = list_events(number, time_start, time_stop)

        date_start = datetime.fromtimestamp(time_start)
        date_stop = datetime.fromtimestamp(time_stop)

        try:
            embed = discord.Embed(
                title=f"📅 Événements CTF du {date_start} au {date_stop}",
                description="Données récupérées depuis [CTFtime.org](https://ctftime.org/)",
                color=discord.Color.red()
            )

            orga_name = data['organizers']['name']
            ctftime_url = data['nom']
            ctf_name = data['title']
            ctf_id = data['id']
            ctf_description = data['description']
            ctf_format = data['format']
            ctf_url = data['url']
            ctf_onsite = data['onsite']
            ctf_start = data['start']
            ctf_finish = data['finish']
            
            if ctf_onsite == "true":
                ctf_location = data['location']

            for event in data:

                embed.add_field(
                    name=f"🚩 {ctf_name} - ID {ctf_id}",
                    value=f"**Organisateur:** {orga_name}\n"
                        f"**Description:** {ctftime_description}\n"
                        f"**Début:** {ctf_start}\n"
                        f"**Fin:** {ctf_finish}\n"
                        f"**Format:** {ctf_format}\n"
                        f"**Onsite:** {ctf_onsite}\n "
                        f"**Liens CTF:** [Site]({ctf_url}) | [CTFtime]({ctftime_url})",
                    inline=False
                )
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
