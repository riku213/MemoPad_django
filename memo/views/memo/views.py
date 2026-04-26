from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.utils import timezone
from memo.models import Memo
from memo.forms.memo.forms import MemoForm

# メモ一覧の表示
class MemoListView(generic.ListView):
    model = Memo
    queryset = Memo.objects.order_by('-created_at') # 新しい順に並べる
    paginate_by = 10 # 1ページに10件表示
    template_name = "memo/list_memo.html"
    success_url = reverse_lazy('home')

# メモの新規作成
class MemoCreateView(generic.CreateView):
    model = Memo
    form_class = MemoForm
    template_name = "memo/memo_form.html"
    success_url = reverse_lazy('memo:list_memo')
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_at = timezone.now() # 現在時刻をセット
        self.object.save()
        return redirect('memo:list_memo')

# メモの編集
class MemoUpdateView(generic.UpdateView):
    model = Memo
    form_class = MemoForm
    template_name = "memo/memo_form.html"
    success_url = reverse_lazy('memo:list_memo')
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return redirect('memo:list_memo')

# メモの削除
class MemoDeleteView(generic.DeleteView):
    model = Memo
    success_url = reverse_lazy('memo:list_memo')
    
    def get(self, request, *args, **kwargs):
        self.object = Memo.objects.get(pk=kwargs['pk'])
        self.object.delete()
        return redirect('memo:list_memo')