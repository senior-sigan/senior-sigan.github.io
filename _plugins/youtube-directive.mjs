import { visit } from "unist-util-visit";

// This plugin turns `::youtube` into iframes.
/** @type {import('unified').Plugin<[], import('mdast').Root>} */
export default function youtubeDirective() {
  return (tree, file) => {
    visit(tree, (node) => {
      if (
        node.type === "textDirective" ||
        node.type === "leafDirective" ||
        node.type === "containerDirective"
      ) {
        if (node.name !== "youtube") return;

        const data = node.data || (node.data = {});
        const attributes = node.attributes || {};
        const id = attributes.id;

        if (node.type === "textDirective")
          file.fail("Text directives for `youtube` not supported", node);
        if (!id) file.fail("Missing video id", node);

        data.hName = "iframe";
        data.hProperties = {
          src: "https://www.youtube.com/embed/" + id,
          width: 640,
          height: 360,
          frameBorder: 0,
          allow: "picture-in-picture",
          allowFullScreen: true,
        };
      }
    });
  };
}
