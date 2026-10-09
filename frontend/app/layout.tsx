import type { Metadata, Viewport } from 'next';
import './globals.css';
export const metadata: Metadata = { title: 'Sahi GST — Invoice clarity. Business confidence.', description: 'Review invoices, understand mismatches and prepare supplier correction requests in one workspace.', manifest: '/manifest.webmanifest' };
export const viewport: Viewport = { themeColor: '#155d48' };
export default function RootLayout({ children }: Readonly<{children: React.ReactNode}>) { return <html lang="en"><body>{children}</body></html>; }
