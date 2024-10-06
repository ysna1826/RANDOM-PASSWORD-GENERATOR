import random
import string
def get():
    """GETTING USER PREFERENCES FOR PASSWORD"""
    length=int(input("ENTER THE LENGTH OF PASSWORD: "))
    upper=input("UPPERCASE LETTERS ? (y/n): ").lower()=='y'
    lower=input("LOWERCASE LETTERS ? (y/n): ").lower()=='y'
    digits=input("DIGITS ? (y/n): ").lower()=='y'
    symbols=input("SYMBOLS ? (y/n): ").lower()=='y'
    return length,upper,lower,digits,symbols
def generate(upper,lower,digits,symbols):
    """BUILDING THE PASSWORD BASED ON USER PREFERECES"""
    gen=""
    if upper:
        gen=gen+string.ascii_uppercase
    if lower:
        gen=gen+string.ascii_lowercase
    if digits:
        gen=gen+string.digits
    if symbols:
        gen=gen+string.punctuation
    return gen
def password(length,gen):
    """GENEATING THE PASSWORD"""
    pw=''.join(random.choice(gen) for _ in range(length))
    return pw
def main():
    """TO RETURN THE PASSWORD"""
    length,upper,lower,digits,symbols=get()
    gen=generate(upper,lower,digits,symbols)
    if not gen:
        print("NO CHARACTERS SETS ARE SELECTED.PLEASE SELECT AT LEAST ONE.")
        return
    pw=password(length,gen)
    print(f"PASSWORD IS: {pw}")
if __name__=="__main__":
    main()