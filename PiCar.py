from adafruit_crickit import crickit
import blynklib

# Add your blynk API key from the admin console or app
BLYNK_AUTH = 'ADD_API_KEY_HERE'

# The server is running on the same pi you're controlling 
# no change needed here
blynk = blynklib.Blynk(BLYNK_AUTH, server='0.0.0.0', port='8080')

momo1 = crickit.dc_motor_1
momo2 = crickit.dc_motor_2

@blynk.handle_event('write V0')
def go_forward(pin, value):
    if int(value[0]) == 1:
        momo1.throttle = 1
        momo2.throttle = 1
    else:
        momo1.throttle = 0
        momo2.throttle = 0

@blynk.handle_event('write V1')
def go_back(pin, value):
    if int(value[0]) == 1:
        momo1.throttle = -1
        momo2.throttle = -1
    else:
        momo1.throttle = 0
        momo2.throttle = 0

@blynk.handle_event('write V2')
def turn_right(pin, value):
    if int(value[0]) == 1:
        momo1.throttle = -1
        momo2.throttle = 1
    else:
        momo1.throttle = 0
        momo2.throttle = 0

@blynk.handle_event('write V3')
def turn_left(pin, value):
    if int(value[0]) == 1:
        momo1.throttle = 1
        momo2.throttle = -1
    else:
        momo1.throttle = 0
        momo2.throttle = 0
		
		
		
while True:
    blynk.run()
