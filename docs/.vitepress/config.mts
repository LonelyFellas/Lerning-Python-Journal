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
          { text: "Pack Unpack", link: "/basic/pack-unpack.md" },
          { text: "String", link: "/basic/string.md" },
          { text: "Set", link: "/basic/set.md" },
          { text: "Dict", link: "/basic/dict.md" },
        ],
      },
      {
        text: "Function",
        collapsed: true,
        items: [
          { text: "All", link: "/functions/all.md" },
          { text: "Range", link: "functions/range.md" },
          { text: "Zip", link: "functions/zip.md" },
          { text: "Attr", link: "functions/attr.md" },
          { text: "Decorator", link: "functions/decorator.md" },
        ],
      },
      {
        text: "Module",
        collapsed: true,
        items: [{ text: "Datetime", link: "modules/datetime.md" }],
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
