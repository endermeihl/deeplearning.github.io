def isPalindrome(self, x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0: return False
    if x % 10 == 0 and x != 0: return False
    cur = 0
    num = x
    while int(num) != 0:
        cur = cur * 10 + int(num) % 10
        num /= 10
    return cur == x

isPalindrome(1,121)
