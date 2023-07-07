"""
from django.shortcuts import render
from django.http import Http404

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.template import loader

from .models import Question,Choice


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

# ...
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


# ...
def vote(request, question_id):
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
    
    
    """

from django.http import HttpResponseRedirect,HttpResponse, Http404
from django.shortcuts import get_object_or_404, render, redirect
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

from .models import Choice, Question


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
     title='Inquilinos'
    #  return render (request,"polls/inquilinos/all-inquilinos.html",{
    #       'mytitle':title
    #  })
     
# export const renderinquilinos = async (req, res) => {
#   const inquilinos = await inquilino.find({ user: req.user.id })
#     .sort({ date: "desc" })//ordenar datos de manera descendente
#     .lean();
#   res.render("inquilinos/all-inquilinos", { inquilinos });
# };

     



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


        
        
    