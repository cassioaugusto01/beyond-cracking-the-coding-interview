def max_7_days(sales):
    l, r = 0, 0
    window_sum = 0
    cur_max = 0
    while r < len(sales):
        window_sum += sales[r]
        r += 1
        if r-l == 7:
            cur_max = max(cur_max, window_sum)
            window_sum -= sales[l]
            l += 1
    return cur_max

print(max_7_days([0, 3, 7, 12, 10, 5, 0, 1, 0, 15, 12, 11, 1]))
