import React from "react";
import s from "./subscription-card.module.css";

export default function SubscriptionCard(props) {
	return (
		<div className={s.subscription_card}>
			<div className={s.details_box}>
				<h1>{props.title}</h1>
				<h2>${props.price}</h2>
				<p>{props.description}</p>
			</div>
			<button>Buy now</button>
		</div>
	);
}
