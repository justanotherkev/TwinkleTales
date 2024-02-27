"use client";
import FormButton from "../form-button/form-button";
import s from "./login-box.module.css";
import { useSignIn } from "@clerk/nextjs";

export default function LoginBox() {
	const { signIn, isActive, isLoaded } = useSignIn();

	const verifyCredentials = () => {
		console.log("Verifying credentials...");
	};

	const handleSubmit = async (e) => {
		console.log("Submitting...");
		e.preventDefault();

		const username = e.target.username.value;
		const password = e.target.password.value;

		console.log(username);
		console.log(password);
	};

	if (!isLoaded) {
		return (
			<div className={s.login_box}>
				<h2 className={s.title}>Loading...</h2>
			</div>
		);
	} else {
		return (
			<div className={s.login_box}>
				<h2 className={s.title}>Login</h2>

				<form
					onSubmit={handleSubmit}
					// action="/submit"
					// method="post"
					className={s.form}
				>
					<div className={s.credentials_box}>
						<div className={s.credential_detail}>
							<label for="username">Username</label>
							<input type="text" id="username" name="username" required />
						</div>

						<div className={s.credential_detail}>
							<label for="password">Password</label>
							<input type="password" id="password" name="password" required />
						</div>
					</div>

					{/* <div class="continue-with-google">
						<span>Continue with Google</span>
					</div>
					<div class="continue-with-facebook">
						<span>Continue with Facebook</span>
					</div> */}

					<FormButton
						isNav={false}
						name={"Login"}
						onClick={verifyCredentials}
					/>
				</form>
			</div>
		);
	}
}

// autofill ofr STT
// upgrade to GPT 3.5
//nltk psacy for prompt gen
// use summariser
