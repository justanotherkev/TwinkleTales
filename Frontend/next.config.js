/** @type {import('next').NextConfig} */

module.exports = {
	images: {
		domains: ["replicate.delivery"],
	},
};

const nextConfig = {
	reactStrictMode: false,
	images: {
		remotePatterns: [
			{
				protocol: "https",
				hostname: "replicate.com",
			},
			{
				protocol: "https",
				hostname: "replicate.delivery",
			},
		],
	},
	rewrites: async () => {
		return [
			{
				source: "/api/:path*",
				destination:
					process.env.NODE_ENV === "development"
						? "http://127.0.0.1:8000/api/:path*"
						: "/api/",
			},
			{
				source: "/docs",
				destination:
					process.env.NODE_ENV === "development"
						? "http://127.0.0.1:8000/docs"
						: "/api/docs",
			},
			{
				source: "/openapi.json",
				destination:
					process.env.NODE_ENV === "development"
						? "http://127.0.0.1:8000/openapi.json"
						: "/api/openapi.json",
			},
		];
	},
};

module.exports = nextConfig;
