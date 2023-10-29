import React from "react";
import { ElevatedMedium } from "../../component/ElevatedMedium";
import { MockupSaas } from "../../component/MockupSaas";
import { OpenSansMontserrat } from "../../component/OpenSansMontserrat";
import "./style.css";

export const Jumbotron = () => {
  return (
    <div className="description">
      <div className="overlap-group">
        <OpenSansMontserrat
          className="open-sans-montserrat-instance"
          embraceLifeSClassName="open-sans-montserrat-2"
          hasDiv={false}
          hasItSABigWorldOut={false}
          hasStyles={false}
          itSABigWorldOutClassName="design-component-instance-node"
          text=""
          text1="Stay organized, focused, and achieve more with our powerful productivity web app. Take control of your tasks, conquer your goals. Utilize your time wisely."
        />
        <p className="p">Enhance Productivity and Achieve Greater Efficiency</p>
        <ElevatedMedium
          className="elevated-medium-elevated-button"
          divClassName="elevated-medium-instance"
          leftIcon={false}
          rightIcon={false}
          states="default"
          text="Create an Account"
        />
        <div className="ellipse" />
        <div className="rectangle-2" />
        <MockupSaas
          className="mockup-saas-instance"
          rectangle="https://c.animaapp.com/32oA29eJ/img/rectangle-21-1.png"
          rectangleClassName="mockup-saas-2"
        />
      </div>
    </div>
  );
};
