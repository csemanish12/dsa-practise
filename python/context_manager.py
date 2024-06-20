class HelloContextManager:
    def __enter__(self):
        print("doing random setup")
        return "setup output"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exiting custom context")


with HelloContextManager() as h:
    print(h)