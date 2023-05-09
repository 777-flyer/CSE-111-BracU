def vowelCalculator(name):

  vowels = "AEIOUaeiou"
  counter = 0
  vowel_container = ""
  for i in name:
    if i in vowels:
      counter += 1
      vowel_container += i + ","
  if counter == 0:
    return "No vowels in the name"
  else:
    return f'Vowels: {vowel_container} Total number of vowels: {counter}'

print(vowelCalculator("Steve Jobs"))