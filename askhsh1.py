import random

def func1(arr):#υπολογισμος ασσων για καθε πινακα ετσι ωστε οταν γεμισουν οι θεσεις με καθε μεγεθος να μην ξαναδωθει τιμη σε κουτι που ηδη υπαρχει
    sum=0
    for x in range(3):
        for y in range(3):
            sum=sum+arr[x][y]
    return sum
 
def func2(arr):#εφοσον υπαρχει 1 η περισσοτερες κενες θεσεις στη λιστα δινουμε τυχαια τιμη σε αυτην(σε κενο κελι)
    n = random.randint(0,2)
    y = random.randint(0,2)
    while arr[n][y]==1:#ελεγχος εαν υπαρχει ηδη τιμη(1) στο κελι που επιλεξαμε
        n = random.randint(0,2)#εφοσον υπαρχει μπαινουμε στο while και δινουμε νεες μεχρι να βρεθει κελι με τιμη(0)
        y = random.randint(0,2)   
    arr[n][y]=1 #μολις βρεθει κενο κελι δινεται η τιμη (1)
    return True

def func3(arr):#η συναρτηση ελεγχει ολους τους δυνατους συνδυασμους ετσι ωστε να ληξει το παιχνιδι για τους πινακες arr,arr1,arr2 χωριστα
    if arr[0][0]==1 and arr[1][1]==1 and arr[2][2]==1:
        return True
    elif arr[2][0]==1 and arr[1][1]==1 and arr[0][2]==1:
        return True
    elif arr[0][0]==1 and arr[0][1]==1 and arr[0][2]==1:
        return True
    elif arr[1][0]==1 and arr[1][1]==1 and arr[1][2]==1:
        return True
    elif arr[2][0]==1 and arr[2][1]==1 and arr[2][2]==1:
        return True
    elif arr[0][0]==1 and arr[1][0]==1 and arr[2][0]==1:
        return True
    elif arr[0][1]==1 and arr[1][1]==1 and arr[2][1]==1:
        return True
    elif arr[0][2]==1 and arr[1][2]==1 and arr[2][2]==1:
        return True
   
def func4(lst,lst1,lst2):#η συναρτηση ελεγχει ολους τους δυνατους συνδυασμους νικης με τριαδες απο μικρα μεσαια μεγαλα και αντιστροφα
    if lst[0][0]==1 and lst1[1][1]==1 and lst2[2][2]==1:
        return True
    elif lst[2][0]==1 and lst1[1][1]==1 and lst2[0][2]==1:
        return True
    elif lst[0][0]==1 and lst1[0][1]==1 and lst2[0][2]==1:
        return True
    elif lst[1][0]==1 and lst1[1][1]==1 and lst2[1][2]==1:
        return True
    elif lst[2][0]==1 and lst1[2][1]==1 and lst2[2][2]==1:
        return True
    elif lst[0][0]==1 and lst1[1][0]==1 and lst2[2][0]==1:
        return True
    elif lst[0][1]==1 and lst1[1][1]==1 and lst2[2][1]==1:
        return True
    elif lst[0][2]==1 and lst1[1][2]==1 and lst2[2][2]==1:
        return True
 
c=0
for x in range(100):
    win=False
    rows, cols = (3, 3)
    arr = [[0 for i in range(cols)] for j in range(rows)]#πινακας των 9 μικρων δακτυλιων(βαζουμε 0 σε ολες τις θεσεις του)
    arr1 = [[0 for i in range(cols)] for j in range(rows)]#πινακας των 9 μεσαιων δακτυλιων(βαζουμε 0 σε ολες τις θεσεις του)
    arr2 = [[0 for i in range(cols)] for j in range(rows)]#πινακας των 9 μεγαλων δακτυλιων (βαζουμε 0 σε ολες τις θεσεις του)
    while win==False:#οσο δεν εχει βρεθει νικητης τοποθετουνται νεες τιμες στις λιστες μεχρι να βρεθει νικητηρια τριαδα
        timh=False
        k=random.randint(1,3)
        if k==1 and func1(arr)<9:
            timh=func2(arr)
        elif k==2 and func1(arr1)<9:
            timh=func2(arr1)
        elif k==3 and func1(arr2)<9:
            timh=func2(arr2)
        if timh==True:#εαν η μεταβλητη timh ειναι True που σημαινει οτι δωθηκε νεα τιμη σε μια απο τις λιστες γινεται αναζητηση νικητη
            c=c+1#καθε φορα που δινεται μια νεα τιμη σε ενα απο τα κελια της λιστας μετραται ως βημα για να υπολιστει ο μεσος ορος στο τελος
            #εαν καποια απο τις παρακατω func3 η func4 επιστρεψει τιμη True σημαινει πως το παιχνιδι εληξε
            if func3(arr)==True:
                win=True#εαν υπαρξει νικητης η μεταβλητη win γινεται True και λιγει το παιχνιδι 
            elif func3(arr1)==True:
                win=True
            elif func3(arr2)==True:
                win=True
            elif func4(arr,arr1,arr2)==True:
                win=True
            elif func4(arr2,arr1,arr)==True:
                win=True  

mesos=c/100#διαιρεση του συνολου των βηματων με το 100(παιχνιδια) για την ευρεση του μεσου ορου
print("o mesos oros twn vimatwn gia na lixei to paixnidi einai",mesos) 