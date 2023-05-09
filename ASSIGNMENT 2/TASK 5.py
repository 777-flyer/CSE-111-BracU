def email_domain(email_address, new, old="kaaj.com"):
    domain = email_address.split("@")

    if domain[1] != new:
        domain[1] = new
        new_email = domain[0] + "@" + domain[1]
        print(f'Changed: {new_email}')
    else:
        print(f'Unchanged: {email_address}')


email_domain(input("Enter your old email: "),
             input("Enter your new domain: "),
             input("Enter your old domain: "))
