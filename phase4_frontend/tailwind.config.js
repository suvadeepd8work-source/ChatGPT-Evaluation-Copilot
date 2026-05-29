/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        chatgpt: {
          gray: '#212121',
          sidebar: '#171717',
          hover: '#2f2f2f',
          text: '#ececec',
          secondary: '#b4b4b4'
        },
        evaluation: {
          primary: '#10a37f',
          warning: '#f4ac36',
          error: '#ef4444',
          info: '#3b82f6',
          background: '#1a1a1a'
        }
      }
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
}
