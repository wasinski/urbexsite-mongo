import jwtDecode from 'jwt-decode';

import { checkHttpStatus, parseJSON } from 'utils';
import { API_DOMAIN } from 'config.js';

export const LOGIN_REQUEST = 'LOGIN_REQUEST';
export const LOGIN_SUCCESS = 'LOGIN_SUCCESS';
export const LOGIN_FAILURE = 'LOGIN_FAILURE';
export const LOGOUT_SUCCESS = 'LOGOUT_SUCCESS';
export const LOGOUT_REQUEST = 'LOGOUT_REQUEST';


function requestLogin(credentials) {
    return {
        type: LOGIN_REQUEST,
        isFetching: true,
        isAuthenticated: false,
        credentials: credentials
    };
}

function receiveLogin(token) {
    localStorage.setItem('token', token);
    return {
        type: LOGIN_SUCCESS,
        isFetching: false,
        isAuthenticated: true,
        token: token.token
    };
}

function loginError(message) {
    return {
        type: LOGIN_FAILURE,
        isFetching: false,
        isAuthenticated: false,
        message: message
    };
}

function requestLogout() {
    return {
        type: LOGOUT_REQUEST,
        isFetching: true,
        isAuthenticated: true
    };
}

function receiveLogout() {
    return {
        type: LOGIN_SUCCESS,
        isFetching: false,
        isAuthenticated: false
    };
}


export function loginUser(credentials) {
    return (dispatch) => {
        dispatch(requestLogin(credentials));
        return fetch(
            `${ API_DOMAIN }/api-token-auth/`,
            {
                method: 'post',
                // credentials: 'include', FIXME: commented because with it CORS have to have specific domain, not wildcard. 
                headers: {'Accept': 'application/json', 'Content-Type': 'application/json'},
                body: JSON.stringify({email: credentials.email, password: credentials.password})
            }
        ).then(checkHttpStatus)
        .then(parseJSON)
        .then(response => {
            try {
                jwtDecode(response.token);
                dispatch(receiveLogin(response.token));
            } catch (e) {
                dispatch(loginError("Invalid token"));
            }
        }).catch(error => {dispatch(loginError(error.message));});
    };
}


export function logoutUser() {
    return (dispatch) => {
        dispatch(requestLogout());
        localStorage.removeItem('token');
        dispatch(receiveLogout());
    };
}
