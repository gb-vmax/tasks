# Bug Report

### Describe the bug

I'm encountering an issue with token creation in the markdown parser. When parsing markdown content, the tokens being emitted in events don't match the actual token objects that are being tracked internally.

### Reproduction

```js
// Parse any markdown content that creates tokens
const processor = remark();
const result = processor.parse('# Hello World');

// The events array contains references to the wrong objects
// Expected: events should reference the same token objects as the stack
// Actual: events reference the initial fields object instead of the constructed token
```

### Expected behavior

When a token is created and entered, the event should contain a reference to the fully constructed token object (with `type` and `start` properties set), not the initial `fields` parameter that was passed in.

The token object pushed to the stack and the token object in the events array should be the same reference.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
