# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX parser where it seems like the parser initialization is not working correctly. After a recent change, the parser appears to be returning incorrect tokenizer functions, which breaks the entire parsing flow.

### Reproduction

When trying to parse MDX content, the parser fails to properly initialize its tokenizers. The issue manifests when:

1. Initialize a parser with `parse3(options)`
2. Try to use the returned parser to process MDX content
3. The parser doesn't work as expected because the tokenizer creation is broken

```js
const parser = parse3({ extensions: [...] });
// Parser is not functioning correctly
// Tokenizers are not being created properly
```

### Expected behavior

The parser should properly initialize all tokenizers (document, flow, string, text) and be able to parse MDX content correctly. The constructs should be combined with any provided extensions and used throughout the parsing process.

### Additional context

This seems related to how the tokenizers are being created and how the constructs are being combined. The parser worked fine before but now something in the initialization logic appears to be off.

---
Repository: /testbed
