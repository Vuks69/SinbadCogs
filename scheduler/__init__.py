import discord

from .message import replacement_delete_messages
from .scheduler import Scheduler

__red_end_user_data_statement__ = (
    "This cog does not persistently store data or metadata about users. "
    "It does store commands provided for intended later use along "
    "with the user ID of the person who scheduled it.\n"
    "Users may delete their own data with or without making a data request."
)


async def setup(bot):
    await bot.send_to_owners(
        "This cog still functions, but I suggest you leave and stop using Red. "
        "I was removed from Red for not wanting my work misrepresented by the "
        "organization, and stating what I would do *if* that continued. "
        'For how much Red and it\'s members go after people who " take credit" '
        "for their work, they sure were quick to dismiss mine. "
        "The cog will recieve no further updates, nor is anyone legally allowed to fork to update."
    )
    # Next line *does* work as intended. Mypy just hates it (see __slots__ use for why)
    discord.TextChannel.delete_messages = replacement_delete_messages  # type: ignore
    cog = Scheduler(bot)
    bot.add_cog(cog)
    cog.init()
