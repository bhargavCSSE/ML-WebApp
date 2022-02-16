import React, { Component, Fragment } from "react";
import ReactDOM from "react-dom";

import Header from "./layout/Header.js";
import Dashboard from "./leads/Dashboard.js";

class App extends Component {
  render() {
    return (
      <Fragment>
        <Header />
        <div className="container">
          <Dashboard />
        </div>
      </Fragment>
    );
  }
}

ReactDOM.render(<App />, document.getElementById("app"));
