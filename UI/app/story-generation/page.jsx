"use client";
import React, { useState } from "react";
import PageComponent2 from "../../components/page-component-2/page-component-2.jsx";
import StoryImageBox from "@/components/story-image-box/story-image-box.jsx";
import BackButton from "@/components/back-button/back-button.jsx";
import { useRouter } from "next/navigation.js";

export default function StoryGeneration() {

  const router = useRouter();

  const handleRouting = () => {
		router.push("/prompt");
	};

	const [imageSource, setImageSource] = useState();

	return (
		<PageComponent2
			src={"/story-reading-img.png"}
			component={
				<>
					<StoryImageBox src={imageSource} />
					<BackButton handleRouting={handleRouting}/>
				</>
			}
		/>
	);
}
