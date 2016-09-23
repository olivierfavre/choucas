from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

@login_required
def index(request):
    return HttpResponse("GENDLOC")

@login_required
#@permission_required('gendloc.can_send')
def envoi_sms(request):
    #Vérifier permission
    #Vérifier crédit
    #Récupération des paramètres
    phonenumber = '+33625397570'
    lang = 'FR'
    validite = 1
    message = 'Geoloc'
    #Déterminer le SENDER
    sender = 'GENDLOC'
    #Déterminer le texte
    texte = 'Hello World !'
    #Envoyer le SMS
    import callr
    api = callr.Api(settings.CALLR_NAME, settings.CALLR_PWD)
    result = api.call('sms.send', sender, phonenumber, texte, None)
    #ajout entrée Model.SMS
    #Retour au template
    return HttpResponse(result)  

@login_required
def maj(request):
    #Vérifier permission
    #Récupération liste SMS des 24 dernières heures de l'unité
    #Retour au template
	return HttpResponse(liste_sms)

@login_required
def geoloc(request):
	pass
