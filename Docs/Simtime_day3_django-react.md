1.  frontend app 만들고 file구조 만들기

   ```
   python manage.py startapp frontend
   mkdir -p .\frontend\src\components
   mkdir -p .\frontend\static\frontend
   mkdir -p .\frontend\templates\frontend
   ```

   ![html](https://github.com/arara90/images/blob/master/Simtime/simtime%20004.png?raw=true)

   src\components => react apps

   static\frontend => compiled javascripts

   templates\frontend => load .html pages



2. Webpack

   pipfile이 있는 root directory로 이동 후, 

   ```
   npm init -y	
   npm i -D webpack webpack-cli
   ```

3. babel

   ```
   npm i -D @babel/core babel-loader @babel/preset-env @babel/preset-react babel-plugin-transform-class-properties
   ```

4. react

   ```
   npm i -D react react-dom prop-types styled-components
   ```



5. package.json 확인

```
{
  "name": "SimTime",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "dependencies": {
    "webpack": "^4.41.5",
    "webpack-cli": "^3.3.10"
  },
  "devDependencies": {
    "@babel/core": "^7.8.3",
    "@babel/preset-env": "^7.8.3",
    "@babel/preset-react": "^7.8.3",
    "babel-loader": "^8.0.6",
    "babel-plugin-transform-class-properties": "^6.24.1",
    "prop-types": "^15.7.2",
    "react": "^16.12.0",
    "react-dom": "^16.12.0",
    "styled-components": "^5.0.0"
  },
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/arara90/Simtime.git"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "bugs": {
    "url": "https://github.com/arara90/Simtime/issues"
  },
  "homepage": "https://github.com/arara90/Simtime#readme"
}

```

6. root 에 .**babelrc** 파일 생성

```
{
    "presets": ["@babel/preset-env", "@babel/preset-react"],
    "plugins": ["transform-class-properties"]
}
```



7. root에 webpack.config.js 파일 생성

```javascript
// load babel load
module.exports = {
    module:{
        rules: [
            {
                test:/\.js$/, //any js files
                exclude: /node_modules/,
                use:{
                    loader: "babel-loader"
                }
            }
        ]
    }
}
```



8. package.json 의 scripts test->dev로 변경

   *  --output 뒤에는 index.html에 포함되는 actual compiled js 
   * 모드에 따라 npm run build    or   npm run dev 

   ```json
   "scripts": {
       "dev": "webpack --mode development ./Simtime/frontend/src/index.js --output ./Simtime/frontend/static/frontend/main.js",
       "build": "webpack --mode production ./Simtime/frontend/src/index.js --output ./Simtime/frontend/static/frontend/main.js"
     },
     
   ```

   

9. src>components>App.js

   ```python
   import React,{Component} from 'react';
   import ReactDom from 'react-dom'
   
   class App extends Component{
       render(){
           return <h1>React App</h1>
       }
   }
   
   // templates/index.html에 있는 id ='app' 요소를 찾아서 App을 render해준다.
   ReactDom.render(<App />, document.getElementById('app')); 
   ```

   

10. src > index.js

    ```python
    import App from "./components/APP";
    ```

    

11. templates 에 index.html


```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Lead Manager</title>
</head>
<body>
    <div id="app"></div>
    {% load static %}
    <script src ="{% static "frontend/main.js" %}"></script>
</body>
</html>
```

![static folder](https://github.com/arara90/images/blob/master/Simtime/simtime%20005.png?raw=true)

* npm run dev or build 하는 순간, static 내부에 main.js가 생성된다.





## bootstrap 및 urls 설정

1. bootwatch -> cosmo 선택  

```
<link rel ="stylesheet" href="https://bootswatch.com/4/cosmo/bootstrap.min.css"> 
```



2. getbootstrap.com

```html
<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
```



3. 파일 수정

* index.html

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <link rel ="stylesheet" href="https://bootswatch.com/4/cosmo/bootstrap.min.css"> 
      <title>Lead Manager</title>
  </head>
  <body>
      <div id="app"></div>
      {% load static %}
      <script src ="{% static "frontend/main.js" %}"></script>
      <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
      <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
      <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
      
  </body>
  </html>
  ```

  



* views.py

```python
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'frontend/index.html')
```



* urls.py

```python
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index)
]
```



* (project) urls.py에 추가

```python

from django.contrib import admin
from django.urls import path, include

print('urls.py')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('todos/', include('todos.urls')),
    path('', include('leads.urls')),
    path('', include('frontend.urls')),
]

```



4. root에서 npm run dev

![run](https://github.com/arara90/images/blob/master/Simtime/simtime%20006.png?raw=true)

​	main.js 파일 확인 후 서버 재시작

​	python manage.py runserver)



5. 확인

   ![react app](https://github.com/arara90/images/blob/master/Simtime/simtime%20007.png?raw=true)

   > 원하는 대로 react app이 안나왔었다. 그 이유는 ./urls.py에  path('', include(...)) 가 두가지로 정해져있었기 때문에. 위에 있는 것이 우선순위를 갖기 때문에 이전에 설정해둔 leads.url를 따라갔다. 
   >
   > 단순히 위아래만 바꿔주면 정상적으로 React App이 뜨는 것을 확인할 수 있었다.
   >
   > ```python
   > urlpatterns = [
   >     # 위에 있는 것이 우선순위 높다
   >     path('admin/', admin.site.urls),
   >     path('todos/', include('todos.urls')),
   >     path('', include('frontend.urls')), 
   >     path('', include('leads.urls')),
   > ]
   > 
   > # 이 경우 path('', include('frontend.urls')), 가 우선권을 갖는다.
   > ```
   >
   > 



## React Component 만들기

1. install  [ dsznajder.es7-react-js-snippets ]

![](https://github.com/arara90/images/blob/master/Simtime/simtime%20008.png?raw=true)



2. src/components/layout/Header.js

   RCE - > tab 자동완성 이용해보기 (class 기반) (rcf -> function 기반)

![RCE](https://github.com/arara90/images/blob/master/Simtime/simtime%20010.png?raw=true)

![auto-react](https://github.com/arara90/images/blob/master/Simtime/simtime%20011.png?raw=true)



3. https://getbootstrap.com/docs/4.4/components/navbar/ 에서 Hidden brand 부분 copy, 수정

```js
import React, { Component } from 'react'

export class Header extends Component {
    render() {
        return (
            <nav className="navbar navbar-expand-sm navbar-light bg-light">
            <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo01" aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarTogglerDemo01">
                <a className="navbar-brand" href="#">Lead Manager</a>
                <ul className="navbar-nav mr-auto mt-2 mt-lg-0">
                </ul>
            </div>
            </nav>
        )
    }
}

export default Header

```



4. App.js

   ```js
   import React,{Component} from 'react';
   import ReactDom from 'react-dom'
   import Header from './layout/Header'
   
   class App extends Component{
       render(){
           return <Header />
       }
   
   }
   
   // templates/index.html에 있는 id ='app' 요소를 찾아서 App을 render해준다.
   ReactDom.render(<App />, document.getElementById('app')); 
   ```



5. npm run dev 후 runserver   - 적용된 것 확인

   ![bootstrap](https://github.com/arara90/images/blob/master/Simtime/simtime%20012.png?raw=true)



6. 하지만, Header 내용 변경때마다, npm run dev로 다시 build해줘야 하는 불편함이 있음! 이를 극복하자!

   * package.json - > "scripts"에 --watch 옵션 추가

     ```json
     "scripts": {
         "dev": "webpack --mode development --watch ./Simtime/frontend/src/index.js --output ./Simtime/frontend/static/frontend/main.js",
         "build": "webpack --mode production ./Simtime/frontend/src/index.js --output ./Simtime/frontend/static/frontend/main.js"
       },
     ```

     ![watch](https://github.com/arara90/images/blob/master/Simtime/simtime%20013.png?raw=true)



### conponent 추가하기

1. 폴더 및 파일추가

   ![addcomponents](https://github.com/arara90/images/blob/master/Simtime/simtime%20014.png?raw=true)



2. 소스 작성

   ```js
   # Form.js
   import React, { Component } from 'react'
   
   export class Form extends Component {
       render() {
           return (
               <div>
                   <h1>Add Lead Form</h1>
               </div>
           )
       }
   }
   
   export default Form
   ```

   ```js
   # Leads.js
   import React, { Component } from 'react'
   
   export class Leads extends Component {
       render() {
           return (
               <div>
                   <h1>Leads List</h1>
               </div>
           )
       }
   }
   
   export default Leads
   ```

   ```js
   # Dashboard.js
   import React, { Fragment } from 'react'
   import Form from './Form'
   import Leads from './Leads'
   
   export default function Dashboard() {
       return (
           <Fragment>
               <Form />
               <Leads />
           </Fragment>
       )
   }
   ```

   ```js
   # App.js
   import React,{Component, Fragment} from 'react';
   import ReactDom from 'react-dom'
   import Header from './layout/Header'
   import Dashboard from './leads/Dashboard'
   
   class App extends Component{
       render(){
           return(
               <Fragment>
                   <Header />
                   <div className="containder">
                       <Dashboard />
                   </div>
               </Fragment>
           )
       }
   
   }
   
   // templates/index.html에 있는 id ='app' 요소를 찾아서 App을 render해준다.
   ReactDom.render(<App />, document.getElementById('app')); 
   ```





3. 짜란- 완성!

![react-first](https://github.com/arara90/images/blob/master/Simtime/simtime%20017.png?raw=true)





> [ tips ] extention [**Prettier** - Code formatteresbenp]
>
> -> 자동으로 format 맞춰서 저장
>
> 
>
> ![prettier](https://github.com/arara90/images/blob/master/Simtime/simtime%20015.png?raw=true)
>
> 
>
> * file -> references -> settings 에서 format save on 검색 후 체크
>
> ![settings](https://github.com/arara90/images/blob/master/Simtime/simtime%20016.png?raw=true)

