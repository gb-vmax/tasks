# Bug Report

### Describe the bug

I'm encountering an issue with markdown parsing where strikethrough syntax is not being rendered correctly in certain scenarios. It seems like the strikethrough handler is being applied twice or in the wrong order, which causes unexpected behavior when parsing GFM (GitHub Flavored Markdown) content.

### Reproduction

When parsing markdown with strikethrough syntax:

```js
const markdown = `
This is ~~strikethrough~~ text.
Some more ~~deleted~~ content here.
`;

// Parse the markdown
const result = parseMarkdown(markdown);
```

The strikethrough elements are not processed correctly, and the output doesn't match the expected GFM rendering.

### Expected behavior

Strikethrough syntax (`~~text~~`) should be parsed and rendered correctly according to GFM specification. The markdown transformations should be applied in the correct order without duplication.

### System Info
- remark-gfm version: 4.0.0
- Node version: Latest

Has anyone else run into this? It seems like something changed in how the GFM extensions are being registered.

---
Repository: /testbed
