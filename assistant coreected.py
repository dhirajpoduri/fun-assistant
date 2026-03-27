import random
import datetime
import webbrowser

JOKES = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "What do you call fake spaghetti? An impasta!",
    "Why did the computer get cold? It left its Windows open.",
    "I told my computer I needed a break, and it said 'No problem — I'll go to sleep.'"
]

RESPONSES = {
    "hello": "Hey there! I'm your fun assistant. Try: joke, time, date, open, play, quit",
    "help": "Commands: joke, time, date, calc, open, play, quit",
}

def tell_joke():
    print(random.choice(JOKES))

def tell_time():
    now = datetime.datetime.now()
    print("Current time:", now.strftime("%H:%M:%S"))

def tell_date():
    today = datetime.date.today()
    print("Today's date:", today.strftime("%Y-%m-%d"))

def calc(expr):
    try:
        # Safe eval without builtins
        ans = eval(expr, {"__builtins__": None}, {})
        print(f"{expr} = {ans}")
    except Exception as e:
        print("Could not calculate:", e)

def open_site(site):
    if not site.startswith(("http://", "https://")):
        site = "http://" + site
    try:
        webbrowser.open(site)
        print("Opened", site)
    except Exception as e:
        print("Error opening", site, e)

def play():
    print("Let's play rock-paper-scissors!")
    choices = ["rock", "paper", "scissors"]
    user = input("Choose rock/paper/scissors: ").strip().lower()
    if user not in choices:
        print("Invalid choice.")
        return
    comp = random.choice(choices)
    print("Computer chose", comp)
    if user == comp:
        print("It's a tie!")
    elif (user, comp) in [("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")]:
        print("You win!")
    else:
        print("Computer wins!")

