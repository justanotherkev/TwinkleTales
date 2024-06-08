"use client";
import PageComponent from "@/components/page-component/page-component";
import SignUpBox from "@/components/sign-up-box/sign-up-box";
import { useRouter } from "next/navigation";

export default function SignUp() {
  const router = useRouter();

  const handleRouting = () => {
    router.push("/tutorial");
  };

  return (
    <PageComponent
      src={"/login-signup-img.png"}
      form_component={<SignUpBox handleRouting={handleRouting} />}
    />
  );
}
