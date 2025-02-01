###############################################
'''
{% if request.user.groups.all.0.name == "ngouser" %}
<a class="nav-link" href="{% url 'event_list' %}">
    <div class="sb-nav-link-icon"><i class="fas fa-chart-area"></i></div>
    Events
</a>
{% endif %}  '''
#########################################