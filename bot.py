import discord
import re

class Bot(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
    
    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        # check call for !pepper command
        args = message.content.split()
        
        if args[0] == '!pepper':
            # 2 scenarios :
            # - 1 more argument and argument == help
            # - x more arguments of type user id
            if len(args) == 2 and args[1] == 'help':
                await message.channel.send('Pepper Bot send peppers to people like this:\n`!pepper @member1 @member2 @member3`')
            elif len(args) >= 2:
                # check if all arguments are valid member tags
                valid_member_tags = True
                for arg in args[1:]:
                    try:
                        member_id = re.search('<@!(.+?)>', arg).group(1)
                    except:
                        valid_member_tags = False
                        break
                
                if not valid_member_tags:
                    await message.channel.send('<@!{0}> all arguments must be valid user tags, for help please use `!pepper help`'.format(message.author.id))
                    return
                
                # if all is ok, send them a pepper, cheers !
                for member_tag in args[1:]:
                    await message.channel.send('{0}, here is a pepper for you ! :hot_pepper:'.format(member_tag))
            else:
                # with no argument send a notification to author
                await message.channel.send('<@!{0}> not enough arguments, for help please use `!pepper help`'.format(message.author.id))