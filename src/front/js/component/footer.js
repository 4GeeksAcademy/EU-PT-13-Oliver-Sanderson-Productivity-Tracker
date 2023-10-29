import React from "react";
import "./style.css";


const Footer = () => {
    const year = new Date().getFullYear();
  
    return  <div className="desktop-footer">{`Copyright © Your Website ${year}`}
    <p className="item-item-item">
      <span className="text-wrapper">Terms & Conditions</span>
      <span className="span"> | </span>
      <span className="text-wrapper">FAQ's</span>
      <span className="span"> | </span>
      <span className="text-wrapper"> Feedback</span>
    </p>
  </div>
    
  };
  
  export default Footer;

 