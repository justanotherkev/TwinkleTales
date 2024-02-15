"use client";
import s from "./button-action.module.css";

export default function ButtonAction() {
	const handleClick = () => {};
	return (
		<>
			<button className={s.button} onClick={handleClick}>
				Tap to Speak
			</button>
		</>
	);
}
