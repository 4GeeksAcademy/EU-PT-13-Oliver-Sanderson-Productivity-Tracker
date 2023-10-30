import React from "react";
import "./OpenSansMontserrat.css";

export const OpenSansMontserrat = ({ text, text1 }) => {
  return (
    <div className="open-sans-montserrat">
      <h2>{text}</h2>
      <p>{text1}</p>
    </div>
  );
};