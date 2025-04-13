# doubly-linked list to suppot fast insertion/deletion at ends. maintain size in the LL object (router)
class ll_node(object):
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class Router(object):

    def __init__(self, memoryLimit):
        """
        :type memoryLimit: int
        """
        self.memoryLimit = memoryLimit
        self.firstpack = None
        self.lastpack = None
        self.size = 0
        self.unique = set()
        self.library = {}

    def addPacket(self, source, destination, timestamp):
        """
        :type source: int
        :type destination: int
        :type timestamp: int
        :rtype: bool
        """
        new_node = ll_node((source,destination,timestamp))
        # empty list
        if self.size == 0:
            # assign head and tail to new node, update size
            self.firstpack = new_node
            self.lastpack = new_node
            self.size += 1
            self.add_library((source,destination,timestamp))
            return True
        # check if there's a duplicate, return False if so
        if self.add_library((source, destination, timestamp)):
            new_node.next = self.firstpack
            self.firstpack.prev = new_node
            self.firstpack = new_node
            self.size += 1
            self.resize()
            return True
        else:
            return False

    def forwardPacket(self):
        """
        :rtype: List[int]
        """
        if self.size == 0:
            return []
        # get first packet, remove it from ll and library
        last = self.lastpack
        # update first and last
        if self.size == 1:
            self.firstpack = None
            self.lastpack =  None
        else:
            self.lastpack = self.lastpack.prev
            self.lastpack.next = None
        self.size -= 1        
        return self.rm_library(last.item)
        

    def getCount(self, destination, startTime, endTime):
        """
        :type destination: int
        :type startTime: int
        :type endTime: int
        :rtype: int
        """
        if destination in self.library:
            A = self.library[destination]
            # find insertion point of startTime
            start = bisect_left(A, startTime)
            # find insertion point of endTime
            end = bisect_right(A, endTime)
            if start <= end:
                return end-start
        return 0

    def resize(self):
        if self.size > self.memoryLimit:
            last = self.lastpack
            # access library with destination as key, pop timestamp
            self.rm_library(last.item)
            # remove last packet from ll
            self.lastpack = self.lastpack.prev
            self.lastpack.next = None
            # update size
            self.size -= 1
    
    def rm_library(self, packet):
        source, destination, timestamp = packet[0], packet[1], packet[2]
        self.unique.remove(packet)

        A = self.library[destination]
        index = bisect_left(A, timestamp)
        A.pop(index)
        if len(A) == 0:
            self.library.pop(destination)
        return [source, destination, timestamp]
    
    def add_library(self, packet):
        source, destination, timestamp = packet[0], packet[1], packet[2]
        if packet in self.unique:
            return False
         # add new packet to packet library, with destination as key and timestamps in an array
        else:
            if destination not in self.library:
                self.library[destination] = []
            self.library[destination].append(timestamp)
        # add to list of unique packets
        self.unique.add(packet)
        return True


## bisection functions
def bisect_left(array, target):
    start, end = 0, len(array)
    while start < end:
        mid = (start + end)//2
        if array[mid] < target:
            start = mid+1
        else:
            end = mid
    return end

def bisect_right(array, target):
    start, end = 0, len(array)
    while start < end:
        mid = (start + end)//2
        if array[mid] <= target:
            start = mid+1
        else:
            end = mid
    return end


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)


A_rray = [2,2,3,4]
print(bisect_left(A_rray, 4))
print(bisect_right(A_rray, 1))