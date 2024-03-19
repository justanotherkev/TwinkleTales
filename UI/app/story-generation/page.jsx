"use client";
import React, { useEffect, useState } from "react";
import PageComponent2 from "../../components/page-component-2/page-component-2.jsx";
import StoryImageBox from "@/components/story-image-box/story-image-box.jsx";
import BackButton from "@/components/back-button/back-button.jsx";
import { useRouter } from "next/navigation.js";

export default function StoryGeneration({ searchParams }) {
	const [imageSourceList, setImageSourceList] = useState();
	const [end, setEnd] = useState(false);
	const [answers, setAnswers] = useState("Answers will show here");
	const [playMusic, setPlayMusic] = useState(false);
	const audioUrl =
		"https://utfs.io/f/e7c7db5e-a02e-48b9-b7c1-d9e10c91bfec-xnnced.mp3";

	const imageList = [
		"https://replicate.delivery/pbxt/w8fWfmHNPzlcYkCesaThvCc1rcEXGUmnThelaB5cevAumv0TC/out-0.png", // clouds
		"https://replicate.delivery/pbxt/5MOT1UByyc64L9HV4Tp0JfwQAg1D5cMNy2p5zOLEoT5helekA/out-0.png", // three animals
		"https://replicate.delivery/pbxt/YMsGLF3PvT6xBpBkg6gOy4CtyD8o2IcqzYnKf1TjZwf1AmekA/out-0.png", // village sky
		"https://replicate.delivery/pbxt/svk0bKOXf1yWA6y9MOfJXsdAEg8uKMvCsZv7f1vN8mWpuL9kA/out-0.png", // more couds
		"https://replicate.delivery/pbxt/vkFyesbz2I1zVaPVnHXtKYLDQkuJRfCU54EKTty7fJ4IvL9kA/out-0.png", // rabbits
		"https://replicate.delivery/pbxt/10YRWJ13j5INHRQJeEjjQ74ORNhYhzGGkJkCljf4CMi33lekA/out-0.png", // mice
	];

	const router = useRouter();

	const handleClick = () => {
		setPlayMusic(true);
	};

	const audioElement = document.getElementById("audio-player");
	if (playMusic) {
		audioElement.play();
	}

	const handleRouting = () => {
		router.push("/prompt");
	};

	useEffect(() => {
		
	}, []);

	const sendSpeechPrompts = async () => {
		const list1 = ["David","London","Football","park","sunny"]
		try{

			console.log("Sending the output page data")
			const res = await fetch("http://localhost:8000/",{
				method:"POST",
				headers: { "Content-Type": "application/json" },
				body:JSON.stringify({list1})
			})
		}
		catch{

			console.log("Something went wront while sending the data.")
			
		}
	}

	const generateImages = async () => {
		console.log("Generating...");
		// const res = await fetch("http://localhost:8000/", {
		// 	method: "GET",
		// 	headers: { "Content-Type": "application/json" },
		// });
		// data = await res.json();

		sendSpeechPrompts()


		// let i = 0;
		// const intervalId = setInterval(() => {
		// 	if (i >= imageList.length) {
		// 		setImageSourceList();
		// 		setEnd(true);
		// 		clearInterval(intervalId); // stop the interval
		// 	} else {
		// 		setImageSourceList(imageList[i]);
		// 		i++;
		// 	}
		// }, 2000);
	};

	return (
		<PageComponent2
			src={"/story-reading-img.png"}
			component={
				<>
					<p style={{ color: "white" }}>{answers}</p>
					<StoryImageBox src={imageSourceList} end={end} />
					<BackButton handleRouting={handleRouting} />
					<button onClick={handleClick}>play audio</button>

					<audio
						className="audio-player-styles"
						id="audio-player"
						controls={true}
						src={audioUrl}
						autoPlay
					/>
					<button onClick={generateImages}>.</button>
				</>
			}
		/>
	);
}
