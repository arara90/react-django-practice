# (React) Auth_State&Private_Routes

* 유투브 강의 : [Traversy Media - Full Stack React & Django [6] - Auth State & Private Routes](https://youtu.be/EmAc4wQikwY?list=PLillGF-RfqbbRA-CIUxlxkUpbq0IFkX60)



##### UI

##### ROUTER

##### State에 Auth 정보 담아 관리하기

##### redirects





#### react-router-dom 설치

```
npm i react-router-dom
```



### UI

##### frontend > src > components > layout > Login.js

```js
import React, { Component } from "react";
import { Link } from "react-router-dom";

export class Login extends Component {
  state = {
    username: "",
    password: ""
  };

  onSubmit = e => {
    e.preventDefault();
    console.log("submit");
  };

  onChange = e => this.setState({ [e.target.name]: e.target.value });

  render() {
    const { username, password } = this.state;
    return (
      <div className="col-md-6 m-auto">
        <div className="card card-body mt-5">
          <h2 className="text-center">Login</h2>
          <form onSubmit={this.onSubmit}>
            <div className="form-group">
              <label>Username</label>
              <input
                type="text"
                className="form-control"
                name="username"
                onChange={this.onChange}
                value={username}
              />
            </div>

            <div className="form-group">
              <label>Password</label>
              <input
                type="password"
                className="form-control"
                name="password"
                onChange={this.onChange}
                value={password}
              />
            </div>

            <div className="form-group">
              <button type="submit" className="btn btn-primary">
                Login
              </button>
            </div>
            <p>
              Don't have an account? <Link to="/register">Register</Link>
            </p>
          </form>
        </div>
      </div>
    );
  }
}

export default Login;

```



##### frontend > src > components > layout > Register.js

```js
import React, { Component } from "react";
import { Link } from "react-router-dom";

export class Register extends Component {
  state = {
    username: "",
    email: "",
    password: "",
    password2: ""
  };

  onSubmit = e => {
    e.preventDefault();
    console.log("submit");
  };

  onChange = e => this.setState({ [e.target.name]: e.target.value });

  render() {
    const { username, email, password, password2 } = this.state;
    return (
      <div className="col-md-6 m-auto">
        <div className="card card-body mt-5">
          <h2 className="text-center">Register</h2>
          <form onSubmit={this.onSubmit}>
            <div className="form-group">
              <label>Username</label>
              <input
                type="text"
                className="form-control"
                name="username"
                onChange={this.onChange}
                value={username}
              />
            </div>
            <div className="form-group">
              <label>Email</label>
              <input
                type="email"
                className="form-control"
                name="email"
                onChange={this.onChange}
                value={email}
              />
            </div>
            <div className="form-group">
              <label>Password</label>
              <input
                type="password"
                className="form-control"
                name="password"
                onChange={this.onChange}
                value={password}
              />
            </div>
            <div className="form-group">
              <label>Confirm Password</label>
              <input
                type="password"
                className="form-control"
                name="password2"
                onChange={this.onChange}
                value={password2}
              />
            </div>
            <div className="form-group">
              <button type="submit" className="btn btn-primary">
                Register
              </button>
            </div>
            <p>
              Already have an account? <Link to="/login">Login</Link>
            </p>
          </form>
        </div>
      </div>
    );
  }
}

export default Register;

```



##### frontend > src > components > layout > Header.js

```js
import React, { Component } from "react";
import { Link } from "react-router-dom";

export class Header extends Component {
  render() {
    return (
      <nav className="navbar navbar-expand-sm navbar-light bg-light">
        <div className="container">
          <button
            className="navbar-toggler"
            type="button"
            data-toggle="collapse"
            data-target="#navbarTogglerDemo01"
            aria-controls="navbarTogglerDemo01"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarTogglerDemo01">
            <a className="navbar-brand" href="#">
              Lead Manager
            </a>
            <ul className="navbar-nav mr-auto mt-2 mt-lg-0">
              <li className="nav-item">
                <Link to="/register" className="nav-link">
                  Register
                </Link>
              </li>
              <li className="nav-item">
                <Link to="/login" className="nav-link">
                  Login
                </Link>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    );
  }
}

export default Header;

```



#### UI - App Main

##### frontend > src > components > App.js

```js
//...
import ReactDom from "react-dom";
import {
  HashRouter as Router,
  Route,
  Switch,
  Redirect
} from "react-router-dom";

import Header from "./layout/Header";
import Login from "./accounts/Login";
import Register from "./accounts/Register";
import PrivateRoute from "./common/privateRoute";
//..


//..
class App extends Component {
  render() {
    return (
      <Provider store={store}>
        <AlertProvider template={AlertTemplate} {...alertOptions}>
          <Router>
            <Fragment>
              <Header />
              <Alerts />
              <div className="container">
                <Switch>
                  {/* <Router exact path="/" component={Dashboard} />
                  <Router exact path="/register" component={Register} />
                  <Router exact path="/login" component={Login} /> */}
                  <PrivateRoute exact path="/" component={Dashboard} />
                  <Router exact path="/register" component={Register} />
                  <Router exact path="/login" component={Login} />
                </Switch>
              </div>
            </Fragment>
          </Router>
        </AlertProvider>
      </Provider>
    );
  }
}

// templates/index.html에 있는 id ='app' 요소를 찾아서 App을 render해준다.
ReactDom.render(<App />, document.getElementById("app"));

```



### State로 Auth 관리

##### frontend > src  > reducers > auth.js

```js
const initialState = {
  token: localStorage.getItem("token"),
  isAuthenticated: null, // Once we login or load the user, this will get turn true.
  isLoading: false, // When we make a request, It will be 'true'
  user: null
};

export default function(state = initialState, action) {
  switch (action.type) {
    default:
      return state;
  }
}

```

```js
// index.js
import { combineReducers } from "redux";
import leads from "./leads";
import errors from "./errors";
import messages from "./messages";
import auth from "./auth";

export default combineReducers({
  leads,
  errors,
  messages,
  auth
});

```

![authInState](https://github.com/arara90/images/blob/master/Simtime/simtime%20043.png?raw=true)



### privateRoute

* Check to see if the user is logged in.

##### frontend > src > components > common > privateRoute.js

```js
import React from "react";
import { Route, Redirect } from "react-router-dom";
import { connect } from "react-redux";

const PrivateRoute = ({ component: Component, auth, ...rest }) => {
  return (
    <Route
      {...rest}
      render={props => {
        if (auth.isLoading) {
             // Between firing or the action and getting response from the request, It's gonna be in this loading State. 
          return <h2>Loading</h2>;
        } else if (!auth.isAuthenticated) {
            // Checking
          return <Redirect to="/login" />;
        } else {
          return <Component {...props}></Component>;
        }
      }}
    />
  );
};

const mapStateToProps = state => ({
  auth: state.auth
});

export default connect(mapStateToProps)(PrivateRoute);

```





### Action

#### load-user-actions

* Why? REST API는 stateless하기 떄문에 유저가 로그인 한 상태인지 지속적으로  체크해야한다. 

  즉, component가 로드될 대마다 체크한다.

> **Stateless**?
>
> **REST(Representational State Transfer) API**는 HTTP의 특성을 이용하기 때문에 stateless(무상태성)을 갖는다. 즉, 서버에 어떤 작업을 하기 위해 상태정보를 기억할 필요가 없고, 들어온 요청에 대해 처리만 해준다.

* load user 액션은 auth API에 token과 함께 auth user를 요청하고, isAuthenticated를 결정한다.



##### 1. action > type.js

$$

$$

```js
export const USER_LOADING = "USER_LOADING";
export const USER_LOADED = "USER_LOADED";
export const AUTH_ERROR = "AUTH_ERROR";
```



##### 2. reducers > auth.js

```js
import { USER_LOADING, USER_LOADED, AUTH_ERROR } from "../actions/types";

const initialState = {
  token: localStorage.getItem("token"),
  isAuthenticated: null,
  isLoading: false,
  user: null
};

export default function(state = initialState, action) {
  switch (action.type) {
    case USER_LOADING:
      return {
        ...state,
        isLoading: true
      };
    case USER_LOADED:
      return {
        ...state,
        isAuthenticated: true,
        isLoading: false,
        user: action.payload
      };
    case AUTH_ERROR:
      localStorage.removeItem("token");
      return {
        ...state,
        token: null,
        user: null,
        isAuthenticated: false,
        isLoading: false
      };

    default:
      return state;
  }
}

```



##### 3. actions > auth.js

```js
import axios from "axios";
import { returnErrors } from "./messages";
import { USER_LOADED, USER_LOADING, AUTH_ERROR } from "./types";

// CHECK  THE TOKEN & LOAD USER
export const loadUser = () => (dispatch, getState) => {
  // User Loading
  dispatch({ type: USER_LOADING });

  // Get Token from state
  const token = getState().auth.token;

  // Haders
  const config = {
    headers: {
      "Content-Type": "application/json"
    }
  };

  // If token, add to headers config
  if (token) {
    config.headers["Authorization"] = `Token ${token}`;
  }

  //
  axios
    .get("/api/auth/user", config)
    .then(res => {
      dispatch({
        type: USER_LOADED,
        payload: res.data
      });
    })
    .catch(err => {
      dispatch(returnErrors(err.response.data, err.response.status));
      dispatch({
        type: AUTH_ERROR
      });
    });
};

```



##### 5. App.js

```js
// loadUser 추가
import store from "../store";
import { loadUser } from "../actions/auth";

//...
class App extends Component {
  componentDidMount(){
    store.dispatch(loadUser());
  }

```

