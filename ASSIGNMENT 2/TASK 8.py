def ddmmyy(days):
  years = days // 365
  rem_days = days % 365
  months = rem_days // 30
  rem_days = rem_days % 30

  return f"{years} years, {months} months and {rem_days} days"


print(ddmmyy(4000))