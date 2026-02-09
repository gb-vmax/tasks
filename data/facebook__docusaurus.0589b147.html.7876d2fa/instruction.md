# Bug Report

### Describe the bug

I'm experiencing an issue with HTML rendering in markdown processing. When I have raw HTML content in my markdown and the `allowDangerousHtml` option is enabled, the HTML is not being rendered - it just disappears from the output. 

### Reproduction

```js
const processor = unified()
  .use(remarkParse)
  .use(remarkRehype, { allowDangerousHtml: true })
  .use(rehypeStringify)

const markdown = `
# Heading

<div class="custom">
  Some raw HTML content
</div>

More text
`

const result = processor.processSync(markdown)
console.log(result.toString())
// Expected: HTML should include the div with "custom" class
// Actual: The div is missing from the output
```

### Expected behavior

When `allowDangerousHtml` is set to `true`, raw HTML nodes in the markdown should be preserved and included in the final output. The HTML content should appear in the rendered result.

### System Info
- remark-rehype version: 11.0.0
- Node version: 18.x

This seems like it might be a regression as I'm pretty sure this was working before. Any help would be appreciated!

---
Repository: /testbed
