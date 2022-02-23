import socket

from optparse import OptionParser

def open(ip,port): #测试端口是否开放
    s = socket.socket()
    try:
        s.connect((ip, port))
        return True
    except:
        return False

#默认扫描
def scan(ip,port):
    for x in port:
        if open(ip,x):
            print("%s host %s port open~"%(ip,x))
        else:
            print("%s host %s port close~" % (ip, x))

#范围扫描
def rscan(ip,s,e):
    for x in range(s, e):
        if open(ip, x):
            print("%s host %s port open~"%(ip, x))
        else:
            print("%s host %s port close~" % (ip, x))


def main():
    usage = "usage:xxx.py -i <ip address> -p <port>"  #帮助文件
    parser = OptionParser(usage=usage) #添加usage方法，xxx.py -h就会出现以上帮助
    parser.add_option("-i", "--ip", type="string", dest="ipadd", help="your target ip")
    parser.add_option("-p", "--port", type="string", dest="port", help="your target port")
    (options, args) = parser.parse_args()  #获取选项和参数进行赋值

    ip = options.ipadd
    port = options.port

    defaultport = [135, 139, 445, 1433, 3306, 3389, 5944]

    if ',' in port:  #xxx.py -i <ip address> -p 21,22,80
        port = port.split(',')
        a = []
        for x in port:
            a.append(int (x))
        scan(ip, a)

    elif '-' in port: #xxx.py -i <ip address> -p 21-80
        port = port.split('-')
        s = int(port[0])
        e = int(port[1])
        rscan(ip, s, e)

    elif 'all' in port:
        rscan(ip, 1, 65535)

    elif 'default' in port:
        scan(ip, defaultport)
    pass

if __name__ == '__main__':
    main()