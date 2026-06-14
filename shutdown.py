def shutdown(asker):
    return asker(print(asker))
asker=input("Shutdown the system?: ").upper()
if asker=='YES':
    print("Shutting down")
else:
    print("Sorry")

