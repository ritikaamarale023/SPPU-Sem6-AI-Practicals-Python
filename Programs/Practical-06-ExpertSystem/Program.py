# Expert System - Help Desk Management

print("===== Help Desk Expert System =====")
print("Type 'exit' to stop\n")

while True:

    problem = input("Enter your problem: ").lower()

    if problem == "internet":
        print("Solution: Restart the router and check cables.")

    elif problem == "slow computer":
        print("Solution: Close unnecessary applications and restart system.")

    elif problem == "password reset":
        print("Solution: Click on 'Forgot Password' option.")

    elif problem == "printer":
        print("Solution: Check printer connection and install drivers.")

    elif problem == "software installation":
        print("Solution: Run installer as administrator.")

    elif problem == "exit":
        print("Thank you for using Help Desk Expert System.")
        break

    else:
        print("Solution not found in knowledge base.")
        