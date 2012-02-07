#!/usr/bin/env python             
                                  
import sys                        
# map the occurences of requests from an ip
# grep out the column titles first though
                                  
for line in sys.stdin:            
  columns = line.split()          
  #print columns                  
  if columns and columns[2].isdigit():                                                                               
    timestamp = columns[0] + ' ' + columns[1] 
    kbmemfree = columns[2]          
    kbbuffers = columns[5]          
    kbcached = columns[6]           
    total = int(kbmemfree) + int(kbbuffers) + int(kbcached)
    print '%s %s ' % (timestamp, total)
