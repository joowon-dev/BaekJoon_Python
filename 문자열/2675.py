for T in range (int(input())):
    P=''
    R,S = input().split(' ')
    for i in range (len(S)):
        for j in range(int(R)):
            P=P+S[i]
    print(P)
