# ---- Sample Policies ----
policies = [
    {'PolicyID': 1, 'Owner': 'Alice', 'Premium': 1000, 'Payout': 5000, 'Active': True},
    {'PolicyID': 2, 'Owner': 'Bob', 'Premium': 1500, 'Payout': 7000, 'Active': True},
    {'PolicyID': 3, 'Owner': 'Charlie', 'Premium': 2000, 'Payout': 10000, 'Active': True}
]

# ---- Function to submit a claim ----
def submit_claim(policy_id):
    for policy in policies:
        if policy['PolicyID'] == policy_id:
            if policy['Active']:
                policy['Active'] = False
                print(f"Claim Approved for {policy['Owner']}! Payout: ${policy['Payout']}")
            else:
                print(f"Policy {policy_id} is already claimed or inactive.")
            return
    print(f"No policy found with ID {policy_id}.")

# ---- Function to list policies ----
def list_policies():
    print("\nCurrent Policies:")
    for policy in policies:
        status = "Active" if policy['Active'] else "Claimed/Inactive"
        print(f"ID: {policy['PolicyID']}, Owner: {policy['Owner']}, Status: {status}, Payout: ${policy['Payout']}")
    print()

# ---- Main Program ----
def main():
    while True:
        print("1. List Policies")
        print("2. Submit Claim")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            list_policies()
        elif choice == '2':
            try:
                pid = int(input("Enter Policy ID to claim: "))
                submit_claim(pid)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
