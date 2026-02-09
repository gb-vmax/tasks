# Bug Report

### Describe the bug

When parsing HTML entities in text content, the output is incorrect - entities are being replaced with empty strings instead of their decoded values. This affects any text that contains HTML entities like `&amp;`, `&lt;`, `&gt;`, etc.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
This is a test with &amp; ampersand and &lt; less than.
`

const result = await compile(mdxContent)
console.log(result)
// Expected: "This is a test with & ampersand and < less than."
// Actual: "This is a test with  ampersand and  less than."
```

The entities are being consumed but the decoded text is not appearing in the output. It looks like the text is being cleared before it's pushed to the result.

### Expected behavior

HTML entities should be properly decoded and appear in the final output. `&amp;` should become `&`, `&lt;` should become `<`, etc.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node.js version: 18.x

---
Repository: /testbed
