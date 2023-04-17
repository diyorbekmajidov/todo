<https://majidovdiyorbek.pythonanywhere.com/api/>

The modani API has the following endpoints:

|method   |endpoint   |description   |
|---|---|---|
|POST   |<a href = "#create">`CreateUserView/`</a>|add user        |
|GET   |<a href = "#getusers">`GetAllUsers/`</a>|get user        |
|POST   |<a href = "#createtodo`">`CreateTodo/`</a>|add todo        |
|GET   |<a href = "#createtodo">`CreateTodo/`</a>|get todo        |
|PUT   |<a href = "#updatetodo">`TodoUpdate/`</a>|update todo     |
|DELETE |<a href = "#deletetodo">`TodoDelete/`</a>|delete todo     |
|POST   |<a href = "#login">`Login/`</a>|login user       |
|POST   |<a href = "#logout">`Logout/`</a>|logout user      |

<br><br><br><br>
<hr>

<hr>
<div id="create"> 

**POST** ```api/create```
### url to add directory
```python
        input:
            {
                "username": str, 
                "password": str,
                "email": str,
                "first_name": str,
                "last_name": str,
            }
        return: json ->
            {
                "username": str, 
                "password": str,
                "email": str,
                "first_name": str,
                "last_name": str,
            }
        
```
<a href = "#base">^ to the top ^</a> 
</div>
<hr>

<hr>
<div id="getusers">

**GET** ```api/getusers```

### url to get all users
```python
        input:
        return: json ->
            {
                "username": str, 
                "password": str,
                "email": str,
                "first_name": str,
                "last_name": str,
            }
        
```
<a href = "#base">^ to the top ^</a>
</div>
<hr>

<hr>

<div id="createtodo">

**POST** ```api/createtodo```

### url to add todo
```python
        input:
            {
                "title": str,
                "user": int,
            }
        return: json ->
            {
                "title": str,
                "user": int,
            }
        
```

<a href = "#base">^ to the top ^</a>

</div>

<hr>

<hr>

<div id="gettodo">

**GET** ```api/gettodo```

### url to get all todo
```python
        input:
        return: json ->
            {
                "title": str,
                "user": int,
            }
        
```


<a href = "#base">^ to the top ^</a>

</div>

<hr>

<hr>

<div id="updatetodo">

**PUT** ```api/updatetodo```

### url to update todo
```python
        input:
            {
                "title": str,
                "user": int,
            }
        return: json ->
            {
                "title": str,
                "user": int,
            }
        
```

<a href = "#base">^ to the top ^</a>

</div>

<hr>

<hr>

<div id="deletetodo">

**POST** ```api/deletetodo```

### url to delete todo
```python
       Delete todo by id
        input:
            {
                "id": int,
            }
        return: json ->
            {
                "title": str,
                "user": int,
            }
        
```

<a href = "#base">^ to the top ^</a>

</div>

<hr>

<hr>

<div id="login">

**POST** ```api/login```

### url to login user
```python
        input:
            {
                "username": str,
                "password": str,
            }
        return: json ->
            {
                "token": str,
            }
        
```

<a href = "#base">^ to the top ^</a>

</div>

<hr>

<hr>

<div id="logout">

**POST** ```api/logout```

### url to logout user
```python
        input:
            {
                "token": str,
            }
        return: json ->
            {
                "message": str,
            }
        
```

<a href = "#base">^ to the top ^</a>

</div>

<hr>





