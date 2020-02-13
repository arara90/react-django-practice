# Error Handling & Alerts

* 유투브 강의 : [Traversy Media - Full Stack React & Django [4] - Error Handling & Alerts](https://youtu.be/Fia-GGgHpK0)

* 참고 : [팝업과 메시지 with React]([https://hyunvinci.tistory.com/entry/41-%EC%98%88%EC%99%B8%EC%B2%98%EB%A6%AC%EC%99%80-%EC%95%8C%EB%A6%BC-%EC%84%9C%EB%B9%84%EC%8A%A4third-party-package%EC%8D%A8%EB%93%9C%ED%8C%8C%ED%8B%B0-%EC%82%AC%EC%9A%A9-%EC%98%81%EC%96%B4%EC%8C%A4%EC%9D%B4-%EB%A7%8C%EB%93%9C%EB%8A%94-%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85-%EC%9D%B8%EC%A6%9DCRUD-%EB%A7%8C%EB%93%A4%EC%96%B4%EC%9A%A4-%EB%A6%AC%EC%95%A1%ED%8A%B8%EC%99%80-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%A5%EA%B3%A0](https://hyunvinci.tistory.com/entry/41-예외처리와-알림-서비스third-party-package써드파티-사용-영어쌤이-만드는-회원가입-인증CRUD-만들어욤-리액트와-파이썬-장고))



1. Alert Component 만들기 -> react-alert의 withAlert

   

2. App에 (Alert 띄울 화면)에reat-alert가 제공하는 Provider 사용해서 감싸기

   Provider에는 Alert의 position및 timeout 설정, template가 속성으로 들어간다.

3. App에 (Alert 띄울 화면)에 1에서 만들었던 Alert Component 코드 내에 넣어주기.



4. action type에 등록하고 GET_ERRORS 작성, action에서 catch에 걸릴 경우

err => console.log(err.response.data)) 에서 전달받은 err에 대한 상태를 볼 수 있음



5. reducer에 등록해서 alert 고쳐보기

    -> catch에서 변수에 에러 메시지, 상태 저장 후에 dispatch 하기.



### Data 입력하지 않고 Submit

![submitwithoutdata](https://github.com/arara90/images/blob/master/Simtime/simtime%20025.png?raw=true)

WHY? .isRequired로 설정한 Name과 Email에 대한 정보가 없기때문에 Format Error다.

* 근데 어디에서 isRequired로 했더라...ㅠㅠ?
  * Invitations -> model.py : blank=False로 했더니 'This field may not be blank.' Error 발생! 



## react-alert

https://github.com/schiehll/react-alert



### 설치

```
npm i react-alert react-alert-template-basic react-transition-group
```



### 소스 수정



* **src > components > layout > Alerts.js** 

```js
import React, { Component, Fragment } from "react";
import { withAlert } from "react-alert";

export class Alerts extends Component {
  componentDidMount() {
    this.props.alert.show("It Works");
  }

  render() {
    return <Fragment />;
  }
}

export default withAlert()(Alerts);
//it should be 'export default withAlert()(Alerts)' if you are using react-alert version 6.0.0, otherwise withAlert(Alerts);

```



* **src > components > App.js**

```js
import {Provider as AlertProvider} from 'react-alert';
import AlertTemplate from 'react-alert-template-basic';
import Alerts from "./layout/Alerts";
...

// Alert Options 추가
const alertOptions = {
  timeout: 3000,
  position: "top center"
};

// Provider 내부에 Fragment 전체를 감싼다.
class App extends Component {
  render() {
    return (
      <Provider store={store}>
        <AlertProvider template={AlertTemplate} {...alertOptions}>
          <Fragment>
            <Header />
            <Alerts />
            <div className="container">
              <Dashboard />
            </div>
          </Fragment>
        </AlertProvider>
      </Provider>
    );
  }
}

ReactDom.render(<App />, document.getElementById("app"));

```





* **src > actions> type.js**

```js
export const GET_LEADS = "GET_LEADS";
export const DELETE_LEAD = "DELETE_LEAD";
export const ADD_LEAD = "ADD_LEAD";
export const GET_ERRORS = "GET_ERRORS";
```



* **src > actions> leads.js**

```js
// ADD LEAD
export const addLead = lead => dispatch => {
  axios
    .post(`/api/leads/`, lead)
    .then(res => {
      // pass in an object with a type
      dispatch({
        type: ADD_LEAD,
        payload: res.data
      });
    })
    .catch(err => console.log(err.response.data));
};

```



#### 완성

![Itworks](https://github.com/arara90/images/blob/master/Simtime/simtime%20026.png?raw=true)

![themessages](https://github.com/arara90/images/blob/master/Simtime/simtime%20027.png?raw=true)







### 다른 메세지로 고쳐보자.



* **src > reducers> index.js** 

```js
import { combineReducers } from "redux";
import leads from "./leads";

export default combineReducers({
  leads,
  errors
});

```



* **src > reducers > errors.js**

```js
import { GET_ERRORS } from "../actions/types";

const initialState = {
  msg: {},
  status: null
};

export default function(state = initialState, action) {
  switch (action.type) {
    case GET_ERRORS:
      return {
        msg: action.payload.msg,
        status: action.payload.status
      };
    default:
      return state;
  }
}
```





* **src > actions> leads.js**

```js
// ADD LEAD
export const addLead = lead => dispatch => {
  axios
    .post(`/api/leads/`, lead)
    .then(res => {
      dispatch({
        type: ADD_LEAD,
        payload: res.data
      });
    })
    .catch(err => {
      const errors = {
        msg: err.response.data,
        status: err.response.status
      };
	//dispatch 추가
      dispatch({
        type: GET_ERRORS,
        payload: errors
      });
    });
};
```

![](https://github.com/arara90/images/blob/master/Simtime/simtime%20028.png?raw=true)

state에 반영된 것을 알 수 있다.

* **src > components > layout > Alerts.js**

```js
import React, { Component, Fragment } from "react";
import { withAlert } from "react-alert";
import { connect } from "react-redux";
import PropTypes from "prop-types";

export class Alerts extends Component {
  static propTypes = {
    error: PropTypes.object.isRequired
  };

  // when we get a new prop such as the error, then this is gonna run.
  componentDidUpdate(prevProps) {
    const { error, alert } = this.props;
    if (error !== prevProps.error) {
      alert.error("There is an error");
    }
  }

  render() {
    return <Fragment />;
  }
}

const mapStateToProps = state => ({
  error: state.errors // the reducer that we want
});

export default connect(mapStateToProps)(withAlert()(Alerts));
// It should be 'export default withAlert()(Alerts)' if you are using react-alert version 6.0.0
// otherwise  withAlert(Alerts);


```

![ErrorMessage](https://github.com/arara90/images/blob/master/Simtime/simtime%20029.png?raw=true)



#### 여러가지 Error Message 보여주기

* **src > conponents > layout > Alerts.js**

```js
  // when we get a new prop such as the error, then this is gonna run.
  componentDidUpdate(prevProps) {
    const { error, alert } = this.props;
    if (error !== prevProps.error) {
      // if (error.msg.email) alert.error("Email is required");  
      if (error.msg.name) alert.error(`Name: ${error.msg.name.join()}`);
      if (error.msg.email) alert.error(`Email: ${error.msg.email.join()}`);
      if (error.msg.message) alert.error(`Message: ${error.msg.message.join()}`);
    
    }
  }
```

![Message](https://github.com/arara90/images/blob/master/Simtime/simtime%20030.png?raw=true)





#### CREATE MESSAGES

##### DELETE 메세지를 만들어보자!

![deleteMessage](https://github.com/arara90/images/blob/master/Simtime/simtime%20031.png?raw=true)

* **ACTIONS**

  1. **types.js**

     ```js
     export const GET_MESSAGES = "GET_MESSAGES";
     export const CREATE_MESSAGE = "CREATE_MESSAGE";
     ```

  2. **messages.js**

     ```js
     import { CREATE_MESSAGE } from "./types";
     
     // CREATE_MESSAGE
     export const createMessage = msg => {
       return {
         type: CREATE_MESSAGE,
         payload: msg
       };
     };
     
     ```

  3. **leads.js (event 발생지)**

     ```js
     import { createMessage } from "./messages";
     
     // DELETE LEAD
     export const deleteLead = id => dispatch => {
       axios
         .delete(`/api/leads/${id}/`)
         .then(res => {
           dispatch(createMessage({ deleteLead: "Lead Deleted" }));
           // pass in an object with a type
           dispatch({
             type: DELETE_LEAD,
             payload: id
           });
         })
         .catch(err => console.log(err));
     };
     ```

     

  

  

* **REDUCER**

  1. **index.js**

     ```
     import { combineReducers } from "redux";
     import leads from "./leads";
     import errors from "./errors";
     import messages from "./messages";
     
     export default combineReducers({
       leads,
       errors,
       messages
     });
     
     ```

  2. **messages.js**

     ```
     import { GET_MESSAGES, CREATE_MESSAGE } from "../actions/types";
     
     const initialState = {};
     
     export default function(state = initialState, action) {
       switch (action.type) {
         case GET_MESSAGES:
           return action.payload;
         case CREATE_MESSAGE:
           return (state = action.payload);
         default:
           return state;
       }
     }
     
     ```

     

* **COMPONENT**

  1. **Alerts.js**

     ```js
     //propType 추가
     static propTypes = {
         error: PropTypes.object.isRequired,
         message: PropTypes.object.isRequired
       };
     
     componentDidUpdate(prevProps) {
          // message 로직 추가
         const { error, alert, message } = this.props;
     
         ...
     
         if (message !== prevProps.message) {
           if (message.deleteLead) alert.success(message.deleteLead);
         }
       }
     ```

     





##### Challenge! - ADD 메세지를 만들어보자!

* ACTION

  1. type.js

  2. message.js

  3. leads.js

     ```js
     // ADD LEAD
     export const addLead = lead => dispatch => {
       axios
         .post(`/api/leads/`, lead)
         .then(res => {
           // pass in an object with a type
           dispatch({
             type: ADD_LEAD,
             payload: res.data
           });
     
           dispatch(createMessage({ addLead: "Lead Added" }));
         })
         .catch(err => {
           const errors = {
             msg: err.response.data,
             status: err.response.status
           };
     
           dispatch({
             type: GET_ERRORS,
             payload: errors
           });
         });
     };
     ```

     

* REDUCER

  1. message.js

     

* COMPONENT

  1. Alert.js

     ```js
     // when we get a new prop such as the error, then this is gonna be run.
       componentDidUpdate(prevProps) {
         const { error, alert, message } = this.props;
         if (error !== prevProps.error) {
           // if (error.msg.name) alert.error("Name is required"")
           // if (error.msg.email) alert.error("Email is required");
           if (error.msg.name) alert.error(`Name: ${error.msg.name.join()}`);
           if (error.msg.email) alert.error(`Email: ${error.msg.email.join()}`);
           if (error.msg.message)
             alert.error(`Message: ${error.msg.message.join()}`);
         }
     
         if (message !== prevProps.message) {
           if (message.deleteLead) alert.success(message.deleteLead);
           if (message.addLead) alert.success(message.addLead);
         }
       }
     ```



#### 마지막으로 submit 후 Form Clear하기

Components > leads>  Form.js

```js
onSubmit = e => {
    e.preventDefault();
    const { name, email, message } = this.state;
    const lead = { name, email, message };
    this.props.addLead(lead);
    this.setState({
      name: "",
      email: "",
      message: ""
    });
  };
```

