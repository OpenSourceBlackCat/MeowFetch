from platform import uname
from getpass import getuser
from colorama import Fore, init as coloramaInit
from psutil import cpu_count, cpu_freq, virtual_memory, boot_time, disk_partitions, disk_usage
from datetime import timedelta
from time import time
from math import floor, log, pow
from GPUtil import getGPUs
class AmeyFetch:
	def __init__(self):
		coloramaInit()
		self.host = uname().system
		self.host_name = uname().node
		self.user_name = getuser()
		self.OS = f"{self.host_name} {uname().release}"
		self.OS_version = uname().version
		self.cpu_name = uname().processor
		self.cpu_count = cpu_count(logical=False)
		self.cpu_thread = cpu_count(logical=True)
		self.cpu_freq_max = cpu_freq().max
		self.gpu_name = getGPUs()[0].name
		self.gpu_mem = f"{getGPUs()[0].memoryUsed} MiB / {getGPUs()[0].memoryTotal} MiB"
		self.ram_usage = f"{self.memCon(virtual_memory().used)} / {self.memCon(virtual_memory().total)}"
		self.uptime = timedelta(seconds=(time()-boot_time()))
		self.disk_name = disk_partitions()[0].device.replace("\\", "")
		self.disk_usage = f"{self.memCon(disk_usage(disk_partitions()[0].mountpoint).used)} / {self.memCon(disk_usage(disk_partitions()[0].mountpoint).total)}"
		self.ameyFetchLogo = []
		self.totalInfo = []
	def memCon(self, size_bytes):
		if size_bytes == 0:
			return "0B"
		size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
		i = int(floor(log(size_bytes, 1024)))
		p = pow(1024, i)
		s = round(size_bytes / p, 2)
		return "%s %s" % (s, size_name[i])
	def getLogo(self):
		if len(self.ameyFetchLogo)==0:
			with open("logo.txt", "r") as logoFile:
				for line in logoFile:
					line = line.rstrip("\n")
					if line.endswith("."):
						line = line.rstrip(".")
					self.ameyFetchLogo.append(line)
		return self.ameyFetchLogo
if __name__ == "__main__": 
	ameyFetch = AmeyFetch()
	userNameWithHostName = f"{ameyFetch.user_name}@{ameyFetch.host_name}"
	finalPrintDesign = "-"*len(userNameWithHostName)
	ameyFetch.totalInfo.append(userNameWithHostName)
	ameyFetch.totalInfo.append(finalPrintDesign)
	ameyFetch.totalInfo.append(f"OS: {ameyFetch.OS}")
	ameyFetch.totalInfo.append(f"HOST: {ameyFetch.host}")
	ameyFetch.totalInfo.append(f"KERNEL: {ameyFetch.OS_version}")
	ameyFetch.totalInfo.append(f"UPTIME: {ameyFetch.uptime}")
	ameyFetch.totalInfo.append(f"CPU: {ameyFetch.cpu_name}")
	ameyFetch.totalInfo.append(f"CPU CORES: {ameyFetch.cpu_count}/{ameyFetch.cpu_thread}")
	ameyFetch.totalInfo.append(f"CPU FREQ: {ameyFetch.cpu_freq_max}")
	ameyFetch.totalInfo.append(f"GPU: {ameyFetch.gpu_name}")
	ameyFetch.totalInfo.append(f"GPU MEM: {ameyFetch.gpu_mem}")
	ameyFetch.totalInfo.append(f"SYSTEM MEM: {ameyFetch.ram_usage}")
	ameyFetch.totalInfo.append(f"DISK ({ameyFetch.disk_name}): {ameyFetch.disk_usage}")
	if (len(ameyFetch.totalInfo)>len(ameyFetch.getLogo())):
		for i in range(len(ameyFetch.totalInfo)):
			try:
				print(f"{ameyFetch.getLogo()[i]}{ameyFetch.totalInfo[i]}")
			except:
				print(f"{ameyFetch.getLogo()[i]}")
	else:
		for i in range(len(ameyFetch.getLogo())):
			try:
				print(f"{ameyFetch.getLogo()[i]}{ameyFetch.totalInfo[i]}")
			except:
				print(f"{ameyFetch.getLogo()[i]}")