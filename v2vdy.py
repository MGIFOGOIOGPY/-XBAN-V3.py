import telebot
import requests
import datetime

TOKEN = "6805046418:AAE1OQGv9BJARLBFQe_C7u2Aiozp4_j2MhM"

# List of admin IDs


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👻")
    activate_user(message)

def activate_user(message):
    user_id = str(message.from_user.id)
   

@bot.message_handler(func=lambda message: True)

    
def get_player_info(message):
    
            if '--' in message.text:
                player_id = message.text.split('--')[1]
                id = player_id
                region = "me"

                url = 'https://freefireapi.com.br/api/search_id?id={}&region={}'.format(player_id, region)
                response = requests.get(url)
                if response.status_code == 200:
                    player_data = response.json()
                    basic_info = player_data.get('basicInfo', {})
                    profile_info = player_data.get('profileInfo', {})
                    history_ep_info = player_data.get('historyEpInfo', [])
                    clan_basic_info = player_data.get('clanBasicInfo', {})
                    captain_basic_info = player_data.get('captainBasicInfo', {})
                    social_info = player_data.get('socialInfo', {})

                    name = basic_info.get('nickname', 'Name not found')
                    level = basic_info.get('level', 'Level not found')
                    player_id = basic_info.get('accountId', 'Player ID not found')
                    exp = basic_info.get('exp', 'Experience not found')
                    liked = basic_info.get('liked', 'Likes not found')
                    last_login = datetime.datetime.utcfromtimestamp(int(basic_info.get('lastLoginAt', 0)))
                    creation_date = datetime.datetime.utcfromtimestamp(int(basic_info.get('createAt', 0)))
                    rank_token = basic_info.get('rankingPoints', 'Rank token not found')
                    rank_number = basic_info.get('rank', 'Rank number not found')
                    language = social_info.get('language', 'Language not found')
                    bio = social_info.get('signature', 'Bio not found')
                    guild_id = clan_basic_info.get('clanId', 'Guild ID not found')
                    admin_id = captain_basic_info.get('accountId', 'Admin ID not found')
                    admin_name = captain_basic_info.get('nickname', 'Admin name not found')
                    clan_level = clan_basic_info.get('clanLevel', 'Clan level not found')
                    clan_capacity = clan_basic_info.get('capacity', 'Clan capacity not found')
                    clan_max_capacity = clan_basic_info.get('memberNum', 'Clan maximum capacity not found')

                    Answer_message = f"اسم اللاعب: {name}\nمستوى اللاعب: {level}\nمعرف اللاعب: #{player_id}\nالخبرة: {exp}\nالإعجابات: {liked}\nآخر تسجيل دخول: {last_login}\nتاريخ الإنشاء: {creation_date} \nرمز التصنيف: {rank_token}\nرقم التصنيف: {rank_number}\nاللغة: {language}\nالسيرة الذاتية: {bio}\nمعرّف النقابة: {guild_id}\nمعرّف المسؤول: {admin_id}\nاسم المسؤول: {admin_name}\nمستوى العشيرة : {clan_level}\nسعة العشيرة: {clan_capacity}\nالسعة القصوى للعشيرة: {clan_max_capacity}\n\n مطور البوت \n @XmodG "

                    bot.reply_to(message, Answer_message)
                else:
                    print(message, "Invalid command format. Please use --Cemetery ID++Player ID.")
            else:
                print(message, "Invalid command format. Please use --Cemetery ID++Player ID.")
        
try:
    bot.polling()
except Exception as e:
    print(f"An error occurred: {str(e)}")