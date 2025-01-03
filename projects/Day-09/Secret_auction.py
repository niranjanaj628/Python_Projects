#Secret Auction : Day-9

#function for retreiving the highest bidder's name and bid amount
def highest_bid(bids):
    name_list = list(bids.keys())
    bid_amounts=list(bids.values())
    winner_name=name_list[bid_amounts.index(max(bid_amounts))]
    
    return winner_name ,max(bid_amounts)

#initiating a dictionary to store the values of the bidders and their amounts as key-value pairs
bids={}

#loop to keep asking for bids until user says no
while True:
    name=input('What is your name? :')
    bid=int(input('What is your bid? :'))
    
    bids[name]=bid
    
    if input('Are there any other bidders? (yes/no) :').lower()=='no':
        break
    
#calling the function to find the highest bidder and their bid amount and printing the result
res=highest_bid(bids)
print(f"The winner is {res[0]} with a bid of {res[1]}")