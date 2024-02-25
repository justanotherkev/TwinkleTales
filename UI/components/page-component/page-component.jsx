import HeaderTitle from "../header-title/header-title.jsx";
import s from "./page-component.module.css";
import Image from "next/image";

export default function PageComponent(props) {
  return (
    <div className={s.home}>
      <HeaderTitle />
      <div className={s.body}>
        <div className={s.image}>
          <Image src={props.src} width={650} height={650} />
        </div>
        <div className={s.form_box}>{props.form_component}</div>
      </div>
    </div>
  );
}
