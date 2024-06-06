"use client";
import React, { useEffect, useRef, useState } from "react";
import PageComponent2 from "../../components/page-component-2/page-component-2.jsx";
import StoryImageBox from "@/components/story-image-box/story-image-box.jsx";
import BackButton from "@/components/back-button/back-button.jsx";
import { useRouter } from "next/navigation.js";
import EmptyStoryBox from "@/components/empty-story-box/empty-story-box.jsx";
import EmptyBackButton from "@/components/empty-back-button/empty-back-button.jsx";

export default function StoryGeneration({ searchParams }) {
	const [imageSourceList, setImageSourceList] = useState([]);
	const [currentImage, setCurrentImage] = useState();
	const [end, setEnd] = useState(false);
	const [error, setError] = useState(false);
	const [enabled, setEnabled] = useState(false);
	const [playMusic, setPlayMusic] = useState(false);
	const [selectedAudioUrl, setSelectedAudioUrl] = useState("");
	const [imageDuration, setImageDuration] = useState();
	const [noStoryData, setNoStoryData] = useState(true);
	const router = useRouter();
	const firstRender = useRef(true);
	const narrationPath = "/narration_audio.mp3";

	// Sends the speech prompts to the integration file upon a page load/reload
	useEffect(() => {
		// Sends prompts to integration.py
		// Receives image URLs from integration.py
		// Passes URLs to getNarration
		const getStoryData = async () => {
			try {
				console.log("Getting story items");
				const res = await fetch("http://localhost:8001/", {
					method: "GET",
					headers: { "Content-Type": "application/json" },
				});
				const data = await res.json();
				if (data.length != 0) {
					console.log("Data received");
					setImageSourceList(data[0]);
					setSelectedAudioUrl(data[1]);
					setImageDuration(data[2]);
					setPlayMusic(true);
					setEnabled(true);
					setNoStoryData(false);
				} else {
					setNoStoryData(true);
				}
			} catch {
				console.log("Something went wrong while sending the data.");
				setError(true);
				setEnabled(true);
			}
		};
		getStoryData();
	}, []);

	// useEffect to be triggered only when the state changes
	//Plays the music automatically
	useEffect(() => {
		if (firstRender.current) {
			firstRender.current = false;
			return;
		}
		const backgroundMusic = document.getElementById("background-music-player");
		const narration = document.getElementById("narration-player");

		// Displays each image in the imageList for a set duration
		const showImages = () => {
			let i = 1;
			console.log("Source list length: " + imageSourceList.length);
			console.log("Image duration: " + imageDuration);

			//displays the first image immediatley
			setCurrentImage(imageSourceList[0]);
			const intervalId = setInterval(() => {
				if (i < imageSourceList.length) {
					console.log("Current image " + i + ": " + imageSourceList[i]);
					setCurrentImage(imageSourceList[i]);
					i++;
				} else {
					const closingInterval = setInterval(() => {
						setCurrentImage();
						setEnd(true);
						setPlayMusic(false);
						clearInterval(intervalId);
						clearInterval(closingInterval);
					}, 2000);
				}
			}, imageDuration);
		};

		if (playMusic) {
			console.log("Starting everything...");
			showImages();
			if (backgroundMusic && narration) {
				console.log("Playing");
				backgroundMusic.volume = 0.2;
				backgroundMusic.play();
				narration.play();
			}
		} else {
			console.log("Stopping everything...");
			backgroundMusic.pause();
			narration.pause();
		}
	}, [playMusic, imageDuration, imageSourceList]);

	//Navigates to the prompt page when New Story button is clicked.
	const goToThemePage = () => {
		router.push("/theme-selection");
	};

	if (noStoryData) {
		return (
			<PageComponent2
				src={"/story-reading-img.png"}
				component={
					<>
						<EmptyStoryBox />
						<EmptyBackButton goToThemePage={goToThemePage} />
					</>
				}
			/>
		);
	} else {
		return (
			<PageComponent2
				src={"/story-reading-img.png"}
				component={
					<>
						<StoryImageBox src={currentImage} end={end} error={error} />
						<BackButton
							setPlayMusic={setPlayMusic}
							goToThemePage={goToThemePage}
							enabled={enabled}
						/>

						<audio
							className="audio-player-styles"
							id="background-music-player"
							controls={false}
							src={selectedAudioUrl}
							autoPlay={false}
							muted={true}
						/>

						<audio
							className="audio-player-styles"
							id="narration-player"
							controls={false}
							src={narrationPath}
							autoPlay={false}
							muted={true}
						/>
					</>
				}
			/>
		);
	}
}
