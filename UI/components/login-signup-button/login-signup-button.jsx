import s from "./login-signup-button.module.css";
import Link from "next/link";

export default function LoginSignupButton(props) {
	return (
		<Link href={props.href} className={s.link}>
			<div className={s.link_button}>{props.name}</div>
		</Link>
	);
}
