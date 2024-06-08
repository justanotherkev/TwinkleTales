"use client";

import React from "react";
import s from "./page.module.css";
import HeaderTitle from "@/components/header-title/header-title";

export default function Tutorial() {
	const handleClick = () => {
		window.location.href = "/theme-selection";
	};

	return (
		<div className={s.tutorial_page}>
			<HeaderTitle line1="How to" line2="use" />
			<p className={s.subtitle}>
				Your story will be ready in three simple steps
			</p>
			<div className={s.tutorial_box}>
				<div className={s.instruction_card}>
					<h1>Step 01</h1>
					<p>Pick a theme that you like</p>
				</div>
				<div className={s.instruction_card}>
					<h1>Step 02</h1>
					<p>Answer the questions</p>
				</div>
				<div className={s.instruction_card}>
					<h1>Step 03</h1>
					<p>Relax and enjoy the story</p>
				</div>
			</div>

			<button type="button" onClick={handleClick} className={s.link}>
				<div className={s.start_button}>Let's Start</div>
			</button>
		</div>
	);
}
