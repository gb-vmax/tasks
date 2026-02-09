# Bug Report

### Describe the bug
I'm experiencing an issue with code fence rendering in MDX files. When I have multiple consecutive fenced code blocks in my MDX document, only the first one renders correctly. The subsequent code blocks appear to be getting their content mixed up or not rendering at all.

### Reproduction
```mdx
# My Document

First code block:
```js
console.log('first');
```

Second code block:
```js
console.log('second');
```

Third code block:
```js
console.log('third');
```
```

When this is rendered, the first code block shows up fine, but the second and third blocks don't display their content properly. It seems like the parser is getting confused about where one code fence ends and another begins.

### Expected behavior
Each fenced code block should render independently with its own content preserved. All three code blocks should display their respective code snippets correctly.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have started happening recently. I've tried different code fence syntaxes but the issue persists with multiple blocks in sequence.

---
Repository: /testbed
