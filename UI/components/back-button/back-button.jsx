"use client";
import React from "react";
import s from "./back-button.module.css";

export default function BackButton(props) {


	return (
		<button type="button" onClick={props.handleRouting} className={s.link}>
			<div className={s.link_button}>New Story</div>
		</button>
	);
}
