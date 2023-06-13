def check_pair_of_socks(socks):
    sock_counts = {}

    # Count the occurrences of each sock color
    for sock in socks:
        if sock in sock_counts:
            sock_counts[sock] += 1
        else:
            sock_counts[sock] = 1

    # Check if all sock colors have an even count
    for count in sock_counts.values():
        if count % 2 != 0:
            return False

    return True

socks_input = input()
result = check_pair_of_socks(socks_input)
print(result)  
