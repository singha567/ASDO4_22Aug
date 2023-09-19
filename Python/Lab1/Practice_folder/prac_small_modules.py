def new_string(text):
  if len(text) >= 2 and text [:2] == "Is":
    return text[-1:-3]
  return "Is" + text[1:2]

print(new_string("Array"))
print(new_string("IsEmpty")) 