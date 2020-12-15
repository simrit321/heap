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
        index = self._data.index(v)
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
 
    
    def extract_min(self):
        '''Remove minimal value in self. Restore heap property.
        Raise EmptyHeapException if heap is empty.'''
        
        if len(self._data) == 0:
            raise Exception("No values in min heap")
        else:
            ind = len(self._data) - 1
            a, b = self._data[0], self._data[ind]
            self._data[b], self._data[a] = self._data[a], self._data[b]
            m = self._data.pop(ind)
            
            index = 0
            il = left(index)
            ir = right(index)
            r = self._data[0]
            l = self._data[il]
            ri = self._data[ir]
            
            while r > l or r > ri:
                
                if l > ri:
                    smaller = ri
                elif l < ri:
                    smaller = l
                  
                x,y = self._data.index(r), self._data.index(smaller)
                self._data[y], self._data[x] = self._data[x], self._data[y]
                index = self._data.index(r)
                il = left(index)
                ir = right(index)
                l = self._data[il]
                r = self._data[ir]
            return self             
 
    
    def _percolate_up(self):
        '''Restore heap property of self after 
        adding new item'''
        
        pass
    
    
    def _percolate_down(self, i):
        ''' Restore heap property of subtree 
        rooted at index i.
        '''
        
        # while larger than at least one child
        # swap with smaller child and repeat    
        pass
    
    
    def _min_heapify(self):
        '''Turn unordered list into min-heap.'''
        
        # for each node in the first half of the list
        # percolate down
        pass
if __name__ == '__main__':
    s = MinHeap(L=[0,1,5,7])
    s.insert(2)
    s.insert(4)
    print(s)
    s.extract_min()
    print(s)