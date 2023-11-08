import time

def countdown(count):
    int = 0
    while int < count:
        print(f"{count - int} SECOND(S)!")
        int += 1
    print("HAPPY NEW YEAR!")

# countdown(10)

def countdown_with_sleep(count):
    i = 0
    while i < count:
        print(f"{count - i} SECOND(S)!")
        time.sleep(1)
        i += 1

    print("HAPPY NEW YEAR!")