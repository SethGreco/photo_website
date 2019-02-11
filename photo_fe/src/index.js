import React from 'react';
import ReactDOM from 'react-dom';
import 'bootstrap/dist/css/bootstrap.css'
import {
    Row, Col, Card, CardBlock, CardTitle, CardText
} from 'reactstrap';
import './index.css';

//import './index.css';
//import App from './App';
//import * as serviceWorker from './serviceWorker';

class PhotoGallery extends React.Component {
    constructor() {
        super();

        this.state = {
            'photos': []
        }
    }

    componentDidMount() {
        this.getPhotos();
    }

    getPhotos() {
        fetch('http://192.168.56.101:8000/api/images')
            .then(results => results.json())
            .then(results => this.setState({'photos': results}));
    }

    render() {
        return (
            <ul>
                {this.state.photos.map(function (photos, index) {
                        return (
                            <ContentPhoto photos={photos} />

                        )
                    }
                )}
            </ul>
        );
    }
}

class ContentPhoto extends React.Component {
        render() {
            return(
                <Row className="ContentItem">
                    <Col xs="6">
                         <Card>
                             <CardBlock>
                                 <CardTitle>
                                     {this.props.photos.title}
                                 </CardTitle>
                                 <CardText>{this.props.photos.model_pic}</CardText>
                             </CardBlock>
                         </Card>
                    </Col>
                </Row>

            )
        }
}
ReactDOM.render(
    <PhotoGallery />,
    document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: http://bit.ly/CRA-PWA
//serviceWorker.unregister();
