const syntaxHighlight = require("@11ty/eleventy-plugin-syntaxhighlight");
//const mathjaxPlugin = require("eleventy-plugin-mathjax");
const mathjaxPlugin = require("@sunt-programator/eleventy-plugin-mathjax");
/*const Image = require("@11ty/eleventy-img");*/
const markdownItImageCaption = require("@andatoshiki/markdown-it-image-caption");
const eleventyNavigationPlugin = require("@11ty/eleventy-navigation");
//const mdownmjax = require("markdown-it-mathjax3")

const markdownItTable = require("markdown-it-multimd-table");

const embedEverything = require("eleventy-plugin-embed-everything");

module.exports = function(eleventyConfig) {
  eleventyConfig.addPlugin(syntaxHighlight);
  eleventyConfig.addPlugin(eleventyNavigationPlugin);
  eleventyConfig.addPlugin(embedEverything);
  eleventyConfig.addPlugin(mathjaxPlugin, {
  outputFormat: 'svg',tex: {tags: 'ams'}});
  //eleventyConfig.addPlugin(EleventyRenderPlugin);
  eleventyConfig.addPassthroughCopy('assets');
  eleventyConfig.addPassthroughCopy("hiking/grays_torreys_kelso/*.jpg");
  eleventyConfig.addPassthroughCopy("hiking/wetterhorn_loop/*.jpg");
  eleventyConfig.addPassthroughCopy("hiking/**/*.png");
  eleventyConfig.addPassthroughCopy("hiking/**/*.jpg");
  eleventyConfig.addPassthroughCopy("ramblings/**/*.jpg");
  eleventyConfig.addPassthroughCopy("ramblings/**/*.png");
  eleventyConfig.addPassthroughCopy("engineering/drone/*.png");
  eleventyConfig.addPassthroughCopy("engineering/drone/**/*.png");
  eleventyConfig.addPassthroughCopy("engineering/drone/*/*.png");
  eleventyConfig.addPassthroughCopy("engineering/drone/*.jpg");
  eleventyConfig.addPassthroughCopy("engineering/drone/**/*.jpg");
  eleventyConfig.addPassthroughCopy("engineering/drone/*/*.jpg");
  eleventyConfig.addPassthroughCopy("engineering/resume/*.png");
  eleventyConfig.addPassthroughCopy("engineering/drone/*/*.html_");
  eleventyConfig.addPassthroughCopy("engineering/drone/*/*.svg");
  eleventyConfig.addPassthroughCopy("engineering/drone/**/*.svg");

  
  eleventyConfig.addPassthroughCopy("engineering/computer_graphics/ray_tracer/*.png");
  eleventyConfig.addPassthroughCopy("engineering/computer_graphics/ray_tracer/*.jpg");

  eleventyConfig.addPassthroughCopy("engineering/**/*.png");
  eleventyConfig.addPassthroughCopy("engineering/**/*.jpg");

  eleventyConfig.addPassthroughCopy("engineering/computer_graphics/**/*.png");
  eleventyConfig.addPassthroughCopy("engineering/computer_graphics/**/*.jpg");

  eleventyConfig.addPassthroughCopy({ 
    "node_modules/reveal.js/dist": "assets/reveal/",
    "node_modules/reveal.js/plugin": "assets/reveal/plugin",
});

  eleventyConfig.addLayoutAlias('default', 'default.njk');
  eleventyConfig.amendLibrary("md", mdLib => mdLib.use(markdownItImageCaption));
  eleventyConfig.setChokidarConfig({
		usePolling: true,
		interval: 500,
	});
  //eleventyConfig.amendLibrary("md", mdLib => mdLib.use(markdownItTable));
  //eleventyConfig.amendLibrary("md", mdLib => mdLib.use(mdownmjax, { tex: {tags: 'ams'} }));
  /*eleventyConfig.addShortcode("image", async function(src, alt) {
		return `<img src="${src}" class="img-fluid" loading="lazy" decoding="async">`;
	});*/

  return {
    passthroughFileCopy: true
  }
};