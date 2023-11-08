import winreg


key_path = r"Software\Policies\Microsoft\Windows\System"
value_name = "DisableCMD"
key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path)
winreg.SetValueEx(key, value_name, 0, winreg.REG_DWORD,1) #The Last Value is the Value SET