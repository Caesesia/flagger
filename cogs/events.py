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

            for event in data:

                organizers = event.get('organizers', [])
                orga_name = organizers[0].get('name', 'Inconnu') if organizers else 'Inconnu'
                ctftime_url = event.get('ctftime_url', 'https://ctftime.org/')
                ctf_name = event.get('title', 'Événement inconnu')
                ctf_id = event.get('id', 'N/A')
                ctf_description = event.get('description', 'Aucune description disponible')
                ctf_format = event.get('format', 'Inconnu')
                ctf_url = event.get('url', '#')
                ctf_onsite = event.get('onsite', False)
                ctf_start = event.get('start', 'Inconnu')
                ctf_finish = event.get('finish', 'Inconnu')
                ctf_location = event.get('location', 'Inconnu') if ctf_onsite else "En ligne"
                
                embed.add_field(
                    name=f"🚩 {ctf_name} - ID {ctf_id}",
                    value=f"**Organisateur:** {orga_name}\n"
                        #f"**Description:** {ctf_description}\n"
                        f"**Début:** {ctf_start}\n"
                        f"**Fin:** {ctf_finish}\n"
                        f"**Format:** {ctf_format}\n"
                        f"**Onsite:** {'Oui' if ctf_onsite else 'Non'}\n"
                        f"**Lieu:** {ctf_location}\n"
                        f"**Liens CTF:** [Site]({ctf_url}) | [CTFtime]({ctftime_url})\n"
                        "\u200B",
                    inline=False
                )
            
            embed.set_footer(text="Récupéré depuis l'API CTFtime")
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
