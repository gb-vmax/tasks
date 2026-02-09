# Bug Report

### Describe the bug

I'm encountering an issue with TDZ (Temporal Dead Zone) detection for variables that are declared and used at the exact same position. When a variable reference occurs at the same start position as its declaration, it's incorrectly being flagged as a TDZ violation.

### Reproduction

```js
// Example where identifier starts at the same position as declaration
const x = x + 1; // Should be TDZ error but the detection is incorrect
```

The problem occurs when:
1. A variable is referenced before its declaration
2. The reference and declaration have the same `start` position
3. Both are in the same function or top-level scope

Currently, variables that are accessed at the exact same position as their declaration are being treated as TDZ violations when they shouldn't be (or vice versa, depending on the expected behavior).

### Expected behavior

The TDZ detection should correctly handle edge cases where the start positions are equal. The comparison logic needs to properly distinguish between:
- References that occur strictly before the declaration
- References that occur at the same position as the declaration

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
