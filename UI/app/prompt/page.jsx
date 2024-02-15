import Button from "../../components/button-action/button-action.jsx";
import ButtonNavigation from "../../components/navigate/navigation-button.jsx";
import s from "./page.module.css";
import Image from "next/image";


export default function Prompt() {
	return (
		<div>
			<Button name={"Go back"} />
			<ButtonNavigation />
			<Image className={s.image} />
		</div>
	);
}

<Button text={"Home"} />;
