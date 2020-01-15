### components > leads > Form.js

```js
import React, { Component } from "react";

export class Form extends Component {
  state = {
    name: "",
    email: "",
    message: ""
  };

  onChange = e => this.setState({ [e.target.name]: e.target.value });
  onSubmit = e => {
    e.preventDefault();
    console.log("submit");
  };

  render() {
    const { name, email, message } = this.state;
    return (
      <div className="card card-body mt-4 mb-4">
        <h2>ADD Lead</h2>
        <form onSubmit={this.onSubmit}>
          <div className="form-group">
            <label>Name</label>
            <input
              className="form-control"
              type="text"
              name="name"
              onChange={this.onChange}
              value={name}
            />
          </div>
          <div className="form-group">
            <label>Email</label>
            <input
              className="form-control"
              type="email"
              name="email"
              onChange={this.onChange}
              value={email}
            />
          </div>
          <div className="form-group">
            <label>Message</label>
            <input
              className="form-control"
              type="text"
              name="message"
              onChange={this.onChange}
              value={message}
            />
          </div>
          <div className="form-group">
            <button type="submit" className="btn btn-primary">
              Submit
            </button>
          </div>
        </form>
      </div>
    );
  }
}

export default Form;

```



![form](https://github.com/arara90/images/blob/master/Simtime/simtime%20024.png?raw=true)



하지만 add 후에 자동으로 Leads 목록이 갱신되지 않았다. 

addLead라는 action을 만들고, server를 update해서 갱신시키도록 해보자!

이를 통해서 state를 sharing하는 것이 얼마나 helpful한지 알 수 있을 것이다. 

Let's  go!



#### 1. action > leads.js

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
    .catch(err => console.log(err));
};
```

* type.js에도 추가하기



#### 2. reducer 수정하기

```js
    case ADD_LEAD:
      return {
        ...state,
        leads: [...state.leads, action.payload]
      };
```



#### 3. Form components에 connect 및 import

```js
import React, { Component } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types"; //impt + tab
import { addLead } from "../../actions/leads";
//...

// ...
export default connect(null, { addLead })(Form);
// cf. export default connect(mapStateToProps, { getLeads, deleteLead })(Leads); 
```

* Lead에서는 Leads를 다시 불러와야했지만, Form에서는 다시 불러올 필요가 없기 때문에 mapStateToProps 없이 action만 전달하면 된다. (?!)