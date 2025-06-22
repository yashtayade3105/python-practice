try:
    import colorama
    from colorama import Fore
except ImportError:
    print("❌ Module not installed. Run: pip install colorama")
    exit()

print(Fore.GREEN + "Module imported successfully! 🎉")
