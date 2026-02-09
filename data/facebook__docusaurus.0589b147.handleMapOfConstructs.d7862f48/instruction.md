# Bug Report

### Describe the bug

I'm experiencing an issue where certain character codes are not being processed correctly in the tokenizer. When passing specific input, the tokenizer seems to be checking for null values incorrectly, which causes it to skip valid constructs.

### Reproduction

```js
// When tokenizing content with specific character codes
const parser = createParser();
const tokenizer = createTokenizer(parser, initialize, from);

// Characters that should match a specific construct are being ignored
// The tokenizer appears to be looking up the wrong key in the construct map
```

### Expected behavior

The tokenizer should correctly look up constructs based on the character code. Non-null character codes should retrieve their corresponding construct from the map, and the construct should be processed properly.

### Additional context

This seems to affect how the construct map is being queried. The behavior changed recently and now certain valid inputs are not being handled as expected. The lookup logic appears to have the condition reversed for null checks.

---
Repository: /testbed
