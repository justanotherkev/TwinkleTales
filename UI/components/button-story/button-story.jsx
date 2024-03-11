"use client";
import { useState } from "react";
import s from "./button-story.module.css";

export default function ButtonAction(props) {
	const [buttonText, setButtonText] = useState("Tell me a story");

	const handleClick = async () => {
		props.setShowDisplay(true);
		props.setIsError(false);
		props.setPrompt("");
		setButtonText("Listening");

		let data;

		try {
			for (let i = -1; i < 5; i++) {
				console.log("Calling: " + i);
				const res = await fetch("http://localhost:8000/", {
					method: "GET",
					headers: { "Content-Type": "application/json" },
				});
				data = await res.json();

				const intervalId = setInterval(() => {
					console.log(i + ". " + data.message[0] + ", " + data.message[1]);
					props.setPrompt(data.message[0]);
					props.setAnswers(data.message[1]);
					clearInterval(intervalId);
				}, 2500);
			}

		} catch (error) {
			props.setIsError(true);
			props.setPrompt("Oh no! Something went wrong. Please try again later");
			setButtonText("Tell me a story");
		}

		props.goToStoryPage(data.message[2]);
	};

	return (
		<button type="button" onClick={handleClick} className={s.link} id="button">
			<div className={s.link_button}>{buttonText}</div>
		</button>
	);
}
