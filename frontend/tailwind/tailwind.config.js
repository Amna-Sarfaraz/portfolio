// tailwind.config.js
module.exports = {
  content: [
    "../backend/portfolio/templates/**/*.html",
    "../backend/portfolio/static/js/**/*.js",
  ],
  theme: {
    extend: {
      colors: {
        noir: "#0f0f0f",
        parchment: "#f5f1e8",
        antique: "#c9a24d",
      },
    },
  },
  plugins: [],
}
