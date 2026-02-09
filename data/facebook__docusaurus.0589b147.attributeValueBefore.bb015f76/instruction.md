# Bug Report

### Describe the bug

Single-quoted attribute values in JSX/MDX tags are not being parsed correctly. When using single quotes (`'`) for attribute values, the parser seems to treat them the same as double quotes internally, which causes issues with proper quote matching and termination.

### Reproduction

```jsx
<Component attr='single quoted value' />
```

When parsing the above JSX with single-quoted attributes, the closing quote is not properly detected because the parser always expects a double quote (`"`) to close the attribute value, regardless of which quote character was actually used to open it.

### Expected behavior

The parser should track which quote character (single `'` or double `"`) was used to open an attribute value and look for the matching closing quote of the same type. Single-quoted attributes should close with single quotes, and double-quoted attributes should close with double quotes.

### Additional context

This appears to affect attribute value parsing in MDX/JSX tags. The issue manifests when trying to use single quotes for attribute values - the parser doesn't properly match the opening and closing quotes.

---
Repository: /testbed
