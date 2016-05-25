import { LOGIN_REQUEST, LOGIN_SUCCESS, LOGIN_FAILURE, LOGOUT_SUCCESS } from 'actions/auth';

const initialState = {
    isFetching: false,
    isAuthenticated: localStorage.getItem('token') ? true : false,
    errorMessage: ''
};

export function authReducer(state=initialState, action) {
    switch (action.type) {
    case LOGIN_REQUEST:
        return Object.assign({}, state, {
            isFetching: true,
            isAuthenticated: false,
            user: action.credentials
        });
    case LOGIN_SUCCESS:
        return Object.assign({}, state, {
            isFetching: false,
            isAuthenticated: true,
            errorMessage: ''
        });
    case LOGIN_FAILURE:
        return Object.assign({}, state, {
            isFetching: false,
            isAuthenticated: false,
            errorMessage: action.message
        });
    case LOGOUT_SUCCESS:
        return Object.assign({}, state, {
            isFetching: false,
            isAuthenticated: false
        });
    default:
        return state;
    }
}
