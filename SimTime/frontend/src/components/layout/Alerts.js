import React, { Component, Fragment } from "react";
import { withAlert } from "react-alert";
import { connect } from "react-redux";
import PropTypes from "prop-types";

export class Alerts extends Component {
  static propTypes = {
    error: PropTypes.object.isRequired,
    message: PropTypes.object.isRequired
  };

  // when we get a new prop such as the error, then this is gonna be run.
  componentDidUpdate(prevProps) {
    const { error, alert, message } = this.props;
    if (error !== prevProps.error) {
      if (error.msg.name) alert.error(`Name: ${error.msg.name.join()}`);
      if (error.msg.email) alert.error(`Email: ${error.msg.email.join()}`);
      if (error.msg.message)
        alert.error(`Message: ${error.msg.message.join()}`);
      if (error.msg.username) alert.error(error.msg.username.join());
      if (error.msg.non_field_errors)
        alert.error(error.msg.non_field_errors.join());
    }

    if (message !== prevProps.message) {
      if (message.deleteLead) alert.success(message.deleteLead);
      if (message.addLead) alert.success(message.addLead);
      if (message.passwordsNotMatch) alert.error(message.passwordsNotMatch);
    }
  }

  render() {
    return <Fragment />;
  }
}

const mapStateToProps = state => ({
  error: state.errors, // the reducer that we want
  message: state.messages
});

export default connect(mapStateToProps)(withAlert()(Alerts));
// It should be 'export default withAlert()(Alerts)' if you are using react-alert version 6.0.0
// otherwise  withAlert(Alerts);
