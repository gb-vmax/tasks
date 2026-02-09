# Bug Report

### Describe the bug

I'm encountering an issue with directive name parsing in remark-directive. It seems like directives with valid names are being rejected, while invalid characters are being accepted in directive names.

### Reproduction

```js
// This should work but doesn't:
:::myDirective
content
:::

// Names starting with letters are not recognized
::inlineDirective[content]

// Meanwhile, names with invalid characters seem to be processed incorrectly
```

When trying to use directives with standard alphanumeric names (starting with a letter), they're not being parsed correctly. The parser appears to be rejecting valid directive names.

### Expected behavior

Directives should accept names that:
- Start with an alphabetic character (a-z, A-Z)
- Can contain alphanumeric characters, hyphens (-), and underscores (_)

Standard directive syntax like `:::myDirective` or `::inline-directive` should be parsed without issues.

### System Info
- remark-directive version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
