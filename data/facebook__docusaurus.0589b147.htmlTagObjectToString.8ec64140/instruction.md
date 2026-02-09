# Bug Report

### Describe the bug

When using `injectHtmlTags` to add custom HTML tags with attributes to the site, the generated HTML output is malformed. Attributes are being wrapped in an extra array, causing them to be rendered incorrectly in the final HTML.

### Reproduction

```js
// In docusaurus.config.js
module.exports = {
  plugins: [
    function myPlugin() {
      return {
        name: 'my-plugin',
        injectHtmlTags() {
          return {
            headTags: [
              {
                tagName: 'meta',
                attributes: {
                  name: 'description',
                  content: 'My site description',
                },
              },
            ],
          };
        },
      };
    },
  ],
};
```

### Expected behavior

The generated HTML should be:
```html
<meta name="description" content="My site description">
```

### Actual behavior

The attributes are not being joined correctly, resulting in malformed HTML output where the attributes appear to be concatenated incorrectly.

### System Info

- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

This seems to have broken recently and is affecting the generation of meta tags, link tags, and other custom HTML elements injected through plugins.

---
Repository: /testbed
