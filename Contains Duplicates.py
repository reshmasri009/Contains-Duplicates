nums = list(map(int, input("Enter numbers separated by space: ").split()))
seen = set()
for num in nums:
    if num in seen:
        print("True (duplicate found:", num, ")")
        break
    seen.add(num)
else:
    print("False (no duplicates)")
