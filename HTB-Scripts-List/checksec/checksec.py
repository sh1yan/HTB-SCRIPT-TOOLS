#!/usr/bin/python3
import lief, colorama, sys

def print_color(name, result):
    colorama.init(autoreset=True)
    if result is True:
        color = colorama.Fore.GREEN
        result = "True"
    elif result is False:
        color = colorama.Fore.RED
        result = "False"
    else:
        color = ""
    padding = " " * (18 - len(name))
    print("    " + name + ":" + padding + color + result)

def aslr(characteristics):
    return lief.PE.DLL_CHARACTERISTICS.DYNAMIC_BASE in characteristics

def seh(characteristics):
    return lief.PE.DLL_CHARACTERISTICS.NO_SEH in characteristics

def dep(characteristics):
    return lief.PE.DLL_CHARACTERISTICS.NX_COMPAT in characteristics

def cfg(characteristics):
    return lief.PE.DLL_CHARACTERISTICS.GUARD_CF in characteristics

def hev(characteristics):
    return lief.PE.DLL_CHARACTERISTICS.HIGH_ENTROPY_VA in characteristics

def results(characteristics):
    print_color("ASLR", aslr(characteristics))
    print_color("SafeSEH", seh(characteristics))
    print_color("DEP", dep(characteristics))
    print_color("ControlFlowGuard", cfg(characteristics))
    print_color("HighEntropyVA", hev(characteristics))

def checksec(filename):
    print("[" + colorama.Fore.BLUE + "*" + colorama.Style.RESET_ALL + "] '" + filename + "'")
    binary = lief.parse(filename)
    if lief.is_pe(filename):
        results(binary.optional_header.dll_characteristics_lists)

if len(sys.argv) < 2:
    print("[" + colorama.Fore.RED + "-" + colorama.Style.RESET_ALL + f"] Usage: python3 {sys.argv[0]} <file>")
    sys.exit(1)
else:
    checksec(sys.argv[1])
