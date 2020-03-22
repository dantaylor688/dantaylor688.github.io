---
layout: default
title: Sunday School
---
## COVID-19

In compliance with the requests of Federal, State and Local government authorities to slow the spread of coronavirus COVID-19, the Boys' 14-15 year old Sunday school class is temporarily moving online. Here, I will post each week's lesson consisting of a few notes from me about the chapter we are studying as well as some questions. Your assignment will be to:

1. read the relevant chapter of the Bible and whatever notes I post
2. answer at least __two__ of the questions given throughout the lesson (in the comments section) and
3. read and respond to someone else's answer (to a different question than you answered).

Note that you will need to sign up for an account with [Disqus](https://disqus.com/profile/login/) to be able to leave a comment.

I hope this exercise will allow us to still feel somewhat connected during this crazy time in our country.

{% for post in site.sunday-school-lessons %}
  * {{ post.date | date_to_string }} &raquo; [ {{ post.title }} ]({{ post.url }})
{% endfor %}

<!-- <div class="posts">
  {% for post in site.sunday-school-lessons%}
  <article class="post">
    <h1 class="post-title">
      <a href="{{ post.url }}">
        {{ post.title }}
      </a>
    </h1>

    <time datetime="{{ post.date | date_to_xmlschema }}" class="post-date">{{ post.date | date_to_string }}</time>
  </article>
  {% endfor %}
</div> -->

<!-- <div class="pagination">
  {% if paginator.next_page %}
    <a class="pagination-item older" href="{{ site.baseurl }}page{{paginator.next_page}}">Older</a>
  {% else %}
    <span class="pagination-item older">Older</span>
  {% endif %}
  {% if paginator.previous_page %}
    {% if paginator.page == 2 %}
      <a class="pagination-item newer" href="{{ site.baseurl }}">Newer</a>
    {% else %}
      <a class="pagination-item newer" href="{{ site.baseurl }}page{{paginator.previous_page}}">Newer</a>
    {% endif %}
  {% else %}
    <span class="pagination-item newer">Newer</span>
  {% endif %}
</div> -->
