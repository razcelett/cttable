{% load widget_tweaks %}
{% load static %}
{% load  templatetags %}
<!DOCTYPE html>
<html lang="en">
   <head>
      <title>{% block title %}Change Password{% endblock %}</title>
      <!-- Custom fonts for this template-->
      <link href="{% static 'vendor/fontawesome-free/css/all.min.css' %}" rel="stylesheet" type="text/css">
      <link
         href="https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i" rel="stylesheet">
      <!-- Custom styles for this template-->
      <link href="{% static 'css/sb-admin-2.css' %}" rel="stylesheet">
      <link href="{% static 'css/student-profile.css' %}" rel="stylesheet">
   </head>
   <body>
      <center>
        <div class="container-xl px-1 mt-1">
         <!-- Account page navigation-->
         <center>
            <div class="row" style="margin-top: 150px; margin-left: 200px;">
               <div class="col-xl-10">
                  <!-- Account details card-->
                  <div class="card mb-5">
                     <div class="card-header">Change Password</div>
                     <div class="card-body">
                        {% if messages %}
                        {% for message in messages %}
                          {% if message.tags and message.tags == 'error' %}
                            <div class="alert alert-danger" role="alert">
                              <strong>Error:</strong> {{ message }}
                              <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                                <span aria-hidden="true">&times;</span>
                              </button>
                            </div>
                          {% else %}
                            <div class="alert alert-success" role="alert">
                              {{ message }}
                              <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                                <span aria-hidden="true">&times;</span>
                              </button>
                            </div>
                          {% endif %}
                        {% endfor %}
                        {% endif %}
                        <form action="" method="post">
                           {% csrf_token %}
                           <div class="input-group mb-3">
                              {{ form.old_password }}
                              <div class="input-group-append">
                                 <div class="input-group-text">
                                    <span class="fa fa-fw fa-eye field-icon id_old_password" onclick="togglePassword('id_old_password')"></span>
                                 </div>
                              </div>
                           </div>
                           <span class="text-error">{{ form.old_password.errors }}</span>
                           <div class="input-group mb-3">
                              {{ form.new_password1 }}
                              <div class="input-group-append">
                                 <div class="input-group-text">
                                    <span class="fa fa-fw fa-eye field-icon id_new_password1" onclick="togglePassword('id_new_password1')"></span>
                                 </div>
                              </div>
                           </div>
                           <span class="text-error">{{ form.new_password1.errors }}</span>
                           <div class="input-group mb-3">
                              {{ form.new_password2 }}
                              <div class="input-group-append">
                                 <div class="input-group-text">
                                    <span class="fa fa-fw fa-eye field-icon id_new_password2" onclick="togglePassword('id_new_password2')"></span>
                                 </div>
                              </div>
                           </div>
                           <span class="text-error">{{ form.new_password2.errors }}</span>
                           <button type="submit" class="btn btn-primary shadow-2 mb-4">Confirm</button>
                        </form>
                        {% if request.user.is_superuser %}
                        <p class="mb-0 text-muted">
                           <a href="timetable">Go Back</a>
                        </p>
                        {% elif not request.user.is_superuser and not request.user.email|contains_numbers %}
                        <p class="mb-0 text-muted">
                           <a href="faculty-update">Go Back</a>
                        </p>
                        {% else %}
                        <p class="mb-0 text-muted">
                           <a href="student-update">Go Back</a>
                        </p>
                        {% endif %}
                     </div>
                  </div>
               </div>
            </div>
        </div>
      </center>
      <!-- Specific Page JS goes HERE  -->
      {% block javascripts %}
      <script>
         function togglePassword(inputId) {
             var input = document.getElementById(inputId);
             var icon = document.querySelector("." + inputId);
             console.log(inputId);
             console.log(input)
             if (input.type === "password") {
                 input.type = "text";
                 icon.classList.remove("fa-eye");
                 icon.classList.add("fa-eye-slash");
             } else {
                 input.type = "password";
                 icon.classList.remove("fa-eye-slash");
                 icon.classList.add("fa-eye");
             }
         }
      </script>
      {% endblock javascripts %}
   </body>
</html>