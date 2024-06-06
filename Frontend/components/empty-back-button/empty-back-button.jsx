"use client";
import s from "./empty-back-button.module.css";

export default function EmptyBackButton(props) {
	const handleClick = () => {
		props.goToThemePage();
	};

	return (
		<button type="button" onClick={handleClick} className={s.link}>
			<div className={s.enabled_link_button}>New Story</div>
		</button>
	);
}
