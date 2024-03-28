def main():
    input_str = input()
    symbol = input_str[0]
    numlist = [int(num) for num in input_str.split()[1:] if num.isdigit()]
    solve_problem(symbol, numlist)

def solve_problem(symbol, numlist):
    for num in numlist:
        print(symbol * num)

if __name__ == "__main__":
    main()
