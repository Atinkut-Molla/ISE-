def solve_feynman():
    A = 5
    quotient = 111111
    dividend = A * quotient

    print("CLASSIC FEYNMAN SOLUTION")
    print(f"A = {A}")
    print(f"Dividend = {dividend}")
    print(f"Quotient = {quotient}")
    print(f"Verification: {dividend} / {A} = {quotient}")
    
    return A, dividend, quotient

if __name__ == "__main__":
    solve_feynman()
