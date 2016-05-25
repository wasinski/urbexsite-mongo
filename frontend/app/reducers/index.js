import { combineReducers } from 'redux';

import { authReducer } from './auth';


const shoppingListApp = combineReducers({
    auth: authReducer
});


export default shoppingListApp;
