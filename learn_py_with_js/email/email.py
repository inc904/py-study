import re
emailAddresses = [
    "john.doe@example1.com",
    "jane.smith@example2.com",
    "foo@bar.com",
];
regex = re.compile(r'([^@]+)@(.+)')

for email in emailAddresses:
    match = regex.match(email)
    if match:
        username, domain = match.groups()
        print(f"Username: {username}, Domain: {domain}")