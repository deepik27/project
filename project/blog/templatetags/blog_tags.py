from blog.models import Post
from django import template
register = template.Library()


#By using simple_tag to return no of posts published
@register.simple_tag
def total_posts():
    return Post.objects.count()


#by using inclusion tag to display lastes posts

@register.inclusion_tag('blog/latest_posts.html')
def show_latest_posts():
    latest_posts=Post.objects.order_by('-publish')[:3]
    return {'latest_posts': latest_posts}


#By using assignment_tag to display the most commented posts

from django.db.models import Count
#@register.simple_tag
#def get_most_commented_posts(count=2):
    #return Post.objects.annotate(total_comments=count('comments')).order_by('total_comments')[:count]
'''

<h3>Most Commented Posts: </h3> {% get_most_commented_posts as most_commented_posts %}
    <ul>
        {% for post in most_commented_posts %}
        <li><a href="{{post.get_absolute_url}}">{{post.title}}</a></li>
        {%endfor%}
    </ul>
'''