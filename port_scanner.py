#// Don't forget to hit SUBSCRIBE, COMMENT, LIKE, SHARE! and LEARN... Its good to learn! :)
# But srsly, hit that sub button so you don't miss out on more content! 


'''Port scanner FOR ports ending in 000 eg, 1000,2000,3000 etc - 
untill find hidden service port'''


'''imports'''
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)


#port = 1000
for portx in range(1, 100):
    try:
        s.connect(('ad.samsclass.info', portx))
        r = s.recv(1024)
        if 'Congratulations' in r.decode('utf8'):
            print('[!] HIDDEN SERVICE FOUND: %s ~ %s' % (portx, r.decode('utf8')))
            s.close()
            break
        else:
            print('%s ~ %s' % (portx, r.decode('utf8')))
            s.close()
    except socket.error as err:
        print('%s ~ %s' % (portx, err))

    #port += 1000
