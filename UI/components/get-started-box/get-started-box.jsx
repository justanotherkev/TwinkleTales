import LoginSignupButton from "../login-signup-button/login-signup-button";
import s from "./get-started-box.module.css";

export default function GetStartedBox() {
	return (
		<div className={s.get_started_box}>
			<div className={s.text}>
				<h2>Get started</h2>
				<p>Explore captivating stories tailored to your child's imagination</p>
			</div>

			<div className={s.actions}>
				<LoginSignupButton href={"./login"} name={"Login"} />
				<LoginSignupButton href={"./sign-up"} name={"Sign Up"} />
			</div>
		</div>
	);
}
