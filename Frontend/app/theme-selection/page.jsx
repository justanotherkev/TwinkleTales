"use client";

import React, { useEffect } from "react";
import s from "./page.module.css";
import HeaderTitle from "@/components/header-title/header-title";
import ThemeCard from "@/components/theme-card/theme-card";
import { useRouter } from "next/navigation";
import { SignedIn, UserButton } from "@clerk/nextjs";

export default function ThemeSelection() {
	const router = useRouter();

	const navigateToPrompt = (selectedTheme) => {
		router.push(
			"/prompt?theme=" + encodeURIComponent(JSON.stringify(selectedTheme))
		);
	};

	useEffect(() => {
		const adjustBackgroundNoise = async () => {
			console.log("Adjusting for background noise");
			try {
				const res = await fetch("http://localhost:8000/adjust_noise", {
					method: "GET",
					headers: { "Content-Type": "application/json" },
				});
				const data = await res.json();
				console.log(data.message);
			} catch (error) {
				console.log("Something went wrong:\n" + error);
			}
		};
		adjustBackgroundNoise();
	});

	// adjustBackgroundNoise()

	return (
		<div className={s.page}>
			<SignedIn>
				<div className={s.user_button}>
					<UserButton />
				</div>
			</SignedIn>
			<HeaderTitle line1="Select your" line2="theme" />
			<div className={s.theme_container}>
				<ThemeCard
					title="Superhero"
					subtitle="Join the brave heroes as they save the world from villains!"
					src="/theme_bunny_superhero.png"
					navigateToPrompt={navigateToPrompt}
				/>

				<ThemeCard
					title="Adventure"
					subtitle="Embark on thrilling journeys and uncover hidden treasures!"
					src="/theme_bunny_adventure.png"
					navigateToPrompt={navigateToPrompt}
				/>

				<ThemeCard
					title="Fairy Tale"
					subtitle="Dive into magical worlds with epic quests and hidden magic!"
					src="/theme_bunny_fairytales.png"
					navigateToPrompt={navigateToPrompt}
				/>

				<ThemeCard
					title="Sports"
					subtitle="Immerse yourself in the action and unleash your inner athlete!"
					src="/theme_bunny_sports.png"
					navigateToPrompt={navigateToPrompt}
				/>
			</div>
		</div>
	);
}
