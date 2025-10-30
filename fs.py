def swap_first_two_digits(N):
    power_of_10 = 10
    temp = N
    while temp >= 100:
        temp //= 10
        power_of_10 *= 10

    first_digit = N // power_of_10
    second_digit = (N // (power_of_10 // 10)) % 10
    remaining_part = N % (power_of_10 // 10)

    new_number = (second_digit * power_of_10) + (first_digit * (power_of_10 // 10)) + remaining_part

    return new_number
