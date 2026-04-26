from django import forms
from memo.models import Memo # 先ほど作ったModelをインポート

class MemoForm(forms.ModelForm): # DjangoのModelForm機能を継承
    class Meta:
        model = Memo
        fields = ['id', 'content', 'created_at'] # 扱う項目を指定 

    # メモ本文の入力欄設定
    content = forms.CharField(
        label="Content",
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'size': '58'}), # 入力枠の長さを指定 
    )

    # 作成日時の入力欄設定
    created_at = forms.DateField(
        label='Created at',
        required=False,
        input_formats=['%Y-%m-%d'],
        widget=forms.TextInput(attrs={'size': '12'}), # 日付用の枠サイズ 
    )