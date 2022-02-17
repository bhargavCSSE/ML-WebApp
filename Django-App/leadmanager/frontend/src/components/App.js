import React, { Component, Fragment } from "react";
import ReactDOM from "react-dom";

import Header from "./layout/Header.js";
import Dashboard from "./leads/Dashboard.js";

import { Provider } from "react-redux";
import store from "../store.js";

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

ReactDOM.render(<App />, document.getElementById("app"));
