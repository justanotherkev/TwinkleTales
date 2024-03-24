import FormButton from "../form-button/form-button";
import s from "./get-started-box.module.css";

export default function GetStartedBox() {
	return (
		<div className={s.get_started_box}>
			<div className={s.text}>
				<h2>Get started</h2>
				<p>Explore captivating stories tailored to your child&apos;s imagination</p>
			</div>

			<div className={s.actions}>
				<FormButton href={"./login"} name={"Login"} isNav={true} />
				<FormButton href={"./sign-up"} name={"Sign Up"} isNav={true} />
			</div>
		</div>
	);
}
