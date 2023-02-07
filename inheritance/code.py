class Device:
    def __init__(self, name, connected_by):
        self.name=name
        self.connected_by=connected_by
        self.connected=True
    
    def __str__(self):
        return f"Device {self.name} connected ({self.connected_by})" 
    
    def disconnect(self):
        self.connected=False
        print("Disconnected")   
        
        
printer = Device("Printer", "USB")
print(printer)
printer.disconnect()


class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
    def __str__(self):
        return f"{super().__str__()} have capacity {self.capacity}"
    
    def print(self, pages):
        if not self.connected:
            print("Your printer is not connected")
            return
        print("Printing {pages} pages")

printer = Printer("Printer", "USB", 500)
printer.print(20)
print(printer)