"use client";
import React, { useState } from "react";
import s from "./back-button.module.css";

export default function BackButton(props) {

	// const [loadingAmount, setLoadingAmount] = useState(0)
	
	// const loadingProgress = () => {
	// 	console.log("Increasing...")

	// 		let timer = setInterval(function() {
  //       let increment = Math.random() * 30; // Random increment
	// 			setLoadingAmount(loadingAmount+increment);
  //       if (loadingAmount >= 100) {
  //           setLoadingAmount(100);
  //           console.log("Loading complete!");
  //           clearInterval(timer);
  //       }
  //   }, 2000); 
	// }

	const handleClick = () => {
		props.setPlayMusic(false);
		props.goToPromptPage();
	};

	if (props.enabled) {
		return (
			<button type="button" onClick={handleClick} className={s.link}>
				<div className={s.enabled_link_button}>New Story</div>
			</button>
		);
	} else {
		// loadingProgress()
		return (
			<button type="button" className={s.link}>
				<div className={s.link_button}>
					{/* <small>Creating story...</small> {loadingAmount}% */}
					Creating your <br />
					story...
				</div>
			</button>
		);
	}
}
