import React from "react";
import s from "./empty-story-box.module.css";

export default function EmptyStoryBox() {
	return (
		<div className={s.empty_story_box}>
			<h2 className={s.title}>Oops! You haven&apos;t created a story yet</h2>
			<p className={s.subtitle}>Click on the button below to get started</p>
		</div>
	);
}
