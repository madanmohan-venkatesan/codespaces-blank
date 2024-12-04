#souce:A
#Dest: C
#Aux: B
def tower_of_hanoi(n,a,b,c):
    if n==1:
        print(f"Move disk 1 from {a} to {b}")
    else:
        #Move n-1 from A to B
        tower_of_hanoi(n-1,a,c,b)
        print(f"Move {n} from A to B")
        tower_of_hanoi(n-1,c,b,a)

if __name__=='__main__':
    sol=tower_of_hanoi(64,"A","B","C")
    print(sol)