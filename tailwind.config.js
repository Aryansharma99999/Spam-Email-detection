export default {
  content: ['./index.html', './src/**/*.{js,jsx}'],
  theme: {
    extend: {
      colors: {
        cyber: {
          bg: '#050816',
          panel: 'rgba(8, 15, 32, 0.72)',
          border: 'rgba(0, 255, 159, 0.26)',
          green: '#00ff9f',
          blue: '#00eaff',
          red: '#ff4d6d',
        },
      },
      fontFamily: {
        display: ['Orbitron', 'sans-serif'],
        mono: ['JetBrains Mono', 'monospace'],
      },
      boxShadow: {
        neon: '0 0 20px rgba(0, 255, 159, 0.45)',
        blue: '0 0 24px rgba(0, 234, 255, 0.35)',
        danger: '0 0 24px rgba(255, 77, 109, 0.45)',
      },
      backgroundImage: {
        radar: 'radial-gradient(circle at top, rgba(0, 234, 255, 0.18), transparent 35%), radial-gradient(circle at bottom, rgba(0, 255, 159, 0.18), transparent 30%)',
      },
      keyframes: {
        pulseGlow: {
          '0%, 100%': { opacity: '0.45', transform: 'scale(1)' },
          '50%': { opacity: '0.95', transform: 'scale(1.02)' },
        },
        scanLine: {
          '0%': { transform: 'translateY(-120%)' },
          '100%': { transform: 'translateY(120%)' },
        },
        gridMove: {
          '0%': { transform: 'translateY(0px)' },
          '100%': { transform: 'translateY(40px)' },
        },
      },
      animation: {
        pulseGlow: 'pulseGlow 2.4s ease-in-out infinite',
        scanLine: 'scanLine 5s linear infinite',
        gridMove: 'gridMove 8s linear infinite alternate',
      },
    },
  },
  plugins: [],
};
