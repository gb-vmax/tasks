# Bug Report

### Describe the bug

I'm encountering an issue with MDX JSX flow tag parsing where the arguments passed to `factoryTag.call()` appear to be in the wrong order. This is causing the parser to fail when processing JSX components in MDX files.

### Reproduction

When parsing MDX content with JSX flow tags, the parser seems to be mixing up the callback order, specifically the `after` and `nok` callbacks. This leads to incorrect parsing behavior where:

1. Valid JSX components may be rejected
2. Error handling callbacks are triggered at the wrong time
3. The parser state machine doesn't transition correctly

Example MDX content that triggers the issue:
```mdx
<MyComponent prop="value">
  Content here
</MyComponent>
```

The parser should handle this correctly but seems to be calling callbacks in an unexpected order.

### Expected behavior

The `factoryTag.call()` should receive its callbacks in the correct order so that:
- Success callback is invoked when parsing succeeds
- Error callback is invoked when parsing fails
- The state machine transitions properly through parsing states

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest LTS

---
Repository: /testbed
