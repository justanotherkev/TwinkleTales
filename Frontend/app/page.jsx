"use client";

import PageComponent from "@/components/page-component/page-component";
import GetStartedBox from "@/components/get-started-box/get-started-box";
import { useRouter } from "next/navigation";
import { useUser } from "@clerk/nextjs";

export default function Home() {
	const router = useRouter();
	const user = useUser();
	if (user.isSignedIn) {
		router.push("/theme-selection");
	}

	return (
		<PageComponent
			src={"/get-started-img.png"}
			form_component={<GetStartedBox />}
		/>
	);
}
