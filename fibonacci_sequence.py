#FIBONACCI OPERATION

no_of_terms=10
first_term=0
second_term=1
count=0
 
print('fibonacci sequence for',no_of_terms,':')
while count<no_of_terms:                       #if count holds true execute the statement below
    print(first_term,end=' ')    
    nth_term = first_term + second_term
    first_term = second_term
    second_term = nth_term
    count+=1
print()