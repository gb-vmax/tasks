# Bug Report

### Describe the bug

I'm experiencing an issue with markdown image rendering when using URLs that contain certain characters. It seems like the angle bracket wrapping behavior for image URLs has changed and is now producing incorrect output.

### Reproduction

```js
const imageNode = {
  type: 'image',
  url: 'https://example.com/image.png',
  title: 'My Image'
}

// The generated markdown output is wrapping the URL in angle brackets
// when it shouldn't be
```

When I try to render an image with a standard URL (no special characters or whitespace), the output is wrapping it in `<>` brackets like `![](<https://example.com/image.png> "title")` instead of the expected `![](https://example.com/image.png "title")`.

### Expected behavior

URLs without control characters or whitespace should not be wrapped in angle brackets. Only URLs that contain special characters (control characters, whitespace, etc.) should get the angle bracket treatment.

The current behavior seems to be doing the opposite - wrapping normal URLs and not wrapping URLs that should be wrapped.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
