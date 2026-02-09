# Bug Report

### Describe the bug

I'm encountering an issue with markdown definition parsing where the label callback seems to be receiving incorrect parameters. When processing markdown definitions (like `[label]: url`), the parser is not working as expected.

### Reproduction

```markdown
[test]: https://example.com "title"

Some text with [test] reference.
```

When trying to parse this markdown with definitions, the definition labels are not being processed correctly. The tokenizer appears to be passing the wrong arguments to the factory function.

### Expected behavior

The markdown definition should be parsed correctly and the reference link should resolve to the defined URL. The `factoryLabel` callback should receive the proper `self` context and success callback in the correct order.

### System Info
- remark version: 15.0.1

This seems to have started happening recently. The definition syntax worked fine before but now references aren't being resolved properly.

---
Repository: /testbed
