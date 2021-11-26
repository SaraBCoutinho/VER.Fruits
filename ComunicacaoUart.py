from fpioa_manager import fm
from machine import UART
from board import board_info
from fpioa_manager import fm

from Maix import FPIOA

class fm:
  fpioa = FPIOA()

  def help():
    __class__.fpioa.help()

  def get_pin_by_function(function):
    return __class__.fpioa.get_Pin_num(function)

  def register(pin, function, force=False):
    pin_used = __class__.get_pin_by_function(function)
    if pin_used == pin:
      return
    if None != pin_used:
      info = "[Warning] function is used by %s(pin:%d)" % (
          fm.str_function(function), pin_used)
      if force == False:
        raise Exception(info)
      else:
        print(info)
    __class__.fpioa.set_function(pin, function)

  def unregister(pin):
    __class__.fpioa.set_function(pin, fm.fpioa.RESV0)

  def str_function(function):
    if fm.fpioa.GPIOHS0 <= function and function <= fm.fpioa.GPIO7:
      if fm.fpioa.GPIO0 <= function:
        return 'fm.fpioa.GPIO%d' % (function - fm.fpioa.GPIO0)
      return 'fm.fpioa.GPIOHS%d' % (function - fm.fpioa.GPIOHS0)
    return 'unknown'

  def get_gpio_used():
    return [(__class__.str_function(f), __class__.get_pin_by_function(f)) for f in range(fm.fpioa.GPIOHS0, fm.fpioa.GPIO7 + 1)]


if __name__ == "__main__":
  import time
  print('check register')
  for item in fm.get_gpio_used():
    print(item)
  print('test unregister')
  for pin in range(8, 48):
    fm.unregister(pin)
  print('check register')
  for item in fm.get_gpio_used():
    print(item)
  # gpio test
  from Maix import GPIO

  def gpio_test():
    for i in range(5):
      led_b.value(1)
      led_g.value(1)
      time.sleep_ms(100)
      print('woking...')
      led_b.value(0)
      led_g.value(0)
      time.sleep_ms(100)
      print('woking...')
  print('register...')
  fm.register(12, fm.fpioa.GPIO0)
  fm.register(13, fm.fpioa.GPIOHS0)
  led_b = GPIO(GPIO.GPIO0, GPIO.OUT)
  led_g = GPIO(GPIO.GPIOHS0, GPIO.OUT)
  gpio_test()
  print('unregister...')
  fm.unregister(12)
  fm.unregister(13)
  gpio_test()
  print('register...')
  fm.register(12, fm.fpioa.GPIO0)
  fm.register(13, fm.fpioa.GPIOHS0)
  gpio_test()
  fm.unregister(12)
  fm.unregister(13)
  # register Coverage test
  fm.register(12, fm.fpioa.GPIO0)
  time.sleep_ms(500)
  try:
    fm.register(13, fm.fpioa.GPIO0)  # fail
  except Exception as e:
    print('Exception')
    print(e)
  time.sleep_ms(500)
  fm.register(12, fm.fpioa.GPIOHS0)  # pass
  time.sleep_ms(500)
  print('Warning')
  fm.register(13, fm.fpioa.GPIOHS0, force=True)  # pass
  time.sleep_ms(500)
  fm.unregister(12)
  fm.unregister(13)


class board_info:
  def set(key, value=None):
    return setattr(__class__, key, value)
  def all():
    return dir(__class__)
  def get():
    return getattr(__class__, key)
  def load(__map__={}):
    for k, v in __map__.items():
      __class__.set(k, v)

from Maix import config
tmp = config.get_value('board_info', None)
if tmp != None:
    board_info.load(tmp)
else:
    print('[Warning] Not loaded from /flash/config.json to board_info.')

if __name__ == "__main__":
  def check_config_json(data):
    try:
      with open('/flash/config.json', 'rb') as f:
        tmp = json.loads(f.read())
        if tmp["type"] != data["type"]:
          raise Exception('config.json no exist')
    except Exception as e:
      with open('/flash/config.json', "w") as f:
        f.write(cfg)
      import machine
      machine.reset()

  print(board_info.all())
  board_info.set('test', 123)
  print(board_info.test)
  print(board_info.all())

  import json
  test = {
      "type": "test",
      "board_info": {
          'PIN10': 10,
          'BOOT_KEY': 16,
          'WIFI_TX': 6,
          'WIFI_RX': 7,
          'WIFI_EN': 8,
      }
  }
  cfg = json.dumps(test)
  check_config_json(test)
  from Maix import config
  tmp = config.get_value('board_info', None)
  if tmp != None:
    board_info.load(tmp)
  print(board_info.all())
  print(board_info.PIN10)
  print(board_info.BOOT_KEY)
  print(board_info.WIFI_TX)
  print(board_info.WIFI_RX)
  print(board_info.WIFI_EN)






# maixduino board_info PIN10/PIN11/PIN12/PIN13 or other hardware IO 12/11/10/3
fm.register(board_info.PIN10, fm.fpioa.UART1_TX, force=True)
#fm.register(board_info.PIN11, fm.fpioa.UART1_RX, force=True)
#fm.register(board_info.PIN12, fm.fpioa.UART2_TX, force=True)
#fm.register(board_info.PIN13, fm.fpioa.UART2_RX, force=True)

uart_A = UART(UART.UART1, 115200, 8, 0, 0, timeout=1000, read_buf_len=4096)
uart_B = UART(UART.UART2, 115200, 8, 0, 0, timeout=1000, read_buf_len=4096)

write_bytes =print('hello world')
for i in range(20):
    uart_A.write(str(write_bytes))
    if uart_A.any():
        read_data = uart_B.read()
        if read_data:
            print("write_bytes = ", write_bytes)
            if read_data == write_bytes:
                print("baudrate:115200 bits:8 parity:0 stop:0 ---check Successfully")

uart_A.deinit()
uart_B.deinit()
del uart_A
del uart_B 