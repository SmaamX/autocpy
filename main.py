from os import system as sys
from sys import argv
import os
import random
import string

import mouseinfo
import pynput
try:
    if __name__ == '__main__':
        import os
        import random
        import string
        import tempfile
        import random
        import sys as si
        TMP = tempfile.gettempdir() + "\\" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        si._MEIPASS = str(TMP)
        import psutil
        import os
        import ctypes
        scrn = ctypes.windll.user32.GetForegroundWindow()
        print('scrn:',scrn)
        ctypes.windll.user32.SetWindowDisplayAffinity(scrn,1)
        sys('cls')
        try:
            import ctypes
            import random
            ntdll = ctypes.WinDLL("ntdll.dll")
            ntdll.NtQueryInformationProcess.restype = ctypes.c_int
            ntdll.NtQueryInformationProcess.argtypes = [ctypes.c_void_p, ctypes.c_uint, ctypes.c_void_p, ctypes.c_uint,
                                                        ctypes.POINTER(ctypes.c_uint)]
            def NtQueryInformationProcess(processHandle, processInformationClass, processInformation,
                                          processInformationLength, returnLength):
                return 0
            ntdll.NtQueryObject.restype = ctypes.c_int
            ntdll.NtQueryObject.argtypes = [ctypes.c_void_p, ctypes.c_uint, ctypes.c_void_p, ctypes.c_ulong,
                                            ctypes.POINTER(ctypes.c_ulong)]
            def NtQueryObject(objectHandle, objectInformationClass, objectInformation, objectInformationLength,
                              returnLength):
                return 0
            try:
                ntdll.NtQuerySessionInformation.restype = ctypes.c_int
                ntdll.NtQuerySessionInformation.argtypes = [ctypes.c_ulong, ctypes.c_uint, ctypes.c_void_p,
                                                            ctypes.c_ulong, ctypes.POINTER(ctypes.c_ulong)]
                def NtQuerySessionInformation(sessionId, sessionInformationClass, sessionInformation,
                                              sessionInformationLength, returnLength):
                    return 0
            except:
                print('QueSession - Fai')
            ntdll.NtQuerySystemInformation.restype = ctypes.c_int
            ntdll.NtQuerySystemInformation.argtypes = [ctypes.c_ulong, ctypes.c_void_p, ctypes.c_ulong,
                                                       ctypes.POINTER(ctypes.c_ulong)]
            def NtQuerySystemInformation(systemInformationClass, systemInformation, systemInformationLength,
                                         returnLength):
                return 0
            try:
                ntdll.PsLookupProcessByProcessId.restype = ctypes.c_int
                ntdll.PsLookupProcessByProcessId.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
                def PsLookupProcessByProcessId(processId, process):
                    return 0
            except:
                print('PsLookup - Fai')
            try:
                ntdll.PsGetProcessImageFileName.restype = ctypes.c_int
                ntdll.PsGetProcessImageFileName.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_ulong]
                def PsGetProcessImageFileName(process, imageName, imageNameSize):
                    return 0
            except:
                print('PsGet - Fai')
            def inject_process():
                target_process_id = random.randint(1000, 9999)
                kernel32 = ctypes.WinDLL('kernel32')
                OpenProcess = kernel32.OpenProcess
                OpenProcess.restype = ctypes.c_void_p
                process_handle = OpenProcess(0x1F0FFF, False, target_process_id)
                code_to_inject = b'''
            import ctypes
            kernel32 = ctypes.WinDLL('kernel32')
            dll_path = "kernel32.dll"
            kernel32.LoadLibraryA(dll_path)
            '''
                code_c_buffer = ctypes.create_string_buffer(code_to_inject)
                code_address = ctypes.addressof(code_c_buffer)

                kernel32.VirtualAllocEx.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t, ctypes.c_ulong,
                                                    ctypes.c_ulong]
                kernel32.VirtualAllocEx.restype = ctypes.c_void_p
                allocated_memory = kernel32.VirtualAllocEx(process_handle, 0, len(code_to_inject), 0x1000, 0x40)

                kernel32.WriteProcessMemory.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p,
                                                        ctypes.c_size_t, ctypes.POINTER(ctypes.c_size_t)]
                kernel32.WriteProcessMemory(process_handle, allocated_memory, code_address, len(code_to_inject), None)

                kernel32.CreateRemoteThread.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t,
                                                        ctypes.c_void_p, ctypes.c_void_p,
                                                        ctypes.c_ulong, ctypes.POINTER(ctypes.c_ulong)]
                kernel32.CreateRemoteThread.restype = ctypes.c_void_p
                kernel32.CreateRemoteThread(process_handle, None, 0, ctypes.cast(allocated_memory, ctypes.c_void_p),
                                            None, 0, None)


            inject_process()
            print('Inject - True')
        except:
            print('Inject - Fa')
        print('STemp:', TMP)
        length = random.randint(9, 10)
        proc = ''.join(random.choices(string.ascii_lowercase, k=length))
        argv[0] = proc
        print('Spoofed:', proc)
        pid = os.getpid()
        print('PID:', pid)
        try:
            import os

            kernel32 = ctypes.WinDLL("kernel32.dll")

            program_path = os.path.abspath(__file__)

            file_handle = kernel32.CreateFileW(
                program_path,
                ctypes.c_uint32(0x40000000),
                ctypes.c_uint32(0),
                None,
                ctypes.c_uint32(3),
                ctypes.c_uint32(128),
                None
            )

            kernel32.SetFileAttributesW(file_handle, 0x80000000)
            kernel32.CloseHandle(file_handle)
            print("SignSpoofed")
        except:
            pass
        try:
            print('[FucHide]')
            han = ctypes.windll.kernel32.GetModuleHandleW(None)
            ctypes.windll.kernel32.SetProcessWorkingSetSizeEx(han, -1, -1, 0x100)
            spoof2 = ''.join(random.choices(string.ascii_lowercase, k=length))
            ctypes.windll.kernel32.SetConsoleTitleW(spoof2)
            print('ConsoleTitle:', spoof2)
            ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)
            p = psutil.Process(pid)
            p.nice(psutil.HIGH_PRIORITY_CLASS)
            import ctypes
            kernel32 = ctypes.WinDLL('kernel32',use_last_error=True)
            getproc =kernel32.GetCurrentProcess()
            procid = kernel32.GetProcessId(getproc)
            prohan = kernel32.OpenProcess(0x1F0FFF,False,procid)
            kernel32.SetHandleInformation(prohan)
            #
            PROCESS_ALL_ACCESS = 0x1F0FFF
            PROCESS_QUERY_INFORMATION = 0x0400
            PROCESS_VM_READ = 0x0010
            han3 = ctypes.windll.kernel32.OpenProcess(PROCESS_ALL_ACCESS, False,
                                                      ctypes.windll.kernel32.GetCurrentProcessId())
            path = ctypes.create_unicode_buffer(1024)
            ctypes.windll.psapi.GetModuleFileNameExW(han3, 0, path, ctypes.sizeof(path))
            ctypes.windll.ntdll.NtSetInformationProcess(han3, 0x1D, path, ctypes.sizeof(path))
            ctypes.windll.kernel32.CloseHandle(han3)
            #
            F = 0
            jb_id = 0
            pid2 = ctypes.windll.kernel32.GetCurrentProcessId()
            try:
                SetProcessDefaultLayout = ctypes.windll.kernel32.SetProcessDefaultLayout
            except:
                print('EC/12/SetProcessDefaultLayout')
            try:
                IsProcessInJob = ctypes.windll.kernel32.IsProcessInJob
                IsProcessInJob(pid2, jb_id)
            except:
                print('EC/13/RemoveProcessFromJob')
                F = 1
            NtSetInformationProcess = ctypes.windll.ntdll.NtSetInformationProcess
            NtSetInformationProcess(pid2, 22, 0, 0)
            #
            import ctypes
            import struct


            def get_process_id(proc_name):
                PROC_ALL_ACCESS = 0x1F0FFF
                snapshot = ctypes.windll.kernel32.CreateToolhelp32Snapshot(0x2, 0)
                if snapshot != -1:
                    entry = ctypes.create_unicode_buffer(proc_name)
                    pe32 = struct.pack("I", 296)
                    if ctypes.windll.kernel32.Process32FirstW(snapshot, pe32):
                        while True:
                            # noinspection PyTypeChecker
                            if entry.value.lower() == ctypes.wstring_at(pe32 + 0x44).lower():
                                return struct.unpack("I", pe32)[0]
                            if not ctypes.windll.kernel32.Process32NextW(snapshot, pe32):
                                break
                    ctypes.windll.kernel32.CloseHandle(snapshot)
                return 0


            # noinspection PyTypeChecker
            def get_module_base_address(proc_id, mod_name):
                snapshot = ctypes.windll.kernel32.CreateToolhelp32Snapshot(0x8 | 0x10, proc_id)
                if snapshot != -1:
                    mod_entry = struct.pack("I", 44)
                    if ctypes.windll.kernel32.Module32FirstW(snapshot, mod_entry):
                        while True:
                            module_name = ctypes.wstring_at(mod_entry + 0x1c).split("\x00")[0]
                            if module_name.lower() == mod_name.lower():
                                return struct.unpack("I", mod_entry + 0x10)[0]
                            if not ctypes.windll.kernel32.Module32NextW(snapshot, mod_entry):
                                break
                    ctypes.windll.kernel32.CloseHandle(snapshot)
                return 0


            def patch_memory(address, value):
                PROCESS_VM_OPERATION = 0x0008
                PROCESS_VM_READ = 0x0010
                PROCESS_VM_WRITE = 0x0020
                PAGE_READWRITE = 0x04
                h_process = ctypes.windll.kernel32.OpenProcess(
                    PROCESS_VM_OPERATION | PROCESS_VM_READ | PROCESS_VM_WRITE, 0, int(address.split("-")[0]))
                if h_process:
                    old_protection = ctypes.c_long(0)
                    ctypes.windll.kernel32.VirtualProtectEx(h_process, int(address, 16), len(value), PAGE_READWRITE,
                                                            ctypes.byref(old_protection))
                    ctypes.windll.kernel32.WriteProcessMemory(h_process, int(address, 16), value, len(value), None)
                    ctypes.windll.kernel32.VirtualProtectEx(h_process, int(address, 16), len(value), old_protection,
                                                            ctypes.byref(old_protection))
                    ctypes.windll.kernel32.CloseHandle(h_process)


            process_mgr = ["ProcessHacker.exe", "TaskMgr.exe", "procexp.exe", "procexp64.exe", "procexp64a.exe"]
            HCD = input('AntiCheatPROC:')
            process_mgr.append(HCD)


            def hide():
                NtQuerySystemInformation = ctypes.windll.ntdll.NtQuerySystemInformation
                SYSTEM_PROCESS_INFORMATION = 5

                class SYSTEM_PROCESS_INFORMATION_Structure(ctypes.Structure):
                    _fields_ = [
                        ("NextEntryOffset", ctypes.c_ulong),
                        ("NumberOfThreads", ctypes.c_ulong),
                        ("WorkingSetPrivateSize", ctypes.c_size_t),
                        ("HardFaultCount", ctypes.c_ulong),
                        ("NumberOfThreadsHighWatermark", ctypes.c_ulong),
                        ("CycleTime", ctypes.c_ulonglong * 2),
                        ("CreateTime", ctypes.c_ulonglong),
                        ("UserTime", ctypes.c_ulonglong),
                        ("KernelTime", ctypes.c_ulonglong),
                        ("ImageName", ctypes.c_wchar * 260),
                        ("BasePriority", ctypes.c_long),
                        ("UniqueProcessId", ctypes.c_ulong),
                        ("InheritedFromUniqueProcessId", ctypes.c_ulong),
                        ("HandleCount", ctypes.c_ulong),
                        ("SessionId", ctypes.c_ulong),
                        ("UniqueProcessKey", ctypes.c_ulong),
                        ("PeakVirtualSize", ctypes.c_size_t),
                        ("VirtualSize", ctypes.c_size_t),
                        ("PageFaultCount", ctypes.c_ulong),
                        ("PeakWorkingSetSize", ctypes.c_size_t),
                        ("WorkingSetSize", ctypes.c_size_t),
                        ("QuotaPeakPagedPoolUsage", ctypes.c_size_t),
                        ("QuotaPagedPoolUsage", ctypes.c_size_t),
                        ("QuotaPeakNonPagedPoolUsage", ctypes.c_size_t),
                        ("QuotaNonPagedPoolUsage", ctypes.c_size_t),
                        ("PagefileUsage", ctypes.c_size_t),
                        ("PeakPagefileUsage", ctypes.c_size_t),
                        ("PrivatePageCount", ctypes.c_size_t),
                        ("ReadOperationCount", ctypes.c_ulonglong),
                        ("WriteOperationCount", ctypes.c_ulonglong),
                        ("OtherOperationCount", ctypes.c_ulonglong),
                        ("ReadTransferCount", ctypes.c_ulonglong),
                        ("WriteTransferCount", ctypes.c_ulonglong),
                        ("OtherTransferCount", ctypes.c_ulonglong),
                        ("WorkingSetSizePrivate", ctypes.c_size_t),
                        ("CommitCharge", ctypes.c_size_t),
                        ("PeakPagefileUsagePrivate", ctypes.c_size_t),
                        ("VadPhysicalPages", ctypes.c_size_t),
                        ("VadPhysicalPagesPeak", ctypes.c_size_t),
                        ("CommitChargeLimit", ctypes.c_size_t),
                        ("PeakWorkingSetSizePrivate", ctypes.c_size_t),
                        ("PrivatePageCountPeak", ctypes.c_size_t),
                        ("ThreadCount", ctypes.c_ulong),
                        ("DeletePending", ctypes.c_long),
                        ("Flags2", ctypes.c_ulong),
                        ("JobStatus", ctypes.c_ulonglong),
                        ("iob[0]", ctypes.c_void_p),
                        ("iob[1]", ctypes.c_void_p),
                        ("iob[2]", ctypes.c_void_p),
                        ("iob[3]", ctypes.c_void_p),
                        ("VadRoot", ctypes.c_void_p),
                        ("Session", ctypes.c_void_p),
                        ("ImageFileName", ctypes.c_wchar * 16),
                        ("PriorityClass", ctypes.c_ulong),
                        ("SecurityPort", ctypes.c_void_p),
                        ("Wow64Process", ctypes.c_void_p),
                        ("ImageFile", ctypes.c_void_p),
                    ]

                myNtQueryInformationProcessRVA = ctypes.windll.kernel32.GetProcAddress(
                    ctypes.windll.kernel32.GetModuleHandleA(b"ntdll.dll"), b"NtQuerySystemInformation")
                for proc_name in process_mgr:
                    proc_id = get_process_id(proc_name)
                    if proc_id:
                        h_proc = ctypes.windll.kernel32.OpenProcess(0x1F0FFF, False, proc_id)
                        if h_proc and h_proc != -1:
                            ntdll_base = get_module_base_address(proc_id, "ntdll.dll")
                            NtQueryInformationProcessRVA = (myNtQueryInformationProcessRVA - get_module_base_address(
                                ctypes.windll.kernel32.GetCurrentProcessId(), "ntdll.dll"))
                            patch_memory(hex(ntdll_base + NtQueryInformationProcessRVA + 0x3), b"\xB8\x35\x00\x00\x00")
                            ctypes.windll.kernel32.CloseHandle(h_proc)


            hide()
        except:
            print('[un_FucHide]')
except:
    print('un_spoof')


def cleanC(a):
    try:
        while True: a.remove(',')
    except:
        pass
    return a


def color(x, C):
    if C == 1: print('\u001b[31m' + x)
    if C == 2: print('\u001b[32m' + x)
    if C == 3: print('\u001b[34m' + x)

#Bruh
color('PyKernel32 - Beta/CLI',random.randint(1,3))


from random import randint as ri
from time import sleep as sl

try:
    import pyautogui
except ModuleNotFoundError:
    print('pip install pyautogui')
    exit()
#
PACCT = 0
PACC = 0
st = float(0)

def stf():
    global st
    st = float(st)
    st = float(ri(20, 70) * (10 ** -3))
    print(st)
    return float(st)
# module
def PACCS(YS):
    global st
    stf()
    global PACCT
    PLT = ri(1, YS)
    if PLT == YS:
        T = ri(2, 70)
        T = T * 10 ** -3
        F = ri(2, 40)
        F = F * 10 ** -3
    else:
        T = ri(2, 100)
        T = T * 10 ** -3
        F = ri(2, 41)
        F = F * 10 ** -3
    if T - PACCT + F > 0:
        T = T - (PACCT + F)
    else:
        T + PACCT - F
    PACCT = T
    print('PACCT:', PACCT)
    return PACCT


def PACCXY(YS):
    global st
    stf()
    global PACC
    SS = ri(1, 4)
    PLT = ri(1, YS)
    if PLT == YS:
        T = ri(1, 2)
        F = ri(1, 4)
    else:
        T = ri(1, 2)
        F = ri(1, 3)
    if SS == 1:
        T = T * -1
    elif SS == 2:
        F = F * -1
    elif SS == 3:
        T = T * -1
        F = F * -1
    elif SS == 4:
        pass
    if T - (PACC + F) < 0:
        T = T - (PACC + F)
    else:
        T + PACC - F
    PACC = T
    print('PACCTX:', PACC)
    return PACC


#
PACCT = 0
PACC = 0


# module
def PACCS(YS):
    global st
    stf()
    global PACCT
    PLT = ri(1, YS)
    if PLT == YS:
        T = ri(2, 70)
        T = T * 10 ** -3
        F = ri(2, 40)
        F = F * 10 ** -3
    else:
        T = ri(2, 100)
        T = T * 10 ** -3
        F = ri(2, 41)
        F = F * 10 ** -3
    if T - PACCT + F > 0:
        T = T - (PACCT + F)
    else:
        T + PACCT - F
    PACCT = T
    print('PACCT:', PACCT)
    return PACCT


def PACCXY(YS):
    global st
    stf()
    global PACC
    SS = ri(1, 4)
    PLT = ri(1, YS)
    if PLT == YS:
        T = ri(1, 2)
        F = ri(1, 4)
    else:
        T = ri(1, 2)
        F = ri(1, 3)
    if SS == 1:
        T = T * -1
    elif SS == 2:
        F = F * -1
    elif SS == 3:
        T = T * -1
        F = F * -1
    elif SS == 4:
        pass
    if T - (PACC + F) < 0:
        T = T - (PACC + F)
    else:
        T + PACC - F
    PACC = T
    print('PACCTX:', PACC)
    return PACC


#
TLPS = 0
DSS = 0
def ACC(RL):
    global st
    global TLPS
    global DSS
    stf()
    def movex(Rang):
        X = PACCXY(70)
        Y = PACCXY(70)
        T = PACCS(60)
        CrashS = ri(1, Rang)
        if CrashS == 1:
            pyautogui.move(X, Y, T)
        elif CrashS > 1:
            for x in range(1, CrashS):
                pyautogui.move(X, Y, T)
    TLP = ri(1, 3) + TLPS ** 2 - ri(1, 2)
    DS = ri(1, 12) + TLPS ** 2 - ri(1, 2)
    if DS == 1:
        if RL == 'R':
            pyautogui.mouseDown(button='right')
        elif RL == 'L':
            pyautogui.mouseDown(button='left')
        for pll in range(1, TLP): movex(4)
        sl(st)
        if RL == 'R':
            pyautogui.mouseUp(button='right')
        elif RL == 'L':
            pyautogui.mouseUp(button='left')
    if DS == 2:
        if RL == 'R':
            pyautogui.mouseDown(button='right')
        elif RL == 'L':
            pyautogui.mouseDown(button='left')
        sl(st)
        for pll in range(1, TLP): movex(4)
        if RL == 'R':
            pyautogui.mouseUp(button='right')
        elif RL == 'L':
            pyautogui.mouseUp(button='left')
    if DS == 3:
        if RL == 'R':
            pyautogui.mouseDown(button='right')
        elif RL == 'L':
            pyautogui.mouseDown(button='left')
        for pll in range(1, TLP): movex(4)
        sl(st)
        for pll in range(1, TLP): movex(4)
        if RL == 'R':
            pyautogui.mouseUp(button='right')
        elif RL == 'L':
            pyautogui.mouseUp(button='left')
    if DS == 4:
        for pll in range(1, TLP): movex(4)
        if RL == 'R':
            pyautogui.mouseDown(button='right')
        elif RL == 'L':
            pyautogui.mouseDown(button='left')
        sl(st)
        if RL == 'R':
            pyautogui.mouseUp(button='right')
        elif RL == 'L':
            pyautogui.mouseUp(button='left')
    if DS == 5:
        if RL == 'R':
            pyautogui.mouseDown(button='right')
        elif RL == 'L':
            pyautogui.mouseDown(button='left')
        sl(st)
        if RL == 'R':
            pyautogui.mouseUp(button='right')
        elif RL == 'L':
            pyautogui.mouseUp(button='left')
        for pll in range(1, TLP): movex(4)
    if DS == 6:
        if RL == 'R':
            pyautogui.mouseDown(button='right')
        elif RL == 'L':
            pyautogui.mouseDown(button='left')
        sl(st)
        for pll in range(1, TLP): movex(4)
        if RL == 'R':
            pyautogui.mouseUp(button='right')
        elif RL == 'L':
            pyautogui.mouseUp(button='left')
        for pll in range(1, TLP): movex(4)
    if DS == 7:
        if RL == 'R':
            pyautogui.mouseDown(button='right')
        elif RL == 'L':
            pyautogui.mouseDown(button='left')
        for pll in range(1, TLP): movex(4)
        sl(st)
        if RL == 'R':
            pyautogui.mouseUp(button='right')
        elif RL == 'L':
            pyautogui.mouseUp(button='left')
        for pll in range(1, TLP): movex(4)
    if DS == 8:
        for pll in range(1, TLP): movex(4)
        if RL == 'R':
            pyautogui.mouseDown(button='right')
        elif RL == 'L':
            pyautogui.mouseDown(button='left')
        sl(st)
        if RL == 'R':
            pyautogui.mouseUp(button='right')
        elif RL == 'L':
            pyautogui.mouseUp(button='left')
        for pll in range(1, TLP): movex(4)
    if DS == 9:
        for pll in range(1, TLP): movex(4)
        if RL == 'R':
            pyautogui.mouseDown(button='right')
        elif RL == 'L':
            pyautogui.mouseDown(button='left')
        for pll in range(1, TLP): movex(4)
        sl(st)
        if RL == 'R':
            pyautogui.mouseUp(button='right')
        elif RL == 'L':
            pyautogui.mouseUp(button='left')
    if DS == 10:
        for pll in range(1, TLP): movex(4)
        if RL == 'R':
            pyautogui.mouseDown(button='right')
        elif RL == 'L':
            pyautogui.mouseDown(button='left')
        for pll in range(1, TLP): movex(4)
        sl(st)
        for pll in range(1, TLP): movex(4)
        if RL == 'R':
            pyautogui.mouseUp(button='right')
        elif RL == 'L':
            pyautogui.mouseUp(button='left')
    if DS == 11:
        if RL == 'R':
            pyautogui.mouseDown(button='right')
        elif RL == 'L':
            pyautogui.mouseDown(button='left')
        for pll in range(1, TLP): movex(4)
        sl(st)
        for pll in range(1, TLP): movex(4)
        if RL == 'R':
            pyautogui.mouseUp(button='right')
        elif RL == 'L':
            pyautogui.mouseUp(button='left')
        movex(4)
    if DS == 12:
        for pll in range(1, TLP): movex(4)
        if RL == 'R':
            pyautogui.mouseDown(button='right')
        elif RL == 'L':
            pyautogui.mouseDown(button='left')
        for pll in range(1, TLP): movex(4)
        sl(st)
        for pll in range(1, TLP): movex(4)
        if RL == 'R':
            pyautogui.mouseUp(button='right')
        elif RL == 'L':
            pyautogui.mouseUp(button='left')
        movex(4)


def AutoCS():
    global LBM
    global h1
    global leftCL
    global rightCL
    global h2
    global fini
    sys('cls')
    try:
        if fini == 12: print('Ena:True')
    except:
        print('Ena:False')
        pass
    try:
        import keyboard
        from keyboard import is_pressed as ip
    except ModuleNotFoundError:
        print('pip install keyboard')
        exit()
    from time import sleep as sl
    from random import randint as ri
    pyautogui.PAUSE = 0
    #
    color('START', 3)
    color('R.I.P Technoblade', 2)
    LBM = input('Jitter D:Y (Y/N):')
    LBM = False if any(x.lower() in ['y', 'yes'] for x in LBM) else True
    if LBM == True:
        color('ON', 2)
    else:
        color('OFF', 1)
    sl(1)

    #
    def randx(x, y, z, ax, x0, y0, z0, a0, x1, y1, z1, a1, x2, y2, z2, a2, x3, y3, z3, a3, x4, y4, z4, a4, x5, y5, z5,
              a5, h2):
        global LBM, a, g
        if LBM == False:
            a = grandom(x2, y2, z2, a2)
            g = grandom(x3, y3, z3, a3)
        elif LBM == True:
            a = grandom(x4, y4, z4, a4)
            g = grandom(x5, y5, z5, a5)
        m = grandom(x, y, z, ax)
        m1 = grandom(x0, y0, z0, a0)
        m2 = grandom(x1, y1, z1, a1)
        if a > h2 and not a / m2 - g + m - m1 <= 0:
            a = a / m2 - g + m - m1
        elif a - g <= 0:
            a = (g - a + m) * (m1 / m2) + m2
        elif a < h2 and not a / m2 - g - m + (m1 / 2) <= 0:
            a = a / m2 - g - m + (m1 / 2)
        else:
            a = (a + g - m) * (m1 / m2) + m2
        return a

    #
    def std(x, y, z):
        std = ri(0, z)
        x1 = ri(x, y)
        x2 = ri(0, 9)
        x3 = ri(0, 9)
        if std == 1:
            x1 = x1 * 10 ** -1
            x1 = x1 + (x2 * 10 ** -2) + (x3 * 10 ** -3)
        elif std == 0:
            x1 = x1 * 10 ** -2
            x1 = x1 + (x3 * 10 ** -3)
        else:
            x1 = x1 * 10 ** -3
        x = x1
        color('STD:' + str(std), 1)
        return x

    #
    def cooldown(b, d):
        global LBM, p
        pt1 = False
        pt2 = False
        pt3 = False
        pt4 = False
        coold = 0
        if LBM == True:
            p = ri(1, b)
        elif LBM == False:
            p = ri(1, d)
        if p == 1:
            coold = grandom(1, 2, 3, 4)
            coold = coold * 10 ** -1
            pt1 = True
        elif p == 20:
            coold = grandom(1, 3, 4, 5)
            coold = coold * 10 ** -2
            pt2 = True
        elif p == 25:
            coold = grandom(1, 3, 4, 5)
            coold = coold * 10 ** -3
        elif p == 30:
            coold = grandom(1, 2, 3, 4)
            coold = coold * 10 ** -2
            pt3 = True
        elif p == 35:
            coold = grandom(1, 2, 3, 4)
            coold = coold * 10 ** -3
        elif p == 40:
            coold = grandom(1, 3, 4, 5)
            coold = coold * 10 ** -1
            pt4 = True
        if pt1 or pt2 or pt3 or pt4 == True:
            if pt1 == True: sp1 = ri(1, 9);sp1 = sp1 * (10 ** -2);sp2 = ri(1, 9);sp2 = sp2 * (
                    10 ** -3);coold = coold + sp1 + sp2
            if pt2 == True: sp2 = ri(1, 9);sp2 = sp2 * (10 ** -3);coold = coold + sp2
            if pt3 == True: sp2 = ri(1, 9);sp2 = sp2 * (10 ** -3);coold = coold + sp2
            if pt4 == True: sp1 = ri(1, 9);sp1 = sp1 * (10 ** -2);sp2 = ri(1, 9);sp2 = sp2 * (
                    10 ** -3);coold = coold + sp1 + sp2
        color('CoolDown:' + str(coold), 2)
        sl(coold)

    #
    def grandom(x, y, z, a):
        d = ri(1, 2)
        if d == 1:
            r1 = ri(x, y)
            ri2 = ri(z, a)
            r = ri(r1, ri2)
        else:
            r1 = ri(z, a)
            ri2 = ri(x, y)
            r = ri(ri2, r1)
        return r

    try:
        h1 = 0
        h2 = 0

        def start():
            global leftCL
            global h1
            global LBM
            global st
            cooldown(40, 50)
            p = randx(2, 5, 6, 8, 1, 2, 3, 4, 2, 3, 4, 5, 12, 31, 32, 191, 3, 10, 22, 23, 6, 16, 19, 20, 10, 11, 24, 25,
                      h2)
                                                                                                                                       #                                                                     #
            h1 = p
            p = p * 10 ** -3
            if LBM == True:
                st1 = std(0, 1, 70)
            else:
                st1 = std(0, 1, 60)
            # color('STD:'+str(st1),2)
            sl(p)
            try:
                if leftCL != None:
                    pass
            except:
                leftCL = None
            if leftCL != None:
                if keyboard.is_pressed(leftCL):
                    ACC('L')
            else:
                ACC('L')

        #
        def start2():
            global rightCL
            global h2
            global LBM
            global st
            cooldown(40, 50)
            p = randx(2, 5, 6, 8, 1, 2, 3, 4, 2, 3, 4, 5, 12, 31, 32, 191, 3, 12, 25, 26, 7, 21, 22, 24, 12, 24, 25, 26,
                      h2)
            #                    #
            h2 = p
            p = p * 10 ** -3
            if LBM == True:
                st = std(0, 1, 50)
            else:
                st = std(0, 1, 40)
            sl(p)
            try:
                if rightCL != None:
                    pass
            except:
                rightCL = None
            if rightCL != None:
                if keyboard.is_pressed(rightCL):
                    ACC('R')
            else:
                ACC('R')


        def on_start_pressed():
            start()

        def on_start2_pressed():
            start2()

        def on_stop_pressed():
            print('Stop')
            sl(1)
            while True:
                if keyboard.is_pressed(skey):
                    print('Restart')
                    sl(1)
                    break

        def fixkey(x, y, rt):
            keyboard.add_hotkey(x + '+' + y, rt)
            keyboard.add_hotkey(y + '+' + x, rt)

        #
        def fixkey3(x, y, z, rt):
            keyboard.add_hotkey(x + '+' + y + '+' + z, rt)
            keyboard.add_hotkey(z + '+' + x + '+' + y, rt)
            keyboard.add_hotkey(x + '+' + z + '+' + y, rt)
            keyboard.add_hotkey(y + '+' + x + '+' + z, rt)
            keyboard.add_hotkey(z + '+' + y + '+' + x, rt)
            keyboard.add_hotkey(y + '+' + z + '+' + x, rt)

        #
        def fixkey4(x, y, z, s, rt):
            keyboard.add_hotkey(x + '+' + y + '+' + z + '+' + s, rt)
            keyboard.add_hotkey(x + '+' + y + '+' + s + '+' + z, rt)
            keyboard.add_hotkey(x + '+' + s + '+' + y + '+' + z, rt)
            keyboard.add_hotkey(s + '+' + x + '+' + y + '+' + z, rt)
            keyboard.add_hotkey(z + '+' + x + '+' + y + '+' + s, rt)
            keyboard.add_hotkey(z + '+' + x + '+' + s + '+' + y, rt)
            keyboard.add_hotkey(z + '+' + s + '+' + x + '+' + y, rt)
            keyboard.add_hotkey(s + '+' + z + '+' + x + '+' + y, rt)
            keyboard.add_hotkey(x + '+' + z + '+' + y + '+' + s, rt)
            keyboard.add_hotkey(x + '+' + z + '+' + s + '+' + y, rt)
            keyboard.add_hotkey(x + '+' + s + '+' + z + '+' + y, rt)
            keyboard.add_hotkey(s + '+' + x + '+' + z + '+' + y, rt)
            keyboard.add_hotkey(y + '+' + x + '+' + z + '+' + s, rt)
            keyboard.add_hotkey(y + '+' + x + '+' + s + '+' + z, rt)
            keyboard.add_hotkey(y + '+' + s + '+' + x + '+' + z, rt)
            keyboard.add_hotkey(s + '+' + y + '+' + x + '+' + z, rt)
            keyboard.add_hotkey(z + '+' + y + '+' + x + '+' + s, rt)
            keyboard.add_hotkey(z + '+' + y + '+' + s + '+' + x, rt)
            keyboard.add_hotkey(z + '+' + s + '+' + y + '+' + x, rt)
            keyboard.add_hotkey(s + '+' + z + '+' + y + '+' + x, rt)
            keyboard.add_hotkey(y + '+' + z + '+' + x + '+' + s, rt)
            keyboard.add_hotkey(y + '+' + z + '+' + s + '+' + x, rt)
            keyboard.add_hotkey(y + '+' + s + '+' + z + '+' + x, rt)
            keyboard.add_hotkey(s + '+' + y + '+' + z + '+' + x, rt)

        #
        def fixkey5(x, r, s, rt):
            keyboard.add_hotkey(x + '+' + r + '+' + s, rt)
            keyboard.add_hotkey(s + '+' + x + '+' + r, rt)
            keyboard.add_hotkey(x + '+' + s + '+' + r, rt)
            keyboard.add_hotkey(r + '+' + x + '+' + s, rt)
            keyboard.add_hotkey(s + '+' + r + '+' + x, rt)
            keyboard.add_hotkey(r + '+' + s + '+' + x, rt)

        #
        def mkey(x, y, z, a, r, s, rt):
            fixkey(x, r, rt)
            fixkey(y, r, rt)
            fixkey(a, r, rt)
            fixkey(z, r, rt)
            fixkey(s, r, rt)
            fixkey3(x, y, r, rt)
            fixkey3(x, a, r, rt)
            fixkey3(x, z, r, rt)
            fixkey3(y, z, r, rt)
            fixkey3(y, a, r, rt)
            fixkey3(a, z, r, rt)
            fixkey5(x, r, s, rt)
            fixkey5(y, r, s, rt)
            fixkey5(z, r, s, rt)
            fixkey5(a, r, s, rt)
            fixkey4(x, y, r, s, rt)
            fixkey4(x, a, r, s, rt)
            fixkey4(x, z, r, s, rt)
            fixkey4(y, z, r, s, rt)
            fixkey4(y, a, r, s, rt)
            fixkey4(a, z, r, s, rt)

        def tomkey(x, y, z, a, r, s, c, sh, rt):
            mkey(x, y, z, a, r, s, rt)
            mkey(x, y, z, c, r, s, rt)
            mkey(x, y, z, a, r, c, rt)
            mkey(x, y, z, sh, r, s, rt)
            mkey(x, y, z, a, r, sh, rt)

        sys('cls')

        def checkACP():
            global Chlps
            try:
                if fini == 12: AutoKB = AutoKeyB()
            except:
                pass

        while True:
            color('KeyMap editor', 2)
            try:
                keymap = int(input('1.Minecraft\n2.Custom\n3.Button[Beta]\n'))
            except:
                keymap = 0
            if keymap == 1:
                sys('cls')
                print('Minecraft')
                leftCL = 'r'
                rightCL = 'f'
                tomkey('w', 'a', 's', 'd', 'r', 'space', 'ctrl', 'shift', on_start_pressed)
                tomkey('w', 'a', 's', 'd', 'f', 'space', 'ctrl', 'shift', on_start2_pressed)
                keyboard.add_hotkey('r', on_start_pressed)
                keyboard.add_hotkey('f', on_start2_pressed)
                skey = 'ctrl+y'
                keyboard.add_hotkey('ctrl+y',
                                    on_stop_pressed)  # for stop - skey = 'x';keyboard.add_hotkey('x',on_stop_pressed)
                checkACP()
                break
            elif keymap == 2:
                sys('cls')
                # 0 and ckeymapR just for r and f key if 1 just 1 key = [0]
                def godkey(ckeymap,ons1=on_start_pressed,ons2=on_start2_pressed):
                    global leftCL
                    global rightCL
                    global skey
                    ERR = False
                    try:
                        while True: ckeymap.remove(',')
                    except:
                        pass
                    try:
                        ckeymapA = len(ckeymap)
                        if ckeymapA > 1: ckeymapS = ckeymap[-1];ckeymap.remove(ckeymap[-1]);print('stop key=',
                                                                                                  'Ctrl' + '+' + ckeymapS);skey = ckeymapS;keyboard.add_hotkey(
                            'ctrl' + '+' + ckeymapS, ons1)
                        print('Keys:', ckeymap)
                        ckeymapN = len(ckeymap)
                        if ckeymapN == 1:
                            keyboard.add_hotkey(ckeymap[0], ons1)
                        elif ckeymapN == 2:
                            leftCL = ckeymap[0]
                            rightCL = ckeymap[1]
                            tomkey(ckeymap[0], 'F6', 'F7', 'F8', 'F9', 'F10',
                                   'F11', 'F12', ons1)
                            tomkey(
                                ckeymap[1], 'F6', 'F7', 'F8', 'F9', 'F10', 'F12', 'F11',
                                on_start2_pressed)
                            keyboard.add_hotkey(ckeymap[0],
                                                ons1)
                            keyboard.add_hotkey(ckeymap[1],
                                                ons2)
                        elif ckeymapN == 3:
                            leftCL = ckeymap[0]
                            rightCL = ckeymap[1]
                            tomkey(ckeymap[0], ckeymap[2], 'F7', 'F8', 'F9',
                                   'F10', 'F11', 'F12',
                                   ons1)
                            tomkey(ckeymap[1],
                                   ckeymap[2], 'F7',
                                   'F8', 'F9', 'F10',
                                   'F12', 'F11',
                                   ons2)
                            keyboard.add_hotkey(
                                ckeymap[0], ons1)
                            keyboard.add_hotkey(ckeymap[1], ons2)
                        elif ckeymapN == 4:
                            leftCL = ckeymap[0]
                            rightCL = ckeymap[1]
                            tomkey(ckeymap[0], ckeymap[2], ckeymap[3], 'F8',
                                   'F9', 'F10', 'F11', 'F12',
                                   ons1)
                            tomkey(ckeymap[1],
                                   ckeymap[2],
                                   ckeymap[3], 'F8',
                                   'F9', 'F10', 'F12',
                                   'F11',
                                   ons2)
                            keyboard.add_hotkey(
                                ckeymap[0], ons1)
                            keyboard.add_hotkey(ckeymap[1], ons2)
                        elif ckeymapN == 5:
                            leftCL = ckeymap[0]
                            rightCL = ckeymap[1]
                            tomkey(ckeymap[0], ckeymap[2], ckeymap[3],
                                   ckeymap[4], 'F9', 'F10', 'F11', 'F12',
                                   ons1)
                            tomkey(ckeymap[1],
                                   ckeymap[2],
                                   ckeymap[3],
                                   ckeymap[4], 'F9',
                                   'F10', 'F12',
                                   'F11',
                                   ons2)
                            keyboard.add_hotkey(
                                ckeymap[0], ons1)
                            keyboard.add_hotkey(ckeymap[1], ons2)
                        elif ckeymapN == 6:
                            leftCL = ckeymap[0]
                            rightCL = ckeymap[1]
                            tomkey(ckeymap[0], ckeymap[2], ckeymap[3],
                                   ckeymap[4], ckeymap[5], 'F10', 'F11', 'F12',
                                   ons1)
                            tomkey(ckeymap[1],
                                   ckeymap[2],
                                   ckeymap[3],
                                   ckeymap[4],
                                   ckeymap[5], 'F10',
                                   'F12', 'F11',
                                   ons2)
                            keyboard.add_hotkey(
                                ckeymap[0], ons1)
                            keyboard.add_hotkey(ckeymap[1], ons2)
                        elif ckeymapN == 7:
                            leftCL = ckeymap[0]
                            rightCL = ckeymap[1]
                            tomkey(ckeymap[0], ckeymap[2], ckeymap[3],
                                   ckeymap[4], ckeymap[5], ckeymap[6], 'F11',
                                   'F12', ons1)
                            tomkey(ckeymap[1],
                                   ckeymap[2],
                                   ckeymap[3],
                                   ckeymap[4],
                                   ckeymap[5],
                                   ckeymap[6],
                                   'F12',
                                   'F11',
                                   ons2)
                            keyboard.add_hotkey(
                                ckeymap[0], ons1)
                            keyboard.add_hotkey(ckeymap[1], ons2)
                        elif ckeymapN == 8:
                            leftCL = ckeymap[0]
                            rightCL = ckeymap[1]
                            tomkey(ckeymap[0], ckeymap[2], ckeymap[3],
                                   ckeymap[4], ckeymap[5], ckeymap[6],
                                   ckeymap[7], 'F11', ons1)
                            tomkey(
                                ckeymap[1], ckeymap[2], ckeymap[3], ckeymap[4], ckeymap[5], ckeymap[6], ckeymap[7],
                                'F11', ons2)
                            keyboard.add_hotkey(ckeymap[0],
                                                ons1)
                            keyboard.add_hotkey(
                                ckeymap[1], ons2)
                        elif ckeymapN > 8:
                            color('Error/Above', 1)
                            ERR = True
                        elif ckeymapN < 1:
                            color('Error/Below', 1)
                            ERR = True
                        elif ckeymapN == 0:
                            color('Error/Zero', 1)
                            ERR = True
                    except:
                        print('E/KNF')
                    return ERR

                ckeymap = list(input(
                    'Give custom KeyMap {1,9} keys\nexample ~ r,f,a,w,d,end ~~ (r) = hotkey for r click and (f) for l\n0 = r and 1 = f and end = ctrl + (stop key)\n'))
                ERR = godkey(ckeymap)
                checkACP()
                if ERR == False:
                    break
                elif ERR == True:
                    pass
            if keymap == 3:
                def Dclick():
                    from threading import Thread
                    global leftCL
                    global rightCL
                    lr = input('L or R -> ')
                    if lr == 'L' or lr == 'l':
                        while True:
                            if ctypes.windll.user32.GetAsyncKeyState(0x1) > 1:
                                t = Thread(target=on_start_pressed)
                                t.start()
                                t.join()
                            elif ctypes.windll.user32.GetAsyncKeyState(0x2) > 1:
                                t = Thread(target=on_start_pressed)
                                t.start()
                                t.join()
                    if lr == 'R' or lr == 'r':
                        while True:
                            if ctypes.windll.user32.GetAsyncKeyState(0x1) > 1:
                                t = Thread(target=on_start2_pressed)
                                t.start()
                                t.join()
                            elif ctypes.windll.user32.GetAsyncKeyState(0x2) > 1:
                                t = Thread(target=on_start2_pressed)
                                t.start()
                                t.join()

                Dclick()
                #my bullshit method
            else:
                color('Bad input', 1)
        if fini == 12:
            print('AutoKey/')
            import keyboard
            def sls():
                global LBM
                if LBM == True:
                    stK = std(0, 1, 50)
                else:
                    stK = std(0, 1, 40)
                print(stK)
                sl(stK)

            def KeyRun(KeyB):
                global LBM
                if LBM == True:
                    stK = std(0, 1, 50)
                else:
                    stK = std(0, 1, 40)
                keyboard.press(KeyB)
                RPL = ri(2, 3)

            def rts():
                rf1 = ri(0, 1)
                rf2 = ri(1, 999)
                slt = rf1 + (rf2 * (10 ** -3))
                sl(slt)
                print(slt)

            def AutoKeyBS():
                global Chlps
                global ChlpsXC
                global ChlpsX
                global tryx
                if tryx == True:
                    try:
                        a = Chlps[0]
                        d = Chlps[1]
                        c = Chlps[2]
                        f = Chlps[3]
                        g = Chlps[4]
                        print(
                            'i/77')
                        tryx = False
                        ChlpsX = [a, d, c, f, g]
                    except:
                        pass
                print('Run:', ChlpsX)
                if ChlpsX[0] == '=': print('E/EmpA')
                KeyRun(ChlpsX[0])
                sls()
                aq = True
                # = empty
                if ChlpsX[1] != '=': 
                    KeyRun(ChlpsX[1]);sls()
                    try:sl(float(ChlpsXC[1]))
                    except:pass
                    dq = True
                if ChlpsX[2] != '=': 
                    KeyRun(ChlpsX[2]);sls()
                    try:sl(float(ChlpsXC[2]))
                    except:pass
                    cq = True
                if ChlpsX[3] != '=': 
                    KeyRun(ChlpsX[3]);sls()
                    try:sl(float(ChlpsXC[3]))
                    except:pass
                    fq = True
                if ChlpsX[4] != '=': 
                    KeyRun(ChlpsX[4]);sls()
                    try:sl(float(ChlpsXC[4]))
                    except:pass
                    gq = True
                try:
                    listZ = [1, 2, 3, 4, 5]
                    for x in listZ:
                        f = random.choice(listZ)
                        try:
                            def az():
                                if aq == True: keyboard.release(ChlpsX[0]);sls();var = aq == False

                            if f == 1: az()
                        except:
                            pass
                        try:
                            def dz():
                                if dq == True: keyboard.release(ChlpsX[1]);sls();var = dq == False

                            if f == 2: dz()
                        except:
                            pass
                        try:
                            def cz():
                                if cq == True: keyboard.release(ChlpsX[2]);sls();var = cq == False

                            if f == 3: cz()
                        except:
                            pass
                        try:
                            def fz():
                                if fq == True: keyboard.release(ChlpsX[3]);sls();var = fq == False

                            if f == 4: fz()
                        except:
                            pass
                        try:
                            def gz():
                                if gq == True: keyboard.release(ChlpsX[4]);sls();var = gq == False

                            if f == 5: gz()
                        except:
                            pass
                        listZ.remove(f)
                except:
                    pass
                cooldown(70, 40)

            global Chlps
            global ChlpsXC
            global tryx
            tryx = True
            Chlps = input('Give Keylist {1,5}/like a,d,f,h,b: ')
            ChlpsXCP = input('Give Time Sleep {1,5}/like 1,2,3,4,5: ')
            ChlpsXC = ChlpsXCP.split(',')
            ChlpsXC = cleanC(ChlpsXC)
            Chlps = Chlps.split(',')
            Chlps = cleanC(Chlps)
            Chl = input('Give {1,2} hotkey for this macro: ')
            Chl = Chl.split(',')
            Chl = cleanC(Chl)
            ChlpsN = len(Chlps)
            ChlN = len(Chl)
            if ChlN == 1:
                keyboard.add_hotkey(Chl[0], AutoKeyBS)
            elif ChlN == 2:
                keyboard.add_hotkey(Chl[0] + '+' + Chl[1], AutoKeyBS)
                keyboard.add_hotkey(Chl[1] + '+' + Chl[0],
                                    AutoKeyBS)
            else:
                print('Bad input Key')
                exit()
            if ChlpsN == 1:
                Chlps = [Chlps[0], '=', '=', '=', '=']
            elif ChlpsN == 2:
                Chlps = [Chlps[0], Chlps[1], '=', '=', '=']
            elif ChlpsN == 3:
                Chlps = [Chlps[0], Chlps[1], Chlps[2], '=', '=']
            elif ChlpsN == 4:
                Chlps = [Chlps[0], Chlps[1], Chlps[2], Chlps[3], '=']
            elif ChlpsN == 5:
                Chlps = [Chlps[0], Chlps[1], Chlps[2], Chlps[3], Chlps[4]]
            print(Chl)
        keyboard.wait()
    except KeyboardInterrupt:
        print('ForceStop')
#################TermPy_conf#################
## memory editor 1.3
import pymem
def wr1(proc,addre,val,type,l=4):
    import pymem
    mem = pymem.memory
    mex = pymem.Pymem(proc)
    mexd = mex.process_handle
    type = str(type);mexd = str(mexd);addre = str(addre);val = str(val);l = str(l)
    if type == 'bytes':r='mem.write_'+type+'('+mexd+', '+addre+', '+val+', '+l+')';eval(r)
    else:r = 'mem.write_'+type+'('+mexd+','+addre+','+val+')';eval(r)
def re1(proc,addre,val,type,l=4):
    import pymem
    mem = pymem.memory
    mex = pymem.Pymem(proc)
    mexd = mex.process_handle
    type=str(type);mexd=str(mexd);addre=str(addre);val=str(val);l=str(l)
    if type == 'bytes':r='mem.read_'+type+'('+mexd+', '+addre+', '+val+', '+l+')';eval(r)
    else:r='mem.read_'+type+'('+mexd+', '+addre+', '+val+')';eval(r)
    return s
# ex -> wr1('Tutorial-x86_64.exe',0x01571478,100,'int')
## hotkey
import keyboard
import threading
def fixkey(x, y, rt):
    keyboard.add_hotkey(x + '+' + y, rt)
    keyboard.add_hotkey(y + '+' + x, rt)

#
def fixkey3(x, y, z, rt):
    keyboard.add_hotkey(x + '+' + y + '+' + z, rt)
    keyboard.add_hotkey(z + '+' + x + '+' + y, rt)
    keyboard.add_hotkey(x + '+' + z + '+' + y, rt)
    keyboard.add_hotkey(y + '+' + x + '+' + z, rt)
    keyboard.add_hotkey(z + '+' + y + '+' + x, rt)
    keyboard.add_hotkey(y + '+' + z + '+' + x, rt)

#
def fixkey4(x, y, z, s, rt):
    keyboard.add_hotkey(x + '+' + y + '+' + z + '+' + s, rt)
    keyboard.add_hotkey(x + '+' + y + '+' + s + '+' + z, rt)
    keyboard.add_hotkey(x + '+' + s + '+' + y + '+' + z, rt)
    keyboard.add_hotkey(s + '+' + x + '+' + y + '+' + z, rt)
    keyboard.add_hotkey(z + '+' + x + '+' + y + '+' + s, rt)
    keyboard.add_hotkey(z + '+' + x + '+' + s + '+' + y, rt)
    keyboard.add_hotkey(z + '+' + s + '+' + x + '+' + y, rt)
    keyboard.add_hotkey(s + '+' + z + '+' + x + '+' + y, rt)
    keyboard.add_hotkey(x + '+' + z + '+' + y + '+' + s, rt)
    keyboard.add_hotkey(x + '+' + z + '+' + s + '+' + y, rt)
    keyboard.add_hotkey(x + '+' + s + '+' + z + '+' + y, rt)
    keyboard.add_hotkey(s + '+' + x + '+' + z + '+' + y, rt)
    keyboard.add_hotkey(y + '+' + x + '+' + z + '+' + s, rt)
    keyboard.add_hotkey(y + '+' + x + '+' + s + '+' + z, rt)
    keyboard.add_hotkey(y + '+' + s + '+' + x + '+' + z, rt)
    keyboard.add_hotkey(s + '+' + y + '+' + x + '+' + z, rt)
    keyboard.add_hotkey(z + '+' + y + '+' + x + '+' + s, rt)
    keyboard.add_hotkey(z + '+' + y + '+' + s + '+' + x, rt)
    keyboard.add_hotkey(z + '+' + s + '+' + y + '+' + x, rt)
    keyboard.add_hotkey(s + '+' + z + '+' + y + '+' + x, rt)
    keyboard.add_hotkey(y + '+' + z + '+' + x + '+' + s, rt)
    keyboard.add_hotkey(y + '+' + z + '+' + s + '+' + x, rt)
    keyboard.add_hotkey(y + '+' + s + '+' + z + '+' + x, rt)
    keyboard.add_hotkey(s + '+' + y + '+' + z + '+' + x, rt)

#
def fixkey5(x, r, s, rt):
    keyboard.add_hotkey(x + '+' + r + '+' + s, rt)
    keyboard.add_hotkey(s + '+' + x + '+' + r, rt)
    keyboard.add_hotkey(x + '+' + s + '+' + r, rt)
    keyboard.add_hotkey(r + '+' + x + '+' + s, rt)
    keyboard.add_hotkey(s + '+' + r + '+' + x, rt)
    keyboard.add_hotkey(r + '+' + s + '+' + x, rt)

#
def mkey(x, y, z, a, r, s, rt):
    fixkey(x, r, rt)
    fixkey(y, r, rt)
    fixkey(a, r, rt)
    fixkey(z, r, rt)
    fixkey(s, r, rt)
    fixkey3(x, y, r, rt)
    fixkey3(x, a, r, rt)
    fixkey3(x, z, r, rt)
    fixkey3(y, z, r, rt)
    fixkey3(y, a, r, rt)
    fixkey3(a, z, r, rt)
    fixkey5(x, r, s, rt)
    fixkey5(y, r, s, rt)
    fixkey5(z, r, s, rt)
    fixkey5(a, r, s, rt)
    fixkey4(x, y, r, s, rt)
    fixkey4(x, a, r, s, rt)
    fixkey4(x, z, r, s, rt)
    fixkey4(y, z, r, s, rt)
    fixkey4(y, a, r, s, rt)
    fixkey4(a, z, r, s, rt)

def tomkey(x, y, z, a, r, s, c, sh, rt):
    mkey(x, y, z, a, r, s, rt)
    mkey(x, y, z, c, r, s, rt)
    mkey(x, y, z, a, r, c, rt)
    mkey(x, y, z, sh, r, s, rt)
    mkey(x, y, z, a, r, sh, rt)
def TermPyS():
    from os import system as sis
    sis('cls')
    color('CCETermPy 1.2', 2)
    script = input('Script file address (use /) (Give admin access to run memory editor correctly) -> ')
    try:
        with open(script) as f:
            scrx = f.read()
    except:
        print('ECode/1')
    exec(scrx)
#################inp.Mcq_conf#################
##############################################
# GUI
fini = 0
import tkinter as tk
import random

root = tk.Tk()
root.wm_attributes("-topmost",True)
root.wm_attributes("-transparentcolor","white")
root.overrideredirect(1)
root.geometry("+0+0")


def rword():
    return ''.join(random.choice(string.ascii_letters) for i in range(7))


root.title(rword())


#
def AutoC():
    root.destroy()
    AutoCS()


def AutoCPlus():
    root.destroy()
    global fini
    fini = 12
    AutoCS()


def TermPy():
    root.destroy()
    TermPyS()


def Exit():
    root.destroy()
    exit()

#
AutoC = tk.Button(root, text="AutoC", command=AutoC)
AutoC.pack()
AutoCPlus = tk.Button(root, text="AutoCPlus", command=AutoCPlus)
AutoCPlus.pack()
TermPy = tk.Button(root, text="TermPy", command=TermPy)
TermPy.pack()
Exit = tk.Button(root, text="Exit", command=Exit)
Exit.pack()
root.mainloop()