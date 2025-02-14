from datetime import datetime, timedelta

# Subtract five days from current date
current_date = datetime.now()
new_date = current_date - timedelta(days=5)
print("Date five days ago:", new_date.strftime('%Y-%m-%d'))

# Print yesterday, today, tomorrow
yesterday = current_date - timedelta(days=1)
tomorrow = current_date + timedelta(days=1)
print("Yesterday:", yesterday.strftime('%Y-%m-%d'))
print("Today:", current_date.strftime('%Y-%m-%d'))
print("Tomorrow:", tomorrow.strftime('%Y-%m-%d'))

# Drop microseconds from datetime
now = datetime.now().replace(microsecond=0)
print("Current datetime without microseconds:", now)

# Calculate difference between two dates in seconds
date1 = datetime(2024, 2, 10, 12, 0, 0)
date2 = datetime(2024, 2, 14, 12, 0, 0)
difference = (date2 - date1).total_seconds()
print("Difference in seconds:", difference)