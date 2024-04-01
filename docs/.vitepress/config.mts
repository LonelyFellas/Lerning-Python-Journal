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
        collapsed: true,
        items: [
          {
            text: "First Python Program",
            link: "/basic/first-python-program.md",
          },
          { text: "Loop-else", link: "/basic/loop-else.md" },
          { text: "Data type", link: "/basic/data-type.md" },
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
