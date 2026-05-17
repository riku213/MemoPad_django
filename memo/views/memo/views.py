from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.utils import timezone
from django.db.models import Q # スライド39枚目：Qオブジェクトをインポート
from memo.models import Memo
from memo.forms.memo.forms import MemoForm

# メモ一覧の表示（検索機能付き）
class MemoListView(generic.ListView):
    model = Memo
    paginate_by = 10
    template_name = "memo/list_memo.html"
    success_url = reverse_lazy('home')

    # スライド36〜38枚目：表示するデータ（クエリセット）を動的に変更する
    def get_queryset(self):
        # 1. まず全てのメモを新着順で取得
        queryset = Memo.objects.order_by('-created_at')
        
        # 2. ブラウザの検索窓から入力された文字（q）を受け取る
        keyword = self.request.GET.get('q')
        
        # 3. もしキーワードが入力されていたら、絞り込み（フィルター）を行う
        if keyword:
            # スライド38〜39枚目：contentにキーワードが含まれる、という条件
            # ※「__contains」は、SQLの「LIKE '%キーワード%'」に翻訳されます
            queryset = queryset.filter(
                Q(content__contains=keyword)
            )
        return queryset

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