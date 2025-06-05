import discord
from discord import app_commands
from discord.ext.commands import Bot, Cog


class MiscCog(Cog):
    def __init__(self, bot: Bot) -> None:
        super().__init__()

    @app_commands.command(name="parrot")
    async def parrot(self, interaction: discord.Interaction, message: str) -> None:
        embed = discord.Embed(title="Parrotくん", description="「{}」".format(message))
        embed.set_thumbnail(
            url="https://em-content.zobj.net/thumbs/240/twitter/322/parrot_1f99c.png"
        )
        await interaction.response.send_message(embed=embed)


async def setup(bot: Bot) -> None:
    await bot.add_cog(MiscCog(bot))
