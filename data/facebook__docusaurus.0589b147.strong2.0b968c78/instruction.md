# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where bold/strong text is not being rendered correctly. When I use double asterisks or double underscores to create bold text, the output is broken or missing.

### Reproduction

```js
const markdown = '**bold text**';
const result = remark().use(remarkHtml).processSync(markdown);
console.log(result.toString());
// Expected: <strong>bold text</strong>
// Actual: broken or missing output
```

Also happens with:
```js
const markdown = '__another bold__';
// Same issue - bold formatting doesn't work
```

### Expected behavior

Bold/strong markdown syntax should be properly converted to `<strong>` tags in the HTML output. The text content should be preserved and wrapped correctly.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
