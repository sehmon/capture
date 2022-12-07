import React, { useEffect, useState } from "react";
import { Link } from 'react-router-dom';
import styled from 'styled-components';

function Root() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/posts')
        .then(response => response.json())
        .then(data => {
          console.log(data)
          setPosts(data)
        });
  }, [])

  navigator.geolocation.getCurrentPosition(function(position) {

    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;
    const altitude = position.coords.altitude;
    const accuracy = position.coords.accuracy;
    const altitudeAccuracy = position.coords.altitudeAccuracy;
    const heading = position.coords.height;
    const speed = position.coords.speed;
    const timestamp = position.timestamp;

    // work with this information however you'd like!
  });

  return (
    <>
      <HomeHeader>
        <h1 >Capture</h1>
        <hr/>
      </HomeHeader>
      <CaptureLink>
        <Link to="/capture">
          <CaptureImage src="shutter.png"/>
        </Link>
      </CaptureLink>
      <PostFeed>
      {
        posts.map((post, i) => 
        <>
        <p><b>{post.img_name}</b></p>
        {
          post.timestamp &&
          <p>{post.timestamp}</p>
        }
        <ImageSquare key={i}>
          {
            post.annotations.map((category, j) => 
            <p>{category}</p>
          )}
        </ImageSquare>
        </>
      )}
    </PostFeed>
    </>
  );
}

const HomeHeader = styled.header`
  position: sticky;
  top: 0;
  width: 100%;
  background-color: white;
`;

const CaptureImage = styled.img`
  width: 100%;
  height: 100%;
`;

const CaptureLink = styled.div`
  position: fixed;
  right: 20px;
  bottom: 20px;
  height: 40px;
  width: 40px;
`;

const PostFeed = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
`

const ImageSquare = styled.div`
  width: 600px;
  height: 600px;
  margin-bottom: 60px;
  border: 1px solid black;
  display: flex;
  flex-direction: column;
  align-items: center;
`

export default Root;