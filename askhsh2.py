def text_to_binary(text):#συνάρτηση μετρατροπής των χαρακτήρων του ascii αρχείου σε ακολουθια δυαδικων αριθμών
    total_binary = ''
    total_binary2 = ''
    
    for i in range(len(text)):#επανάληψη για όλο το μήκος του αρχείου που δίνεται
        binary = ''
        string_ord = ord(text[i:i+1])#μετατροπή χαρακτήρα σε δεκαδικό

        while string_ord > 0:#μετατροπή δεκαδικού αριθμού στον αντίστοιχο δυαδικό 7 ψηφίων
            x = string_ord % 2
            string_ord = string_ord // 2
            binary=str(x)+str(binary)
        if len(binary) < 7:#χαρακτήρες ascii όπου σε δεκαδικό είναι μικρότερες ή ίσες του 32 μεταφράζονται απο το παραπάνω κομμάτι κώδικα με τον μικρότερο δυνατό αριθμό δυαδικών ψηφίων(πχ το tab θα γίνει 1001) Επομένως θα πρέπει να τους αλλάξουμε σε 7 ψηφία όπως γίνεται παρακάτω
            while len(binary) !=7:
                binary='0'+ binary        
        total_binary+= binary + ' '
        total_binary2+= binary 
    print("Οι χαρακτήρες του αρχείου που δώθηκε σε δυαδική μορφή είναι:",total_binary)
    number_sequence(total_binary2)

def ascii_file():
    f = open("arxeio1.txt", "r",encoding="utf8")#παράδειγμα αρχείου
    k=f.read()
    text_to_binary(k)
    f.close()

def number_sequence(numbers):#συνάρτηση εύρεσης μεγαλύτερης ακολουθίας 0 και 1 
    c1=0
    m2=0
    c=0
    m1=0
    for i in range(len(numbers)):
        if numbers[i]=='1':
            c+=1
        else:
            if c > m1:
                m1=c
            c=0
        if numbers[i]=='0':
            c1+=1
        else:
            if c1 > m2:
                m2=c1
            c1=0
    print("Η μεγαλύτερη ακολουθία απο συνεχόμενα 1 ειναι:",m1)
    print("Και η μεγαλύτερη ακολουθία απο συνεχόμενα 0 ειναι:",m2)
            
ascii_file()


