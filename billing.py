import numpy as np
products=np.array(["Rice","Sugar","Milk","Oil","Soap"])
price=np.array([60,45,30,150,35])
qty=np.array([5,2,4,1,3])
amount=price*qty
subtotal=amount.sum()
discount=subtotal*0.10
gst=(subtotal-discount)*0.05
final=subtotal-discount+gst
print(final)