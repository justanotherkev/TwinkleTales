"use client";
import { useEffect, useState } from "react";
import s from "./button-story.module.css";

export default function ButtonAction(props) {
	const [buttonText, setButtonText] = useState("");
	const [theme, setTheme] = useState("");
	const [enabled, setEnabled] = useState(true);

	const endpoint = "http://localhost:8000/";

	useEffect(() => {
		// speech_input_handler.py reset values
		// resetServer();
		setTheme(props.buttonText);
		if (props.buttonText === '"Adventure"') {
			setButtonText("Tell me an adventure story");
		} else {
			setButtonText(
				"Tell me a " +
					props.buttonText.toLowerCase().replaceAll('"', "") +
					" story"
			);
		}
	}, []);

	// Triggers the speech_prompt_handler.py file to reset it's variables
	const resetServer = async () => {
		try {
			await fetch(endpoint + "reset", {
				method: "GET",
				headers: { "Content-Type": "application/json" },
			});
		} catch (error) {
			console.log(error);
		}
	};

	const handleClick = async () => {
		if (enabled) {
			resetServer();
			setEnabled(false);
			setButtonText("Listening");
			props.setShowDisplay(true);
			props.setAnswers("")
			props.setPrompt("");
			props.setIsError(false);

			let data;

			try {
				// Request sent to speech_prompt_handler.py six times
				// Recieves a response each time containing the prompt and the answers
				for (let i = 0; i < 6; i++) {
					const res = await fetch(
						endpoint +
							"ask_question/" +
							theme.toLowerCase().replaceAll('"', "") +
							"/" +
							i,
						{
							method: "GET",
							headers: { "Content-Type": "application/json" },
						}
					);
					data = await res.json();

					const intervalId = setInterval(() => {
						props.setPrompt(data[0]);
						props.setAnswers(data[1]);
						if (i == 5) {
							props.setAnswersList(data[2]);
						}
						clearInterval(intervalId);
					}, 2500);
				}
				props.setShowDisplay(false);
				setEnabled(true);
				setButtonText(
					"Tell me a " + theme.toLowerCase().replaceAll('"', "") + " story"
				);
			} catch (error) {
				setEnabled(true);
				console.log(error);
				props.setIsError(true);
				props.setPrompt("Oh no! Something went wrong. Please try again later");
				setButtonText(
					"Tell me a " + theme.toLowerCase().replaceAll('"', "") + " story"
				);
			}
		}
	};

	return (
		<button type="button" onClick={handleClick} className={s.link} id="button">
			<div className={enabled ? s.link_button : s.link_button_disabled}>
				{buttonText}
			</div>
		</button>
	);
}
