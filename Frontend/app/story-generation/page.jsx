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
	const [playStory, setPlayStory] = useState(false);

	const [answers, setAnswers] = useState("Answers will show here");
	const [playMusic, setPlayMusic] = useState(false);
	const audioUrl =
		"https://utfs.io/f/e7c7db5e-a02e-48b9-b7c1-d9e10c91bfec-xnnced.mp3";
	const [selectedAudioIndex, setSelectedAudioIndex] = useState(0);
	const [audioUrls, setAudioUrls] = useState([]);
	const firstRender = useRef(true);

	// Runs
	useEffect(() => {
		if (firstRender.current) {
			firstRender.current = false;
			return;
		}
		showImages(imageSourceList);
		getNarration();
	}, [playStory]);

	const router = useRouter();

	// Fetching all the audio URLs from the database upon a page load/reload.
	// useEffect(() => {
	// 	fetchAudioUrls();
	// }, []);

	// Randomly pick a audio Url from the audioUrls variable
	// useEffect(() => {
	// 	if (audioUrls.length > 0) {
	// 	  const randomIndex = Math.floor(Math.random() * audioUrls.length);
	// 	  setSelectedAudioIndex(randomIndex);
	// 	}
	// }, [audioUrls]);

	// Upon a page load/reload sending the speech prompts to the integration file
	useEffect(() => {
		console.log(searchParams.data);
		// sendSpeechPrompts()
	}, []);

	// Upon a page load/reload play the narration from the integration file
	// useEffect(() => {
	// 	getNarration();
	// })

	// Fetch request for getting the audio URLs from the database
	const fetchAudioUrls = async () => {
		console.log("Fetching audio URLs...");
		try {
			//Chnage port 8000 to sm else cause main.py is on port 8000
			const response = await fetch("http://localhost:8002/", {
				method: "GET",
				headers: { "Content-Type": "application/json" },
			});
			console.log("Fetch complete");

			const data = await response.json();
			console.log("Fetched audio URLs:", data);
			setAudioUrls(data.message); // Set the audio URLs from the fetched data
		} catch (error) {
			console.error("Error fetching audio URLs:", error);
		}
	};

	const selectedAudioUrl =
		audioUrls.length > 0 ? audioUrls[selectedAudioIndex].audio_url : "";

	//To play the music upon the button click
	const handleClick = () => {
		// setPlayMusic(true);
	};

	//To play the music
	// const audioElement = document.getElementById("audio-player");
	// if (playMusic) {
	// 	audioElement.play()
	// }

	// Displays each image in the imageList for a set duration
	const showImages = (imageList) => {
		let i = 0;
		console.log(imageList.length);

		// Replace the function below with Kishon's timer
		const intervalId = setInterval(() => {
			if (i >= imageList.length) {
				setCurrentImage();
				setEnd(true);
				clearInterval(intervalId); // stop the interval
			} else {
				console.log("Current image: " + imageList[i]);
				setCurrentImage(imageList[i]);
				i++;
			}
		}, 4000);
	};

	// Sends a get request to integration.py
	// Triggers the audio to play and images to show upon return message from integration.py
	const getNarration = async () => {
		try {
			console.log("Getting narration....");
			const res = await fetch("http://localhost:8001/", {
				method: "GET",
				headers: { "Content-Type": "application/json" },
			});
			const data = await res.json();
			console.log(
				"Return from integration.py - get_narration() " + data.message
			);
		} catch (Error) {
			console.log(
				"Error sending get request to integration.py get_narration()."
			);
			console.error("The error: ", Error);
		}
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
			console.log("Images received");
			console.log(data.message);
			setImageSourceList(data.message);

			if (data.message) {
				setPlayStory(true);
			} else {
				console.log("No response from integration.py get_narration()");
			}

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

					<button onClick={sendSpeechPrompts}>send speech prompts</button>
					{/* <button onClick={getNarration}>get narration</button> */}

					{/* <audio
						className="audio-player-styles"
						id="audio-player"
						controls={true}
						src={selectedAudioUrl}
						autoPlay
					/> */}
					{/* <button onClick={getNarration}>.</button> */}
				</>
			}
		/>
	);
}
