"use client";

import ButtonStory from "@/components/button-story/button-story";
import PageComponent2 from "@/components/page-component-2/page-component-2.jsx";
import s from "./page.module.css";
import { useState } from "react";
import { useRouter } from "next/navigation";

export default function Prompt() {
	const [prompt, setPrompt] = useState("");
	const [answers, setAnswers] = useState("");
	const [isError, setIsError] = useState(false);
	const [showDisplay, setShowDisplay] = useState(false);
	const router = useRouter();

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

	if (isError) {
		const answersDisplay = document.getElementById("answers");
		answersDisplay.style.maxHeight = "0px";
		answersDisplay.style.padding = "0px";
		answersDisplay.style.color = "transparent";
	}

	const goToStoryPage = (answer_data) => {
		console.log("In push");
		console.log("Pushing");
		router.push(
			"/story-generation?data=" +
				encodeURIComponent(JSON.stringify(answer_data))
		);
	};

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
						setIsError={setIsError}
						goToStoryPage={goToStoryPage}
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
