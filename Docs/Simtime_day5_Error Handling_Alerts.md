# Error Handling & Alerts

* 유투브 강의 : [Traversy Media - Full Stack React & Django [4] - Error Handling & Alerts](https://youtu.be/Fia-GGgHpK0)

### 

### Data 입력하지 않고 Submit

![submitwithoutdata](https://github.com/arara90/images/blob/master/Simtime/simtime%20025.png?raw=true)

WHY? .isRequired로 설정한 Name과 Email에 대한 정보가 없기때문에 Format Error다.



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
import Alerts from "./layout/Alert";
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



* **src > reducers> index.js** 

```js
import { combineReducers } from "redux";
import leads from "./leads";

export default combineReducers({
  leads,
  errors
});

```



* **src > conponents > App.js**

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



#### 다른 메세지로 고쳐보자.

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

