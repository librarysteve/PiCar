import blynklib
from time import sleep
BLYNK_AUTH = 'ADD_AUTH_KEY_HERE'

blynk = blynklib.Blynk(BLYNK_AUTH, server='0.0.0.0', port='8080')

@blynk.handle_event('write V0')
def test_input(pin, value):
    msg = "Virtual Pin Number {0} Value: {1}".format(pin, value)
    print(msg)

print("Connecting to the server\n")
print("Use ctrl+c to quit")

while True:
    try:
        blynk.run()
    except KeyboardInterrupt:
        print("\nExiting!")
        sleep(1)
        exit()
