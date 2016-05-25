import React from 'react';
import ReactDOM from 'react-dom';
import { createStore, applyMiddleware } from 'redux';
import { Provider } from 'react-redux';
import thunkMiddleware from 'redux-thunk';
import combinedReducer from 'reducers';

import Routes from './routes';

// TODO: add api to middleware
let createStoreWithMiddleware = applyMiddleware(thunkMiddleware)(createStore);
let store = createStoreWithMiddleware(combinedReducer);

ReactDOM.render(<Provider store={store}><Routes /></Provider>, document.getElementById('app'));
