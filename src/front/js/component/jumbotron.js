import React from "react";
import { MockupSaas } from "mockupSaas.js";
import { ElevatedMedium } from "elevatedmedium.js";
import { OpenSansMontserrat } from "openSansMontserrat.js";
import "./style.css";

export const Jumbotron = () => {
  return (
    <div className="description">
      <div className="overlap-group">
        <OpenSansMontserrat
          text=""
          text1="Stay organized, focused, and achieve more with our powerful productivity web app. Take control of your tasks, conquer your goals. Utilize your time wisely."
        />
        <p className="p">Enhance Productivity and Achieve Greater Efficiency</p>
        <ElevatedMedium
          text="Create an Account"
        />
        <div className="ellipse" />
        <div className="rectangle-2" />
        <MockupSaas
          rectangle="https://c.animaapp.com/32oA29eJ/img/rectangle-21-1.png"
        />
      </div>
    </div>
  );
};