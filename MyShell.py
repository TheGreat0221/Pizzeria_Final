import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pizza.settings")

import django
django.setup()

from pizzas.models import Pizza


p = Pizza.objects.get(id=1)
print(p.name)
print(p.date_added)

#To get data through a foriegn key relationship, you use the lowercase name of the
# related model followed by an underscore and the word set
comments = p.comment_set.all()

for comment in comments:
    print(comment)



