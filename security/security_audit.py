import os

def run_security_audit():
    os.system('safety check')

if __name__ == "__main__":
    run_security_audit()
