from blish.blish import bot

@bot.command()
async def test(ctx, *, arg):
    ''''''
    await ctx.send(arg)