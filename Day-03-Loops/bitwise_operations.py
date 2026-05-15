   # Bitwise Operations Demo
   a = 5 # 0101
   b = 3 # 0011

   print("AND:", a & b) # 0001 = 1
   print("OR:", a | b) # 0111 = 7
   print("XOR:", a ^ b) # 0110 = 6
   print("NOT a:", ~a) # -6
   print("Left Shift:", a << 1) # 1010 = 10
   print("Right Shift:", a >> 1) # 0010 = 2

   # Even/Odd check using &
   num = 10
   if num & 1:
       print(num, "is Odd")
   else:
       print(num, "is Even")
