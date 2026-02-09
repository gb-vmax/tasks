# Bug Report

### Describe the bug
After a recent update, code blocks in MDX files are not rendering correctly. The code blocks appear to be completely broken - they're either not showing up at all or displaying as empty/null content.

### Reproduction
```mdx
# My Document

Some text here.

```js
const example = 'this should be a code block';
console.log(example);
```

More text.
```

When this MDX is processed, the code block either doesn't render or shows up as empty/broken.

### Expected behavior
Code blocks should render properly with their content intact, showing the syntax-highlighted code as expected.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have started happening after the latest changes. Previously code blocks were working fine.

---
Repository: /testbed
