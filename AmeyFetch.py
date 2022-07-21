from platform import uname, node
from getpass import getuser
from psutil import cpu_count, cpu_freq, cpu_percent, virtual_memory, swap_memory, boot_time, disk_partitions, disk_usage, disk_io_counters
from GPUtil import getGPUs
class AmeyFetch:
	def __init__(self):
		self.host_name = node()
		self.user_name = getuser()
		self.cpu_name = uname().processor
		self.cpu_count = cpu_count(logical=False)
		self.cpu_thread = cpu_count(logical=True)
		self.cpu_freq_max = cpu_freq().max
		self.ram_usage = virtual_memory().used
		self.total_ram = virtual_memory().total
  
if __name__ == "__main__": 
	ameyFetch = AmeyFetch()
	for i in ameyFetch:
		print(i)
