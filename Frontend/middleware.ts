import { authMiddleware } from "@clerk/nextjs";

export default authMiddleware({
	// Use for deployment
	publicRoutes: ["/", "/login", "/sign-up"],

	// Use for development
	// publicRoutes: ["/", "/login", "/sign-up", "/prompt", "/story-generation", "/theme-selection", "/tutorial"],
});

export const config = {
	matcher: ["/((?!.+\\.[\\w]+$|_next).*)", "/", "/(api|trpc)(.*)"],
};
