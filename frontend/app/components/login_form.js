import React from 'react';
import axios from 'axios';


export class Login extends React.Component {

    render = () => {
        const { errorMessage } = this.props;

        return (
            <div>
                <input type='text' ref='email' className="form-control" style={{ marginRigh: '5px' }} placeholder='Username'/>
                <input type='password' ref='password' className="form-control" style={{ marginRigh: '5px' }} placeholder='Password'/>
                <button onClick={(event) => this.handleClick(event)} className="btn btn-primary">Login</button>
                {errorMessage && <p style={{color: 'red'}}>{errorMessage}</p>}
            </div>
        );
    }

    handleClick = (e, dispatch) => {
        const email = this.refs.email;
        const password = this.refs.password;
        const credentials = { email: email.value.trim(), password: password.value.trim() };
        this.props.dispatch(this.props.onLoginClick(credentials));
        console.log(localStorage.getItem('token'))
    }
}

Login.propTypes = {
    onLoginClick: React.PropTypes.func.isRequired,
    errorMessage: React.PropTypes.string
};
