import React,{Component} from 'react';
import ReactDom from 'react-dom'

class App extends Component{
    render(){
        return <h1>React App</h1>
    }

}

// templates/index.html에 있는 id ='app' 요소를 찾아서 App을 render해준다.
ReactDom.render(<App />, document.getElementById('app')); 