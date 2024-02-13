// import sound from "../public/welcome_background_music.mp3";
import s from "./page.module.css";
import Link from "next/link";

export default function Home() {
	// function play() {
	// 	new Audio(sound).play();
	// }

	// play();

	return (
		<div className={s.home}>
			<h1 className={s.header_title}>
				<span>TWINKLE</span>
				<span>TALES</span>
			</h1>
			<div className={s.body}>
				<div className={s.image}></div>

				<div className={s.get_started}>
					<div className={s.get_started_text}>
						<h2>Get started</h2>
						<p>
							Explore captivating stories tailored to your child's imagination
						</p>
					</div>

					<div className={s.get_started_actions}>
						<Link href="./login" className={s.link}>
							<div className={s.link_button}>Login</div>
						</Link>
						<Link href="./sign-up" className={s.link}>
							<div className={s.link_button}>Sign Up</div>
						</Link>
					</div>
				</div>
			</div>
		</div>
	);
}
