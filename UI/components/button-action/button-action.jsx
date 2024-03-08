"use client";
import { useState } from "react";
import s from "./button-action.module.css";

export default function ButtonAction(props) {
	const [buttonText, setButtonText] = useState("Tell me a story");

	const handleClick = async () => {
		props.setShowDisplay(true);
		setButtonText("Listening");

		let data;

		setTimeout(function () {
			props.setPrompt(
				"So tell me, what is the name of your character in today's story?"
			);
		}, 2500);

		try {
			for (let i = 0; i < 6; i++) {
				const res = await fetch("http://localhost:8000/", {
					method: "GET",
					headers: { "Content-Type": "application/json" },
				});
				data = await res.json();
				setTimeout(function () {
					console.log(data.message[0]);
					console.log(data.message[1]);
					props.setPrompt(data.message[0]);
					props.setAnswers("You said: " + data.message[1]);
				}, 2500);
			}

			// console.log(data.message[0].name);

			// setButtonText(data.message);
		} catch (error) {
			props.setPrompt("Oh no! Something went wrong. Please try again later");
		}

		while (true) {
			props.setPrompt();
		}
	};

	return (
		<button type="button" onClick={handleClick} className={s.link} id="button">
			<div className={s.link_button}>{buttonText}</div>
		</button>
	);
}