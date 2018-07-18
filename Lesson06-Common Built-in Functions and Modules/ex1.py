def eight_queens(a):
    i = 0 
    j = 0
    if a[0][0] != a[1][0] != a[2][0] != a[3][0] != a[4][0] != a[5][0] != a[6][0] != a[7][0]:
        i += 1
        if a[0][1]!= a[1][1] !=a[2][1] != a[3][1] != a[4][1] != a[5][1] != a[6][1] != a[7][1]:
            j +=1
            if i == 1 and j == 1:
                print('true')
            else:
                print('False')
        else:
            print('False')
    else:
        print('False')
eight_queens([[0, 0], [1, 4], [2, 7], [3, 5], [4, 2], [5, 6], [6, 1], [7, 3]])