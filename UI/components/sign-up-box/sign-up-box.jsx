"use client";
import FormButton from "../form-button/form-button";
import s from "./sign-up-box.module.css";
import { useSignUp } from "@clerk/nextjs";

export default function SignUpBox() {
	const { signUp, isActive, isLoaded } = useSignUp();

	const verifyCredentials = () => {
		console.log("Verifying credentials...");
	};

	const handleSubmit = async (e) => {
		console.log("Submitting...");
		e.preventDefault();

		const username = e.target.username.value;
		const email = e.target.email.value;
		const password = e.target.password.value;
		const confirmPass = e.target.confirmPass.value;

		console.log(username);
		console.log(email);
		console.log(password);
		console.log(confirmPass);
	};

	if (!isLoaded) {
		return (
			<div className={s.sign_up_box}>
				<h2 className={s.title}>Loading...</h2>
			</div>
		);
	} else {
		return (
			<div className={s.sign_up_box}>
				<h2 className={s.title}>Sign Up</h2>

				<form
					onSubmit={handleSubmit}
					// action="/submit"
					// method="post"
					className={s.form}
				>
					<div className={s.credentials_box}>
						<div className={s.credential_detail}>
							<label for="name">Username</label>
							<input type="text" id="username" name="username" required />
						</div>

						<div className={s.credential_detail}>
							<label for="email">Email</label>
							<input type="email" id="email" name="email" required />
						</div>

						<div className={s.credential_detail}>
							<label for="password">Password</label>
							<input type="password" id="password" name="password" required />
						</div>

						{/* <div className={s.credential_detail}>
							<label for="confirmPass">Confirm</label>
							<input
								type="password"
								id="confirmPass"
								name="confirmPass"
								required
							/>
						</div> */}
					</div>

					<FormButton
						isNav={false}
						name={"Sign Up"}
						onClick={verifyCredentials}
					/>
				</form>
			</div>
		);
	}
}
