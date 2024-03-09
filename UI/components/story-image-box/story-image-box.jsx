import React from "react";
import s from "./story-image-box.module.css";
import Image from "next/image";


export default function StoryImageBox(props) {
	if (props.src) {
		return (
			<div className={s.story_image_box}>
				<Image src={props.src} />
			</div>
		);
	} else {
		return (
			<div className={s.story_image_box}>
				<h2 className={s.title}>
        Your story is <br /> almost ready!
          </h2> 
        <img className={s.loading_arrows} src="/loading-arrows.svg" alt="" />
			</div>
		);
	}
}
