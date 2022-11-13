import logo from './logo.svg';
import './App.css';

import React from 'react';
import Camera from 'react-html5-camera-photo';
import 'react-html5-camera-photo/build/css/index.css';

function App() {

  function handleTakePhoto (dataUri) {
    // Do stuff with the photo...
    console.log('takePhoto');

    const data = new FormData();
    data.append("name", "Image Upload");
    data.append("file_attachment", dataUri)

    // Simple POST request with a JSON body using fetch
    const requestOptions = {
      method: 'POST',
      body: data,
    };
    fetch('http://127.0.0.1:5000/images', requestOptions)
        .then(response => response.json())
        .then(data => console.log(data));
  }

  return (
    <div className="App">
      <Camera
        onTakePhoto = { (dataUri) => { handleTakePhoto(dataUri); } }
      />
    </div>
  );
}

export default App;
