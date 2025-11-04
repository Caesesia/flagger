import discord
from discord.ext import commands
from utils.team import show_team
from utils.long import split

class Teams(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def team(self, ctx, team_id: str):

        data = show_team(team_id)

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
    await bot.add_cog(Teams(bot))
