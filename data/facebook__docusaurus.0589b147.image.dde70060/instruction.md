# Bug Report

### Describe the bug

I'm having an issue with image rendering in MDX where the `alt` attribute is not being set correctly on `<img>` elements when the `alt` value is an empty string. It seems like empty strings are being treated as falsy and the alt attribute is being omitted entirely, even though an empty alt attribute is valid and semantically different from a missing alt attribute.

### Reproduction

```mdx
![](image.jpg)
```

When the above MDX is processed, the resulting HTML should include `alt=""` but instead the alt attribute is completely missing from the img tag.

### Expected behavior

Images with empty alt text should render with `alt=""` attribute present. An empty alt attribute has semantic meaning (decorative image) and is different from no alt attribute at all (which is an accessibility issue).

The generated HTML should be:
```html
<img src="image.jpg" alt="">
```

But currently it's generating:
```html
<img src="image.jpg">
```

### Additional context

This affects accessibility since screen readers treat missing alt attributes differently than empty alt attributes. Empty alt tells screen readers to skip the image (decorative), while missing alt is an error that screen readers will announce.

---
Repository: /testbed
