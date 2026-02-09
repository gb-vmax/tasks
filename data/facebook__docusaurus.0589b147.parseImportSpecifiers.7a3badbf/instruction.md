# Bug Report

### Describe the bug

I'm encountering an issue with parsing import statements that have both default and named imports. After a recent update, the parser seems to hang or behave incorrectly when processing certain import syntax patterns.

### Reproduction

```js
// This import statement causes issues
import defaultExport, { namedExport } from 'module';

// The parser appears to get stuck or not properly consume tokens
// when there's a default import followed by named imports
```

### Expected behavior

The parser should correctly handle import statements with both default and named specifiers, properly consuming all tokens and moving through the import declaration without getting stuck.

### Additional context

This seems to affect any import that combines:
1. A default import
2. Followed by a comma
3. Followed by named imports in braces

The issue might be related to how tokens are being consumed when transitioning from the default import to the named imports section.

---
Repository: /testbed
