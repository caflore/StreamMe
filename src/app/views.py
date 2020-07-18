from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator

from .forms import UserRegistrationForm
from .models import Vod
from stream.models import Stream

def home(request):
    return render(request, 'app/home.html')

class VodListView(ListView):
    model = Vod
    template_name = 'app/vods.html'
    context_object_name = 'vods'
    ordering = ['-date_posted']

class VodDetailView(DetailView):
    model = Vod
    template_name = 'app/vod_detailview.html'
    context_object_name = 'vod'

class VodCreateView(LoginRequiredMixin, CreateView):
    model = Vod
    fields = ['title', 'description', 'vod']
    template_name = 'app/vod_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class StreamListView(ListView):
    model = Stream
    template_name = 'app/streams.html'
    context_object_name = 'streams'

class StreamDetailView(DetailView):
    model = Stream
    template_name = 'app/stream_detailview.html'
    context_object_name = 'stream'

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('app-login')
    else:
        form = UserRegistrationForm()
    return render(request, 'app/signup.html', {'form': form})

def login(request):
    return render(request, 'app/login.html')

@login_required
def profile(request):
    return render(request, 'app/profile.html')
