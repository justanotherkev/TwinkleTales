"use client";
import React from "react";
import s from "./back-button.module.css";

export default function BackButton(props) {
	const handleClick = () => {
		props.setPlayMusic(false);
		props.goToPromptPage();
	};

	if (props.enabled) {
		return (
			<button type="button" onClick={handleClick} className={s.link}>
				<div className={s.enabled_link_button}>New Story</div>
			</button>
		);
	} else {
		return (
			<button type="button" className={s.link}>
				<div className={s.link_button}>
					Creating your <br />
					story...
				</div>
			</button>
		);
	}
}
