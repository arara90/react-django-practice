## [react] Modal 만들기

강의 영상 - https://www.youtube.com/watch?v=WGjv-p9jYf0



### **Case 1** - CSS를 이용한 modal

Reusable component displayed inside of another component.

![react-modal-case1.png](https://github.com/arara90/images/blob/master/react/react-modal-case1.png?raw=true)

App.js

```html
<div>
 ..
    <div className = "left">
        <h1>hehehehehhe</h1>
        <h2>hehehehehhe</h2>
        <h13hehehehehhe</h3>
    </div>
    <div className = "right">
        <h1>hehehehehhe</h1>
        <h2>hehehehehhe</h2>
        <h13hehehehehhe</h3>
        
        <BadModal>
            <h1> This is Modal</h1>h1>
            <p>ETC.</p>
            <Colors />
		</BadModal>
    </div>
	
..
<div>
```

```css
/* 아래 주석을 푸는 순간! 더 left가 modal보다 앞에 나오면서 가장 앞에 나와야하는 modal이 본래의 역할을 상실한다!  */
/* .left{
    z-index: 3;
}*/

.right{
    z-index: 1;
}

body .modal{
    position: fixed;
    top : 40px;
    left : 40px;
    right : 40px;
    bottom : 40px;
    border....
    ...
    ...
}
```



* #### 문제점

  * 모든 Component에 대해 Z-index 이슈를 항상 고려해야한다. 개발이나 유지보수 시에 매우 성가신 일.



### Case 2 - Modal을 documnet.body의 child로 만들기

 Placing a Modal Make it  Child of Document.Body!

![react-modal-case2.png](https://github.com/arara90/images/blob/master/react/react-modal-case2.png?raw=true)

​								

```
import React, {Component} from 'react';
import ReactDom from 'react-dom';

class Modal extends Component{
	componentDidMount(){
		this.modalTarget = document.createElement('div');
		this.modalTarget.className = 'modal';
		document.body.appendChild(this.modalTarget);
		this._render();
	}
	
	componentWillUpdate(){
		this._render();
	}
	
	componentWillUnmount(){
		ReactDom.unmountComponentAtNode(this.modalTarget);
		documnet.body.removeChild(this.modalTarget)
	}
	
	_render(){
		ReactDOM.render(<div>{this.props.children}</div>,
		this.modalTarget
		);
	}
	
	render(){
		return <noscript />;
	}
}
```

```
<div>
 ..
    <div className = "left">
        <h1>hehehehehhe</h1>
        <h2>hehehehehhe</h2>
        <h13hehehehehhe</h3>
    </div>
    <div className = "right">
        <h1>hehehehehhe</h1>
        <h2>hehehehehhe</h2>
        <h13hehehehehhe</h3>
        <div>
       		<Modal>
                <h1> This is Modal</h1>h1>
                <p>ETC.</p>
                <Colors />
			</Modal>
		<div>
    </div>
	
..
<div>

```

- no more CSS issues.

- react 기본 규칙을 거스르는 구조.

  

- #### 문제점 

  * colors와 같은 redux connected component는 다음과 같은 Error가 발생

    ![modal_store_error](https://github.com/arara90/images/blob/master/react/react%20031.png?raw=true)

    Root내 Provider 태그를 통해 connect가 동작하는데 이를 벗어났기 때문에 store에 접근할 수 없기 때문이다. 

    

    즉, react 최상위 컴포넌트의 render는 대부분 Provider로 감싼 구조로 구성되므로, 하이어라키 구조상 자식이 아닌 형제?에 해당하는 Modal은 store에 대한 연결고리가 없다.

    ```js
    render() {
        return (
          <Provider store={store}>
            <App />
          </Provider>
        );
      }
    ```



### Case 3 - Fixing Redux

![react-modal-case3.png](https://github.com/arara90/images/blob/master/react/react-modal-case3.png?raw=true)

```js
import React, {Component} from 'react';
import ReactDom from 'react-dom';
import {store} from '../index';
import {Provider} from 'react-redux';

class Modal extends Component{
	componentDidMount(){
		this.modalTarget = document.createElement('div');
		this.modalTarget.className = 'modal';
		document.body.appendChild(this.modalTarget);
		this._render();
	}
	
	componentWillUpdate(){
		this._render();
	}
	
	componentWillUnmount(){
		ReactDom.unmountComponentAtNode(this.modalTarget);
		documnet.body.removeChild(this.modalTarget)
	}
	
	_render(){
		ReactDOM.render(
		<Provider store = {store}>
			<div>{this.props.children}</div>
		</Provider>,
		this.modalTarget
		);
	}
	
	render(){
		return <noscript />;
	}
}
```



It works!

만약 react-modal 라이브러리도 이와 유사하게 동작한다. 하지만, modal안에 connected component(redux)를 사용한다면  해당 라이브러리는  case 2에서 설명한 Provider 문제로 잘 동작하지 않는다.

 



더 살펴보기

[React Modal Component 만들기](https://velog.io/@zynkn/React-Modal-Component-만들기)

[Build a simple Modal Component with React](https://blog.bitsrc.io/build-a-simple-modal-component-with-react-16decdc111a6)

