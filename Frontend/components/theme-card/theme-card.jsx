"use client";

import React from "react";
import s from "./theme-card.module.css";
import Image from "next/image";

export default function ThemeCard(props) {
	const handleClick = (title) => {
		props.navigateToPrompt(title);
	};

	return (
		<div className={s.theme_card} onClick={() => handleClick(props.title)}>
			<div className={s.name_section}>
				<h1 className={s.title}>{props.title}</h1>
				<p>{props.subtitle}</p>
			</div>
			<div className={s.image_section}>
				<Image src={props.src} height={200} width={200} alt="Theme image" />
			</div>
		</div>
	);
}
