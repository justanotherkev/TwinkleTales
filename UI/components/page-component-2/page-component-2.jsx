import HeaderTitle from "../header-title/header-title.jsx";
import s from "./page-component-2.module.css";
import Image from "next/image";

export default function PageComponent(props) {
  return (
    <div className={s.body}>
      <div className={s.image}>
        <Image src={props.src} width={650} height={650} />
      </div>
      <div className={s.container}>{props.form_component}</div>
    </div>
  );
}
