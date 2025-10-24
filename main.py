def PrimeList(N):
    if N <= 2:
        return ""
    
    # 创建一个布尔数组，表示数字是否为质数
    is_prime = [True] * N
    # 0和1不是质数
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(N**0.5) + 1):
        if is_prime[i]:
            # 将i的倍数标记为非质数
            for j in range(i*i, N, i):
                is_prime[j] = False
    
    # 收集所有质数并转为空格分隔的字符串
    primes = [str(i) for i, prime in enumerate(is_prime) if prime]
    return ' '.join(primes)
