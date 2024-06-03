import React, { useEffect } from "react";
import s from "./loading-bar.module.css";

export default function LoadingBar(props) {
	useEffect(() => {
		const percent = document.getElementById("percent");
		const progress = document.getElementById("progress");

		if (progress && percent && props.startLoading) {
			let currentWidth = 0.0;
			const interval = setInterval(() => {
				let randomWidth = Math.random() * (0.02 - 0.001) + 0.1;
				console.log(currentWidth + "+" + randomWidth + "=");
				currentWidth += randomWidth;
				progress.style.width = `${currentWidth}%`;
				percent.innerHTML = `${currentWidth.toFixed(2)}%`;
				console.log(currentWidth);
				console.log("\n");

				if (currentWidth >= 93) {
					clearInterval(interval);
				}
			}, 100);
		}
	});
	return (
		<div className={s.loading_bar}>
			<p id="percent">0%</p>
			<div className={s.progress} id="progress"></div>
		</div>
	);
}
