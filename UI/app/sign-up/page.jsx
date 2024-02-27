import PageComponent from "@/components/page-component/page-component";
import SignUpBox from "@/components/sign-up-box/sign-up-box";

export default function SignUp() {
	return (
		<PageComponent
			src={"/login-signup-img.png"}
			form_component={<SignUpBox />}
		/>
	);
}
