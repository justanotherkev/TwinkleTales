import React, { useEffect } from "react";
import s from "./loading-bar.module.css";

export default function LoadingBar(props) {
	useEffect(() => {
		const percent = document.getElementById("percent");
		const progress = document.getElementById("progress");

		if (props.loadingComplete) {
			progress.style.width = "100%";
			percent.innerHTML = "100%";
		}

		if (progress && percent && props.startLoading && !props.loadingComplete) {
			let currentWidth = 0.0;

			const interval = setInterval(() => {
				let randomWidth = Math.random() * (0.02 - 0.001) + 0.1;
				currentWidth += randomWidth;
				progress.style.width = `${currentWidth}%`;
				percent.innerHTML = `${currentWidth.toFixed(2)}%`;

				if (currentWidth >= 98.31) {
					clearInterval(interval);
				}
			}, 100);
		}
	}, [props.loadingComplete]);

	return (
		<div className={s.loading_bar}>
			<p id="percent">0%</p>
			<div className={s.progress} id="progress"></div>
		</div>
	);
}
