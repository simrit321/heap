# helper functions

def left(index):
    '''Return index's left child index.
    '''
    return index * 2 + 1


def right(index):
    '''Return index's left child index.
    '''
    return index * 2 + 2
    
    
def parent(index):
    '''Return index's parent index.'''
    
    return (index - 1) // 2


class MinHeap:
    
    def __init__(self, L=None):
        '''Create a new MinHeap.
        This method is complete.'''
        
        if not L:        
            self._data = []
        else:
            self._data = L
            self._min_heapify()

        
    def __len__(self):
        '''Return the length of the MinHeap.
        This method is complete.'''
        
        return len(self._data)
    

    def __str__(self):
        '''Return a string representation of the heap.
        This method is complete.'''
        
        return str(self._data)
    
    
    def insert(self, v):
        '''Insert v in self. Maintain heap property.'''
        self._data.append(v)
        self._percolate_up()
        
        
        return self
 
    
    def extract_min(self):
        '''Remove minimal value in self. Restore heap property.
        Raise EmptyHeapException if heap is empty.'''
        
        if len(self._data) == 0:
            raise EmptyHeapException()
        elif len(self._data) == 1:
            return self._data[0]  
        else:
            ind = len(self._data) - 1
            a, b = 0, ind
            self._data[b], self._data[a] = self._data[a], self._data[b]
            m=self._data.pop(len(self._data)-1)
            self._percolate_down(i=0)
        self._percolate_up()
        return m
            
 
    
    def _percolate_up(self):
        '''Restore heap property of self after 
        adding new item'''
        index = len(self._data)
        v = self._data[index-1]
        i = parent(index)
        p = self._data[i]
        while v < p:
            a,b = self._data.index(v), self._data.index(p)
            self._data[b], self._data[a] = self._data[a], self._data[b]
            index = self._data.index(v)
            i = parent(index)
            p = self._data[i]
            if index == 0:
                break
        return self
        
        
    def _percolate_down(self, i):
        ''' Restore heap property of subtree 
        rooted at index i.
        '''

        index = i 
        index_left = left(index)
        index_right = right(index)
        node_val = self._data[i]
        
        
        
        if len(self._data) >= 4:
            x=0
            if index_left < len(self._data)-1:
                x += 0.5
                # if x == 0.5, then only a left child exists
            if index_right < len(self._data)-1:
                x += 1
                #if x == 1, then only a right child exists
            #if x>0 then some child exists    
            if x == 1.5:
                left_val = self._data[index_left]
                right_val = self._data[index_right]
                
                q = 0
                if left_val < node_val:
                    q += 0.5
                if right_val < node_val:
                    q += 1
                #if q > 0:
                    #big = True
                 
                    #while big:
                if q > 0:
                        
                    if left_val > right_val:
                        smaller = right_val
                    elif left_val < right_val:
                        smaller = left_val
                    elif left_val == right_val:
                        smaller = left_val
                      
                    x,y = self._data.index(node_val), self._data.index(smaller)
                    self._data[y], self._data[x] = self._data[x], self._data[y]
                    index = self._data.index(node_val)
                    self._percolate_down(i=index)
                    #index_left = left(index)
                    #index_right = right(index)
                    
                    #if index_left < len(self._data)-1:
                        #left_val = self._data[index_left]
                        
                    #if index_right < len(self._data)-1:
                        #right_val = self._data[index_right]
               
                    #else:
                        #break
            elif x == 0.5:
                left_val = self._data[index_left]
                if left_val < node_val:
                    smaller = left_val
                    x,y = self._data.index(node_val), self._data.index(smaller)
                    self._data[y], self._data[x] = self._data[x], self._data[y]
                    index = self._data.index(node_val)
                    self._percolate_down(i=index)
            elif x == 1.0:
                right_val = self._data[index_right]
                if right_val < node_val:
                    smaller = right_val
                    x,y = self._data.index(node_val), self._data.index(smaller)
                    self._data[y], self._data[x] = self._data[x], self._data[y]
                    index = self._data.index(node_val)
                    self._percolate_down(i=index)
                    
        elif len(self._data) == 3 and i==0:
            index_left = 1
            index_right = 2
            left_val = self._data[index_left]
            right_val = self._data[index_right]
            
            x = 0
            if node_val > left_val:
                x += 0.5
            if node_val > right_val:
                x += 1
            if x == 1.5:
                if left_val < right_val:
                    smaller = left_val
                    x,y = self._data.index(node_val), self._data.index(smaller)
                    self._data[y], self._data[x] = self._data[x], self._data[y]
                elif left_val > right_val:
                    smaller = right_val
                    x,y = self._data.index(node_val), self._data.index(smaller)
                    self._data[y], self._data[x] = self._data[x], self._data[y]
                    
                elif left_val == right_val:
                    smaller = left_val
                    x,y = self._data.index(node_val), self._data.index(smaller)
                    self._data[y], self._data[x] = self._data[x], self._data[y]
        elif len(self._data) == 2 and i==0:
            if self._data[0] > self._data[1]:
                smaller = self._data[1]
                x,y = self._data.index(node_val), self._data.index(smaller)
                self._data[y], self._data[x] = self._data[x], self._data[y]
        if len(self._data)-1 == i:
            self._percolate_up()
            
                
            
                
    

            
        # while larger than at least one child
        # swap with smaller child and repeat    
        
    
    
    def _min_heapify(self):
        '''Turn unordered list into min-heap.'''
        length = len(self._data)
        mid = length//2
        first_half = self._data[:mid]

        for item in range(len(first_half[::-1])):
            self._percolate_down(item)
        return self._data
    
                   
        # for each node in the first half of the list
        # percolate down

class EmptyHeapException(Exception):
    pass

if __name__ == '__main__':
    s = MinHeap()
    s.insert(2)
    s.insert(4)
    s.insert(5)
    s.insert(10)
    s.insert(1)
    s.insert(3)
    print(s)
    s.extract_min()
    print(s)
    b = MinHeap(L=[33,2,3])
    print(b)
    b.extract_min()
    b.extract_min()
    print(b)

