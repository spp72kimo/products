# 製作商品和價格的二維清單

products = []

while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入商品價格：')
	products.append([name,price])

for p in products:
	print(p[0], '的價錢是', p[1])

