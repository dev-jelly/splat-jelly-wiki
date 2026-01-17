export default {
  content: ["./src/content/**/*.{md,mdx}", "./src/components/**/*.{astro,tsx}"],
  theme: {
    extend: {
      colors: {
        salmon: {
          primary: '#ff7300',
          secondary: '#ff5033',
          accent: '#b2ff00',
          cyan: '#00f5ff',
          dark: '#0f172a',
          light: '#f8fafc'
        }
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
        display: ['Outfit', 'sans-serif'],
      }
    }
  },
  darkMode: 'class'
}
