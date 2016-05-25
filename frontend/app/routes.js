import React from 'react';
import { Router, Route, browserHistory } from 'react-router';

import Home from 'containers/home';
import Login from 'containers/login';


class Routes extends React.Component {
    render () {
        return (
            <Router history={browserHistory}>
                <Route path="/" component={Home} />
                <Route path="/login" component={Login} />
            </Router>
        );
    }
}


export default Routes;
