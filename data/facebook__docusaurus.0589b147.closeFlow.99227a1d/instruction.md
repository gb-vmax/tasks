# Bug Report

### Describe the bug

I'm encountering a crash when processing MDX documents with certain container structures. The application throws an error about trying to access properties on `undefined`, specifically when calling `write()` on what appears to be a `childFlow` object that has already been set to `undefined`.

### Reproduction

```js
// This seems to happen when processing MDX content with nested containers
const mdx = `
# Heading

Some content with containers
`;

// Process the MDX - crashes during flow closing
compile(mdx);
```

The error occurs during document initialization when the flow is being closed. It looks like there's an attempt to call a method on an object after it's been cleared.

### Expected behavior

The MDX content should compile successfully without throwing errors about undefined references.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
