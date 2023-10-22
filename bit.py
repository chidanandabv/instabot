from instabot import bot
my_bot=bot()

#login cantain

my_bot.login(username="iam.chida1",password="chidananda@2004")

#follw the users
my_bot.follow_users(["ibe.cn","_its_me_dev.12","abhilash23_abhi"])
#my_bot.unfollow_non_followers()

#unfollow

my_bot.unfollow_non_nonfollowers()

#uploading img

my_bot.upload_photo("/home/chidananda/Downloads/photo.png",caption="life is fair when you love your self")

#sending a message to user

my_bot.send_message("hey bro i am a bot ","ibe.cn") 

#like and comment

my_bot.like_user("ibe,cn",amount=4)

user_id = my_bot.get_user_id_from_username("ibe.cn")
media_id=my_bot.get_last_user_medias(user_id)
my_bot.comment(media_id,"nice pic bro")


#list of followers

followers_list=my_bot.get_user_followers("ibe.cn")
following_list=my_bot.get_user_following("ibe.cn")

for count,each_followers in enumerate(followers_list):
    if count>4:
        continue
    sleep(2)
    print(my_bot.get_username_from_user_id(each_followers))

for count1,each_follow in enumerate(following_list):
    if count>4:
        continue
    sleep(5)

    print(my_bot.get_username_from_user_id(each_follow))
    my_bot.logout()

