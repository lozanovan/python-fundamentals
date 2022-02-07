def prime_factors(n):
   #start factor
   i = 2
   factors_list = []

   while i * i <= n:
      #increase the iterator once the factor doesn't bring a whole number result
      if n % i:
         i += 1
      #save the factor, if it brings a whole number result
      else:
         n //= i
         factors_list.append(i)

   #use the remaining number, if there is one
   if n > 1:
      factors_list.append(n)
   return factors_list

n=int(input("Choose a number to find its prime numbers:"))
result=prime_factors(n)

#n=60: [2, 2, 3, 5]; n=61: [61]
print(f"The list of factors for number {n} are: {result}")