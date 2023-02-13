age = int(input("How old are you? "))
income = int(input("How much do you make annually? "))
address = int(input("How long have you lived at your current address? "))
job = int(input("How long have you worked at your current job? "))

pts = 0

if age <= 20:
  pts -= 10
elif age < 30:
  pass
elif age < 50:
  pts += 20
else:
  pts += 30

if income <= 20000:
  pass
elif income <= 45000:
  pts += 12
elif income <= 70000:
  pts += 24
else:
  pts += 30
  
if address < 1:
  pts -= 5
elif address <= 3:
  pts += 5
elif address <= 8:
  pts += 12
else:
  pts += 20
  
if job < 2:
  pts -= 4
elif job <= 4:
  pts += 8
else:
  pts += 15

if pts <= 20:
  print("No card")
elif pts < 35:
  print("card with $500 limit")
elif pts < 60:
  print("card with $5000 limit")
else:
  print("card with $10000 limit")