# expencess = [1200,1300,1400,1500,1700]
# # total_expencess = expencess[0] + expencess[1] + expencess[2] + expencess[3]
# # print(total_expencess)
#
# total_expence = 0
# for expence in expencess:
#     total_expence = total_expence + expence
# print(total_expence)


# monthly_sales = [42,38,33,38,40,45,50]
# thresold = 35
#
# for sales_amount in monthly_sales:
#     if sales_amount > thresold:
#         print(f'sales_amount {sales_amount} is greaterthan thresold')
#     else:
#         print(f'sales_amount {sales_amount} is lessthan thresold')


# n = -5
# message = "Negative" \
#     if n >= 0 else "Positive"
# print(message)

# lst = [1, [2, 3], 4, [5, [6, 7]]]
# print(lst[3][1][0])

# for i in range(4):
#     print(i)

# animals = ["cat", "dog", "rabbit", "wolf"]
# animals.remove("lion")

for i in range(2,10):
    if i%5==0:
        break
    print(i)

office_supplies = ["pen", "paper", "stapler"]
kitchen_supplies = ["fork", "knife", "spoon"]
combined_list =  kitchen_supplies + office_supplies
print(combined_list[2: 4])

prices = [300, 50, 1200, 10]
sorted(prices)
print(prices[2])