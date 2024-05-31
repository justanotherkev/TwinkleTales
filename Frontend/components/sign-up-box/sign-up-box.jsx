"use client";
import { useState } from "react";
import FormButton from "../form-button/form-button";
import s from "./sign-up-box.module.css";
import { useSignUp } from "@clerk/nextjs";
import { useRouter } from "next/navigation";
import Link from "next/link";

export default function SignUpBox() {
	const { isLoaded, signUp, setActive } = useSignUp();

	const [username, setUsername] = useState("");
	const [email, setEmail] = useState("");
	const [password, setPassword] = useState("");

	const [pendingVerification, setPendingVerification] = useState(false);
	const [code, setCode] = useState("");
	const [errorMsg, setErrorMsg] = useState("");

	const router = useRouter();

	const handleSubmit = async (e) => {
		console.log("Submitting credentials...");
		e.preventDefault();

		if (!isLoaded) {
			return;
		}

		try {
			console.log("in try block handleSubmit");
			console.log("Username: " + username);
			console.log("Email: " + email);
			console.log("Password: " + password);

			await signUp.create({
				username: username,
				emailAddress: email,
				password: password,
			});

			// Sends the email with verification code
			await signUp.prepareEmailAddressVerification({ strategy: "email_code" });

			setPendingVerification(true);
			setErrorMsg("");
		} catch (error) {
			console.log(JSON.stringify(error, null, 2));
			console.log(error.errors[0].message);
			setErrorMsg(error.errors[0].message);
		}
	};

	const verifyCode = async (e) => {
		console.log("Verifying code...");
		e.preventDefault();

		// setCode(e.target.code.value);
		console.log("Code entered: " + code);

		if (!isLoaded) {
			return;
		}

		try {
			console.log("in try block verifyCode");
			const completeSignUp = await signUp.attemptEmailAddressVerification({
				code: code,
			});

			if (completeSignUp.status !== "complete") {
				console.log("Could not complete signup");
				console.log(JSON.stringify(completeSignUp, null, 2));
			}

			if (completeSignUp.status === "complete") {
				console.log("Signup completed");
				await setActive({ session: completeSignUp.createdSessionId });
				console.log("Pushing route /theme-selection");
				router.push("/theme-selection");
			}
		} catch (error) {
			console.log(JSON.stringify(error, null, 2));
			setErrorMsg(error.errors[0].message);
		}
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

				{!pendingVerification ? (
					<>
						<form
							onSubmit={handleSubmit}
							action="/submit"
							method="post"
							className={s.form}
						>
							<div className={s.credentials_box}>
								<div className={s.credential_detail}>
									<label for="name">Username</label>
									<input
										onChange={(e) => setUsername(e.target.value)}
										type="text"
										id="username"
										name="username"
										required
									/>
								</div>

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

							<FormButton isNav={false} name={"Sign Up"} type={"submit"} />
							<p className={s.error_message}>{errorMsg}</p>

							<p className={s.go_to_signup}>
								Already have an account?{" "}
								<span>
									<Link href="/login">Log in</Link>
								</span>
							</p>
						</form>
					</>
				) : (
					<>
						<form
							onSubmit={verifyCode}
							// action="/submit"
							// method="post"
							className={s.form}
						>
							<div className={s.code_welcome_message}>
								<h3>Welcome {username}</h3>
								<p>
									Please enter the verification code sent to{" "}
									<span>{email}</span>
								</p>
							</div>
							<div className={s.credentials_box}>
								<div className={s.credential_detail}>
									<label for="code">Code</label>
									<input
										onChange={(e) => setCode(e.target.value)}
										type="text"
										id="code"
										name="code"
										required
									/>
								</div>
							</div>

							<FormButton isNav={false} name={"Verify Code"} type={"submit"} />
							<p className={s.error_message}>{errorMsg}</p>
						</form>
					</>
				)}
			</div>
		);
	}
}

// <UserProdile /> component
