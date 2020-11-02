from flask import Flask, redirect, url_for, request 
import requests

app = Flask(__name__) 
  

def trueorflase(pnr,lname,cmob):
    # return True

    headers = {
    'Host': 'book.goindigo.in',
    'User-Agent': 'Mozilla/5.0 (Android 9; Mobile; rv:68.0) Gecko/68.0 Firefox/68.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://www.goindigo.in',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://www.goindigo.in/',
}

    data = {
  'indiGoRetrieveBooking.RecordLocator': pnr,
  'polymorphicField': lname,
  'typeSelected': 'SearchByNAMEFLIGHT',
  'indiGoRetrieveBooking.IndiGoRegisteredStrategy': 'Nps.IndiGo.Strategies.IndigoValidatePnrContactNameStrategy, Nps.IndiGo',
  'indiGoRetrieveBooking.IsToEmailItinerary': 'false',
  'indiGoRetrieveBooking.EmailAddress': '',
  'indiGoRetrieveBooking.LastName': lname
}

    res = requests.post('https://book.goindigo.in/Booking/RetrieveAEM', headers=headers, data=data)
    ses = res.headers['set-cookie']
    headers = {
    'Host': 'book.goindigo.in',
    'User-Agent': 'Mozilla/5.0 (Android 9; Mobile; rv:68.0) Gecko/68.0 Firefox/68.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://www.goindigo.in',
    'Connection': 'keep-alive',
    'Referer': 'https://www.goindigo.in/booking/view.html?linkNav=view_booking-widget',
    'Cookie': ses
}


    data = {
    'indiGoContact.HomePhoneCountryCode': '91',
    'indiGoContact.HomePhone': cmob,
    'indiGoContact.OtherPhoneCountryCode': '',
    'indiGoContact.OtherPhone': '',
    'indiGoContact.WorkPhoneCountryCode': '91',
    'indiGoContact.WorkPhone': '8980345600',
    'indiGoContact.EmergencyContactRelationship': 'Friend',
    'indiGoContact.EmailAddress': 'smj387@gmail.com'
    }

    res = requests.post('https://book.goindigo.in/Passengers/UpdateDetailsAEM', headers=headers, data=data, allow_redirects=False)

    stat = res.text.find('/Booking/PostCommitAEM')

    if(stat != -1):
        print('\nStatus: Details Updated!')
        return True
    else:
        print('\nStatus: An Error Occured!')
        return False


@app.route('/success/<name>') 
def success(name): 
   return 'welcome %s' % name 

@app.route('/failed/<name>') 
def failed(name): 
   return 'welcomehello %s' % name 
  
@app.route('/login',methods = ['POST','GET']) 
def login(): 

    if request.method == 'POST': 

        pnr = request.form['pnr'] 
        lname = request.form['lname'] 
        cmob = request.form['cmob'] 
        # print(pnr)
        # print(trueorflase(pnr,lname,cmob))
        if trueorflase(pnr,lname,cmob) == True:
            print("Sucess") 
            return redirect(url_for('success',name = pnr)) 
        else:
            print("Failed") 
            return redirect(url_for('failed',name = pnr)) 

            
  
if __name__ == '__main__': 
   app.run(debug = True) 


# pnr = input('Enter PNR: ')
# lname = input('Enter Last Name: ')
# cmob = input('Customer Mobile: ')

# headers = {
#     'Host': 'book.goindigo.in',
#     'User-Agent': 'Mozilla/5.0 (Android 9; Mobile; rv:68.0) Gecko/68.0 Firefox/68.0',
#     'Accept': '*/*',
#     'Accept-Language': 'en-US,en;q=0.5',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
#     'Origin': 'https://www.goindigo.in',
#     'DNT': '1',
#     'Connection': 'keep-alive',
#     'Referer': 'https://www.goindigo.in/',
# }

# data = {
#   'indiGoRetrieveBooking.RecordLocator': pnr,
#   'polymorphicField': lname,
#   'typeSelected': 'SearchByNAMEFLIGHT',
#   'indiGoRetrieveBooking.IndiGoRegisteredStrategy': 'Nps.IndiGo.Strategies.IndigoValidatePnrContactNameStrategy, Nps.IndiGo',
#   'indiGoRetrieveBooking.IsToEmailItinerary': 'false',
#   'indiGoRetrieveBooking.EmailAddress': '',
#   'indiGoRetrieveBooking.LastName': lname
# }

# res = requests.post('https://book.goindigo.in/Booking/RetrieveAEM', headers=headers, data=data)
# ses = res.headers['set-cookie']
# headers = {
#     'Host': 'book.goindigo.in',
#     'User-Agent': 'Mozilla/5.0 (Android 9; Mobile; rv:68.0) Gecko/68.0 Firefox/68.0',
#     'Accept': '*/*',
#     'Accept-Language': 'en-US,en;q=0.5',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
#     'Origin': 'https://www.goindigo.in',
#     'Connection': 'keep-alive',
#     'Referer': 'https://www.goindigo.in/booking/view.html?linkNav=view_booking-widget',
#     'Cookie': ses
# }

# data = {
#   'indiGoContact.HomePhoneCountryCode': '91',
#   'indiGoContact.HomePhone': cmob,
#   'indiGoContact.OtherPhoneCountryCode': '',
#   'indiGoContact.OtherPhone': '',
#   'indiGoContact.WorkPhoneCountryCode': '91',
#   'indiGoContact.WorkPhone': '8980345600',
#   'indiGoContact.EmergencyContactRelationship': 'Friend',
#   'indiGoContact.EmailAddress': 'smj387@gmail.com'
# }

# res = requests.post('https://book.goindigo.in/Passengers/UpdateDetailsAEM', headers=headers, data=data, allow_redirects=False)

# stat = res.text.find('/Booking/PostCommitAEM')

# if(stat != -1):
#     print('\nStatus: Details Updated!')
# else:
# print('\nStatus: An Error Occured!')

