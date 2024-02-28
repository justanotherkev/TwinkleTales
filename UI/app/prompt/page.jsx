import ButtonAction from "@/components/button-action/button-action";
import PageComponent2 from "@/components/page-component-2/page-component-2.jsx";

export default function Prompt() {
	return (
		<PageComponent2
			src={"/story-prompt-img.png"}
			component={<ButtonAction />}
		/>
	);
}
