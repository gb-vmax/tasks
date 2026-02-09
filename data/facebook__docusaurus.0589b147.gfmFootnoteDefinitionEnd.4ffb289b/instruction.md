# Bug Report

### Describe the bug

When parsing markdown with footnote definitions using the GFM (GitHub Flavored Markdown) parser, I'm getting errors about unmatched exit calls. The parser seems to be trying to exit a container twice, which causes the parsing to fail or behave unexpectedly.

### Reproduction

```js
const markdown = `
Here is some text with a footnote[^1].

[^1]: This is the footnote definition.
`;

// Parse the markdown with GFM enabled
const result = parseMarkdown(markdown);
// Error: Cannot exit container, already exited
```

### Expected behavior

The footnote definition should be parsed correctly without any errors. The parser should properly handle the container exit for footnote definitions.

### Additional context

This seems to happen specifically with footnote definitions. Regular footnotes and other GFM features work fine, but when a footnote definition is encountered, the parser throws an error about trying to exit a container that's already been exited.

---
Repository: /testbed
