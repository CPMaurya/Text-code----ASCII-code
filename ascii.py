# Convertion from text code into ASCII code
meg = raw_input("Enter message to encode: ")
print "Decoded string in ASCII:"
for ch in meg:
   print ord(ch),
print "\n\n"

# Convertion from ASCII codes into text code
meg = raw_input("Enter ASCII codes: ")
decodedMessage = ""
for item in meg.split():
   decodedMessage += chr(int(item))   
print "Decoded message:", decodedMessage

