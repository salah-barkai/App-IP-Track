from tkinter import *
from ttkbootstrap import Style
import requests


def localiser_ip():
    
    api_key= '93411ee6e15c754cdbcadb1992d4dbe6'
    #address ip a localiser 
    ip_address =recherche.get()
    #faire une demande l'api sur IPStack
    response = requests.get('http://api.ipstack.com/{}?access_key={}'.format(ip_address, api_key))
    #verification de la demande
    if response.status_code == 200:
        #analyse des donnés jason
        data= response.json()
        #Suppression de texte apres la generation
        text.delete(1.0, END)
        #affiche des informations de localisation d'ip
        print('Pays: ' , data['country_name'])
        print('Ville: ', data['city'])
        print('Code postale: ', data['zip'])
        print('Latitude: ', data['latitude']) 
        print('longitude: ', data['longitude'])
        #inserer le resultat
        text.insert(END,'Pays: '+ '' + data['country_name']+'\n') 
        text.insert(END,'Ville: '+ '' +data['city']+'\n')
        text.insert(END,'Code postale: '+ '' +data['zip']+'\n' )
        text.insert(END, 'Latitude: '+ '' +str(data['latitude'])+'\n')
        text.insert(END,'longitude: '+ '' +str(data['longitude'])+'\n')   
    else:
        print('la demande a echoué ressayer: ' , response.status_code)
        text.delete(1.0, END)
        text.insert(END,'la demande a echoué ressayer: \n', 'Mettez un address IP valide')
#fenetre
root=Tk()
root.title('App IP Track')
#style du theme
style= Style(theme='superhero')

#labels
titre= Label(root, text='Localiser votre IP', font=("arial",16))
titre.pack(padx=50, pady=0)

#input
recherche =Entry(root)
recherche.pack(padx=50, pady=50)

btn= Button(root, text='Rechercher', command=localiser_ip)
btn.pack(padx=50, pady=5)
#affiche du resultat ip 
text= Text(root, width= 30, height=30)
text.pack(padx=10, pady=10)
#text.configure(state=DISABLED)
root.mainloop()

