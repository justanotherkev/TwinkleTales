import Button from "../../components/button-action/button-action.jsx";
import s from "./page.module.css";
import Image from "next/image";

export default function StoryGeneration() {
  return (
    <div>
      <Button text="New Story" />
      <div className={s.image}></div>
    </div>
  );
}
