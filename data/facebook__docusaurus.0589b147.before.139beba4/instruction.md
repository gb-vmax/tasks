# Bug Report

### Describe the bug

I'm encountering an issue with markdown definition parsing where the label callback seems to be getting the wrong arguments. When processing definition syntax like `[label]: url`, the parser is not correctly handling the label portion.

### Reproduction

```markdown
[example]: https://example.com "Example Link"
[test]: https://test.com

Some text with a reference to [example].
```

When parsing the above markdown, the definition labels are not being processed correctly. The parser appears to be passing incorrect parameters to the factory function.

### Expected behavior

The parser should correctly extract and process definition labels, allowing them to be referenced later in the document. The `factoryLabel` call should receive the proper callbacks for handling successful label parsing.

### System Info
- remark version: 15.0.1
- Parser: micromark

---
Repository: /testbed
