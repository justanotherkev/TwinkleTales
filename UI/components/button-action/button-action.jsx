"use client";
import { useState } from "react";
import s from "./button-action.module.css";

export default function ButtonAction(props) {
	const [buttonText, setButtonText] = useState("Tap to Speak");

	const handleClick = () => {
		if (buttonText === "Tap to Speak") {
			setButtonText("Listening...");
		} else {
			setButtonText("Tap to Speak");
		}
	};

	return (
		<button type="submit" onClick={handleClick} className={s.link}>
			<div className={s.link_button}>{buttonText}</div>
		</button>
	);
}