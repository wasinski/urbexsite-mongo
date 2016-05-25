import React, { Component, PropTypes } from 'react';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import { loginUser } from 'actions/auth';

import Nav from 'components/navbar';
import {Login} from 'components/login_form';


class LoginView extends Component {
    render() {
        const { dispatch, errorMessage } = this.props;
        return (
            <div>
                <Nav />
                <Login dispatch={dispatch} errorMessage={errorMessage} onLoginClick={loginUser} />
            </div>
        );
    }
}
LoginView.propTypes = {
    dispatch: PropTypes.func.isRequired,
    onLoginClick: PropTypes.func.isRequired,
    isAuthenticated: PropTypes.bool.isRequired,
    errorMessage: PropTypes.string
};

function mapStateToProps(state) {

    const { auth } = state;
    const { isAuthenticated, errorMessage } = auth;

    return {
        isAuthenticated,
        errorMessage
    };
}

export default connect(mapStateToProps)(LoginView);
