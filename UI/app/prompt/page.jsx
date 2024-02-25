import Button from "../../components/button-action/button-action.jsx";
import BackButton from "../../components/back-button/back-button.jsx";
import s from "./page.module.css";
// import Image from "next/image";

export default function Prompt() {
  return (
    <div className={s.body}>
      <Button text="Tap to speak" />
      <BackButton text="Go Back" />
      <div className={s.image}></div>
      <div className={s.backgroundImage}></div>
    </div>
  );
}

<Button text={"Home"} />;
