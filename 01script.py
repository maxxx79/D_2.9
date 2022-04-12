u1 = User.objects.create_user(username='Анатолий')
u2 = User.objects.create_user(username='Владимир')
Author.objects.create(author_user=u1)
Author.objects.create(author_user=u2)
Category.objects.create(name='sport')
Category.objects.create(name='politic')
Category.objects.create(name='bisness')
author1 = Author.objects.get(pk=1)
author2 = Author.objects.get(id=2)
Post.objects.create(author=author2,category_type='nw',title='sometitle',text='somebigtext')
Post.objects.create(author=author2,category_type='ar',title='sometitle2',text='somebigtext2')
Post.objects.create(author=author1,category_type='ar',title='sometitle3',text='somebigtext3')
Post.objects.get(id=1).post_category.add(Category.objects.get(pk=2))
Post.objects.get(id=1).post_category.add(Category.objects.get(id=1))
Post.objects.get(id=2).post_category.add(Category.objects.get(id=3))
Post.objects.get(id=3).post_category.add(Category.objects.get(pk=2))
a1 = Author.objects.get(id=1)
a2 = Author.objects.get(id=2)
Comment.objects.create(comment_post=Post.objects.get(id=1),comment_user=a1.author_user,text='simpletext1')
Comment.objects.create(comment_post=Post.objects.get(id=2),comment_user=a1.author_user,text='simpletext2')
Comment.objects.create(comment_post=Post.objects.get(id=3),comment_user=a1.author_user,text='simpletext3')
Comment.objects.create(comment_post=Post.objects.get(id=1),comment_user=a2.author_user,text='simpletext4')
Comment.objects.create(comment_post=Post.objects.get(id=2),comment_user=a2.author_user,text='simpletext5')
Comment.objects.get(id=1).like()
Comment.objects.get(id=2).like()
Comment.objects.get(id=2).like()
Comment.objects.get(id=3).like()
Comment.objects.get(id=3).like()
Comment.objects.get(id=3).like()
Comment.objects.get(id=4).like()
Comment.objects.get(id=5).like()
Comment.objects.get(id=5).like()
Comment.objects.get(id=5).like()
Comment.objects.get(id=5).like()
Comment.objects.get(id=1).dislike()
Post.objects.all()[0].like()
Post.objects.all()[1].like()
Post.objects.all()[2].like()
Post.objects.all()[2].dislike()
a1.update_rating()
a2.update_rating()
a1.rating_author
a2.rating_author
a = Author.objects.order_by('-rating_author')[:1]
for i in a:
    i.rating_author
    i.author_user.username
Post.objects.get(id=2).like()
p = Post.objects.order_by('-rating')[:1]
p[0].creation_date.strftime('%Y-%m-%d')
p[0].author.author_user.username
p[0].title
p[0].preview()
p[0].rating
z = Comment.objects.filter(comment_post=p[0])
for i in z:
    i.date_creation.strftime('%Y-%m-%d')
    i.comment_user.username
    i.rating
    i.text