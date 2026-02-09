# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where emphasis markers (like `*` and `_`) are not being recognized properly. It seems like the first attention marker in the list is being skipped, which causes markdown text with emphasis to not render correctly.

### Reproduction

```js
const markdown = '*italic text*';
// Expected: Should parse the asterisk as an emphasis marker
// Actual: The asterisk is not recognized, text renders without emphasis

const markdown2 = '_another italic_';
// Same issue - underscore not working as expected
```

When I try to parse markdown with emphasis syntax, the markers aren't being detected. This affects both asterisks and underscores used for italic/bold text.

### Expected behavior

Emphasis markers should be properly recognized and parsed. Text wrapped in `*` or `_` should be converted to emphasized/italic text in the output.

### System Info
- remark version: 15.0.1
- Browser/Node: Node.js v18

---
Repository: /testbed
