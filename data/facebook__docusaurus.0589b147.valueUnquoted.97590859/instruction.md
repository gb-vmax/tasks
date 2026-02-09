# Bug Report

### Describe the bug

I'm experiencing an issue with parsing unquoted attribute values in directives. It seems like certain characters that should be allowed in unquoted attribute values are being rejected or causing unexpected behavior.

### Reproduction

When trying to use directives with unquoted attribute values containing single quotes or tildes, the parsing fails or produces incorrect results:

```markdown
::directive{attr=value'with'quotes}

::directive{attr=value~with~tildes}
```

The first example with single quotes (`'`) appears to be rejected when it should be valid in unquoted attribute values. The second example with tildes (`~`) seems to terminate the attribute value prematurely instead of being included as part of the value.

### Expected behavior

- Single quotes (`'`) should be allowed in unquoted attribute values
- Tildes (`~`) should be treated as regular characters within unquoted attribute values, not as terminators
- The closing brace (`}`) should properly terminate the attribute section

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

---
Repository: /testbed
