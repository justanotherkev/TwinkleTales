import PageComponent from "@/components/page-component/page-component";
import GetStartedBox from "@/components/get-started-box/get-started-box";

export default function Home() {
	return (
		<PageComponent
			src={"/get-started-img.png"}
			form_component={<GetStartedBox />}
		/>
	);
}

// import sound from "../public/welcome_background_music.mp3";

// function play() {
// new Audio(sound).play();
// }
// play();