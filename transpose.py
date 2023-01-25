# name you function as transpose_matrix and takes a list
# you should return a list of lists
def transpose_matrix(mat):
    n = len(mat)
    m = len(mat[0])
    temp = []
    for i in range(m):
        a = []
        for j in range(n):
            a.append(mat[j][i])
        temp.append(a)
    return temp


# do not change anything below this line
if __name__ == "__main__":
    h = int(input())
    lst = []
    for val in range(0, h):
        lst.append([int(i) for i in input().split(' ')])
    out = transpose_matrix(lst)
    for val in out:
        print(" ".join(str(i) for i in val))