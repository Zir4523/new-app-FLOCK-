from django.contrib import admin
from .models import Post

admin.site.register(Post)

from .models import Memo          # Memo をインポート

# Register your models here.

admin.site.register(Memo)         # 追加