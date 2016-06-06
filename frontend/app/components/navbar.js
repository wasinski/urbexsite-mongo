import React from 'react';
import { Link } from 'react-router';


class Nav extends React.Component {
    render() {
        return (
            <div>
            <h1>Urbex Site</h1>
                <ul role="nav">
                    <li><NavLink to="/">Home</NavLink></li>
                    <li><NavLink to="/login">Login</NavLink></li>
                </ul>
                {this.props.children}
            </div>
        );
    }
}

class NavLink extends React.Component {
    render() {
        return <Link {...this.props} activeClassName="active" />;
    }
}


export default Nav;
