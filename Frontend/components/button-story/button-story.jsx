"use client";
import { useEffect, useState } from "react";
import s from "./button-story.module.css";

export default function ButtonAction(props) {
	const [buttonText, setButtonText] = useState("Tell me a story");
	const endpoint = "http://localhost:8000/";

	useEffect(() => {
		// speech_input_handler.py reset values
		resetServer();
	}, []);

	// Triggers the speech_prompt_handler.py file to reset it's variables
	const resetServer = async () => {
		try {
			await fetch("http://localhost:8000/reset", {
				method: "GET",
				headers: { "Content-Type": "application/json" },
			});
		} catch (error) {
			console.log(error);
		}
	};

	const handleClick = async () => {
		props.setShowDisplay(true);
		props.setIsError(false);
		props.setPrompt("");
		setButtonText("Listening");

		let data;

		try {
			// Request sent to speech_prompt_handler.py six times
			// Recieves a response each time containing the prompt and the answers
			for (let i = -1; i < 5; i++) {
				console.log("Calling: " + i);
				const res = await fetch(endpoint, {
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

		// Prevents goToStoryPage() from running if undefined values are involved
		// Notifies user of an error on the frontend in the above case
		if (data !== undefined) {
			if (data.message[2] !== undefined) {
				props.goToStoryPage(data.message[2]);
			} else {
				props.setIsError(true);
				props.setPrompt("Oh no! Something went wrong. Please try again later");
				setButtonText("Tell me a story");
			}
		} else {
			props.setIsError(true);
			props.setPrompt("Oh no! Something went wrong. Please try again later");
			setButtonText("Tell me a story");
		}
	};

	return (
		<button type="button" onClick={handleClick} className={s.link} id="button">
			<div className={s.link_button}>{buttonText}</div>
		</button>
	);
}
