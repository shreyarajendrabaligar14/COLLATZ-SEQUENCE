def generate_wiki_collatz(n):
    """Generates Collatz sequence and returns it as Wiki bullet points."""
    sequence = []
    
    
    temp_n = n
    while temp_n != 1:
        sequence.append(temp_n)
        if temp_n % 2 == 0:
            temp_n //= 2
        else:
            temp_n = 3 * temp_n + 1
    sequence.append(1) 
    
    
    print(f"== Collatz Sequence for {n} ==")
    for step, value in enumerate(sequence):
        
        print(f"* Step {step}: '''{value}'''")


start_val = 7
generate_wiki_collatz(start_val)
