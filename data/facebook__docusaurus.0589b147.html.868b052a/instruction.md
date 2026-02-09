# Bug Report

### Describe the bug

When processing markdown with HTML content, the `allowDangerousHtml` option seems to be inverted. HTML is being rendered when the option is set to `false`, and being stripped when it's set to `true`.

### Reproduction

```js
const processor = unified()
  .use(remarkParse)
  .use(remarkRehype, { allowDangerousHtml: true })
  .use(rehypeStringify);

const markdown = `
# Test

<div class="custom">
  <p>Raw HTML content</p>
</div>
`;

const result = await processor.process(markdown);
console.log(result.toString());
// Expected: HTML should be preserved
// Actual: HTML is stripped out
```

When I set `allowDangerousHtml: false`, the HTML unexpectedly appears in the output. When set to `true`, the HTML gets removed instead of being preserved.

### Expected behavior

- When `allowDangerousHtml: true` → raw HTML should be preserved in the output
- When `allowDangerousHtml: false` → raw HTML should be stripped/escaped

### System Info

- remark-rehype version: 11.0.0
- Node version: 18.x

This seems like the logic got flipped somehow. Has anyone else encountered this?

---
Repository: /testbed
