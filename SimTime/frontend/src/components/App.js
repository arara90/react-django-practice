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
