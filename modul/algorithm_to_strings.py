import euclidian_algorithm
from euclidian_algorithm import gr_comm_division

def euclidian_string(n1, n2):
    if n1 < n2:
        n1, n2 = n2, n1
    if n1 == n2 & n1 != 0 or n2 == 1:
        s = str(n2) + ' = ' + str(n1) + ' * ' + str(0) + ' + ' + str(n2) + ' * ' + str(1) 
    else:
        if n2 == 0:
            if n1 == 0:
                s = str(0) + ' = ' + str(n1) + ' * ' + str(0) + ' + ' + str(n2) + ' * ' + str(0)
            else:
                s = str(n1) + ' = ' + str(n1) + ' * ' + str(1) + ' + ' + str(n2)
        else:
            s = str(euclidian_algorithm.gr_comm_division(n1, n2)[0]) + ' = ' + str(n1) + ' * ' + str(euclidian_algorithm.gr_comm_division(n1, n2)[1]) + ' + ' + str(n2) + ' * ' + str(euclidian_algorithm.gr_comm_division(n1, n2)[2])
    return(s)