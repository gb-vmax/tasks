# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where complex nested structures aren't being processed correctly. It seems like the parser is stopping too early and not fully tokenizing nested elements.

### Reproduction

When parsing markdown with nested structures (like nested emphasis, links inside lists, or code blocks with complex content), the output is incomplete or malformed:

```js
const markdown = `
* Item with **bold _and italic_** text
* [Link with **bold**](url)
* \`code with special chars\`
`;

const result = parse(markdown);
// The nested formatting is not fully processed
// Only the first level of nesting is handled
```

### Expected behavior

The parser should fully process all levels of nesting in markdown structures. Nested emphasis, links, and other inline elements should be completely tokenized regardless of depth.

### Additional context

This seems to affect any markdown content with multiple levels of nesting. The first pass works fine, but subsequent nested elements remain unparsed. This is particularly noticeable with:
- Nested emphasis (bold inside italic or vice versa)
- Links containing formatted text
- Complex list items with multiple inline elements

The issue appeared recently and breaks rendering of previously working markdown documents.

---
Repository: /testbed
