import React from "react";
import s from "./story-image-box.module.css";
import Image from "next/image";

export default function StoryImageBox(props) {
	if (props.src) {
		console.log("props.src: " + props.src)
		return (
			<div className={s.story_image_box}>
				<Image
					src={props.src}
					width={750}
					height={750}
					className={s.story_images}
				/>
			</div>
		);
	} else {
		return (
			<div className={s.story_image_box}>
				{props.end ? (
					<h2 className={s.title}>The end!</h2>
				) : (
					<>
						<h2 className={s.title}>
							Your story is <br /> almost ready!
						</h2>
						<img
							className={s.loading_arrows}
							src="/loading-arrows.svg"
							alt=""
						/>
					</>
				)}
			</div>
		);
	}
}
