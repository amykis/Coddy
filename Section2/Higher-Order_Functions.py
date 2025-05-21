"""
Challenge task5

Create a function named clean_email_list that takes a list of email addresses
and returns a list of valid, standardized email addresses.

Requirements:

    - Convert all emails to lowercase and strip all whitespace at the beginning or end

    - Only keep emails that:

        - Contain exactly one '@' symbol

        - Have at least one character before the '@'

        - Have at least one character after the ‘@’

Use map() and filter() to solve the problem.
"""


def clean_email_list(emails):
    # Write your code below
    valid_emails = []
    for email in emails:
        count = 0
        for el in email:
            if "@" in el and 0 < email.strip().lower().index("@") < len(email):
                count += 1
        if count == 1:
            print(email.strip().lower())
            valid_emails.append(email.strip().lower())

    return list(valid_emails)


emails = ['@nodomain.com', ' noat', ' multiple@@ats.com']
print(clean_email_list(emails))
