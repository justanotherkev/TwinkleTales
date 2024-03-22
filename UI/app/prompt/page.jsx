"use client";

import ButtonStory from "@/components/button-story/button-story";
import PageComponent2 from "@/components/page-component-2/page-component-2.jsx";
import s from "./page.module.css";
import { useState } from "react";
import { useRouter } from "next/navigation";
import React from "react";
import { SignedIn, SignedOut, UserButton } from "@clerk/nextjs";

export default function Prompt() {
	const [prompt, setPrompt] = useState("");
	const [answers, setAnswers] = useState("");
	const [isError, setIsError] = useState(false);
	const [showDisplay, setShowDisplay] = useState(false);
	const [isHidden, setIsHidden] = useState(true);
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
		console.log("Pushing to story output page");
		router.push(
			"/story-generation?data=" +
				encodeURIComponent(JSON.stringify(answer_data))
		);
	};

	const handleHover = () => {
		setIsHidden(!isHidden); // Toggle isHidden state
	};

	return (
		<>
			<SignedIn>
				<div className={s.user_button}>
					<UserButton />
				</div>
			</SignedIn>

			<SignedOut></SignedOut>

			<div
				className={s.tutorial_button}
				onMouseEnter={handleHover}
				onMouseLeave={handleHover}
				onTouchStart={handleHover}
				onTouchEnd={handleHover}
			>
				<img className={s.question_mark} src="/question-mark.svg" alt="" />
			</div>
			<div className={`${s.tutorial_details} ${isHidden ? s.hidden : ""}`}>
				1. Click the "Tell me a story" button
				<br />
				2. Wait for the prompt
				<br />
				3. Answer the question
			</div>
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
		</>
	);
}
