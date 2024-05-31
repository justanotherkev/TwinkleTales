import HeaderTitle from "../header-title/header-title.jsx";
import s from "./page-component.module.css";
import Image from "next/image";

export default function PageComponent(props) {
	return (
		<div className={s.home}>
			<HeaderTitle line1="Twinkle" line2="Tales" />
			<div className={s.body}>
				<div className={s.image}>
					<Image src={props.src} alt={"Bunny image"} width={750} height={750} />
				</div>
				<div className={s.form_box}>{props.form_component}</div>
			</div>
		</div>
	);
}
