class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SubscriptionSystem:
    def __init__(self):
        self.head = None

    def add_subscription(self, user, package):
        new_subscription = Node({"user": user, "package": package, "pickup_days": []})
        if not self.head:
            self.head = new_subscription
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_subscription

    def choose_package(self, user):
        print("Choose your subscription package:")
        print("1. Standard")
        print("2. Premium")
        print("3. VIP")

        try:
            choice = int(input("Enter the number corresponding to your choice: "))
            if choice == 1:
                package = "Standard"
            elif choice == 2:
                package = "Premium"
            elif choice == 3:
                package = "VIP"
            else:
                print("Invalid choice. Defaulting to Standard.")
                package = "Standard"
        except ValueError:
            print("Invalid input. Defaulting to Standard.")
            package = "Standard"

        self.choose_package_days(user, package)

    def choose_package_days(self, user, package):
        current = self.head
        while current:
            if current.data['user'] == user:
                current.data['package'] = package
                current.data['pickup_days'] = []  # Reset pickup days when choosing a new package
                if package == "Premium" or package == "VIP":
                    current.data['pickup_days'] = self.prompt_pickup_days(package)
                break
            current = current.next

    def prompt_pickup_days(self, package):
        days_to_choose = 2 if package == "Premium" else 3
        selected_days = []
        print(f"Choose {days_to_choose} pickup days for the {package} package:")
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        for i, day in enumerate(days_of_week, start=1):
            print(f"{i}. {day}")

        while len(selected_days) < days_to_choose:
            try:
                choice = int(input("Enter the number corresponding to your choice: "))
                if 1 <= choice <= len(days_of_week):
                    selected_days.append(days_of_week[choice - 1])
                else:
                    print("Invalid choice. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        return selected_days

    def display_subscriptions(self):
        current = self.head
        while current:
            print(f"User: {current.data['user']}, Package: {current.data['package']}, Pickup Days: {current.data['pickup_days']}")
            current = current.next

# Example Usage
subscription_system = SubscriptionSystem()

subscription_system.add_subscription("User1", "Standard")
subscription_system.add_subscription("User2", "Premium")
subscription_system.add_subscription("User3", "VIP")

subscription_system.choose_package("User1")
subscription_system.choose_package("User2")
subscription_system.choose_package("User3")

print("Current Subscriptions:")
subscription_system.display_subscriptions()
