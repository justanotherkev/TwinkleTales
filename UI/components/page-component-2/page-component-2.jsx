import HeaderTitle from "../header-title/header-title.jsx";
import s from "./page-component-2.module.css";
import Image from "next/image";

export default function PageComponent2(props) {
	return (
		<div className={s.home}>
			{/* <HeaderTitle /> */}
			<div className={s.body}>
				<div className={s.image}>
					<Image src={props.src} width={700} height={700} />
				</div>
				<div className={s.form_box}>{props.component}</div>
			</div>
		</div>
	);
}

