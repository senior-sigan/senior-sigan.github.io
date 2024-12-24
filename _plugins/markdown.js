import rehypeHighlight from "rehype-highlight";
import rehypeKatex from "rehype-katex";
import remarkGfm from "remark-gfm";
import remarkMath from "remark-math";
import remarkParse from "remark-parse";
import remarkRehype from "remark-rehype";
import { unified } from "unified";
import rehypeStringify from "rehype-stringify";
import remarkDirective from "remark-directive";
import youtubeDirective from "./youtube-directive.js";
import slidesDirective from "./google-slides.js";
import rehypeRaw from "rehype-raw";

async function createProcessor() {
  // for dynamic imports we have to call .default
  return unified()
    .use(remarkParse)
    .use(remarkDirective)
    .use(youtubeDirective)
    .use(slidesDirective)
    .use(remarkMath)
    .use(remarkGfm)
    .use(remarkRehype, { allowDangerousHtml: true })
    .use(rehypeRaw)
    .use(rehypeKatex)
    .use(rehypeHighlight)
    .use(rehypeStringify);
}

export function eleventyRemark() {
  return {
    render: async (str, data) => {
      const p = await createProcessor();
      const res = await p.data({ eleventy: data }).process(str);
      return res.value;
    },
  };
}
