from django import forms
from memo.models import Memo # 先ほど作ったModelをインポート
from django.core.validators import MinLengthValidator

class MemoForm(forms.ModelForm):
    class Meta:
        model = Memo
        fields = ['id', 'content', 'created_at']

    # メモ本文の入力欄設定（バリデーションを追加）
    content = forms.CharField(
        label="Content",
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'size': '58'}),
        validators=[MinLengthValidator(5, message="メモは5文字以上で入力してください。")]
    )

    # 作成日時の入力欄設定
    created_at = forms.DateField(
        label='Created at',
        required=False,
        input_formats=['%Y-%m-%d'],
        widget=forms.TextInput(attrs={'size': '12'}),
    )