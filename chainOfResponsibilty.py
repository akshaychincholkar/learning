# Handler interface
class Handler:
    def set_successor(self, successor):
        pass

    def handle_request(self, request):
        pass

# Concrete handler 1
class ConcreteHandler1(Handler):
    successor = None
    def set_successor(self, successor):
        self.successor = successor

    def handle_request(self, request):
        if request == 'Handler1':
            print('ConcreteHandler1 handling the request')
        elif self.successor is not None:
            self.successor.handle_request(request)

# Concrete handler 2
class ConcreteHandler2(Handler):
    successor = None
    def set_successor(self, successor):
        self.successor = successor

    def handle_request(self, request):
        if request == 'Handler2':
            print('ConcreteHandler2 handling the request')
        elif self.successor is not None:
            self.successor.handle_request(request)

# Client code
if __name__ == "__main__":
    # Creating instances of handlers
    handler1 = ConcreteHandler1()
    handler2 = ConcreteHandler2()

    # Setting up the chain of responsibility
    handler1.set_successor(handler2)

    # Making requests
    handler1.handle_request('Handler1')
    handler1.handle_request('Handler2')
    handler1.handle_request('Handler3')
