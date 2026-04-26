from django.db import db

class Memo(db.Model):
    # メモの本文（長いテキストを許可）
    text = db.TextField()
    # 更新日時（保存時に自動で現在時刻を入れる）
    updated_at = db.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text