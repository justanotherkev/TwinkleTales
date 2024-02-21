import { SignIn } from "@clerk/nextjs";
import PageComponent from "@/components/page-component/page-component";

export default function Login() {
	return (
		<PageComponent src={"/login-signup-img.png"} form_component={<SignIn />} />
	);
}
