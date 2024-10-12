# Simple auction program
def auction():
    bidders = {}
    while True:
        name = input("What is your name? ").strip()
        bid = float(input("What is your bid? $").strip())
        bidders[name] = bid

        more_bidders = input("Are there any bidders? Type 'yes' or 'no': ").strip().lower()
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        if more_bidders == 'no':
            break

    winner = max(bidders, key=bidders.get)
    print(f"The winner is {winner} with the bid of ${bidders[winner]:.2f}")

# Run the auction
auction()
