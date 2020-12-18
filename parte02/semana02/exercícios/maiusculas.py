def maiusculas(string):
  uppercase = ''
  for i in range(len(string)):
    if ord(string[i]) >= 65 and ord(string[i]) <= 90:
      uppercase += string[i]
  return uppercase
