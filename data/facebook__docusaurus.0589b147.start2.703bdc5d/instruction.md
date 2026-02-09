# Bug Report

### Describe the bug

After a recent update, MDX parsing is not working correctly when using custom fields/context in tokenizers. The context object seems to have its prototype chain inverted, causing fields to not be accessible as expected during tokenization.

### Reproduction

```js
// Create a parser with custom fields
const parser = createParser({
  fields: {
    customField: 'value'
  }
});

// Try to parse MDX content
const result = parser.parse('# Hello World');

// Custom fields are not accessible in the tokenizer context
// Expected: context.customField === 'value'
// Actual: context.customField === undefined
```

### Expected behavior

Custom fields passed to the tokenizer should be accessible through the context object during parsing. The fields should extend the base context, not the other way around.

### Additional context

This appears to affect partial constructs differently than non-partial constructs. The `currentConstruct` assignment logic also seems reversed - it's now being set for partial constructs when it should be set for non-partial ones.

---
Repository: /testbed
