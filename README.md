# micro-eco-sim
A basic microeconomics simulator

microeconomics simulation

to execute:
> cd micro-eco-sim 
> python3 main.py

Entities
1. Person
2. Govt 
3. Goods
4. Auction
5. Universe

Universe contains all the other entities

Goods
- Number of goods = number of buyers. So everyone gets 1 per month (buyers not aware of it so they fear missing out)
- All goods equally important
- Scarcity is not modelled here (since everyone gets 1)
- Preferences are not modelled

Auction
- Seller's way of deciding on price and selling
- Every month 1 auction is run for each type of good
- At the end of auction, every buyer gets the item at the lowest bid for that auction (only fair way to ensure everyone gets the good). Eg if there are 3 people bidding Rs 10, Rs 20, Rs 30 for apple, each will get 1 apple at Rs 10.


Person (Consumer)
- Employed by govt
- Govt decides salary/user/cycle and salaries can be different
- Subscribes to an auction
	- Keeps bidding until it runs out of budget because they are afraid of losing out on goods just in case there is a scarcity (they don't know there're enough goods for everyone)
	- Increases bid by Re 1 each time if they see their bid is not the highest (only if buyer's budget allows)  
- End of month it whatever remains after spending is put into savings (which goes to bank)

Govt (Seller, bank, employer)
- It gets it's entire money back each month that it'd paid as salary at the end of month (either as savings or as payment for goods)
- It can choose to print money and inject into the economy by increasing people's salary in proportion every month
- At the end of month, announces cost of each good and inflation numbers