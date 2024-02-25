"use client";
import Button from "../../components/button-action/button-action.jsx";
import s from "./page.module.css";
import Image from "next/image";
import React, { useState } from "react";
import PageComponent from "../../components/page-component-2/page-component-2.jsx";

export function story_box() {
  return <div className="container"></div>;
}

export default function story_generation() {
  return (
    <PageComponent
      // src={"../../public/story-prompt-img.png"}
      src={"/story-prompt-img.png"}
      form_component={<story_box />}
    />
  );
}
// export default function StoryGeneration() {
//   return (
//     <div className={s.body}>
//       <Button text="New Story" />
//       <div className={s.image}></div>
//     </div>

//   );
// }
