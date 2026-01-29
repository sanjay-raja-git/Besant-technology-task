n=[]
for i in range(1,6):
    n.append(int(input("Enter a  {} natural Number:".format(i))))
print("the Average of given natural numbers is:", sum(n)/len(n))
