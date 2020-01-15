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
