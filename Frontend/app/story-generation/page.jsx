"use client";
import React, { useEffect, useRef, useState } from "react";
import PageComponent2 from "../../components/page-component-2/page-component-2.jsx";
import StoryImageBox from "@/components/story-image-box/story-image-box.jsx";
import BackButton from "@/components/back-button/back-button.jsx";
import { useRouter } from "next/navigation.js";
import { headers } from "next/headers.js";

export default function StoryGeneration({ searchParams }) {

	const [imageSourceList, setImageSourceList] = useState([]);
	const [currentImage, setCurrentImage] = useState();
	const [end, setEnd] = useState(false);
	const [playMusic, setPlayMusic] = useState(false);
	const [selectedAudioUrl, setSelectedAudioUrl] = useState("");
	const [imageDuration, setImageDuration] = useState();
	const router = useRouter();
	const firstRender = useRef(true);
	const [narrationPath,setNarrationPath] = useState("");


	// Upon a page load/reload sending the speech prompts to the integration file
	useEffect(() => {
		sendSpeechPrompts()
	}, []);

	// Put it inside a use effect to be triggered only when the state changes 
	//To play the music automaitically
	useEffect(() => {
		if (firstRender.current) {
			firstRender.current = false;
			return;
		}
		const audioElement = document.getElementById("audio-player");
		const narrationElement = document.getElementById("narration-player");
		if (playMusic) {
			audioElement.play()
			narrationElement.play()
			showImages();
		}
		else {
			audioElement.pause()
		}
	}, [playMusic]);



	// Displays each image in the imageList for a set duration
	const showImages = () => {
		let i = 0;
		console.log(imageSourceList.length);

		const intervalId = setInterval(() => {
			if (i < imageSourceList.length) {
				console.log("Current image: " + imageSourceList[i]);
				setCurrentImage(imageSourceList[i]);
				i++;
			} else {
				setCurrentImage();
				setEnd(true);
				setPlayMusic(false);
				clearInterval(intervalId); // stop the interval
			}
		}, imageDuration);
	};

	

	// Sends prompts to integration.py
	// Receives image URLs from integration.py
	// Passes URLs to getNarration
	const sendSpeechPrompts = async () => {
		const answers = searchParams.data;
		console.log("answers:" + answers);
		try {
			console.log("Sending the output page data");
			const res = await fetch("http://localhost:8001/", {
				method: "POST",
				headers: { "Content-Type": "application/json" },
				body: JSON.stringify(answers),
			});
			console.log("Post request was sent");
			const data = await res.json();
			console.log("Data received");
			console.log(data.message);
			console.log(data.message[0])
			console.log(data.message[1])
			console.log(data.message[2])
			setImageSourceList(data.message[0]);
			setImageDuration(data.message[1]);
			setSelectedAudioUrl(data.message[2]);
			setNarrationPath("narration_output.mp3")
			// setNarrationPath("E:\\IIT studies\\2 ND YEAR MATERIAL\\SDGP\\TwinkleTales\\narration_output.mp3")
			setPlayMusic(true)
			
		} catch {
			console.log("Something went wrong while sending the data.");
		}
	};

	//Navigates to the prompt page when New Story button is clicked.
	const goToPromptPage = () => {
		router.push("/prompt");
	};

	return (
		<PageComponent2
			src={"/story-reading-img.png"}
			component={
				<>
					<StoryImageBox src={currentImage} end={end} />
					<BackButton goToPromptPage={goToPromptPage} />

					{/* <button onClick={sendSpeechPrompts}>send speech prompts</button> */}


					<audio
						className="audio-player-styles"
						id="audio-player"
						controls={true}
						src={selectedAudioUrl}
						autoPlay
					/>

					<audio
						className="audio-player-styles"
						id="narration-player"
						controls={true}
						src={narrationPath}
						autoPlay
					/>

				</>
			}
		/>
	);
}
