import discord

class Paginator(discord.ui.View):
    def __init__(self, pages, timeout=180):
        super().__init__(timeout=timeout)
        self.pages = pages
        self.page = 0

        # Disable back button at start
        self.back.disabled = True

        # Disable next button if only one page
        if len(pages) == 1:
            self.next.disabled = True

    async def update(self, interaction):
        # Disable buttons at boundaries
        self.back.disabled = self.page <= 0
        self.next.disabled = self.page >= len(self.pages) - 1
        await interaction.response.edit_message(embed=self.pages[self.page], view=self)

    @discord.ui.button(label="◀", style=discord.ButtonStyle.primary)
    async def back(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.page -= 1
        await self.update(interaction)

    @discord.ui.button(label="▶", style=discord.ButtonStyle.primary)
    async def next(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.page += 1
        await self.update(interaction)

    @discord.ui.button(label="🗑 Stop", style=discord.ButtonStyle.danger)
    async def stop(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        # Delete the message completely
        await interaction.message.delete()
        # Stop the view so discord.py cleans it up
        self.stop()
