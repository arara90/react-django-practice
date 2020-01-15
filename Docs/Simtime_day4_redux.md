# Redux

### install

```
npm i redux react-redux redux-thunk redux-devtools-extension
```



### store.js (src폴더)

```js
import { createStore, applyMiddleware } from "redux";
import { composeWithDevTools } from "redux-devtools-extension";
import thunk from "redux-thunk";
import rootReducer from "./reducers";

const initialState = {};
const middleWare = [thunk];
const store = createStore(
  rootReducer,
  initialState,
  composeWithDevTools(applyMiddleware(...middleWare))
);

export default store;

```



### frontend > src > reducers > index.js

```js
import { combineReducers } from "redux";

export default combineReducers({});
```



### frontend > src > components > App.js

* Provider 하위에 있는 컴포넌트는 리덕스의 상탯값이 변경되면 자동으로 렌더 함수가 호출되도록 할 수 있다.

```js
import React, { Component, Fragment } from "react";
import ReactDom from "react-dom";
import Header from "./layout/Header";
import Dashboard from "./leads/Dashboard";

//redux
import { Provider } from "react-redux";
import store from "../store";

class App extends Component {
  render() {
    return (
      <Provider store={store}>
        <Fragment>
          <Header />
          <div className="container">
            <Dashboard />
          </div>
        </Fragment>
      </Provider>
    );
  }
}

// templates/index.html에 있는 id ='app' 요소를 찾아서 App을 render해준다.
ReactDom.render(<App />, document.getElementById("app"));

```

![redux-error](https://github.com/arara90/images/blob/master/Simtime/simtime%20018.png?raw=true)



=====================================================================

### frontend > src > actions> types.js

```js
export const GET_LEADS = "GET_LEADS";
```





### frontend > src > reducers > leads.js

```js
import { GET_LEADS } from "../actions/types";

const initialState = {
  leads: [],
  somthing: "text"
};

export default function(state = initialState, action) {
  switch (actions.type) {
    case GET_LEADS:
      return {
        ...state,
        leads: actions.payload
      };
    default:
      return state;
  }
}

```



### frontend > src > reducers > index.js

```js
import { combineReducers } from "redux";
import leads from "./leads";

export default combineReducers({
  leads
});

```



* > **combineReducers** : https://deminoth.github.io/redux/api/combineReducers.html
  >
  > 앱이 점점 복잡해지면 [리듀싱 함수](https://deminoth.github.io/redux/Glossary.html#리듀서)를 [상태](https://deminoth.github.io/redux/Glossary.html#상태)의 독립된 부분들을 관리하는 함수들로 분리하고 싶어질겁니다.
  >
  > `combineReducers` 헬퍼 함수는 서로 다른 리듀싱 함수들을 값으로 가지는 객체를 받아서 [`createStore`](https://deminoth.github.io/redux/api/createStore.html)에 넘길 수 있는 하나의 리듀싱 함수로 바꿔줍니다.
  >
  > 생성된 리듀서는 내부의 모든 리듀서들을 호출하고 결과를 모아서 하나의 상태 객체로 바꿔줍니다. **상태 객체의 형태는 `reducers`로 전달된 키들을 따릅니다**.
  >
  > 결과적으로 상태 객체는 이런 형태가 됩니다:
  >
  > ```
  > {
  >   reducer1: ...
  >   reducer2: ...
  > }
  > ```



============================================================================

### frontend > src > actions> leads.js

* action 폴더에 leads의 http requests를 담당하는 actions들 작성.

* 그 전에 axios 설치

```
npm i axios
```

* > *axios*는 Promise 기반의 자바스크립트 비동기 처리방식을 사용합니다. 그래서 요청후 .then()으로 결과값을 받아서 처리를 하는 형식으로 구성.

#### dispatch

* dispatch an action to our reducer such as GET_LEADS

```js
// http requests
import axios from "axios";

import { GET_LEADS } from "./types";

// GET LEADS
export const getLeads = () => dispatch => {
  axios
    .get("/api/leads/")
    .then(res => {
      // pass in an object with a type
      dispatch({
        type: GET_LEADS,
        payload: res.data
      });
    })
    .catch(err => console.log(err));
};

```

* leads component에서 해당 actions를 call하게 된다.



### frontend > src > components > leads> Leads.js

```js
import React, { Component } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getLeads } from "../../actions/leads";

export class Leads extends Component {
  static propTypes = {
    leads: PropTypes.array.isRequired
  };
  render() {
    return (
      <div>
        <h1>Leads List</h1>
      </div>
    );
  }
}

const mapStateToProps = state => ({
  leads: state.leads.leads
});

export default connect(mapStateToProps)(Leads);

// when the component mounts and the leads come down from the reducer into the component as a prop
// we need to get the state and be able to call this get leads method

```

![map-state](https://github.com/arara90/images/blob/master/Simtime/simtime%20019.png?raw=true)

* 요기에서 생성되었던 state를 이  component의 props에  map한다.
  * this.props.leads

* state.leads (-> we want leads reducers) .leads (-> 노란색 박스안에 있는 그 leads! ) 
  * 즉, reducer.leads



### Redux dev tool에서 state를 확인하면?

![Redux-state](https://github.com/arara90/images/blob/master/Simtime/simtime%20020.png?raw=true)

state에 leads가 있는 것을 확인. 

하지만, 비어있다. 이것은 request만 요청했지 실제로 getleads를 call하지 않았다.

-> props 로부터 해당 method를 call하자

```js
import React, { Component } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getLeads } from "../../actions/leads";

export class Leads extends Component {
  static propTypes = {
    leads: PropTypes.array.isRequired
  };

// 1. add method
  componentDidMount(){
      this.props.getLeads();
  }

  render() {
    return (
      <div>
        <h1>Leads List</h1>
      </div>
    );
  }
}

const mapStateToProps = state => ({
  leads: state.leads.leads
});

// 2. add second parameter
export default connect(mapStateToProps, { getLeads })(Leads);


```

* **connect** : 컴포넌트가 리덕스 상탯값 변경에 반응 하기 위해 connect함수 사용
  * mapStateToProps : 상탯값을 기반으로 컴포넌트에서 **사용할 데이터를 속성값으로 전달**
  * mapDispatchToProps : 리덕스의 상탯값을 변경하는 **함수를 컴포넌트의 속성값으로 전달**



![Result](https://github.com/arara90/images/blob/master/Simtime/simtime%20021.png?raw=true)



### 화면 구성해보기

### src > components > leads > leads.js

```js
import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getLeads } from "../../actions/leads";

export class Leads extends Component {
  static propTypes = {
    leads: PropTypes.array.isRequired
  };

  componentDidMount() {
    this.props.getLeads();
  }

  render() {
    return (
      <Fragment>
        <h2>Leads</h2>
        <table className="table table-striped">
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Email</th>
              <th>Message</th>
              <th />
            </tr>
            <tbody>
              {this.props.leads.map(lead => (
                <tr key={lead.id}>
                  <td>{lead.id}</td>
                  <td>{lead.name}</td>
                  <td>{lead.email}</td>
                  <td>{lead.message}</td>
                  <td>
                    <button className="btn btn-danger btn-sm">Delete</button>
                  </td>
                </tr>
              ))}
            </tbody>
          </thead>
        </table>
      </Fragment>
    );
  }
}

const mapStateToProps = state => ({
  leads: state.leads.leads
});

export default connect(mapStateToProps, { getLeads })(Leads);

// when the component mounts and the leads come down from the reducer into the component as a prop
// we need to get the state and be able to call this get leads ethod

```

![Result2](https://github.com/arara90/images/blob/master/Simtime/simtime%20022.png?raw=true)



### Delete lead를 만들어보자! [3단계]

##### 1. action> lead,type에 DELETE_LEAD 추가

##### 2. reducers에 로직 추가

##### 3. component에 onClick 추가



![Result3](https://github.com/arara90/images/blob/master/Simtime/simtime%20023.png?raw=true)



==================================== result =============================================

#### 1. action> lead,type에 DELETE_LEAD 추가

```js
export const GET_LEADS = "GET_LEADS";
export const DELETE_LEAD = "DELETE_LEAD";
```

```js
import axios from "axios";
import { GET_LEADS, DELETE_LEAD } from "./types";

// GET LEADS
export const getLeads = () => dispatch => {
  axios
    .get("/api/leads/")
    .then(res => {
      // pass in an object with a type
      dispatch({
        type: GET_LEADS,
        payload: res.data
      });
    })
    .catch(err => console.log(err));
};

// DELETE LEAD
export const deleteLead = id => dispatch => {
  axios
    .delete(`/api/leads/${id}/`)
    .then(res => {
      // pass in an object with a type
      dispatch({
        type: DELETE_LEAD,
        payload: id
      });
    })
    .catch(err => console.log(err));
};

```

* 삭제할 id전달
* `${id}`
* payload에 id를 담는다.





#### 2. reducers에 로직 추가

```js
import { GET_LEADS, DELETE_LEAD } from "../actions/types";

const initialState = {
  leads: []
};

export default function(state = initialState, action) {
  switch (action.type) {
    case GET_LEADS:
      return {
        ...state,
        leads: action.payload
      };
    case DELETE_LEAD:
      return {
        ...state,
        leads: state.leads.filter(lead => lead.id !== action.payload)
      };
    default:
      return state;
  }
}
```

* filter 사용

  

#### 3.component에 onClick 추가

```js
import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getLeads, deleteLead } from "../../actions/leads";

export class Leads extends Component {
  static propTypes = {
    leads: PropTypes.array.isRequired
  };

  componentDidMount() {
    this.props.getLeads();
  }

  render() {
    return (
      <Fragment>
        <h2>Leads</h2>
        <table className="table table-striped">
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Email</th>
              <th>Message</th>
              <th />
            </tr>
            <tbody>
              {this.props.leads.map(lead => (
                <tr key={lead.id}>
                  <td>{lead.id}</td>
                  <td>{lead.name}</td>
                  <td>{lead.email}</td>
                  <td>{lead.message}</td>
                  <td>
                    <button
                      onClick={this.props.deleteLead.bind(this, lead.id)}
                      className="btn btn-danger btn-sm"
                    >
                      Delete
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </thead>
        </table>
      </Fragment>
    );
  }
}

const mapStateToProps = state => ({
  leads: state.leads.leads
});

export default connect(mapStateToProps, { getLeads, deleteLead })(Leads);
```

* bind 하는 이유:  https://www.zerocho.com/category/React/post/578232e7a479306028f43393

  this가 window나 undefined가 되기 때문에 확실히 해당 컴포넌트에 bind시켜줘야 lead.id를 제대로 찾을 수 있음.