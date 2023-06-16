import wmi

c = wmi.WMI()
def Get_CPU_other_info():
    # # 硬盘序列号
    for physical_disk in c.Win32_DiskDrive():
        print("硬盘序列号", physical_disk.SerialNumber)

    # CPU序列号
    for cpu in c.Win32_Processor():
        print("CPU序列号", cpu.ProcessorId.strip())

    # 主板序列号
    for board_id in c.Win32_BaseBoard():
        print("主板序列号", board_id.SerialNumber)

    # mac地址
    for mac in c.Win32_NetworkAdapter():
        print("mac地址", mac.MACAddress)

    # bios序列号
    for bios_id in c.Win32_BIOS():
        print("bios序列号", bios_id.SerialNumber.strip())

import socket
def get_computer_name_ip():
    """
    python获取 电脑名、ip地址
    :return:
    """
    #获取本机电脑名
    name = socket.getfqdn(socket.gethostname())
    #获取本机ip
    addr = socket.gethostbyname(name)
    return name,addr

def Get_cpu_percent():
    import psutil

    # 获取CPU信息
    cpu_percent = psutil.cpu_percent()  # CPU使用率
    cpu_count = psutil.cpu_count()  # CPU核数
    cpu_freq = psutil.cpu_freq()  # CPU频率

    print("CPU使用率：{0}%".format(cpu_percent))
    print("CPU核数：{0}".format(cpu_count))
    print("CPU频率：{0}MHz".format(cpu_freq.current))

    # 获取内存信息
    mem = psutil.virtual_memory()  # 内存使用情况

    mem_total = mem.total  # 总内存
    mem_used = mem.used  # 已用内存
    mem_percent = mem.percent  # 内存使用率

    print("总内存：{0:.2f}GB".format(mem_total/(1024*1024*1024)))
    print("已用内存：{0:.2f}GB".format(mem_used/(1024*1024*1024)))
    print("内存使用率：{0}%".format(mem_percent))

if __name__ == '__main__':
    myname,myaddr = get_computer_name_ip()
    print('电脑名:',myname)
    print('ip地址:',myaddr)
    Get_cpu_percent()
