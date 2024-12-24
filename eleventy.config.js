import { DateTime } from "luxon";
import { eleventyRemark } from "./_plugins/markdown.js";

/** @param {import("@11ty/eleventy").UserConfig} eleventyConfig */
export default async function (eleventyConfig) {
  eleventyConfig.addPassthroughCopy("assets");
  eleventyConfig.addPassthroughCopy("styles");

  eleventyConfig.addLayoutAlias("post", "layouts/post.njk");
  eleventyConfig.addLayoutAlias("page", "layouts/page.njk");

  eleventyConfig.setLibrary("md", eleventyRemark());

  // https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#valid-date-string
  eleventyConfig.addFilter("htmlDateString", (dateObj) => {
    return DateTime.fromJSDate(dateObj, { zone: "utc" }).toFormat("yyyy-LL-dd");
  });
  eleventyConfig.addFilter("readableDate", (dateObj) => {
    return DateTime.fromJSDate(dateObj, { zone: "utc" }).toFormat(
      "dd LLL yyyy"
    );
  });
  // Get the first `n` elements of a collection.
  eleventyConfig.addFilter("head", (array, n) => {
    if (!Array.isArray(array) || array.length === 0) {
      return [];
    }
    if (n < 0) {
      return array.slice(n);
    }
    return array.slice(0, n);
  });
}

export const config = {
  templateFormats: ["md", "njk", "html"],
  markdownTemplateEngine: false,
  htmlTemplateEngine: "njk",
  dataTemplateEngine: "njk",
  dir: {
    input: ".",
    includes: "_includes",
    output: "_site",
    data: "_data",
  },
};