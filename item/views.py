from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import LostItem
from .forms import LostItemForm

class LostItemListView(ListView):
    model = LostItem
    template_name = 'item/lostitem_list.html'
    context_object_name = 'items'

class LostItemDetailView(DetailView):
    model = LostItem
    template_name = 'item/lostitem_detail.html'

class LostItemCreateView(LoginRequiredMixin, CreateView):
    model = LostItem
    form_class = LostItemForm
    template_name = 'item/lostitem_form.html'
    success_url = reverse_lazy('item:list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class LostItemUpdateView(LoginRequiredMixin, UpdateView):
    model = LostItem
    form_class = LostItemForm
    template_name = 'item/lostitem_form.html'
    success_url = reverse_lazy('item:list')

class LostItemDeleteView(LoginRequiredMixin, DeleteView):
    model = LostItem
    template_name = 'item/lostitem_confirm_delete.html'
    success_url = reverse_lazy('item:list')
