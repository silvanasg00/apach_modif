from django.shortcuts import render

#request 'es un diccionario que continuamente se va pasando entre el navegador y el servidor'

def Home(request):

	return render(request, 't_home.html')

def Castracion(request):

	return render(request, 't_castracion.html')

def Vacunacion(request):

	return render(request, 't_vacunacion.html')

def Donar(request):

	return render(request, 't_donar.html')


def Veterinarios(request):

	return render(request, 't_vets.html')

