# Find both 'magic' numbers for the 'ac' method of factoring a real quadratic polynomial
def find_magic_nums(a, b, c):
    ac = a * c
    for num in range(-ac, ac + 1):
        try:
            if ac % num == 0:
                other_divisor = ac // num
                if num + other_divisor == b:
                    return num, other_divisor
        except ZeroDivisionError:
            pass


# Implementation of Euclid's algorithm
def find_gcd(a, b):
    mx = max(a, b)
    mn = min(a, b)
    if mn == 0:
        return mx
    else:
        return find_gcd(mn, mx % mn)


# Factor a quadratic polynomial over the reals using the 'ac' method
def factor(a, b, c):
    disc = b ** 2 - 4 * a * c
    # Tell user if input cannot be factored over R
    if disc < 0:
        return 'This quadratic cannot be factored over the reals'
    else:
        magic_nums = find_magic_nums(a, b, c)
        magic_num_one = magic_nums[0]
        magic_num_two = magic_nums[1]
        format_term = lambda num: f"- {-num}" if num < 0 else f"+ {num}"

        if a != 1:  # We treat the a\neq 1 case using factoring by grouping
            gcd_1, gcd_2 = 0, 0
            for num in magic_nums:
                gcd_a = find_gcd(a, num)
                if gcd_a != 1:
                    temp_nums = list(magic_nums)[:]
                    temp_nums.pop(magic_nums.index(num))
                    gcd_1 = gcd_a
                    gcd_2 = find_gcd(c, temp_nums[0])
            gcd_3 = find_gcd(gcd_1, gcd_2)
            if gcd_3 == 1:
                return f'Factored, your polynomial is ({gcd_1}x {format_term(gcd_2)})(x {format_term(c//gcd_2)})'
            else:
                return f'Factored, your polynomial is {gcd_3}({gcd_1//gcd_3}x {format_term(gcd_2//gcd_3)})(x {format_term(c//gcd_2)})'
        else:
            return f'Factored, your polynomial is (x {format_term(magic_num_one)})(x {format_term(magic_num_two)})'


# a = 1 example 1
#print(factor(1, 7, 10))

# a = 1 example 2
#print(factor(1,-7,6))

# a = 1 example 3
#print(factor(1,7,90))

# Grouping example 1
#print(factor(2, 7, 3))

# Grouping example 2
#print(factor(2, 9, 9))

# Grouping example 3
#print(factor(6, 14, 4))