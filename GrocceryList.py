while True: 
	try: 
		bg = float(input("Enter your budget : ")) 
		s = bg 
	except ValueError: 
		print("PRINT NUMBER AS A AMOUNT") 
		continue
	else: 
		break

a ={"name":[], "quant":[], "price":[]} 

b = list(a.values()) 

na = b[0] 

qu = b[1] 

pr = b[2] 

while True: 
	try: 
		ch = int(input("1.ADD\n2.EXIT\nEnter your choice : ")) 
	except ValueError: 
		print("\nERROR: Choose valid option") 
		continue
	else: 
		if ch == 1 and s>0:	 
				 
			pn = input("Enter product name : ") 
			q = input("Enter quantity : ") 
			p = float(input("Enter price of the product : ")) 

			if p>s: 
				print("\nCAN, T BUT THE PRODUCT") 
				continue

			else: 
				if pn in na: 
					ind = na.index(pn) 

					qu.remove(qu[ind]) 

					pr.remove(pr[ind]) 

					qu.insert(ind, q) 

					pr.insert(ind, p) 

					s = bg-sum(pr) 

					print("\namount left", s) 
				else: 
					na.append(pn) 

					qu.append(q) 

					pr.append(p)	 
 
					s = bg-sum(pr) 

					print("\namount left is", s) 

		elif s<= 0: 
			print("\nNO BUDGET LEFT") 
		else: 
			break

print("\nAmount left : Rs.", s) 

if s in pr: 
	print("\nNow you can only buy of amount", na[pr.index(s)]) 

print("\n\n\nYOUR GROCERY LIST IS") 
 
for i in range(len(na)): 
	print(na[i], qu[i], pr[i]) 
