import s from "./form-button.module.css";
import Link from "next/link";

export default function FormButton(props) {
	if (props.isNav) {
		return (
			<Link href={props.href} className={s.link}>
				<div className={s.link_button}>{props.name}</div>
			</Link>
		);
	} else {
		return (
			<button type="submit" onClick={props.onClick} className={s.link}>
				<div className={s.link_button}>{props.name}</div>
			</button>
		);
	}
}
