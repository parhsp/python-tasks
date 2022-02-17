from urllib.request import Request, urlopen

def func1():
    h=''
    req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data = urlopen(req).read()
    esk = str(data)
    k = esk.find("round")#παίρνουμε τον αριθμό του latest round 
    k1 = esk.find("randomness")  
    c = esk[k+7:k1-2]
    c=int(c)#counter για τον υπολογισμό και την έυρεση των 20 προηγούμενων γύρων του latest
    
    for i in range (20):
        req = Request('https://drand.cloudflare.com/public/'+str(c), headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})#ξεκιναμε απο το latest round και παίρνουμε τις προηγούμενες 100 τιμές απο το randomness
        data = urlopen(req).read() 
        c=c-1
        esk = str(data)
        k = esk.find("round")#παιρνουμε καθε φορα τον προηγούμενο αριθμό του round
        k1 = esk.find("randomness")
        k4 = esk.find("randomness")#αντίστοιχα παίρνουμε τους προηγούμενους αριθμούς για κάθε randomness
        k5 = esk.find("signature")
        new_esk = esk[k4+13:k5-3]#oι τιμες απο το πεδίο randomness για καθε γύρο
        h=h+new_esk#το δεκαεξαδικό κείμενο(όλες οι τιμες μαζί)
    
func1()