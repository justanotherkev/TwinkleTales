"use client";
import Button from "../../components/button-action/button-action.jsx";
import s from "./page.module.css";
// import Image from "next/image";
import React, { useState } from "react";

export default function StoryGeneration() {
  return (
    <div className={s.body}>
      <Button text="New Story" />
      <div className={s.image}></div>
    </div>
  );
}
