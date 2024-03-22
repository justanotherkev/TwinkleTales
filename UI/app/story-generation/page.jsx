"use client";
import React, { useEffect, useState } from "react";
import PageComponent2 from "../../components/page-component-2/page-component-2.jsx";
import StoryImageBox from "@/components/story-image-box/story-image-box.jsx";
import BackButton from "@/components/back-button/back-button.jsx";
import { useRouter } from "next/navigation.js";
import { headers } from "next/headers.js";

export default function StoryGeneration({ searchParams }) {
	const [imageSourceList, setImageSourceList] = useState();
	const [end, setEnd] = useState(false);
	const [answers, setAnswers] = useState("Answers will show here");
	const [playMusic, setPlayMusic] = useState(false);
	const audioUrl ="https://utfs.io/f/e7c7db5e-a02e-48b9-b7c1-d9e10c91bfec-xnnced.mp3";
	const [selectedAudioIndex, setSelectedAudioIndex] = useState(0);
	const [audioUrls, setAudioUrls] = useState([]);
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
		sendSpeechPrompts(searchParams.data)
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
		  console.log('Fetched audio URLs:', data);
		  setAudioUrls(data.message); // Set the audio URLs from the fetched data
		} catch (error) {
		  console.error('Error fetching audio URLs:', error);
		}
	};

	const selectedAudioUrl = audioUrls.length > 0 ? audioUrls[selectedAudioIndex].audio_url : '';

	//To play the music upon the button click
	const handleClick = () => {
		// setPlayMusic(true);
	};

	//To play the music 
	// const audioElement = document.getElementById("audio-player");
	// if (playMusic) {
	// 	audioElement.play()
	// }        

	//To push to the prompt taking page upon a new story button click.
	const handleRouting = () => {
		router.push("/prompt");
	};

	// Sending the prompts to the integration file
	// Reciving the image URLs from the integration file inn the response
	// Setting the image Urls in a array varible
	const sendSpeechPrompts = async (answers) => {
		// const answers = searchParams.data
		console.log(answers)

		try{
			console.log("Sending the output page data")
			const res = await fetch("http://localhost:8001/",{
				method:"POST",
				headers: { "Content-Type": "application/json" },
				body:JSON.stringify(answers)
			})
			console.log("Post request was sent")
			const data = await res.json()
			console.log(data.message)
			setImageSourceList(data.message)
		} catch {
			console.log("Something went wrong while sending the data.")
		}
	}

	const getNarration = async () =>{
		try{

			console.log("Getting the narration....")
			const res = await fetch("http://localhost:8001/",{
				method:"GET",
				headers: { "Content-Type": "application/json" }
			})
			const response = await res.json()
			console.log(response)
			
		}
		catch (Error){
			console.log("Error occured while sending a get request to integration file to play the narration.")
			console.error("The error: ",Error)
		}
	}

	const showImages = async () => {
		
		// Kishons timer function
		let i = 0;
		const intervalId = setInterval(() => {
			if (i >= image_URLs.length) {
				setImageSourceList();
				setEnd(true);
				clearInterval(intervalId); // stop the interval
			} else {
				setImageSourceList(image_URLs[i]);
				i++;
			}
		}, 2000);

	};

	

	return (
		<PageComponent2
			src={"/story-reading-img.png"}
			component={
				<>
					<p style={{ color: "white" }}>{answers}</p>
					<StoryImageBox src={imageSourceList} end={end} />
					<BackButton handleRouting={handleRouting} />
					<button onClick={handleClick}>get images</button>

					<audio
						className="audio-player-styles"
						id="audio-player"
						controls={true}
						src={selectedAudioUrl}
						autoPlay
					/>
					<button onClick={getNarration}>.</button>
				</>
			}
		/>
	);
}
