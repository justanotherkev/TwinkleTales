import { Inter } from "next/font/google";
import { ClerkProvider } from "@clerk/nextjs";
import "./globals.css";
import "./imports.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata = {
  title: "TwinkleTales",
  description: "A story generating application for kids",
};

const clerkFrontendApi = process.env.NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY;
const clerkApiKey = process.env.CLERK_API_KEY;

export default function RootLayout({ children }) {
  return (
    <ClerkProvider publishableKey={clerkFrontendApi}>
      <html lang="en">
        <body className={inter.className}>{children}</body>
      </html>
    </ClerkProvider>
  );
}
