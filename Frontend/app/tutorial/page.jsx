import React from "react";
import s from "./page.module.css";
import HeaderTitle from "@/components/header-title/header-title";
import Image from "next/image";

export default function Tutorial() {
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
					<Image
						src="/bunny-with-phone.png"
						height={200}
						width={200}
						alt="Theme image"
					/>
				</div>
				<div className={s.instruction_card}>
					<h1>Step 02</h1>
					<p>Answer the questions</p>
					<Image
						src="/story-prompt-img.png"
						height={200}
						width={200}
						alt="Theme image"
					/>
				</div>
				<div className={s.instruction_card}>
					<h1>Step 03</h1>
					<p>Relax and enjoy the story</p>
					<Image
						src="/get-started-img.png"
						height={200}
						width={200}
						alt="Theme image"
					/>
				</div>
			</div>
		</div>
	);
}
