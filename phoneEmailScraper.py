#! python3

import re, pyperclip

# Create a regex for phone numbers
phoneRegex = re.compile(r'''
# 415-412-1521, 412-1521, (415) 412-1521, 412-1521 ext 12345, 412-1521 ext. 12345, 412-1521 x12345
(
((\(\d\d\d\))|(\d\d\d))?    # Area code(optional)
(\s | -)    # First separator
\d\d\d      # First 3 digits
-           # Second separator
\d\d\d\d    # Last 4 digits
(((ext(\.)?\s)|x)?    # Extension word-part(optional)
    (\d{2,5}))?          # Extension number-part(optional)
)
''', re.VERBOSE)


# Create a regex email addresses
emailRegex = re.compile(r'''
# some.+_thing@something.com

[a-zA-z0-9_.+]+    # name part
@                  # @ symbol
[a-zA-z0-9_.+]+    # domain name part
''', re.VERBOSE)

# Get the text off the clipboard
text = pyperclip.paste()

# Extract the email/phone numbers from this text
emailList = emailRegex.findall(text)
phoneList = phoneRegex.findall(text)
extractedPhones = []

for i in phoneList:
    extractedPhones += [i[0]]

# Copy the extracted email and phone numbers to the clipboard
results = '\n'.join(extractedPhones) + '\n' + '\n'.join(emailList)
pyperclip.copy(results)
