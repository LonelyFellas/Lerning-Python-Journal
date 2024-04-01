import { defineConfig } from "vitepress";

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Lerning python juarnal",
  description: "A VitePress Site",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: "Home", link: "/" },
      { text: "Basic", link: "/basic/first-python-program" },
    ],

    sidebar: [
      {
        text: "Basic",
        items: [
          {
            text: "first-python-program",
            link: "/basic/first-python-program.md",
          },
          { text: "loop-else", link: "/basic/loop-else.md" },
        ],
      },
    ],

    socialLinks: [
      {
        icon: "github",
        link: "https://github.com/LonelyFellas/Lerning-Python-Journal",
      },
    ],
  },
});
