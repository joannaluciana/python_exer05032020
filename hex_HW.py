# def dex_hex(inp_num):   
#     dex_dict=(0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F")
#     hex_num=()
#     reminder=inp_num%16
#     out_hex=""
#     while inp_num > 0:
#         inp_num%16==result 
#         reminder == inp_num-result
#     for i in dex_dict: 
#             if i == reminder:
#                 hex_num.append(i)

#     out_hex= ''.join(reversed(hex_num))
#     return out_hex

# print(dex_hex(256))


# def test_dex_hex():
#     assert dex_hex(256) == 100






a = input('R - 0 - 255 ')
b = input('G - 0 - 255 ')
c = input('B - 0 - 255 ')
# print(rgb_to_name((0, 0, 255)))

def hexcolors (a,b,c ):
    dex_hex=""
    a_hex=hex(int(a))
    b_hex=hex(int(b))
    c_hex=hex(int(c))

   
    
    dex_hex="#"+a_hex[2:]+b_hex[2:]+c_hex[2:]
    return(dex_hex)

print(hexcolors (a,b,c))
