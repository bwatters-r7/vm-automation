
# State Controllers
import esxiServer
import workstationServer

# Host Controllers
import sshHost
import workstationHost
import esxiHost

class managedHost:
	def __init__(self):
		self.stateController = None
		self.hostController = None
		self.name = None
		self.ipAddress = None
		
	def setName(self, name):
		self.name = name
		return self.name
	
	def getName(self, name):
		return self.name
	
	def setIpAddress(self, ipAddress):
		self.ipAddress = ipAddress
		return self.ipAddress
	
	def populteIpAddress(self):
		if stateController not None:
			

	def getIpAddress(self, ipAddress):
		self.ipAddress = ipAddress
		return self.ipAddress
	
	def setStateController(self, stateController):
		self.stateController = stateController
		return self.stateController
	
	
	def setHostController(self, hostController):
		self.hostController = hostController
		return self.hostController
	
	
	def getStateController(self):
		return self.stateController
	
	
	def getHostController(self):
		return self.hostController
	 
	def hasStateController(self):
		if self.stateController == None:
			return False
		else:
			return True

	def hasHostController(self):
		if self.stateController == None:
			return False
		else:
			return True
		
	def createHostController(self, hostControllerType):
		if hostControllerType == 'esxi':
			self.hostController = self.stateController.getVmByName(host.name)
			self.ipAddress = self.hostController.getVmIp()
		if hostControllerType == 'ssh':
			self.hostController = sshHost.sshHostController(self)
		
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
	