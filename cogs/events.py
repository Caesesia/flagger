import discord
from discord.ext import commands
from utils.events import list_events, show_event
from utils.long import split
from utils.pagination import Paginator
import json
from datetime import datetime
from babel.dates import format_datetime

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def events(self, ctx, number: int, time_start: str, time_stop: str):
        
        if time_start is None:
            time_start = int(datetime.now().timestamp())
        if time_stop is None:
            time_stop = int((datetime.now() + timedelta(days=7)).timestamp())

        data = list_events(number, time_start, time_stop)

        pages = []

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
            


            def format_french_datetime(dt_str):
                
                if dt_str == 'Inconnu':
                    return 'Inconnu'
                try:
                    dt = datetime.fromisoformat(dt_str.replace('Z', '+00:00'))
                    return format_datetime(dt, "EEEE d MMM y 'à' HH'h'mm", locale='fr')
                except Exception as e:
                    return dt_str

            

            ctf_start_formatted = format_french_datetime(ctf_start)
            ctf_finish_formatted = format_french_datetime(ctf_finish)

            embed = discord.Embed(
                title=f"📅  {number} premiers événements CTF du {time_start} au {time_stop}",
                description="Données récupérées depuis [CTFtime.org](https://ctftime.org/)",
                color=discord.Color.red()
            )

            embed.add_field(
                    name=f"🚩 {ctf_name}",
                    value=f"**Organisateur :** {orga_name}\n"
                    #f"**Description :** {ctf_description}\n"
                    f"**ID :** {ctf_id}\n"
                    f"**Date :** Du {ctf_start_formatted} au {ctf_finish_formatted}\n"
                    f"**Format :** {ctf_format}\n"
                    f"**Onsite :** {'Oui' if ctf_onsite else 'Non'}\n"
                    f"**Lieu :** {ctf_location}\n",
                    inline=False
                )

            embed.add_field(
                    name = "Liens",
                    value = f"**URLs :** [Site du CTF]({ctf_url}) | [Lien CTFtime]({ctftime_url})\n",
                    inline = False
                )
        
            embed.set_footer(
                    text = f"Récupéré depuis l'API CTFtime\nPage {len(pages) + 1}"
                )

            pages.append(embed)

        view = Paginator(pages)
        await ctx.send(embed = pages[0], view = view)



async def setup(bot):
    await bot.add_cog(Events(bot))
