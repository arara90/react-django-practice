# (React) Auth_State&Private_Routes

* 유투브 강의 : [Full Stack React & Django [7] - Frontend Authentication](https://youtu.be/kfpY5BsIoFg?list=PLillGF-RfqbbRA-CIUxlxkUpbq0IFkX60)

![authInState](https://github.com/arara90/images/blob/master/Simtime/simtime%20045.png?raw=true)



### Log-in User

#### Actions

##### 1. type.js

```js
export const LOGIN_SUCCESS = "LOGIN_SUCCESS";
export const LOGIN_FAIL = "LOGIN_FAIL";
```



##### 2. auth.js 

* axios**.post** 로 수정하는거 잊지 않기. (입력한 정보를 보내서 token을 res로 받아와야하므로)

* Login은 token을 Get하는 것이므로, CHECK TOKEN에서 처럼 getState가 필요없다.

  

```js
// LOGIN USER
export const login = (username, password) => dispatch => {
  const config = {
    // Haders
    headers: {
      "Content-Type": "application/json"
    }
  };

  // Request Body
  const body = JSON.stringify({ username, password });

  axios
    .post("/api/auth/login", body, config)
    .then(res => {
      dispatch({
        type: USER_SUCCESS,
        payload: res.data
      });
    })
    .catch(err => {
      dispatch(returnErrors(err.response.data, err.response.status));
      dispatch({
        type: LOGIN_FAIL
      });
    });
};

```



#### Reducer

##### 1. auth.py

```js
 case LOGIN_SUCCESS:
      //set token
      localStorage.setItem("token", action.payload.token);
      return {
        ...state,
        ...action.payload,
        isAuthenticated: true,
        isLoading: false
      };

    case AUTH_ERROR:
    case LOGIN_FAIL:
      localStorage.removeItem("token");
      return {
        ...state,
        token: null,
        user: null,
        isAuthenticated: false,
        isLoading: false
      };
```



#### Components

##### Login.js

```js
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { login } from "../../actions/auth";

//...

static propTypes = {
    login: PropTypes.func.isRequired,
    isAuthenticated: PropTypes.bool
  };

  onSubmit = e => {
    e.preventDefault();
    this.props.login(this.state.username, this.state.password);
  };


//...
const mapStateToProps = state => ({
  isAuthenticated: state.auth.isAuthenticated
});
export default connect(mapStateToProps, { login })(Login);

```





### Log-out

#### Component

##### 1. Header

```js
import { connect } from "react-redux";
import PropTypes from 'prop-types'
import { logout } from "../../actions/auth";

//...
export class Header extends Component {
  static propType = {
    auth: PropTypes.object.isRequired,
    logout: PropTypes.func.isRequired
  };

  render() {
    const { isAuthenticated, user } = this.props.auth;
    const gusetLinks = (
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
    );

    const authLinks = (
      <ul className="navbar-nav mr-auto mt-2 mt-lg-0">
        <span className="navbar-text mr-3">
          <strong>{user ? `Welcome ${user.username}` : ""}</strong>
        </span>
        <li className="nav-item">
          <button
            onClick={this.props.logout}
            className="nav-link btn btn-info btn-sm text-light"
          >
            Logout
          </button>
        </li>
      </ul>
    );
    
    return (
       <nav className="navbar navbar-expand-sm navbar-light bg-light">
        <div className="container">
       
        //...//

         	<div className="collapse navbar-collapse" id="navbarTogglerDemo01">
            	<a className="navbar-brand" href="#">
              	Lead Manager
            	</a>
          	</div>
          {isAuthenticated ? authLinks : gusetLinks}
        </div>
      </nav>
    );
  }
}

const mapStateToProps = state => ({
  auth: state.auth
});
export default connect(mapStateToProps, { logout })(Header);


```



#### action

##### 1. type.js

```js
export const LOGOUT = "LOGOUT";
```



##### 2. auth.js

```js
// LOGOUT
export const logout = () => (dispatch, getState) => {
  const token = getState().auth.token; // Get Token from state

  const config = {
    // Haders
    headers: {
      "Content-Type": "application/json"
    }
  };

  // If token, add to headers config
  if (token) {
    config.headers["Authorization"] = `Token ${token}`;
  }

  axios
    .post("/api/auth/logout", null, config)
    .then(res => {
      dispatch({
        type: LOGOUT
      });
    })
    .catch(err => {
      dispatch(returnErrors(err.response.data, err.response.status));
    });
};
};

```



#### Reducer

```js
case AUTH_ERROR:
    case LOGIN_FAIL:
    case REGISTER_FAIL:
    case LOGOUT:
      localStorage.removeItem("token");
      return {
        ...state,
        token: null,
        user: null,
        isAuthenticated: false,
        isLoading: false
      };

```



### Incorrect Credential

* 잘못 입력한 경우 다음과 같은 에러 메세지를 확인할 수 있음.

  ![incorrectCredential](https://github.com/arara90/images/blob/master/Simtime/simtime%20045.png?raw=true)

  

#### component

##### Alerts.js

```js
     if (error.msg.non_field_errors)
        alert.error(error.msg.non_field_errors.join());
```

![incorrectCredential](https://github.com/arara90/images/blob/master/Simtime/simtime%20047.png?raw=true)





### Register

#### action

##### 1.type.js

```js
export const REGISTER_SUCCESS = "REGISTER_SUCCESS";
export const REGISTER_FAIL = "REGISTER_FAIL";
```



##### 2.auth.js

```js

// REGISTER USER
export const register = ({ username, email, password }) => dispatch => {
  const config = {
    // Haders
    headers: {
      "Content-Type": "application/json"
    }
  };

  // Request Body
  const body = JSON.stringify({ username, email, password });

  axios
    .post("/api/auth/register", body, config)
    .then(res => {
      dispatch({
        type: REGISTER_SUCCESS,
        payload: res.data
      });
    })
    .catch(err => {
      dispatch(returnErrors(err.response.data, err.response.status));
      dispatch({
        type: REGISTER_FAIL
      });
    });
};
```



#### reducer

##### auth.js

```js
import {
  USER_LOADING,
  USER_LOADED,
  AUTH_ERROR,
  LOGIN_SUCCESS,
  LOGIN_FAIL,
  REGISTER_SUCCESS,
  REGISTER_FAIL,
  LOGOUT
} from "../actions/types";

case LOGIN_SUCCESS:
case REGISTER_SUCCESS:
      //set token
      localStorage.setItem("token", action.payload.token);
      return {
        ...state,
        ...action.payload,
        isAuthenticated: true,
        isLoading: false
      };
      
 case AUTH_ERROR:
    case LOGIN_FAIL:
    case REGISTER_FAIL:
    case LOGOUT:
      localStorage.removeItem("token");
      return {
        ...state,
        token: null,
        user: null,
        isAuthenticated: false,
        isLoading: false
      };

```



#### component

##### Register

```js
import { Link, Redirect } from "react-router-dom";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { register } from "../../actions/auth";
import { createMessage } from "../../actions/messages";


export class Register extends Component {
  state = {
    username: "",
    email: "",
    password: "",
    password2: ""
  };

  static propTypes = {
    register: PropTypes.func.isRequired,
    isAuthenticated: PropTypes.bool
  };

  onSubmit = e => {
    e.preventDefault();
    const { username, email, password, password2 } = this.state;
    if (password !== password2) {
      this.props.createMessage({ passwordsNotMatch: "Passwords do not match" });
    } else {
      const newUser = {
        username,
        email,
        password
      };
      this.props.register(newUser);
    }
  };

  onChange = e => this.setState({ [e.target.name]: e.target.value });

  render() {
    if(this.props.isAuthenticated){
      return <Redirect to ="/" />;
    }
    const { username, email, password, password2 } = this.state;
    
      //...
      
      

const mapStateToProps = state => ({
  isAuthenticated: state.auth.isAuthenticated
});
export default connect(mapStateToProps, { register, createMessage })(Register);

```



##### Alerts.js

```js
  componentDidUpdate(prevProps) {
    const { error, alert, message } = this.props;
    if (error !== prevProps.error) {
      //...exist username
      if (error.msg.username) alert.error(error.msg.username.join());
	  //...

    if (message !== prevProps.message) {
      //.. not matched passwords
      if (message.passwordsNotMatch) alert.error(message.passwordsNotMatch);
    }
  }
```

![notmatchedpasswords](https://github.com/arara90/images/blob/master/Simtime/simtime%20048.png?raw=true)

![notmatchedpasswords2](https://github.com/arara90/images/blob/master/Simtime/simtime%20049.png?raw=true)



![username1](https://github.com/arara90/images/blob/master/Simtime/simtime%20050.png?raw=true)

![username2](https://github.com/arara90/images/blob/master/Simtime/simtime%20051.png?raw=true)







### End-point (leads)에 Auth 전달하기.

![401error](https://github.com/arara90/images/blob/master/Simtime/simtime%20052.png?raw=true)

위와 같은 401 (Unauthorized) 에러를 해결하기 위해, token정보를 leads에 공유전달하자.



#### action

##### auth.js

* token을 가져오는 공통 로직을 정리해서 export 만들어 준다.
* CHECKTOKEN과 LOGOUT에 중복된 코드도 깔끔하게 정리할 수 있게 됐다.

```js
// Setup Config with token - helper
export const tokenConfig = getState => {
  const token = getState().auth.token; // Get Token from state
  const config = {
    // Haders
    headers: {
      "Content-Type": "application/json"
    }
  };

  // If token, add to headers config
  if (token) {
    config.headers["Authorization"] = `Token ${token}`;
  }

  return config;
};


// CHECK  THE TOKEN & LOAD USER
export const loadUser = () => (dispatch, getState) => {
  dispatch({ type: USER_LOADING }); // User Loading

  axios
    .get("/api/auth/user", tokenConfig(getState))
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


// LOGOUT
export const logout = () => (dispatch, getState) => {
  axios
    .post("/api/auth/logout", null, tokenConfig(getState))
    .then(res => {
      dispatch({
        type: LOGOUT
      });
    })
    .catch(err => {
      dispatch(returnErrors(err.response.data, err.response.status));
    });
};

```



##### leads.js

* tokenConfig를 import해서 request에 담아 보내기 위해 다음과 같이 수정. 

  > getLeads = () => (dispatch, getState) => {..
  >
  > ​	axios
  >
  > ​	.get("/api/leads/", tokenConfig(getState))
  >
  > }
  >
  > 

```js
// http requests
import axios from "axios";
import { createMessage, returnErrors } from "./messages";
import { tokenConfig } from "./auth";

import {
  GET_LEADS,
  DELETE_LEAD,
  ADD_LEAD,
  GET_ERRORS,
  CREATE_MESSAGE
} from "./types";

// GET LEADS
export const getLeads = () => (dispatch, getState) => {
  axios
    .get("/api/leads/", tokenConfig(getState))
    .then(res => {
      // pass in an object with a type
      dispatch({
        type: GET_LEADS,
        payload: res.data
      });
    })
    .catch(err =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};

// DELETE LEAD
export const deleteLead = id => (dispatch, getState) => {
  axios
    .delete(`/api/leads/${id}/`, tokenConfig(getState))
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

// ADD LEAD
export const addLead = lead => (dispatch, getState) => {
  axios
    .post(`/api/leads/`, lead, tokenConfig(getState))
    .then(res => {
      // pass in an object with a type
      dispatch({
        type: ADD_LEAD,
        payload: res.data
      });

      dispatch(createMessage({ addLead: "Lead Added" }));
    })
    .catch(err => {
      dispatch(
        returnErrors(
          err.response.data, //message from the server
          err.response.status
        )
      );
    });
};


```



![nomore401error](https://github.com/arara90/images/blob/master/Simtime/simtime%20053.png?raw=true)







### 완성!

![nomore401error](https://github.com/arara90/images/blob/master/Simtime/simtime%20054.png?raw=true)



User별로 다른 leads를 확인할 수 있게 되었다!

