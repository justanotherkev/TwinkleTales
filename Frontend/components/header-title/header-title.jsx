import s from "./header-title.module.css";

export default function HeaderTitle(props) {
	return (
		<h1 className={s.header_title}>
			<span>{props.line1}</span>
			<span>{props.line2}</span>
		</h1>
	);
}
