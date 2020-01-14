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

9. main app components로 위에 명시한 index.js를 CREATE!

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

   

10. src/templates 에 index.html

    

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

