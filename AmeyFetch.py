from platform import uname, node
from getpass import getuser
from turtle import color
from colorama import Fore, init as coloramaInit
from psutil import cpu_count, cpu_freq, cpu_percent, virtual_memory, swap_memory, boot_time, disk_partitions, disk_usage, disk_io_counters
from GPUtil import getGPUs
class AmeyFetch:
	def __init__(self):
		coloramaInit()
		self.host_name = node()
		self.user_name = getuser()
		self.cpu_name = uname().processor
		self.cpu_count = cpu_count(logical=False)
		self.cpu_thread = cpu_count(logical=True)
		self.cpu_freq_max = cpu_freq().max
		self.ram_usage = virtual_memory().used
		self.total_ram = virtual_memory().total
		self.ameyFetchLogo = []
	def getLogo(self):
		if len(self.ameyFetchLogo)==0:
			with open("logo.txt", "r") as logoFile:
				for line in logoFile:
					self.ameyFetchLogo.append(line)
		return self.ameyFetchLogo
if __name__ == "__main__": 
	ameyFetch = AmeyFetch()
	userNameWithHostName = f"{ameyFetch.user_name}@{ameyFetch.host_name}"
	print("-"*len(userNameWithHostName))
	for i in range(len(ameyFetch.getLogo())):
		print(f"{ameyFetch.getLogo()[i]}{userNameWithHostName}".replace("\n", ""))
	print("-"*len(userNameWithHostName))