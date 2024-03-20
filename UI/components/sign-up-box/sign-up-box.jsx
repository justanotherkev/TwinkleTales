("use client");
import { useState } from "react";
import FormButton from "../form-button/form-button";
import s from "./sign-up-box.module.css";
import { useSignUp } from "@clerk/nextjs";
import { useRouter } from "next/navigation";

export default function SignUpBox() {
  const { isLoaded, signUp, setActive } = useSignUp();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [pendingVerification, setPendingVerification] = useState(false);
  const [username, setUsername] = useState("");
  const [code, setCode] = useState("");

  const handleSubmit = async (e) => {
    console.log("Submitting credentials...");
    e.preventDefault();

    if (!isLoaded) {
      return;
    }

    try {
      console.log("in try block handleSubmit");
      await signUp.create({
        emailAddress: email,
        password: password,
      });

      await signUp.prepareEmailAddressVerification({ strategy: "email_code" });

      setPendingVerification(true);
    } catch (error) {
      console.error(JSON.stringify(error, null, 2));
    }
  };

  const verifyCode = async (e) => {
    console.log("Verifying code...");
    e.preventDefault();

    setCode(e.target.code.value);
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
        console.log(JSON.stringify(completeSignUp, null, 2));
      }

      if (completeSignUp.status === "complete") {
        await setActive({ session: completeSignUp.createdSessionId });
        console.log("Pushing route /prompt");
        props.handleRouting;
      }
    } catch (error) {
      console.error(JSON.stringify(error, null, 2));
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
          </form>
        ) : (
          <form
            onSubmit={verifyCode}
            // action="/submit"
            // method="post"
            className={s.form}
          >
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
          </form>
        )}
      </div>
    );
  }
}
