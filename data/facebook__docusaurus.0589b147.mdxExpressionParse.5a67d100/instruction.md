# Bug Report

### Describe the bug

I'm encountering an issue with MDX spread expressions where the parser is checking the wrong property index. When I have a single spread expression like `{...props}`, it's throwing an error about "extra content" even though there's only one property.

### Reproduction

```mdx
<Component {...props} />
```

The parser incorrectly validates the spread and throws:
```
Unexpected extra content in spread: only a single spread is supported
```

This happens with any single spread expression. It seems like the validation is looking at the wrong array index.

### Expected behavior

A single spread expression should be parsed without errors. The "extra content" error should only appear when there are actually multiple properties in the spread.

### Additional context

This affects basic MDX component usage with spread props, which is a pretty common pattern. The error appears even when using the simplest possible spread syntax.

---
Repository: /testbed
