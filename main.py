from utils import mkdir

def main():
    mkdir()

    from fileHandler import lteBilling
    
    lteBilling()

if __name__ == "__main__":
    main()