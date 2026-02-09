# Bug Report

### Describe the bug

I'm experiencing an issue with markdown heading parsing where ATX-style headings (headings with `#` symbols) are not being parsed correctly. The heading text seems to be getting cut off or not captured properly, resulting in incomplete or malformed heading nodes.

### Reproduction

```js
const markdown = `
# Hello World
## Another heading with text
### Multiple words in heading
`;

// Parse the markdown
const result = parse(markdown);

// The heading text is incomplete or missing
console.log(result);
```

When parsing ATX headings, the text content after the `#` symbols doesn't seem to be captured correctly. This affects all levels of ATX headings (`#`, `##`, `###`, etc.).

### Expected behavior

The parser should correctly capture the full text content of ATX-style headings. For example, `# Hello World` should produce a heading node with the complete text "Hello World".

### System Info

- remark version: 15.0.1
- Node version: 18.x

This seems to have broken recently, as it was working fine in previous versions. Any help would be appreciated!

---
Repository: /testbed
