Player_name = [
    {
        "name": "Cristiano Ronaldo",
        "Instagram_follower": 679000000,
        "Description": "Prolific Portuguese forward and five-time Ballon d'Or winner.",
        "Country": "Portugal"
    },
    {
        "name": "Lionel Messi",
        "Instagram_follower": 517000000,
        "Description": "Argentine playmaker, World Cup champion, and eight-time Ballon d'Or winner.",
        "Country": "Argentina"
    },
    {
        "name": "Neymar Jr",
        "Instagram_follower": 242000000,
        "Description": "Skillful Brazilian winger known for his flair and dribbling mastery.",
        "Country": "Brazil"
    },
    {
        "name": "Kylian Mbappé",
        "Instagram_follower": 136000000,
        "Description": "Rapid French forward, World Cup winner, and Real Madrid star.",
        "Country": "France"
    },
    {
        "name": "David Beckham",
        "Instagram_follower": 87000000,
        "Description": "Iconic English midfielder renowned for his bending free-kicks.",
        "Country": "England"
    },
    {
        "name": "Ronaldinho",
        "Instagram_follower": 81000000,
        "Description": "Legendary Brazilian playmaker celebrated for joyful skill and creativity.",
        "Country": "Brazil"
    },
    {
        "name": "Erling Haaland",
        "Instagram_follower": 77000000,
        "Description": "Powerful Norwegian striker known for explosive pace and clinical finishing.",
        "Country": "Norway"
    },
    {
        "name": "Karim Benzema",
        "Instagram_follower": 74000000,
        "Description": "French striker, former Real Madrid captain, and Ballon d'Or winner.",
        "Country": "France"
    },
    {
        "name": "Sergio Ramos",
        "Instagram_follower": 69000000,
        "Description": "Commanding Spanish defender famed for leadership and clutch goals.",
        "Country": "Spain"
    },
    {
        "name": "Mohamed Salah",
        "Instagram_follower": 67000000,
        "Description": "Dynamic Egyptian winger and Liverpool's primary attacking focal point.",
        "Country": "Egypt"
    },
    {
        "name": "Paulo Dybala",
        "Instagram_follower": 58000000,
        "Description": "Agile Argentine forward known for precise finishing and technique.",
        "Country": "Argentina"
    },
    {
        "name": "Vinícius Júnior",
        "Instagram_follower": 56000000,
        "Description": "Electrifying Brazilian winger essential to Real Madrid's attack.",
        "Country": "Brazil"
    },
    {
        "name": "Jude Bellingham",
        "Instagram_follower": 54000000,
        "Description": "Dominant box-to-box English midfielder for Real Madrid.",
        "Country": "England"
    },
    {
        "name": "Zlatan Ibrahimović",
        "Instagram_follower": 54000000,
        "Description": "Acrobatic Swedish striker famous for spectacular, unorthodox goals.",
        "Country": "Sweden"
    },
    {
        "name": "James Rodríguez",
        "Instagram_follower": 53000000,
        "Description": "Creative Colombian playmaker with exceptional vision and ball-striking.",
        "Country": "Colombia"
    },
    {
        "name": "Paul Pogba",
        "Instagram_follower": 52000000,
        "Description": "Flamboyant French midfielder known for pinpoint passing range.",
        "Country": "France"
    },
    {
        "name": "Marcelo Vieira",
        "Instagram_follower": 50000000,
        "Description": "Technically gifted Brazilian left-back and multiple Champions League winner.",
        "Country": "Brazil"
    },
    {
        "name": "Luis Suárez",
        "Instagram_follower": 49000000,
        "Description": "Tenacious Uruguayan striker celebrated for relentless pressing and goal output.",
        "Country": "Uruguay"
    },
    {
        "name": "Robert Lewandowski",
        "Instagram_follower": 37000000,
        "Description": "Lethal Polish number nine with elite positional sense in the box.",
        "Country": "Poland"
    },
    {
        "name": "Luka Modrić",
        "Instagram_follower": 35000000,
        "Description": "Virtuoso Croatian midfielder, Real Madrid icon, and Ballon d'Or winner.",
        "Country": "Croatia"
    }
]

import random
import replit
    
def format_player_data(Player_name):
    ''' take player date and format player data and return in format'''
    
    account_name = Player_name["name"]
    account_follower = Player_name["Instagram_follower"]
    account_description = Player_name["Description"]
    account_country = Player_name["Country"]
    return  f"{account_name} a {account_description} from {account_country}"


def check_answer(user_gauss, a_followers, b_followers):
    ''' Takes user gauss and the follower account and return if they got it right '''
    
    if a_followers > b_followers:
        return user_gauss == "a"
    else:
        return user_gauss == "b"
                       
            
account_b = random.choice(Player_name)
score = 0 
game_should_continue = True

while game_should_continue:
    account_a = account_b
    account_b = random.choice(Player_name)
    print(f"Compare A: {format_player_data(account_a)}")
    print(f"Against B: {format_player_data(account_b)}")
    
    a_followers = account_a["Instagram_follower"]
    b_followers = account_b["Instagram_follower"]

    if account_a == account_b:
        account_b = random.choice(Player_name)
        
    user_gauss = input("Who has more instagram follower? Type 'A' or 'B': ").lower()
    is_correct = check_answer(user_gauss, a_followers, b_followers)

    if is_correct:
        score = score + 1
        print(f"You're right! Current score: {score}")
        replit.clear()
    else:
        print(f"You're worng! final score: {score}")
        game_should_continue = False
        