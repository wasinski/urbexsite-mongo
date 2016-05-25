import React from 'react';

import HelloWorld from 'components/hello_world';
import Nav from 'components/navbar';


class Home extends React.Component {
    render() {
        return (
            <div>
                <Nav />
                <HelloWorld />
            </div>
        );
    }
}


export default Home;
