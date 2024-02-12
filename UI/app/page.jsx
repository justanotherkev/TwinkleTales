import Image from "next/image";
import s from "./page.module.css";
import Link from "next/link";

export default function Home() {
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
						<Link href="./get-started/login">Login</Link>
						<Link href="./get-started/sign-up">Sign Up</Link>
					</div>
				
				
				
				</div>
			</div>
		</div>
	);
}
