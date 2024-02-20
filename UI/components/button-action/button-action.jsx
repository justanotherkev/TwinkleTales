"use client";
import s from "./button-action.module.css";

export default function ButtonAction(props) {
  // const handleClick = () => {};
  return (
    <>
      {/* button className={s.button} onClick={handleClick} */}
      <button className={s.button}>{props.text}</button>
    </>
  );
}
