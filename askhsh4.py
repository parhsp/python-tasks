from urllib.request import Request, urlopen

def func1():
    req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data = urlopen(req).read()
    esk = str(data)
    k = esk.find("round")#παίρνουμε τον αριθμό του latest round 
    k1 = esk.find("randomness")  
    c = esk[k+7:k1-2]
    c=int(c)#counter για τον υπολογισμό και την έυρεση των 100 προηγούμενων γύρων του latest
    
    for i in range (101):
        req = Request('https://drand.cloudflare.com/public/'+str(c), headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})#ξεκιναμε απο το latest round και παίρνουμε τις προηγούμενες 100 τιμές απο το randomness
        data = urlopen(req).read() 
        c=c-1
        esk = str(data)
        k = esk.find("round")#παιρνουμε καθε φορα τον προηγούμενο αριθμό του round
        k1 = esk.find("randomness")
        k4 = esk.find("randomness")#αντίστοιχα παίρνουμε τους προηγούμενους αριθμούς για κάθε randomness
        k5 = esk.find("signature")
        new_esk = esk[k4+13:k5-3]
        binary(new_esk)

def binary(new_esk):#Συνάρτηση μετατροπής απο δεκαεξαδικό σε binary 
    ini_string = new_esk
    n = int(ini_string, 16) 
    binary_str = ''
    while n > 0:
        binary_str = str(n % 2) + binary_str 
        n = n >> 1    
    res = binary_str 
    print ("To binary string ειναι:", str(res))
    number_sequence(res)

def number_sequence(res):#συνάρτηση εύρεσης μεγαλύτερης ακολουθίας 0 και 1 
    c1=0
    m2=0
    c=0
    m1=0
    for i in range(len(res)):
        if res[i]=='1':
            c+=1
        else:
            if c > m1:
                m1=c
            c=0
        if res[i]=='0':
            c1+=1
        else:
            if c1 > m2:
                m2=c1
            c1=0
    print("Η μεγαλύτερη ακολουθία απο συνεχόμενα 1 ειναι:",m1)
    print("Και η μεγαλύτερη ακολουθία απο συνεχόμενα 0 ειναι:",m2)

func1() 