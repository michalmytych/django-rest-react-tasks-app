import React from 'react';



export default function Nav(props) {
  const logged_out_nav = (
    <ul>
      <li
        className="btn" 
        onClick={() => props.display_form('login')}>Zaloguj się</li>
      <li
        className="btn" 
        onClick={() => props.display_form('signup')}>Zarejestruj się</li>
    </ul>
  );

  const logged_in_nav = (
    <ul>
      <li
        className="btn" 
        onClick={props.handle_logout}>Wyloguj się</li>
    </ul>
  );
  return <div>{props.logged_in ? logged_in_nav : logged_out_nav}</div>;
}
