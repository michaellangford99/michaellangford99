const syntaxHighlight = require("@11ty/eleventy-plugin-syntaxhighlight");
//const mathjaxPlugin = require("eleventy-plugin-mathjax");
const mathjaxPlugin = require("@sunt-programator/eleventy-plugin-mathjax");
/*const Image = require("@11ty/eleventy-img");*/
const markdownItImageCaption = require("@andatoshiki/markdown-it-image-caption");
//const mdownmjax = require("markdown-it-mathjax3")

module.exports = function(eleventyConfig) {
  eleventyConfig.addPlugin(syntaxHighlight);
  eleventyConfig.addPlugin(mathjaxPlugin, {
    outputFormat: 'svg',tex: {tags: 'ams'}});
  eleventyConfig.addPassthroughCopy('assets')
  eleventyConfig.addPassthroughCopy("hiking/grays_torreys_kelso/*.jpg");
  eleventyConfig.addPassthroughCopy("hiking/**/*.png");
  eleventyConfig.addLayoutAlias('default', 'default.njk');
  eleventyConfig.amendLibrary("md", mdLib => mdLib.use(markdownItImageCaption));
  //eleventyConfig.amendLibrary("md", mdLib => mdLib.use(mdownmjax, { tex: {tags: 'ams'} }));
  /*eleventyConfig.addShortcode("image", async function(src, alt) {
		return `<img src="${src}" class="img-fluid" loading="lazy" decoding="async">`;
	});*/

  return {
    passthroughFileCopy: true
  }
};