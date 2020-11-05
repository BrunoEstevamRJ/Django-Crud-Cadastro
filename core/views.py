from django.shortcuts import render


def form_manual(request):
    data = {}
    if request.method == 'POST':
        data['nomeCliente'] = request.POST.get('nomeCliente', 'nome não encontrado')
        data['telefoneCliente'] = request.POST.get('telefoneCliente', 'telefone não encontrado')
        data['emailCliente'] = request.POST.get('emailCliente', 'email não encontrado')
        data['msgCliente'] = request.POST.get('msgCliente', 'mensagem não encontrada')
        data['active'] = request.POST.get('active', 'não deseja receber ofertas')
    return render(request, 'core/index.html', data)
