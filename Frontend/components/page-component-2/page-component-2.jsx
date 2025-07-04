// This page component should be used for the log-in and sign-up pages

import s from "./page-component-2.module.css";
import Image from "next/image";

export default function PageComponent2(props) {
	return (
		<div className={s.home}>
			{/* <HeaderTitle line1="Twinkle" line2="Tales" /> */}
			<div className={s.body}>
				<div className={s.image}>
					<Image src={props.src} alt={"Bunny image"} width={750} height={750} />
				</div>
				<div className={s.form_box}>{props.component}</div>
			</div>
		</div>
	);
}
