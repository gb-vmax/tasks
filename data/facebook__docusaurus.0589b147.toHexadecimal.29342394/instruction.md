# Bug Report

### Describe the bug

I'm encountering an issue with HTML entity encoding where hexadecimal character references are being generated incorrectly. Specifically, the semicolon terminator is being omitted when it should be included, or included when it should be omitted.

### Reproduction

```js
// When encoding entities with hexadecimal format
// The semicolon handling appears to be inverted

// Example 1: Entity followed by a hexadecimal character
const result1 = stringifyEntities('test\u00A0A', { useNamedReferences: false, useHexadecimal: true });
// Expected: '&#xA0;A' (semicolon should be present)
// Actual: '&#xA0A' (semicolon missing)

// Example 2: Entity followed by a non-hexadecimal character  
const result2 = stringifyEntities('test\u00A0!', { useNamedReferences: false, useHexadecimal: true });
// Expected: '&#xA0!' (semicolon can be omitted)
// Actual: '&#xA0;!' (semicolon incorrectly added)
```

The logic for determining when to include the semicolon terminator seems to be reversed - it's omitting semicolons when they're needed to prevent ambiguity with following hexadecimal digits, and adding them when they're not necessary.

### Expected behavior

Hexadecimal character references should include a semicolon when followed by a character that could be interpreted as part of the hex code (0-9, A-F, a-f), and can omit the semicolon when followed by other characters (if omit option is enabled).

### System Info
- rehype-stringify version: 10.0.0
- Node version: Latest

---
Repository: /testbed
