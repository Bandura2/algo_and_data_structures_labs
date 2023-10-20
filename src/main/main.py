def calculate_width_board(n, w, h):

    if n < 1 or w < 1 or h < 1 or n >= 1012 or w >= 109 or h >= 109 or w == h:
        return -1, -1

    left = 1
    right = max(w, h) * n

    while left != right:
        temp = (left + right) // 2

        if ((temp // w) * (temp // h)) >= n:
            right = temp
        else:
            left = temp + 1

    return left
