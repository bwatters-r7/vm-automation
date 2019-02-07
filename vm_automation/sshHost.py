import datetime
import subprocess

class sshHostController:
    def __init__(self, name, ipAddr, username, password, logfile = "default.log"):
        self.type =             'ssh'
        self.name =             name
        self.os =               ""
        self.procList =         []
        self.ipAddr =           ipAddr
        self.password =         password
        self.username =         username
        self.testHost =         False
        self.arch =             None
        self.logFile =          "default.log"

    def logMsg(self, strMsg):
        if strMsg == None:
            strMsg="[None]"
        dateStamp = 'sshlog:[' + str(datetime.datetime.now())+ '] '
        try:
            logFileObj = open(self.logFile, 'a')
            logFileObj.write(dateStamp + str(strMsg) + '\n')
            logFileObj.close()
        except IOError:
            return False
        return True
    
    def getFileFromGuest(self, srcFile, dstFile):
        scpCommand = "pscp -pw " + self.password + " " + localFileName + " "
        scpCommand += self.username + "@" + self.ipAddr + ":" + remoteFileName
        self.logMsg("COMMAND: " + scpCommand)
        output = runSshCmd(scpCommand)
        self.logMsg("RESPONSE: " + str(output))
        return verifyLocalFile(dstFile)
        
    def makeDirOnGuest(self, dirPath):
        output = self.runCmdOnGuest(['mkdir ', dirPath])
        return output

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def isTestVm(self):
        return self.testHost

    def isReady(self):
        return False
    
    def verifyRemoteFile(self, fileName):
        output = self.runCmdOnGuest(['stat', fileName])[0]
        if 'Access' in output:
            return True
        else:
            return False

    def runCmdOnGuest(self, cmdAndArgList):
        plinkCmd = "plink -ssh -pw " + self.password + " " + self.username + "@" + self.ipAddr + " " + ' '.join(cmdAndArgList) 
        self.logMsg("COMMAND: " + plinkCmd)
        output = runSshCmd(plinkCmd)
        self.logMsg("RESPONSE: " + str(output))
        return output

    def setPassword(self, sshPassword):
        self.password = vmPassword

    def setTestVm(self):
        self.testVm = True

    def setUsername(self, sshUsername):
        self.username = sshUsername

    def setVmIp(self, ipAddress):
        self.ipAddr = ipAddress
        return True

    def updateProcList(self):
        self.procList = self.runCmdOnGuest('ps -ef')[0]
        return self.procList

    def uploadAndRun(self, srcFile, dstFile, remoteInterpreter = None, useCmdShell = False):
        remoteCmd = []
        if remoteInterpreter!= None:
            remoteCmd.append(remoteInterpreter)
        remoteCmd.append(dstFile)
        if not self.uploadFileToGuest(srcFile, dstFile):
            self.logMsg("[FATAL ERROR]: FAILED TO UPLOAD " + srcFile + " TO " + self.name)
            return False
        if 'win' not in self.os.lower():
            chmodCmdList = "/bin/chmod 755".split() + [dstFile]
            if not self.runCmdOnGuest(chmodCmdList):
                self.logMsg("[FATAL ERROR]: FAILED TO RUN " + ' '.join(chmodCmdList) + " ON " + self.name)
                return False
        if not self.runCmdOnGuest(remoteCmd):
            self.logMsg("[FATAL ERROR]: FAILED TO RUN '" + ' '.join(remoteCmd) + "' ON " + self.name)
            return False
        return True

    def uploadFileToGuest(self, srcFile, dstFile):
        scpCommand = "pscp -pw " + self.password + " " + srcFile
        scpCommand += " " + self.username + "@" + self.ipAddr + ":" + dstFile
        self.logMsg("COMMAND: " + scpCommand)
        output = runSshCmd(scpCommand)
        self.logMsg("RESPONSE: " + str(output))
        return self.verifyRemoteFile(dstFile)

    def runBin(remoteHost, username, password, binFileName):
        plinkCmd = "plink -ssh " + username + "@" + remoteHost + "/" + binFileName + " -pw " + password
        return plinkCmd

def runSshCmd(sshCmd):
    procObj = subprocess.Popen(sshCmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    output = procObj.communicate(input = 'n')
    return output

def verifyLocalFile( fileName):
    return os.path.isfile(fileName)
