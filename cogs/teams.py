import discord
from discord.ext import commands
from utils.teams import show_team
from utils.long import split

class Teams(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def team(self, ctx, team_id: str):

        data = show_team(team_id)

        try:
            team_name = data.get('name', 'Inconnu')
            team_id = data.get('id', 'Inconnu')
            main_alias = data.get('primary_alias', 'Inconnu')
            academic = data.get('academic', 'Inconnu')
            country = data.get('country', 'Inconnu')

            embed = discord.Embed(
                title=f"Équipe: {team_name}",
                description=f"🔗 [Lien vers la page de l'équipe](https://ctftime.org/team/{team_id})",
                color=discord.Color.red()
            )
            embed.add_field(name="**Identifiant :**", value=team_id, inline=True)
            embed.add_field(name="**Alias :**", value=main_alias, inline=True)
            embed.add_field(name="**Académique :**", value="Oui" if academic == "true" else "Non", inline=True)
            embed.add_field(name="**Pays :**", value=country, inline=True)
            embed.set_footer(text = "Récupéré depuis l'API CTFtime")

            await ctx.send(embed=embed)
            print("✅ Embed OK")



        except Exception as e:
            await ctx.send(f"Erreur: {e}")
            print(f"❌ Error NON OK: {e}")        

async def setup(bot):
    await bot.add_cog(Teams(bot))
