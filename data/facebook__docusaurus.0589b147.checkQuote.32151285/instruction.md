# Bug Report

### Describe the bug

When using the markdown serialization with the `quote` option, the quote markers are being inverted. If I set `quote: '"'` in the options, the output uses single quotes instead of double quotes, and vice versa.

### Reproduction

```js
import {remark} from 'remark'

const processor = remark()
  .use(remarkStringify, {quote: '"'})

const result = processor.stringify({
  type: 'root',
  children: [{
    type: 'definition',
    identifier: 'example',
    url: 'https://example.com',
    title: 'Example Title'
  }]
})

// Expected output: [example]: https://example.com "Example Title"
// Actual output: [example]: https://example.com 'Example Title'
```

### Expected behavior

When `quote: '"'` is specified in options, the serializer should use double quotes for titles. When `quote: "'"` is specified, it should use single quotes. The output should respect the configured quote option.

### Additional context

This seems to have started recently. The quote option appears to be working in reverse - specifying double quotes produces single quotes and vice versa.

---
Repository: /testbed
