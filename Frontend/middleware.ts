import { authMiddleware } from "@clerk/nextjs";

export default authMiddleware({
	// publicRoutes: ["/", "/login", "/sign-up"],
	publicRoutes: ["/", "/login", "/sign-up", "/prompt", "/story-generation"],
});

export const config = {
	matcher: ["/((?!.+\\.[\\w]+$|_next).*)", "/", "/(api|trpc)(.*)"],
};
