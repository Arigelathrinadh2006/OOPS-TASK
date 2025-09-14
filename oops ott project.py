from datetime import datetime

class Content:
    def __init__(self, content_id, title, genre, rating):
        self.content_id = content_id
        self.title = title
        self.genre = genre
        self.rating = rating
    
    def get_info(self):  # info
        return f"'{self.title}' | Genre: {self.genre} | Rating: {self.rating}/10"

class Movie(Content):
    def __init__(self, content_id, title, genre, rating, duration):
        super().__init__(content_id, title, genre, rating)
        self.duration = duration
    
    def get_info(self):  # info
        return super().get_info() + f" | Duration: {self.duration} min"

class Series(Content):
    def __init__(self, content_id, title, genre, rating, seasons):
        super().__init__(content_id, title, genre, rating)
        self.seasons = seasons
    
    def get_info(self):  # info
        return super().get_info() + f" | Seasons: {self.seasons}"

class Subscription:
    def __init__(self, plan, price, days):
        self.plan = plan
        self.price = price
        self.days = days
    
    def get_details(self):  # details
        return f"{self.plan} Plan: ₹{self.price} for {self.days} days"

class User:
    def __init__(self, user_id, username, password):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.subscription = None
        self.watch_history = []
    
    def subscribe(self, app):  # subscribe
        print("Here are our subscription plans on Telugu Stream:")
        for i, sub in enumerate(app.subscriptions, 1):
            print(f"{i}. {sub.get_details()}")
        while True:
            ch = input("Pick the plan number that suits you best: ")
            if ch.isdigit() and 1 <= int(ch) <= len(app.subscriptions):
                self.subscription = app.subscriptions[int(ch) - 1]
                print(f"You’re now on the {self.subscription.plan} plan. Enjoy!")
                break
            else:
                print("Oops, that’s not a valid number. Give it another try.")
    
    def watch(self, app):  # watch
        if not self.subscription:
            print("You need a subscription to watch shows. Please subscribe first!")
            return
        app.show_catalog()
        ch = input("Enter the Content ID you want to watch: ")
        try:
            cid = int(ch)
            show = next((c for c in app.contents if c.content_id == cid), None)
            if show:
                info = show.get_info()
                print(f"{self.username} is now watching: {info}")
                self.watch_history.append((datetime.now(), info))
            else:
                print("Couldn’t find that show. Try another ID.")
        except ValueError:
            print("Please enter a valid number.")
    
    def show_history(self):  # history
        print("Your Watch History:")
        if not self.watch_history:
            print("You haven't watched anything yet. Start streaming soon!")
        else:
            for dt, info in self.watch_history:
                print(f"[{dt.strftime('%d-%m-%Y %H:%M')}] {info}")

class TeluguStreamApp:
    def __init__(self):
        self.users = []
        self.contents = []
        self.subscriptions = [
            Subscription("Basic", 99, 30),
            Subscription("Premium", 299, 90)
        ]
    
    def register_user(self):  # register
        print("Welcome to Telugu Stream! Let’s set up your account.")
        username = input("Choose your username: ")
        password = input("Choose a password: ")
        uid = len(self.users) + 1
        self.users.append(User(uid, username, password))
        print(f"Thanks for joining, {username}!")
    
    def login(self):  # login
        print("Login to your Telugu Stream account.")
        username = input("Username: ")
        password = input("Password: ")
        for u in self.users:
            if u.username == username and u.password == password:
                print(f"Welcome back, {username}!")
                return u
        print("Login failed. Check your username and password.")
        return None
    
    def show_catalog(self):  # catalog
        print("Telugu Stream Catalog:")
        if not self.contents:
            print("No shows or movies available right now. Check back later!")
            return
        for c in self.contents:
            print(f"ID:{c.content_id} | {c.get_info()}")
    
    def show_subscriptions(self):  # plans
        print("Subscription Plans:")
        for sub in self.subscriptions:
            print(sub.get_details())

app = TeluguStreamApp()
app.contents.append(Movie(306, "RRR", "Action, Drama, History", 8.0, 182))
app.contents.append(Movie(307, "KGF", "Action, Drama", 8.2, 156))
app.contents.append(Movie(308, "Baahubali: The Beginning", "Action, Drama, Fantasy", 8.1, 159))
app.contents.append(Movie(309, "Baahubali 2: The Conclusion", "Action, Drama, Fantasy", 8.2, 171))
app.contents.append(Movie(310, "Kalki", "Action, Thriller", 7.5, 132))

while True:
    print("\nWelcome to Telugu Stream! What would you like to do?")
    print("1. Register")
    print("2. Login")
    print("3. Browse Catalog")
    print("4. View Subscription Plans")
    print("5. Exit")
    ch = input("Your choice: ")
    try:
        ch_int = int(ch)
    except ValueError:
        print("Please enter a valid number.")
        continue
    
    if ch_int == 1:
        app.register_user()
    elif ch_int == 2:
        user = app.login()
        if user:
            while True:
                print(f"\nMenu for {user.username}:")
                print("1. Subscribe")
                print("2. Watch Content")
                print("3. View Watch History")
                print("4. Browse Catalog")
                print("5. Logout")
                ch_menu = input("Choose an option: ")
                try:
                    ch_menu_int = int(ch_menu)
                except ValueError:
                    print("Invalid input. Please select a valid option.")
                    continue
                
                if ch_menu_int == 1:
                    user.subscribe(app)
                elif ch_menu_int == 2:
                    user.watch(app)
                elif ch_menu_int == 3:
                    user.show_history()
                elif ch_menu_int == 4:
                    app.show_catalog()
                elif ch_menu_int == 5:
                    print("Logged out. See you again!")
                    break
                else:
                    print("Invalid option. Please choose a number from the menu.")
    elif ch_int == 3:
        app.show_catalog()
    elif ch_int == 4:
        app.show_subscriptions()
    elif ch_int == 5:
        print("Thank you for using Telugu Stream! Have a great day!")
        break
    else:
        print("Please enter a number from 1 to 5.")
