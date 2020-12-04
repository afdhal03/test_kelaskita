def recur_fibo(j):
   if j <= 1:
       return j
   else:
       return(recur_fibo(j-1) + recur_fibo(j-2))

n = int(input("Masukkan n bilangan fibonacci : "))

# check if the number of terms is valid
if n <= 0:
   print("Bukan Bilangan Bulat Positif")
else:
   print("Fibonacci sequence:")
   for i in range(n):
       print(recur_fibo(i))