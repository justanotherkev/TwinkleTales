// import Image from "next/image";
// import s from "./page.module.css";
"use client";
import Link from "next/link";
import React from "react";
import s from "./back-button.module.css";

export default function BackButton(props) {
  return (
    <div>
      <div className={s.button}>
        <Link className={s.buttonText} href="../../login">
          {props.text}
        </Link>
      </div>
    </div>
  );
}
