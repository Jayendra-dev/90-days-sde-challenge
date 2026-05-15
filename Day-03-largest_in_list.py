   # Find largest in list without max()
   nums = [10, 45, 2, 99, 23, 67]
   largest = nums[0]

   for num in nums:
       if num > largest:
           largest = num

   print("Largest:", largest)
