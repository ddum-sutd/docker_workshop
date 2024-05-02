// next.config.js

/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    appDir: true,
  },
  async rewrites() {
    return [
      {
        source: '/api/student/:path*',
        destination: 'http://app:5000/student/:path*',
      },
    ];
  },
};

module.exports = nextConfig;