const syntaxHighlight = require("@11ty/eleventy-plugin-syntaxhighlight");
const mathjaxPlugin = require("eleventy-plugin-mathjax");
/*const Image = require("@11ty/eleventy-img");*/
const markdownItImageCaption = require("@andatoshiki/markdown-it-image-caption");

module.exports = function(eleventyConfig) {
  eleventyConfig.addPlugin(syntaxHighlight);
  eleventyConfig.addPlugin(mathjaxPlugin);
  eleventyConfig.addPassthroughCopy('assets')
  eleventyConfig.addLayoutAlias('default', 'default.njk');
  eleventyConfig.amendLibrary("md", mdLib => mdLib.use(markdownItImageCaption));
  /*eleventyConfig.addShortcode("image", async function(src, alt) {
		return `<img src="${src}" class="img-fluid" loading="lazy" decoding="async">`;
	});*/

  return {
    passthroughFileCopy: true
  }
};