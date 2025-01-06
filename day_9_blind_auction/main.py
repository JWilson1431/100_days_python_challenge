import art

print(art.logo)

#Create empty dictionary to hold bids
bids = {}
keep_bidding = True
#While the user wants to keep bidding
while keep_bidding:
    #Get bidding person's name
    name = input("What is your name?")
    #Get bid amount
    bidding_amount = int(input("How much do you want to bid?"))
    bid_again = input("Are there more bids? Type yes or no.")
    bids[name] = bidding_amount
    if bid_again.lower() == "no":
        keep_bidding = False
    if bid_again.lower() == "yes":
        print("\n" *50)

#Get the max bid from the dictionary
max_bid_key = max(bids, key = bids.get)
print(f"The winning bid is {max_bid_key} with the amount {bids[max_bid_key]}")

