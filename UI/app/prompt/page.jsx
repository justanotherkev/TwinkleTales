"use client";

import ButtonStory from "@/components/button-story/button-story";
import PageComponent2 from "@/components/page-component-2/page-component-2.jsx";
import s from "./page.module.css";
import { useState } from "react";

export default function Prompt() {
	const [prompt, setPrompt] = useState("");
	const [answers, setAnswers] = useState("");
	const [showDisplay, setShowDisplay] = useState(false);

	if (showDisplay) {
		const promptDisplay = document.getElementById("prompt");
		promptDisplay.style.maxHeight = "fit-content";
		promptDisplay.style.padding = "25px 10px";
		promptDisplay.style.color = "black";

		const answersDisplay = document.getElementById("answers");
		answersDisplay.style.maxHeight = "fit-content";
		answersDisplay.style.padding = "25px 10px";
		answersDisplay.style.color = "black";
	}

	return (
		<PageComponent2
			src={"/story-prompt-img.png"}
			component={
				<div className={s.container}>
					<div className={s.prompt} id="prompt">
						{prompt}
					</div>
					<ButtonStory
						setPrompt={setPrompt}
						setAnswers={setAnswers}
						setShowDisplay={setShowDisplay}
					/>
					<div className={s.answers} id="answers">
						{answers}
					</div>
				</div>
			}
		/>
	);
}

//So tell me, what are the characters in today's story?
