# year 11 repetition
# fibonacci sequence
# using a loop of your choice, print the first X of the fibonacci sequence
# 0 1 1 2 3 5 8 13 21 34 

fib = [0, 1] # start with 0 and 1

num_of_fibs = 10
counter = 0
while counter + 1 < (num_of_fibs):
    fib.append(fib[counter] + fib[counter + 1])
    counter += 1
print(fib)





