
import os
import platform
import socket
import psutil
import speedtest
from screeninfo import get_monitors
import pygetwindow as gw
import uuid

def get_installed_software_list():
    software_list = [line.split(' ')[0] for line in os.popen('wmic product get name').read().split('\n') if line]
    return software_list

def get_internet_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / 10**6  # Convert to Mbps
    upload_speed = st.upload() / 10**6  # Convert to Mbps
    return download_speed, upload_speed

def get_screen_resolution():
    monitors = get_monitors()
    resolutions = [(monitor.width, monitor.height) for monitor in monitors]
    return resolutions

def get_cpu_info():
    cpu_info = {
        'model': platform.processor(),
        'cores': psutil.cpu_count(logical=False),
        'threads': psutil.cpu_count(logical=True)
    }
    return cpu_info

def get_gpu_info():
    try:
        import GPUtil
        gpu_list = GPUtil.getGPUs()
        if gpu_list:
            return gpu_list[0].name
    except ImportError:
        pass
    return None

def get_ram_size():
    ram_size = psutil.virtual_memory().total / (1024 ** 3)  # Convert to GB
    return ram_size

def get_screen_size():
    try:
        screen_size = gw.getWindowsWithTitle('')[0].width, gw.getWindowsWithTitle('')[0].height
        return screen_size
    except ImportError:
        pass
    return None

def get_network_info():
    wifi_mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(5, -1, -1)])
    public_ip_address = socket.gethostbyname(socket.gethostname())
    return wifi_mac_address, public_ip_address

def get_windows_version():
    return platform.system() + ' ' + platform.version()

installed_software = get_installed_software_list()
internet_speed = get_internet_speed()
screen_resolution = get_screen_resolution()
cpu_info = get_cpu_info()
gpu_info = get_gpu_info()
ram_size = get_ram_size()
screen_size = get_screen_size()
wifi_mac_address, public_ip_address = get_network_info()
windows_version = get_windows_version()

print('Installed Software: ', installed_software)
print('Internet Speed (Download, Upload): ', internet_speed)
print('Screen Resolution: ', screen_resolution)
print('CPU Info: ', cpu_info)
print('GPU Info: ', gpu_info)
print('RAM Size: ', ram_size, 'GB')
print('Screen Size: ', screen_size)
print('Wifi MAC Address: ', wifi_mac_address)
print('Public IP Address: ', public_ip_address)
print('Windows Version: ', windows_version)
