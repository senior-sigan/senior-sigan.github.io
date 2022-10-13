async function createProcessor() {
  const rehypeHighlight = await import("rehype-highlight");
  const rehypeKatex = await import("rehype-katex");
  const remarkGfm = await import("remark-gfm");
  const remarkMath = await import("remark-math");
  const remarkParse = await import("remark-parse");
  const remarkRehype = await import("remark-rehype");
  const { unified } = await import("unified");
  const rehypeStringify = await import("rehype-stringify");
  const remarkDirective = await import("remark-directive");
  const youtubeDirective = await import("./youtube-directive.mjs");

  // for dynamic imports we have to call .default
  return unified()
    .use(remarkParse.default)
    .use(remarkDirective.default)
    .use(youtubeDirective.default)
    .use(remarkMath.default)
    .use(remarkGfm.default)
    .use(remarkRehype.default)
    .use(rehypeKatex.default)
    .use(rehypeHighlight.default)
    .use(rehypeStringify.default);
}

function eleventyRemark() {
  return {
    render: async (str, data) => {
      const p = await createProcessor();
      const res = await p.data({ eleventy: data }).process(str);
      return res.value;
    },
  };
}

module.exports = { eleventyRemark };
