# Cisco Jam 2023

### Challenge 3.4: Have I Been Pwned?

In these challenges, you will need to use the [Have I Been Pwned][pwned-site-url] web APIs. These APIs allow you to check if your email address or password were ever included in a data breach.

#### First, you need to check if a given email has appeared in any breaches.

Usage example:

```
You:
> @Bot check-email: god@heaven.com

Bot:
> Oh no you have been pwned. The "god@heaven.com" appeared in 10 breaches.
```
...looks like no one is safe :(

Notes:
- In the starter code (`has_email_been_pwned`), you have all you need to solve this. Plus some of your knowledge you learned earlier :)
- You can verify that by using the [have I been pwned site][pwned-site-url] directly.
- [Optional], or if you prefer `curl`, you can use the below command in the terminal:

```bash
curl -X GET --location "https://haveibeenpwned.com/api/v3/breachedaccount/god@heaven.com" \
    -H "Content-Type: application/json" \
    -H "user-agent: cisco-jam" \
    -H "hibp-api-key: b1af6276061948d7bf6459c834fc3e48"
```


#### Extra "Real-World" example: Implement a password check

Usage example:

```
You:
> @Bot check-password: qwerty

Bot:
> Oh no you have been pwned. The password "qwerty" appeared in 10579459 times.
```

The password check has a fair amount of logic, which is [explained in API docs here](https://haveibeenpwned.com/API/v3#PwnedPasswords). You will need to read it and then implement it.

In the "real-world", you are never given the steps on how to write the code to solve a task. Rather, you might get some hints and tips on where to find those steps :) ... if you are lucky :P

Notes:
- __!! DO NOT USE YOUR REAL PASSWORDS !!__ Instead, use one of: [most common passwords][wiki-common-passwords]
- The code template (`has_password_been_pwned`) has all the bits you need to implement it. We are giving you very little, as it supposed to be the hardest task of the day.
- Don't forget to check [the cheat sheet](../cheatsheet.py) too!
- You can verify the password by using the [have I been pwned password page][pwned-site-url-password] directly.
- [Optional], or if you prefer `curl`, you can use the below command in the terminal to call the API (here "0136E" is the hash part of the password you check):

```bash
curl -X GET --location "https://api.pwnedpasswords.com/range/0136E" \
    -H "Content-Type: application/json" \
    -H "user-agent: cisco-jam" \
    -H "hibp-api-key: b1af6276061948d7bf6459c834fc3e48"
```


[pwned-site-url]: https://haveibeenpwned.com/
[pwned-site-url-password]: https://haveibeenpwned.com/Passwords
[wiki-common-passwords]: https://en.wikipedia.org/wiki/List_of_the_most_common_passwords
