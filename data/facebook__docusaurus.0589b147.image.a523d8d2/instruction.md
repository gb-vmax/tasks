# Bug Report

### Describe the bug

I'm encountering an issue with image rendering in MDX where the `alt` attribute is being set incorrectly on `<img>` elements. It appears that images without alt text are getting the alt attribute set to `null` or `undefined`, while images that actually have alt text are not getting the attribute at all.

### Reproduction

```mdx
![Image with alt text](image.jpg)

![](image-no-alt.jpg)
```

When rendering the above MDX:
- The first image (with alt text) doesn't have an `alt` attribute in the output HTML
- The second image (without alt text) has `alt="null"` or `alt="undefined"` in the output HTML

### Expected behavior

Images with alt text should have the `alt` attribute set to the provided text, and images without alt text should not have the `alt` attribute (or it should be an empty string).

Expected output:
```html
<img src="image.jpg" alt="Image with alt text" />
<img src="image-no-alt.jpg" />
```

### Additional context

This seems like a regression as it was working correctly in previous versions. The logic for when to include the alt attribute appears to be inverted.

---
Repository: /testbed
