"use client";
import Link from "next/link";
import React from "react";
import s from "./navigate.module.css";

export default function ButtonNavigation(props) {
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
