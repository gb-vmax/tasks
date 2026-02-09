# Bug Report

### Describe the bug

When using emphasis markers in markdown, the output is not rendering correctly. Instead of using the configured emphasis character (or the default `*`), it seems to always output `**` (bold) regardless of the emphasis option setting.

### Reproduction

```js
const processor = remark()
  .use(remarkStringify, {
    emphasis: '_'
  });

const result = processor.stringify({
  type: 'emphasis',
  children: [{type: 'text', value: 'test'}]
});

console.log(result); // Expected: _test_ but getting something else
```

Also happens with the default settings:

```js
const processor = remark();

const result = processor.stringify({
  type: 'emphasis',
  children: [{type: 'text', value: 'italic text'}]
});

// Expected output: *italic text*
// Actual output seems wrong
```

### Expected behavior

Emphasis nodes should be serialized using the configured emphasis character (underscore `_` or asterisk `*`), not always as bold markers `**`.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
