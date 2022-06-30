def sum_range(start, end):
  start, end = sorted((start, end))
  print(type(range(start, end + 1)))
  print(sum([start, end]))
  return sum(range(start, end + 1))

print(sum_range(9, 3))