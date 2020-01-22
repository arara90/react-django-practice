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
      // const errors = {
      //   msg: err.response.data,
      //   status: err.response.status
      // };

      // dispatch({
      //   type: GET_ERRORS,
      //   payload: errors
      // });
      dispatch(
        returnErrors(
          err.response.data, //message from the server
          err.response.status
        )
      );
    });
};
