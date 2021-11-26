import sensor, image, lcd, time
import KPU as kpu
import uos

lcd.init()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_windowing((224, 224))
sensor.set_brightness(0)
sensor.set_auto_gain(1)
sensor.set_vflip(1)
lcd.clear()

labels=['freshapples','freshbanana','freshoranges','rottenapples', 'rottenbanana', 'rottenoranges'] #number of labels should match the number of labels the model was trained with

task = kpu.load(0x300000) #change to "/sd/name_of_the_model_file.kmodel" if loading from SD card
kpu.set_outputs(task, 0, 1, 1, 6) #the actual shape needs to match the last layer shape of your model

while(True):
    kpu.memtest()
    img = sensor.snapshot()
    #img = img.rotation_corr(z_rotation=90.0)   uncomment if need rotation correction - only present in full maixpy firmware
    #a = img.pix_to_ai()
    fmap = kpu.forward(task, img)
    plist=fmap[:]
    pmax=max(plist)
    max_index=plist.index(pmax)
    a = img.draw_string(0,0, str(labels[max_index].strip()), color=(255,0,0), scale=2)
    a = img.draw_string(0,20, str(pmax), color=(255,0,0), scale=2)
    print((pmax, labels[max_index].strip()))
    a = lcd.display(img)
    b = labels[max_index].strip()
    print("files:", uos.listdir("/sd"))
    with open("/sd/nome.txt", "w") as f:
     f.write(b)
    print("files:", uos.listdir("/sd"))

    with open("/sd/nome.txt", "r") as f:
     content = f.read()
    print("read:", content)

a = kpu.deinit(task)
