# '''
# Python Code to implement a heap with general comparison function
# '''

# class Heap:
#     '''
#     Class to implement a heap with general comparison function
#     '''
    
#     def __init__(self, comparison_function, init_array):
#         '''
#         Arguments:
#             comparison_function : function : A function that takes in two arguments and returns a boolean value
#             init_array : List[Any] : The initial array to be inserted into the heap
#         Returns:
#             None
#         Description:
#             Initializes a heap with a comparison function
#             Details of Comparison Function:
#                 The comparison function should take in two arguments and return a boolean value
#                 If the comparison function returns True, it means that the first argument is to be considered smaller than the second argument
#                 If the comparison function returns False, it means that the first argument is to be considered greater than or equal to the second argument
#         Time Complexity:
#             O(n) where n is the number of elements in init_array
#         '''
        
#         # Write your code here
#         pass
        
#     def insert(self, value):
#         '''
#         Arguments:
#             value : Any : The value to be inserted into the heap
#         Returns:
#             None
#         Description:
#             Inserts a value into the heap
#         Time Complexity:
#             O(log(n)) where n is the number of elements currently in the heap
#         '''
        
#         # Write your code here
#         pass
    
#     def extract(self):
#         '''
#         Arguments:
#             None
#         Returns:
#             Any : The value extracted from the top of heap
#         Description:
#             Extracts the value from the top of heap, i.e. removes it from heap
#         Time Complexity:
#             O(log(n)) where n is the number of elements currently in the heap
#         '''
        
#         # Write your code here
#         pass
    
#     def top(self):
#         '''
#         Arguments:
#             None
#         Returns:
#             Any : The value at the top of heap
#         Description:
#             Returns the value at the top of heap
#         Time Complexity:
#             O(1)
#         '''
        
#         # Write your code here
#         pass
    
#     # You can add more functions if you want to



'''
Python Code to implement a heap with general comparison function
'''

def min_comparison(a, b):
    return a < b

def min_comparision_crewmate(a,b):
    return  a.load<b.load

def id_comparator(a,b):
    return a.id<b.id
    
class Heap:
    '''
    Class to implement a heap with general comparison function
    '''
    
    def __init__(self, comparison_function,init_array):
        '''
        Arguments:
            comparison_function : function : A function that takes in two arguments and returns a boolean value
            init_array : List[Any] : The initial array to be inserted into the heap
        Returns:
            None
        Description:
            Initializes a heap with a comparison function
            Details of Comparison Function:
                The comparison function should take in two arguments and return a boolean value
                If the comparison function returns True, it means that the first argument is to be considered smaller than the second argument
                If the comparison function returns False, it means that the first argument is to be considered greater than or equal to the second argument
        Time Complexity:
            O(n) where n is the number of elements in init_array
        '''
        
        # Write your code here
        
        self.comparison_function = comparison_function
        self.heap = init_array[:]
        self.build_heap()
        pass
    
    def build_heap(self):
        '''
        Converts an unordered array into a heap. 
        Time Complexity: O(n), where n is the number of elements in the heap.
        '''
        n = len(self.heap)
        for i in range((n - 2) // 2, -1, -1):
            self.heapify_down(i)
        
    def insert(self, value):
        '''
        Arguments:
            value : Any : The value to be inserted into the heap
        Returns:
            None
        Description:
            Inserts a value into the heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        
        # Write your code here
        
        self.heap.append(value)  # Insert value at the end
        self.heapify_up(len(self.heap) - 1)
        pass
    
    def extract(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value extracted from the top of heap
        Description:
            Extracts the value from the top of heap, i.e. removes it from heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        
        # Write your code here
        
        if not self.heap:
            raise IndexError("Heap is empty")
        
        self.swap(0, len(self.heap) - 1)  # Swap the top and last element
        min_value = self.heap.pop()  # Remove the last element (previous root)
        self.heapify_down(0)
        
        return min_value

        pass
    
    def top(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value at the top of heap
        Description:
            Returns the value at the top of heap
        Time Complexity:
            O(1)
        '''
        
        # Write your code here
        
        if not self.heap:
            raise IndexError("Heap is empty")
        return self.heap[0]
        pass
    
    # You can add more functions if you want to
    
    def heapify_up(self, index):
        '''
        Moves the element at index up to restore the heap property.
        Time Complexity: O(log n)
        '''
        parent = (index - 1) // 2
        while index > 0 and (self.heap[index] == self.heap[parent] or self.comparison_function(self.heap[index], self.heap[parent])):
            self.swap(index, parent)
            index = parent
            parent = (index - 1) // 2

    def heapify_down(self, index):
        '''
        Moves the element at index down to restore the heap property.
        Time Complexity: O(log n)
        '''
        n = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < n and self.comparison_function(self.heap[left], self.heap[smallest]):
                smallest = left
            if right < n and self.comparison_function(self.heap[right], self.heap[smallest]):
                smallest = right

            if smallest != index:
                self.swap(index, smallest)
                index = smallest
            else:
                break

    def swap(self, i, j):
        '''
        Swaps two elements in the heap.
        '''
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def isempty(self):
        return len(self.heap)==0
    def heap_sort(self):
        '''Sort the heap using heap sort (in-place sorting).'''
        sorted_array = []
        original_size = len(self.heap)
        # Repeatedly extract the top element (min/max based on heap type) to sort
        for _ in range(original_size):
            sorted_array.append(self.extract())
        return sorted_array
    


