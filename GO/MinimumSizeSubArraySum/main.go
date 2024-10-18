def subarrays_div_by_k(nums, k):
    remainder_count = {0: 1}
    total_sum = 0
    count = 0

    for num in nums:
        total_sum += num
        remainder = total_sum % k

        # Adjust negative remainders to positive
        if remainder < 0:
            remainder += k

        if remainder in remainder_count:
            count += remainder_count[remainder]

        remainder_count[remainder] = remainder_count.get(remainder, 0) + 1

    return count

# Example usage
nums = [4, 5, 0, -2, -3, 1]
k = 5
print(f"Number of subarrays divisible by {k}: {subarrays_div_by_k(nums, k)}")

