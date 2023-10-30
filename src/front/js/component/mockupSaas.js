import PropTypes from "prop-types";
import React from "react";
import "./style.css";

export const MockupSaas = ({ className, rectangleClassName, rectangle = "rectangle-21.png" }) => {
  return (
    <div className={`mockup-saas ${className}`}>
      <img className={`rectangle ${rectangleClassName}`} alt="Rectangle" src={rectangle} />
    </div>
  );
};

MockupSaas.propTypes = {
  rectangle: PropTypes.string,
};