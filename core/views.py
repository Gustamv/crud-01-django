from django.shortcuts import render, redirect
from . models import Pessoa

def home(request):
    #a variavel pessoas agora recebe todas as pessoas que estao no bd
    pessoas = Pessoa.objects.all()
    #o terceiro parametro eh a forma que sera enviada ao template, no caso, o index.html
    return render(request, 'index.html',{"pessoas": pessoas})

def salvar(request):
    vnome = request.POST.get("nome")
    #assim que cria um dado novo no bd
    Pessoa.objects.create(nome=vnome)
    pessoas = Pessoa.objects.all()
    #passar lista atualizada para o template
    return render(request, 'index.html',{"pessoas": pessoas})

def editar(request, id):
    pessoa = Pessoa.objects.get(id=id)
    return render(request, "update.html", {"pessoa": pessoa})

def update(request, id):
    #pega o nome novo
    vnome = request.POST.get("nome")
    #recuperar o id 
    pessoa = Pessoa.objects.get(id=id)
    #receber o novo nome na variavel
    pessoa.nome = vnome
    pessoa.save()
    #redirecionar para a home
    return redirect(home)

def deletar(request, id):
    #pega a pessoa do banco pelo id
    pessoa = Pessoa.objects.get(id=id)
    #deleta ela
    pessoa.delete()
    #redirecionar para a home
    return redirect(home)

