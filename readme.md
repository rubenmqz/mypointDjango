#Práctica Python, Django y REST

## ACTUALIZACIÓN: Práctica desplegada

Desde el 05/03/2017 puede verse y probarse un despliegue de la practica en la url **django.oncetios.es
(cambiando "once" por el número "11")**. Además de la versión web, se pueden usar los endpoints indicados en los siguientes puntos (adaptando la url, a la de despliegue).

##Instrucciones API

**API DE USUARIOS**

```POST http://127.0.0.1:8000/api/1.0/users/```
<br />
```GET http://127.0.0.1:8000/api/1.0/users/<pk>/```
<br />
```PUT http://127.0.0.1:8000/api/1.0/users/<pk>/```
<br />
```DELETE http://127.0.0.1:8000/api/1.0/users/<pk>/```

<br />
**API DE BLOGS**

```GET http://127.0.0.1:8000/api/1.0/blogs/```

<br />
**API DE POSTS**

```GET http://127.0.0.1:8000/api/1.0/posts/<username>```
<br />
```POST http://127.0.0.1:8000/api/1.0/posts/```
<br />
```GET http://127.0.0.1:8000/api/1.0/posts/<pk>/```
<br />
```PUT http://127.0.0.1:8000/api/1.0/posts/<pk>/```
<br />
```DELETE http://127.0.0.1:8000/api/1.0/posts/<pk>/```