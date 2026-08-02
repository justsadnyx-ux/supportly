from discord.ext import commands

from core.models import HostingMethod, PermissionLevel, getLogger

logger = getLogger(__name__)


def has_premium_predicate():
    async def predicate(ctx):
        if await ctx.bot.is_owner(ctx.author) or ctx.author.id == ctx.bot.user.id:
            return True

        support_guild_id = ctx.bot.config.get("support_guild_id")
        premium_role_id = ctx.bot.config.get("premium_role_id")

        if not support_guild_id or not premium_role_id:
            logger.warning(
                "Premium check is not configured (support_guild_id / premium_role_id unset)."
            )
            return False

        guild = ctx.bot.get_guild(int(support_guild_id))
        if guild is None:
            return False

        member = guild.get_member(ctx.author.id)
        if member is None:
            return False

        return discord.utils.get(member.roles, id=int(premium_role_id)) is not None

    predicate.fail_msg = (
        "You need to be in the support server and have the Premium role to use this command."
    )
    return predicate


def has_premium():
    """
    A decorator that checks if the author is in the support server
    and has the Premium role.
    """

    return commands.check(has_premium_predicate())


def has_permissions_predicate(
    permission_level: PermissionLevel = PermissionLevel.REGULAR,
):
    async def predicate(ctx):
        return await check_permissions(ctx, ctx.command.qualified_name)

    predicate.permission_level = permission_level
    return predicate


def has_permissions(permission_level: PermissionLevel = PermissionLevel.REGULAR):
    """
    A decorator that checks if the author has the required permissions.

    Parameters
    ----------

    permission_level : PermissionLevel
        The lowest level of permission needed to use this command.
        Defaults to REGULAR.

    Examples
    --------
    ::
        @has_permissions(PermissionLevel.OWNER)
        async def setup(ctx):
            await ctx.send('Success')
    """

    return commands.check(has_permissions_predicate(permission_level))


async def check_permissions(ctx, command_name) -> bool:
    """Logic for checking permissions for a command for a user"""
    if await ctx.bot.is_owner(ctx.author) or ctx.author.id == ctx.bot.user.id:
        # Bot owner(s) (and creator) has absolute power over the bot
        return True

    permission_level = ctx.bot.command_perm(command_name)

    if permission_level is PermissionLevel.INVALID:
        logger.warning("Invalid permission level for command %s.", command_name)
        return True

    if (
        permission_level is not PermissionLevel.OWNER
        and ctx.channel.permissions_for(ctx.author).administrator
        and ctx.guild == ctx.bot.supportly_guild
    ):
        # Administrators have permission to all non-owner commands in the Supportly Guild
        logger.debug("Allowed due to administrator.")
        return True

    command_permissions = ctx.bot.config["command_permissions"]
    checkables = {*ctx.author.roles, ctx.author}

    if command_name in command_permissions:
        # -1 is for @everyone
        if -1 in command_permissions[command_name] or any(
            str(check.id) in command_permissions[command_name] for check in checkables
        ):
            return True

    level_permissions = ctx.bot.config["level_permissions"]

    for level in PermissionLevel:
        if level >= permission_level and level.name in level_permissions:
            # -1 is for @everyone
            if -1 in level_permissions[level.name] or any(
                str(check.id) in level_permissions[level.name] for check in checkables
            ):
                return True
    return False


def thread_only():
    """
    A decorator that checks if the command
    is being ran within a Supportly thread.
    """

    async def predicate(ctx):
        """
        Parameters
        ----------
        ctx : Context
            The current discord.py `Context`.

        Returns
        -------
        Bool
            `True` if the current `Context` is within a Supportly thread.
            Otherwise, `False`.
        """
        return ctx.thread is not None

    predicate.fail_msg = "This is not a Supportly thread."
    return commands.check(predicate)


def github_token_required(ignore_if_not_heroku=False):
    """
    A decorator that ensures github token
    is set
    """

    async def predicate(ctx):
        if ignore_if_not_heroku and ctx.bot.hosting_method != HostingMethod.HEROKU:
            return True
        else:
            return ctx.bot.config.get("github_token")

    predicate.fail_msg = (
        "You can only use this command if you have a "
        "configured `GITHUB_TOKEN`. Get a "
        "personal access token from developer settings."
    )
    return commands.check(predicate)


def updates_enabled():
    """
    A decorator that ensures
    updates are enabled
    """

    async def predicate(ctx):
        return not ctx.bot.config["disable_updates"]

    predicate.fail_msg = (
        "Updates are disabled on this bot instance. "
        "View `?config help disable_updates` for "
        "more information."
    )
    return commands.check(predicate)
