// import Image from "next/image";
// import s from "./page.module.css";
"use client";
import Link from "next/link";
import React from "react";
import s from "./navigate.module.css";

export default function ButtonNavigation(props) {
	return (
		<div>
			<button className={s.button}>
				<Link className={s.buttonText} href="../../login">
					{props.name}
				</Link>
			</button>
		</div>
	);
}
