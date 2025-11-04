import discord
from discord.ext import commands
from utils.profile import get_profile
from utils.score import get_score
from utils.long import split

class Challenges(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def challenges(self, ctx, username: str):

        profile = get_profile(username)

        try:
            user_id = profile['id_auteur']

            data = get_score(user_id)

            user_name = data['nom']

            embed = discord.Embed(
                title=f"Utilisateur: {user_name}",
                description=f"🔗 [Lien vers le profil Root-Me](https://www.root-me.org/{user_name})",
                color=discord.Color.red()
            )

            validations = data['validations']

            # Split validations into chunks of 25
            chunks = [validations[i:i+25] for i in range(0, len(validations), 25)]

            for idx, chunk in enumerate(chunks, start=1):
                embed = discord.Embed(
                    title=f"✅ Challenges validés par {user_name} ({len(validations)} au total)",
                    description=f"Page {idx}/{len(chunks)}\n🔗 [Profil Root-Me](https://www.root-me.org/{user_name})",
                    color=discord.Color.red()
                )

                for challenge in chunk:
                    chall_name = challenge.get('titre', '')
                    chall_date = challenge.get('date', '')
                    embed.add_field(name=chall_name, value=chall_date, inline=False)

                embed.set_footer(text="Récupéré depuis l'API Root-Me")

                await ctx.send(embed=embed)
                #print("✅ Embed OK")

        except Exception as e:
            await ctx.send(f"Erreur: {e}")
            print(f"❌ Error NON OK: {e}")        

async def setup(bot):
    await bot.add_cog(Challenges(bot))
