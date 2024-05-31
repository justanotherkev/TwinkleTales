"use client";
import { useRouter } from "next/navigation";
import FormButton from "../form-button/form-button";
import s from "./login-box.module.css";
import { useSignIn } from "@clerk/nextjs";
import { useState } from "react";
import Link from "next/link";

export default function LoginBox() {
	const { isLoaded, signIn, setActive } = useSignIn();
	const [email, setEmail] = useState("");
	const [password, setPassword] = useState("");
	const [errorMsg, setErrMsg] = useState("");
	const router = useRouter();

	// start the sign In process.
	const handleSubmit = async (e) => {
		console.log("Submitting credentials");
		e.preventDefault();

		setEmail(e.target.email.value);
		setPassword(e.target.password.value);

		if (!isLoaded) {
			return;
		}

		// Attempt to create the user
		try {
			const result = await signIn.create({
				identifier: email,
				password: password,
			});

			if (result.status === "complete") {
				console.log(result);
				await setActive({ session: result.createdSessionId });
				router.push("/theme-selection");
			} else {
				console.log(result);
			}
		} catch (error) {
			console.table("error", error.errors[0].longMessage);
			setErrMsg(error.errors[0].longMessage);
			// console.table("Error when logging in: "+ completeS);
			// console.table(JSON.stringify(completeSignUp, null, 2));
		}
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
					className={s.form}
				>
					<div className={s.credentials_box}>
						<div className={s.credential_detail}>
							<label for="email">Email</label>
							<input
								onChange={(e) => setEmail(e.target.value)}
								type="email"
								id="email"
								name="email"
								required
							/>
						</div>

						<div className={s.credential_detail}>
							<label for="password">Password</label>
							<input
								onChange={(e) => setPassword(e.target.value)}
								type="password"
								id="password"
								name="password"
								required
							/>
						</div>
					</div>

					{/* <p>Forgot password</p> */}

					<FormButton isNav={false} name={"Login"} type={"submit"} />
					<p className={s.go_to_signup}>
						No account?{" "}
						<span>
							<Link href="/sign-up">Create one</Link>
						</span>
					</p>
				</form>
				<p className={s.error_message}>{errorMsg}</p>
			</div>
		);
	}
}

