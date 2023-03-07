from datetime import datetime, timedelta
import requests
import json
import hashlib

API_TOKEN = 'b1af6276061948d7bf6459c834fc3e48' # pwned api token

def has_email_been_pwned(email):
    # Hint: You can be smart here and reuse existing code :)
    #
    # You will need to:
    #   - make a GET request
    #   - get the total number of breaches from the result
    #   - return an appropriate message

    url = f'https://haveibeenpwned.com/api/v3/breachedaccount/{email}'
    headers = {
        'User-Agent': 'cisco-jam',
        'hibp-api-key': API_TOKEN,
    }

    # Make your GET request here!

    pwned_times = 0 # This is where you come in!
    pwned_message = f'Oh no you have been pwned. The email "{email}" appeared in {pwned_times} breaches.'
    not_pwned_message = f'All good! The email "{email}" was never pwned.'

    return 'Not yet implemented :('


def get_sha1_hash(password):
    # What is a hash function, anyway?
    #
    # It's essentially a function that transforms data into a form that
    # is "impossible" (or at least, extremely time consuming...) to reverse,
    # ie. given the hash output of a password, it would be hard to figure out
    # what password it originated from. Hashing is a very important part of
    # cryptography, particularly around passwords.
    #
    # TMI? Don't worry. You don't really need to understand how hashing works
    # for this challenge.
    return hashlib.sha1(bytes(password, "utf8")).hexdigest()

def has_password_been_pwned(password):
    #
    #      !! DO NOT USE ANY OF YOUR REAL PASSWORDS AS INPUT !!
    #
    # This one is similar to the email challenge above, but with a few changes
    # and additional logic related to sending passwords (read the API docs).
    # If you've gotten this far, you should be well able for this final challenge :)
    # API docs: https://haveibeenpwned.com/API/v3#PwnedPasswords
    #
    #   GOOD LUCK!

    hash = get_sha1_hash(password)
    hash_prefix = '' # This is where you come in!
    url = f'https://api.pwnedpasswords.com/range/{hash_prefix}'  # NOTE: this url response is in `text` rather than `json()`

    # Make your GET request here!


    # Now you have a list of candidate hashes. From those, you'll need to count which ones
    # equal the full length hash you have above.

    # Now it's time to build the correct response message. You will have to update the pwned_message!
    all_good = f'All good! Your password was never pwned'
    pwned_message = f'Oh no you have been pwned. The password "{password}" appeared {0} times'

    return pwned_message
