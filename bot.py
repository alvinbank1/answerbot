import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("봇 사용 가능")


    game = discord.Game(":명령어")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message, randum=None):
    if message.content.startswith(":제작자"):
        await message.channel.send("alvinbank1#9942 입니다. 디스코드 답 해주는 봇에 봇이 있습니다!")
    if message.content.startswith(":명령어"):
        await message.channel.send("https://discord.gg/nywuW74")
    if message.content.startswith(":봇 이름"):
        await message.channel.send("봇 이름은 답 해주는 봇 입니다.")
    if message.content.startswith(":봇 테스트"):
        await message.channel.send("봇이 정상적으로 작동하고 있습니다")
    if message.content.startswith(":테스트"):
        await message.channel.send("봇이 정상적으로 작동하고 있습니다")
    if message.content.startswith("명령어 사용법"):
            await message.channel.send(":을 입력하고, 명령어를 입력하면 됩니다! 명령어는 ::명령어를 입력해 보세요! 또 질문은 ::질문 을 입력해 보세요!")
    if message.content.startswith(":질문"):
            await message.channel.send("https://discord.gg/nywuW74 참가한 후 질문 채널에 들어가세요!")
    if message.content.startswith(":공지"):
            await message.channel.send("아직 공지가 없습니다. alvinbank1#9942에 1:1 채팅으로 공지를 등록해 보세요!")
    if message.content.startswith(":공지 등록 방법"):
            await message.channel.send("공지는 관리자만 등록할 수 있습니다. 하지만 alvinbank1#9942 와 1:1 게인 채팅으로 문의 하여 공지를 수정할 수 있습니다 위에 내용은 현재 공지 입니다.")
    if message.content.startswith(":공지 등록"):
            await message.channel.send("공지는 관리자만 등록할 수 있습니다. 하지만 alvinbank1#9942 와 1:1 게인 채팅으로 문의 하여 공지를 수정할 수 있습니다 위에 내용은 현재 공지 입니다.")
    if message.content.startswith(":봇을 만든 날짜"):
            await message.channel.send("봇을 만든 날짜는 2020/4/8일 입니다.")
    if message.content.startswith(":1:1 개인 채팅"):
            await message.channel.send("alvinbank1#9942에 채팅을 하세요 게인메세지로 채팅을 하세요")
    if message.content.startswith(":답 해주는 봇 ID"):
        await message.channel.send("697024109787480064 입니다.")
    if message.content.startswith(":완성도"):
        await message.channel.send("아직 계발단계에 있습니다. 봇이 작동 하지 않을 수 있습니다. ⚠주의하세요!⚠  완성도 10% :make:")
    if message.content.startswith(":답 해주는 봇 토큰"):
        await message.channel.send("보안적 문제로 인해 토큰은 공개 할 수 없습니다. 토큰을 알아내면 봇에 큰 영향을 미칠 수 있습니다.")
    if message.author.guild_permissions.administrator == True:
        if message.content.startswith(":채팅"):
            channel = message.content[4:22]
            msg = message.content[23:]
            await client.get_channel(int(channel)).send(msg)
    if message.content.startswith(":DM"):
        author = message.guild.get_member(int(message.content[4:22]))
        msg = message.content[23:]
        await author.send(msg)
    if message.content.startswith(":뮤트"):
        author = message.guild.get_member(int(message.content[4:22]))
        role = discord.utils.get_member (int(message.content[4:12]))
        await author.add_roles(role)
    if message.content.startswith(":언뮤트"):
        author = on_message.guild.get_member(int(message.content[5:23]))
        role = discord.utils.get(message.guild.roles, name="뮤트")
        await author.remove_roles(role)
    if message.content.startswith(":경고"):
        author = message.guild.get_member(int(message.content[4:22]))
        file = openpyxl.load_workbook("경고.xlsx")
        sheet = file.active
        i = 1
        while True:
                if sheet["A" + str(i)].value == str(author.id):
                    sheet["B" + str(i)].value = int(sheet["B" + str(i)].value) + 1
                file.save("경고.xlsx")
                if sheet["B" + str(i)].value == 2:
                    await message.guild.ban(author)
                    await message.channel.send("경고 2회 누적입니다. 서버에서 추방됩니다.")
                else:
                    await message.channel.send("경고를 1회 받았습니다.")
                break
                if sheet["A" + str(i)].value == None:
                    sheet["A" + str(i)].value == str(author.id)
                    sheet["B" + str(i)].value=1
                    file.save("경고.xlsx")
                    await message.channel.sand("경고를 1회 받았습니다.")
                    break
                i += 1


client.run("봇 토큰 입력란")
