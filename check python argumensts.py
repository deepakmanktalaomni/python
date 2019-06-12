def ask_ok(prompt, retries = 4, reminder = 'PLease try your shit again!'):
    while True:
        ok = input(prompt)
        if ok in('y', 'yes', 'ye'):
            return True
        if ok in ('n','no', 'nae', 'nop', 'nope'):
            return False
        retries -= 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

ask_ok(prompt='asa')