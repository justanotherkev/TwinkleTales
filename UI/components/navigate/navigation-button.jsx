// import Image from "next/image";
// import s from "./page.module.css";
"use client";
import Link from "next/link";
import React from "react";
import s from "./navigate.module.css";

export default function ButtonNavigation(props) {
<<<<<<< HEAD
  return (
    <div>
      <div className={s.button}>
        <Link className={s.buttonText} href="../../login">
          {props.text}
        </Link>
      </div>
    </div>
  );
=======
	return (
		<div>
			<button className={s.button}>
				<Link className={s.buttonText} href="../../login">
					{props.name}
				</Link>
			</button>
		</div>
	);
>>>>>>> 6e5ebaf4bd7db7acdc04041f1a23ff052ca8bf5e
}
