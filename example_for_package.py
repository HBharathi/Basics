#code1
#under package ,serveral modules are reside
def calc_gst():
    print("GST  calculated")
    
#code2
#reusing a package and modules
#importing type1
from ecommerence.shipping import calc_gst  #package -module

calc_gst()

#importing type2

from ecommerence import shipping

shipping.calc_gst()


