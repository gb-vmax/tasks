# Bug Report

### Describe the bug

I'm experiencing incorrect character encoding behavior when using rehype-stringify. Characters are being encoded with wrong offsets, which results in malformed HTML output.

### Reproduction

```js
const rehype = require('rehype');
const stringify = require('rehype-stringify');

const processor = rehype()
  .use(stringify);

const html = '<p>Test & content</p>';
const result = processor.processSync(html);

console.log(result.toString());
// Output shows incorrectly encoded characters
```

When processing HTML with special characters that need encoding (like `&`, `<`, `>`), the output is corrupted. It seems like the character encoding is reading from the wrong position in the string.

### Expected behavior

Special characters should be properly encoded based on the correct character position. The HTML output should maintain the same content structure with properly escaped entities where needed.

### System Info
- rehype-stringify version: 10.0.0
- Node version: 18.x

---
Repository: /testbed
