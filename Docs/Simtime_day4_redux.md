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

* Provider를 통해 감싼 하위 요소들이 store에 접근할 수 있다.

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