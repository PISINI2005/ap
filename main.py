# Read input
N = int(input())
F = list(map(int, input().split()))

# Sort desired delivery times
F.sort()

# Find the median
if N % 2 == 1:
    median = F[N // 2]
else:
    median = (F[N // 2 - 1] + F[N // 2]) // 2

# Assign delivery times: median - floor(N/2), ..., median + floor(N/2)
delivery_times = []
start_time = median - (N // 2)
for i in range(N):
    delivery_times.append(start_time + i)

# Sort both lists for optimal assignment
F.sort()
delivery_times.sort()

# Calculate total delay
total_delay = 0
for i in range(N):
    total_delay += abs(F[i] - delivery_times[i])

# Output result
print(total_delay)
