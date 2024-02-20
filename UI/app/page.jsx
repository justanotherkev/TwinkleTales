import HeaderTitle from "@/components/header-title/header-title";
import s from "./page.module.css";
import Link from "next/link";

export default function Home() {
  return (
    <div className={s.home}>
      <HeaderTitle />
      <div className={s.body}>
        <div className={s.image}></div>
        <div className={s.get_started}>
          <div className={s.get_started_text}>
            <h2>Get started</h2>
            <p>
              Explore captivating stories tailored to your child's imagination
            </p>
          </div>

          <div className={s.get_started_actions}>
            <Link href="./login" className={s.link}>
              <div className={s.link_button}>Login</div>
            </Link>
            <Link href="./sign-up" className={s.link}>
              <div className={s.link_button}>Sign Up</div>
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}

// import sound from "../public/welcome_background_music.mp3";

// function play() {
// new Audio(sound).play();
// }
// play();
