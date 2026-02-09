# Bug Report

### Describe the bug

I'm encountering an issue with inline directive parsing in remark-directive. When using inline directives (text directives) with a colon in the name, the parser is rejecting them instead of accepting them. The behavior seems inverted from what it should be.

### Reproduction

```markdown
:directive:name[label]{attributes}
```

When parsing this directive, it's being rejected when it should be accepted. The colon check appears to be backwards - directives with colons are failing validation when they should pass.

Additionally, after parsing attributes, the parser isn't properly completing the directive token. It seems to be calling the wrong callback function after attributes are processed.

### Expected behavior

Inline directives with proper colon syntax should be parsed correctly. The directive should:
1. Accept names that include colons (not reject them)
2. Properly complete parsing after attributes are processed

### System Info
- remark-directive version: 3.0.0
- Parser: micromark-extension-directive

---
Repository: /testbed
