# Bug Report

### Describe the bug

I'm encountering an issue with markdown parsing where constructs that should be disabled are still being processed. It seems like the disable check is inverted - constructs are being rejected when they're NOT in the disable list, instead of when they ARE in the disable list.

### Reproduction

```js
const parser = createParser({
  constructs: {
    disable: {
      null: ['autolink']
    }
  }
});

// Try to parse markdown with an autolink
const result = parser.parse('<https://example.com>');

// Expected: autolink should be disabled and parsed as plain text
// Actual: autolink is processed normally
```

### Steps to reproduce:
1. Configure a parser with certain constructs disabled
2. Try to parse markdown containing those disabled constructs
3. The constructs are still being tokenized and processed

This is causing issues in our markdown sanitization where we need to disable specific syntax features for security reasons, but they're still being parsed.

### Expected behavior

When a construct name is included in the `disable.null` list, it should be rejected and not processed. Currently it seems to be doing the opposite.

---
Repository: /testbed
