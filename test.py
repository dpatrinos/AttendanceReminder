old_price = 26100.34
price = 27001.32

old_price_k = int(old_price/1000)
price_k = int(price/1000)

print("Old price: " + str(old_price_k))
print("New price: " + str(price_k))

if (price_k>old_price_k and not(old_price_k==0)):
    print("Shift from " + str(old_price_k) + "k to " + str(price_k) + "k")