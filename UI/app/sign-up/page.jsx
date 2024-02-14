import { SignUp } from "@clerk/nextjs";
import s from "./page.module.css";
import HeaderTitle from "@/components/header-title/header-title";

export default function Login() {
	return (
		<div className={s.login}>
			<HeaderTitle />
			<SignUp />
		</div>
	);
}
