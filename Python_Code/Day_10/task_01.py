import psutil
import time


# print(psutil.net_if_addrs())
# print(psutil._ppid_map())
# print(psutil.boot_time())
# print(psutil.net_connections())
# print(psutil.disk_partitions())
# print(psutil.users())
# print(psutil.cpu_count())
print(psutil.net_io_counters().bytes_recv)

while True:
    print(f"{(psutil.net_io_counters().bytes_sent)}")
    time.sleep(1)

# print(dir(psutil))      # all fn or other moudule access via psutil