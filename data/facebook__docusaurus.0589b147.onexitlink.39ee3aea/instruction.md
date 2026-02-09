# Bug Report

### Describe the bug

I'm experiencing an issue with markdown link parsing where regular links (with URLs) are being incorrectly treated as reference-style links, and reference-style links are being treated as regular links. The behavior seems to be inverted.

### Reproduction

```js
// Example 1: Regular link with URL
const markdown = '[example](https://example.com)';
// Expected: Should parse as a regular link with url property
// Actual: Being parsed as a reference link with identifier/label

// Example 2: Reference-style link
const markdown2 = '[example][ref]';
// Expected: Should parse as a reference link
// Actual: Being parsed as a regular link with url property
```

When parsing markdown links, the type and properties assigned to link nodes appear to be backwards. Regular inline links are getting `type: "linkReference"` and reference properties, while actual reference links are getting treated as regular links with url/title properties.

### Expected behavior

- Links with explicit URLs like `[text](url)` should be parsed as regular links with `url` and `title` properties
- Reference-style links like `[text][ref]` should be parsed as link references with `identifier`, `label`, and `referenceType` properties

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
