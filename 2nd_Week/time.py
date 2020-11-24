seconds = 1000000
minutes = seconds // 60
hours = minutes // 60
leftover_hours = hours % 24
leftover_minutes = minutes % 60
print(leftover_hours - 12, leftover_minutes)
