// import { SignUp } from "@clerk/nextjs";
import PageComponent from "@/components/page-component/page-component";
import LoginBox from "@/components/login-box/login-box";

export default function Login() {
	return (
		<PageComponent
			src={"/login-signup-img.png"}
			form_component={<LoginBox />}
		/>
	);
}
