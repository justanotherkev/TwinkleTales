"use client";

import ButtonStory from "@/components/button-story/button-story";
import PageComponent2 from "@/components/page-component-2/page-component-2.jsx";
import s from "./page.module.css";
import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import React from "react";
import { SignedIn, UserButton } from "@clerk/nextjs";
import Image from "next/image";
import LoadingBar from "@/components/loading-bar/loading-bar";

export default function Prompt({ searchParams }) {
	const [prompt, setPrompt] = useState("");
	const [answers, setAnswers] = useState("");
	const [answersList, setAnswersList] = useState("");
	const [isError, setIsError] = useState(false);
	const [showDisplay, setShowDisplay] = useState(false);
	const [isHidden, setIsHidden] = useState(true);
	const [loadingComplete, setLoadingComplete] = useState(false);
	const router = useRouter();

	useEffect(() => {
		const loadingScreen = document.getElementById("loading_screen");
		if (answersList == "") {
			loadingScreen.style.display = "none";
		} else {
			loadingScreen.style.display = "flex";

			const sendSpeechPrompts = async () => {
				console.log("answersList: " + answersList);
				try {
					const res = await fetch(
						"http://localhost:8001/" + searchParams.theme,
						{
							method: "POST",
							headers: { "Content-Type": "application/json" },
							body: JSON.stringify(answersList),
						}
					);
					console.log("Post request was sent");
					setAnswersList("");
					const data = await res.json();
					console.log("Story status: " + data);
					if (data == "done") {
						setLoadingComplete(true);
						window.location.href = "/story-generation";
					}
				} catch {
					console.log("Something went wrong while sending the data.");
					setIsError(true);
					setPrompt("Oh no! Something went wrong. Please try again later");
					setAnswersList("");
				}
			};

			sendSpeechPrompts();
		}
	}, [answersList]);

	useEffect(() => {
		if (showDisplay) {
			const promptDisplay = document.getElementById("prompt");
			promptDisplay.style.maxHeight = "fit-content";
			promptDisplay.style.padding = "25px 10px";
			promptDisplay.style.color = "black";

			const answersDisplay = document.getElementById("answers");
			answersDisplay.style.maxHeight = "fit-content";
			answersDisplay.style.padding = "25px 10px";
			answersDisplay.style.color = "black";
		} else {
			const promptDisplay = document.getElementById("prompt");
			promptDisplay.style.maxHeight = "0px";
			promptDisplay.style.padding = "0px";
			promptDisplay.style.color = "transparent";

			const answersDisplay = document.getElementById("answers");
			answersDisplay.style.maxHeight = "0px";
			answersDisplay.style.padding = "0px";
			answersDisplay.style.color = "transparent";
		}
	}, [showDisplay]);

	if (isError) {
		const promptDisplay = document.getElementById("prompt");
		promptDisplay.style.maxHeight = "fit-content";
		promptDisplay.style.padding = "25px 10px";
		promptDisplay.style.color = "black";

		const answersDisplay = document.getElementById("answers");
		answersDisplay.style.maxHeight = "0px";
		answersDisplay.style.padding = "0px";
		answersDisplay.style.color = "transparent";
	}

	const handleHover = () => {
		setIsHidden(!isHidden);
	};

	return (
		<>
			<SignedIn>
				<div className={s.user_button}>
					<UserButton />
				</div>
			</SignedIn>

			<div
				className={s.tutorial_button}
				onMouseEnter={handleHover}
				onMouseLeave={handleHover}
				onTouchStart={handleHover}
				onTouchEnd={handleHover}
			>
				<Image
					className={s.question_mark}
					height={20}
					width={20}
					src="/question-mark.svg"
					alt=""
				/>
			</div>
			<div className={`${s.tutorial_details} ${isHidden ? s.hidden : ""}`}>
				1. Click the &quot;Tell me a{" "}
				{searchParams.theme.toLowerCase().replaceAll('"', "")} story&quot;
				button
				<br />
				2. Wait for the prompt
				<br />
				3. Answer the question
			</div>

			<div className={s.loading_screen} id="loading_screen">
				<h2>
					Your story will be <br /> ready in a few minutes!
				</h2>
				<Image
					className={s.loading_arrows}
					src={"/loading-arrows.svg"}
					alt={"Loading arrows"}
					height={80}
					width={80}
				/>
				<h3>Grab a snack while you wait</h3>
				<LoadingBar
					startLoading={answersList != ""}
					loadingComplete={loadingComplete}
				/>
			</div>

			<PageComponent2
				src={"/story-prompt-img.png"}
				component={
					<div className={s.container}>
						<div className={s.prompt} id="prompt">
							{prompt}
						</div>
						<ButtonStory
							buttonText={searchParams.theme}
							setPrompt={setPrompt}
							setAnswers={setAnswers}
							setAnswersList={setAnswersList}
							setShowDisplay={setShowDisplay}
							setIsError={setIsError}
						/>

						<div className={s.answers} id="answers">
							{answers}
						</div>
						{/* <p className={s.info}>
							If you're in a noisy place, try going somewhere quieter
						</p> */}
					</div>
				}
			/>
		</>
	);
}
