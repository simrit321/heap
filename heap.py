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
        #self._percolate_up()
        self._percolate_down(i=0)
        return m
            
 
    
    def _percolate_up(self):
        '''Restore heap property of self after 
        adding new item'''
        index = len(self._data)
        v = self._data[index - 1]
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
        maxL = len(self._data)-1
        
    
        if (index_left <= maxL) and (index_right <= maxL):
            
            left_val = self._data[index_left]
            right_val = self._data[index_right]
            
            if left_val < node_val and right_val < node_val :
            
                if left_val > right_val:
                    smaller = right_val
                    x,y = self._data.index(node_val), self._data.index(smaller)
                    self._data[y], self._data[x] = self._data[x], self._data[y]
                    index = self._data.index(node_val)
                    self._percolate_down(i=index)
                elif left_val < right_val:
                    smaller = left_val
                    x,y = self._data.index(node_val), self._data.index(smaller)
                    self._data[y], self._data[x] = self._data[x], self._data[y]
                    index = self._data.index(node_val)
                    self._percolate_down(i=index)
                elif left_val == right_val:
                    smaller = left_val
                    x,y = self._data.index(node_val), self._data.index(smaller)
                    self._data[y], self._data[x] = self._data[x], self._data[y]
                    index = self._data.index(node_val)
                    self._percolate_down(i=index)
                  
                
            elif (left_val < node_val) and (right_val >= node_val):
                smaller = left_val
                x,y = self._data.index(node_val), self._data.index(smaller)
                self._data[y], self._data[x] = self._data[x], self._data[y]
                index = self._data.index(node_val)
                self._percolate_down(i=index)
                
            elif (right_val < node_val) and (left_val >= node_val):
                smaller = right_val
                x,y = self._data.index(node_val), self._data.index(smaller)
                self._data[y], self._data[x] = self._data[x], self._data[y]
                index = self._data.index(node_val)
                self._percolate_down(i=index)
                
        elif (index_left <= maxL) and (index_right > maxL):
            left_val = self._data[index_left]
            if left_val < node_val:
                smaller = left_val
                x,y = self._data.index(node_val), self._data.index(smaller)
                self._data[y], self._data[x] = self._data[x], self._data[y]
                index = self._data.index(node_val)
                self._percolate_down(i=index)
                    
        elif (index_right <= maxL) and (index_left > maxL):
            right_val = self._data[index_right]
            if right_val < node_val:
                smaller = right_val
                x,y = self._data.index(node_val), self._data.index(smaller)
                self._data[y], self._data[x] = self._data[x], self._data[y]
                index = self._data.index(node_val)
                self._percolate_down(i=index)
                            
 
        
        return self._data

            
        # while larger than at least one child
        # swap with smaller child and repeat    
        
    
    
    def _min_heapify(self):
        '''Turn unordered list into min-heap.'''
        length = len(self._data)
        mid = length//2 
        
        l = list(range(mid))
        print(l)
        for item in l[::-1]:
            self._percolate_down(item)
            

                   
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
    print('s:')
    print(s)
    s.extract_min()
    print(s)
    print('======')
    b = MinHeap(L=[33,2,3,55,4,0,1])
    #print('MinHeap:')
    print(b)
    #b.extract_min()
    #b.extract_min()
    #print(b)

