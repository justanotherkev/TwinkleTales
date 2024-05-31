import React from "react";
import s from "./page.module.css";
import HeaderTitle from "@/components/header-title/header-title";
import SubscriptionCard from "../../components/subscription-card/subscription-card";

export default function Subscription() {
	return (
		<div className={s.subscription_page}>
			<HeaderTitle line1="Subscription" line2="" />

			<div className={s.subscription_box}>
				<SubscriptionCard
					title="Free Plan"
					price="0.00"
					description="Enjoy 3 stories per month for free."
				/>
				<SubscriptionCard
					title="Daily Plan"
					price="1.99/day"
					description="Get 5 stories for a day. Perfect for short-term access!"
				/>
				<SubscriptionCard
					title="Weekly Plan"
					price="5.99/week"
					description="Get 40 stories for a whole week. Dive into endless adventures!"
				/>
				<SubscriptionCard
					title="Monthly Plan"
					price="14.99/month"
					description="Unlimited stories all month long. Ideal for regular creators!"
				/>
			</div>
		</div>
	);
}
