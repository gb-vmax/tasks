# Bug Report

### Describe the bug

After a recent update, setext headings (underlined headers using `===` or `---`) are not being parsed correctly. The parser seems to be rejecting valid setext heading syntax that was working before.

### Reproduction

```js
const markdown = `
My Heading
==========

Some content here.
`;

// Parse the markdown
const result = parseMarkdown(markdown);

// Expected: heading node with "My Heading"
// Actual: plain text, not recognized as heading
```

Also fails with dash-style underlines:

```js
const markdown = `
Another Heading
---------------
`;
```

### Expected behavior

Valid setext headings with proper underlines should be recognized and parsed as heading nodes. Both equals signs (`=`) for h1 and dashes (`-`) for h2 should work when the underline is on the line following the heading text.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
