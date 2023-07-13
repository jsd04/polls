
from django.http import HttpResponseRedirect,HttpResponse, Http404
from django.shortcuts import get_object_or_404, render, redirect, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.template import loader
#creatiionform
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.db.models import Q

#from .models import Choice, Question, UsuarioInquilino
from .models import Choice, Question, UsuarioInquilo
from .forms import InquilinoForm


#Administrador e Index
def index(request):
     title='Index'
     return render (request,"polls/index.html",{
          'mytitle':title
     })
     
def signup(request):
        if request.method == 'GET':
            print('enviando formulario')
            title='Registrar'
            return render(request, "polls/signup.html",{
                'mytitle':title,
                'form':UserCreationForm
            } ) 
        else:
             if request.POST["password1"] == request.POST["password2"]:
                  #register user
                  try:
                    user = User.objects.create_user(username=request.POST["username"],
                                                   password=request.POST["password1"])
                    user.save()
                    login(request, user)
                    return redirect('/polls/principal/')
                   # return HttpResponse('User creado satisfactoriamente')        
                  except IntegrityError:
                       return render(request, "polls/signup.html",{
                            'error': 'El user ya existe',
                            'form':UserCreationForm
                        } ) 
             return render(request, "polls/signup.html",{
                            'error': 'Passwords no coinciden',
                            'form':UserCreationForm
                        } )   
 

   #return render(request, "polls/signin.html",
def signin(request):
         if request.method == "GET":
            title='Iniciar sesion'
            return render(request, "polls/signin.html",{
                'mytitle':title,
                'form':AuthenticationForm
            } )        
         else:
              user = authenticate( request, username=request.POST['username'], password=request.POST['password'])
              if user is None:
                return render(request, 'polls/signin.html',{
                    'error': "usuario o password es incorrecto.",
                    'form': AuthenticationForm
                    })

              login(request, user)
              return redirect('/polls/principal/')
            
   #return render(request, "polls/signin.html",
@login_required
def principal(request):
     title='Principal Administrador'
     return render (request,"polls/principal.html",{
          'mytitle':title
     })
@login_required
def signout(request):
     logout(request)
     return redirect('/polls/signin/')
def about(request):
     title='About'
     return render (request,"polls/about.html",{
          'mytitle':title
     })

#Inquilinos
def inquilinosinicial(request):
     title='Inquilinos Inicial'
     return render (request,"polls/inquilinos/inquilinos_inicial_copy.html",{
          'mytitle':title
     })
def inquilinos(request):
     inquilinos = UsuarioInquilo.objects.all()
     title='Inquilinos'
     return render (request,"polls/inquilinos/all-inquilinos.html",{
          'mytitle':title,
          'inquilinos':inquilinos
     })

def new_inquilino(request):
     if request.method == "GET":
        return render(request, 'polls/inquilinos/new-inquilino.html', {"form":  InquilinoForm})
     else:
        # print(request.POST)
        # return render(request, 'polls/inquilinos/new-inquilino.html', {"form":  InquilinoForm})
        try:
            form = InquilinoForm(request.POST)
            new_inquilino = form.save(commit=False)
            new_inquilino.save()
            return redirect('/polls/inquilinos/')
        except ValueError:
            return render(request, 'polls/inquilinos/new-inquilino.html', {"form":  InquilinoForm, "error": "Error creando el inquilino."})
def search_inquilino(request):
     busqueda = request.POST.get("buscar")
     print('nusqueda es ',busqueda)
     nombre = request.POST.get("nombre")
     print('nombre es ',nombre)
     piso = request.POST.get("piso")
     print('npiso es ',piso)
     departamento = request.POST.get("departamento")
     print('ndepartamento es ',departamento)
     inquilinos = UsuarioInquilo.objects.all()
     if busqueda:
        inquilinos = UsuarioInquilo.objects.filter(
            Q(piso__icontains = busqueda) | 
            Q(nombre__icontains = busqueda) |
            Q(curp__icontains = busqueda) |
            Q(departamento__icontains = busqueda)
        ).distinct()  
     if nombre:
        inquilinos = UsuarioInquilo.objects.filter(
            Q(nombre__icontains = nombre) 
        ).distinct()  
        print('nombre des ',nombre)
     if piso:
        inquilinos = UsuarioInquilo.objects.filter(
            Q(piso__icontains = piso) 
        ).distinct() 
        print('npiso des ',piso) 
     if departamento:
        inquilinos = UsuarioInquilo.objects.filter(
            Q(departamento__icontains = departamento)
        ).distinct() 
        print('ndepartamento des ',departamento)
        print('inquilino es ',inquilinos)
    # inquilino = get_object_or_404(UsuarioInquilo,pk=inquilino_para)
    #  inquilinos = UsuarioInquilo.objects.filter(nombre='jessica sanchez pruebaF5')
     title='search'
     return render (request,"polls/inquilinos/s-inquilinos.html",{
          'mytitle':title,
          'inquilinos':inquilinos
     })
# def search_inquilino(request,inquilino_para):
#      inquilino = get_object_or_404(UsuarioInquilo,pk=inquilino_para)
#     #  inquilinos = UsuarioInquilo.objects.filter(nombre='jessica sanchez pruebaF5')
#      title='search'
#      return render (request,"polls/inquilinos/search-inquilinos.html",{
#           'mytitle':title,
#           'inquilino':inquilino
#      })
# export const searchInquilinos = async (req, res) => {
#   //console.log('query -> ',req.query)
#   if(req.query.buscar && req.query.piso && req.query.dep){
#     console.log("buscar ", req.query.buscar)
#     console.log("piso ", req.query.piso)
#     console.log("dep ", req.query.dep)
#     const inquilinosFound = await Inquilino.find(
#       { $and: [ {nombre:{ $regex:  req.query.buscar, $options:"$i"}},
#        {piso:{$eq:req.query.piso}}, {departamento:{$eq:req.query.dep}} ]} )
#     //.sort({ date: "desc" })}
#      // {nombre:{ $regex: req.query.buscar, $options:"$i"}})
#     /* ***************** regex y options **************
#       Usa $ regex operador como una expresión regular para encontrar patrones en una cadena.
#       Para distinguir entre mayúsculas y minúsculas, las expresiones regulares utilizan 
#       $ opción y el parámetro con un valor de $ i */

#       //const inquilinosFound = await Inquilino.find({nombre:{ $eq: req.query.buscar}})
#     .sort({ date: "desc" })
#       .lean();
#       console.log('El Inquilino que coincidio es :   ', inquilinosFound)
#       res.render("inquilinos/search-inquilinos",{ inquilinosFound })
#   }
#   else if(req.query.buscar && req.query.piso){
#     console.log("buscar2 ", req.query.buscar)
#     console.log("piso2 ", req.query.piso)
#     console.log("dep2 ", req.query.dep)
#     const inquilinosFound = await Inquilino.find( { $and: [ {nombre:{ $regex:  req.query.buscar, $options:"$i"}}, {piso:{$eq:req.query.piso}} ]})
#     .sort({ date: "desc" })
#       .lean();
#       console.log('El Inquilino que coincidio es :   ', inquilinosFound)
#       res.render("inquilinos/search-inquilinos",{ inquilinosFound })
#   }
#   else{
#     console.log("no hay parametro")
#     res.render("inquilinos/search-inquilinos")
#   }
# }        
     



# GUIA
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    
    context_object_name = "latest_question_list"
    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
            :5
        ]
    """
    """
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
    """
   
    def detail(request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        return render(request, "polls/detail.html", {"question": question},HttpResponse("You're looking at question %s." % question_id))
    """
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"
    """
    def results(request, question_id):
        response = "You're looking at the results of question %s."
        question = get_object_or_404(Question, pk=question_id)
        return render(request, "polls/results.html", {"question": question},HttpResponse(response % question_id))
     """    


def vote(request, question_id):
    ...  # same as above, no changes needed.
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
    #return HttpResponse("You're voting on question %s." % question_id)


        
        
    