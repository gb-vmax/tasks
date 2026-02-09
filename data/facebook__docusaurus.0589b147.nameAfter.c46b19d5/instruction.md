# Bug Report

### Describe the bug

I'm experiencing an issue with directive attribute parsing where attributes with values are not being handled correctly. The parser seems to be exiting and entering attribute initializer types in the wrong order, causing attributes with `=` signs to fail parsing.

### Reproduction

```markdown
::directive{name="value"}
```

When parsing directives with attributes that have values (using the `=` sign), the attribute parsing breaks. The issue appears to be related to how the parser handles the transition from attribute name to the initializer (`=`) and then to the value.

### Expected behavior

Directives with named attributes should parse correctly:
- `::directive{name="value"}` should recognize `name` as the attribute and `"value"` as its value
- The parser should properly handle the `=` initializer between attribute names and values
- Attribute types should be entered and exited in the correct sequence

### System Info
- remark-directive version: 3.0.0
- Parser: micromark-based

The parsing flow seems to be getting confused when encountering the equals sign after an attribute name. It looks like there might be an issue with the order of operations in the `nameAfter` function.

---
Repository: /testbed
