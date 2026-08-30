def sealed_bid():
    bid_dictionary = {}
    bid = True
    
    while bid:
        user_name = input("Enter Your Name: ")
        bid_amount = int(input("Enter Your Bid Amount: $"))
        bid_dictionary[user_name] = bid_amount
        
        bid_continue = input("Type 'yes' for continue biding or Type 'no' for exit from biding: ")
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
            print(f"The Biding Winner is: {bid_winner}")
            
        else:
            continue 
               
sealed_bid()