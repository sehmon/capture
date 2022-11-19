import React, { useEffect, useState } from "react"
import { Link } from 'react-router-dom';


function Root() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/posts')
        .then(response => response.json())
        .then(data => {
          setPosts(data)
        });
  }, [])

  return (
    <>
      <h1>Capture</h1>
      <Link to="/capture">Capture</Link>
      <h3>Feed</h3>
      <hr/>
      {
        posts.map((post, i) => 
        <div key={i}>
          <p><b>{post.img_name}</b></p>
          {
            post.annotations.map((category, j) => 
            <p>{category}</p>
          )}
          <hr/>
        </div>
      )}
    </>
  );
}

export default Root;