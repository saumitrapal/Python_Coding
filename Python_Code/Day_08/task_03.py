import replit

def sealed_bid():
    bid_dictionary = {}
    bid = True
    
    while bid:
        user_name = input("Enter Your Name: ")
        bid_amount = int(input("Enter Your Bid Amount: $"))
        bid_dictionary[user_name] = bid_amount
        
        bid_continue = input("Are there any other bidders? Type 'yes or 'no': ")
        if bid_continue == "no":
            bid = False
            price_list = []
            for i in bid_dictionary:
                price_list.append(bid_dictionary[i])
                
            max_price = max(price_list)
            keys_found = []
            
            for key, value in bid_dictionary.items():
                if value == max_price:
                    keys_found.append(key)
            # print(keys_found)
            
            bid_winner = ''.join(keys_found)
            print(f"The winner is {bid_winner} with a bid of ${max_price}")
            
        else:
            replit.clear()
            continue 
               
sealed_bid()