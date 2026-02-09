# Bug Report

### Describe the bug
When rendering images in MDX, the `src` attribute is not being set on the resulting `<img>` elements. The image source URL appears to be getting lost during the transformation process, causing images to fail to load.

### Reproduction
```jsx
// test.mdx
![Alt text](https://example.com/image.png "Image title")
```

When this MDX is processed, the resulting HTML `<img>` element is missing the `src` attribute entirely. The `alt` and `title` attributes are present, but without `src` the image cannot be displayed.

### Expected behavior
The `<img>` element should have a `src` attribute with the URL from the markdown image syntax. For the example above, the output should include `src="https://example.com/image.png"`.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have started recently. Images were rendering correctly before, but now all images in my MDX files are broken because they're missing the source URL.

---
Repository: /testbed
