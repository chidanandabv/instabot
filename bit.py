from instabot import bot
my_bot=bot()

#login cantain

my_bot.login(username="iam.chida1",password="chidananda@2004")

#follw the users
my_bot.follow_users(["ibe.cn","_its_me_dev.12","abhilash23_abhi"])
my_bot.unfollow_non_followers()

#unfollow

my_bot.unfollow_non_nonfollowers()

