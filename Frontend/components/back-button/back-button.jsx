"use client";
import React from "react";
import s from "./back-button.module.css";

export default function BackButton(props) {
	const handleClick = () => {
		props.setPlayMusic(false);
		props.goToThemePage();
	};

	const playStory = () => {
		props.setPlayMusic(true);
		props.setEnabled(true);
	};

	if (props.enabled) {
		return (
			<button type="button" onClick={handleClick} className={s.link}>
				<div className={s.enabled_link_button}>New Story</div>
			</button>
		);
	} else {
		return (
			<button type="button" className={s.link} onClick={playStory}>
				<div className={s.enabled_link_button}>Play story</div>
			</button>
		);
	}
}
