import math
import numpy as np
def fix_saturate( value,width_bits):
        max_value = int(math.pow(2 , (width_bits-1))-1)
        min_value = int(math.pow(2 , (width_bits-1)) * (-1))

        if value >= max_value : 
            return max_value
        elif value <= min_value :
            return min_value
        else : 
            return value
        
def fix_multiplication(mult,frac_bits):
        array = np.array([mult], dtype=np.int64)
        mul = array >> frac_bits
        return fix_saturate(mul[0])