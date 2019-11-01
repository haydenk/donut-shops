import numpy as np

shops = []
with open('shops.txt', 'r') as file:
    shop = []
    for text in file:
        if "https://www.yelp.com" in text:
            shops.append(shop)
            shop = []
        else:
            shop.append(text.strip())

csv = np.asarray(shops)
np.savetxt("shops.csv", csv, delimiter=",", fmt="%s")
