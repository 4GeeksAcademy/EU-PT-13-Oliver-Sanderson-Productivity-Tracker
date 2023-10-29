import React from "react";
import { FilledMediumFilled } from "./FilledMediumFilled";
import { TextLargeText } from "./TextLargeText";
import "./style.css";

export const Navbar = () => {
  return (
    <div className="desktop-top-navbar">
      <div className="logo">
        <div className="brand-name">KorYoku</div>
      </div>
      <FilledMediumFilled
        className="filled-medium-filled-button"
        divClassName="filled-medium-filled-instance"
        text="Sign In"
      />
      <div className="overlap-group">
        <TextLargeText className="text-large-text-button" divClassName="text-large-text-instance" text="Home" />
        <TextLargeText
          className="text-large-text-button-instance"
          divClassName="text-large-text-instance"
          text="About"
        />
        <TextLargeText className="design-component-instance-node" divClassName="text-large-text-2" text="Contact Us" />
        <TextLargeText className="text-large-text-3" divClassName="text-large-text-2" text="Feedback" />
      </div>
    </div>
  );
};
