import Button from "../../components/button-action/button-action.jsx";
import ButtonNavigation from "../../components/navigate/navigation-button.jsx";
import s from "./page.module.css";
// import Image from "next/image";

export default function Prompt() {
  return (
    <div className={s.body}>
      <Button text="Tap to Speak" />
      <ButtonNavigation text="Go Back" />
      <div className={s.image}></div>
      <div className={s.backgroundImage}></div>
    </div>
  );
}

<Button text={"Home"} />;
