import type { NextConfig } from 'next';
const config: NextConfig = {
  output: process.env.NODE_ENV === 'production' ? 'export' : undefined,
  images: { unoptimized: true },
  ...(process.env.NODE_ENV !== 'production' ? { async rewrites() { return [{ source: '/api/:path*', destination: 'http://127.0.0.1:8000/api/:path*' }, { source: '/accounts/:path*', destination: 'http://127.0.0.1:8000/accounts/:path*' }]; } } : {}),
};
export default config;
