import { visit } from "unist-util-visit";

// This plugin turns `::slides` into iframes.
/** @type {import('unified').Plugin<[], import('mdast').Root>} */
export default function slidesDirective() {
  return (tree, file) => {
    visit(tree, (node) => {
      if (
        node.type === "textDirective" ||
        node.type === "leafDirective" ||
        node.type === "containerDirective"
      ) {
        if (node.name !== "slides") return;

        const data = node.data || (node.data = {});
        const attributes = node.attributes || {};
        const id = attributes.id;

        if (node.type === "textDirective")
          file.fail("Text directives for `slides` not supported", node);
        if (!id) file.fail("Missing slides id", node);

        data.hName = "iframe";
        data.hProperties = {
          src: "https://docs.google.com/presentation/d/e/" + id + "/embed?start=false",
          width: 768,
          height: 455,
          frameBorder: 0,
          allowFullScreen: true,
          mozallowfullscreen: true,
          webkitallowfullscreen: true,
        };
      }
    });
  };
}
