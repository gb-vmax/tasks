# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX parser where token position information appears to be swapped or incorrectly assigned. When parsing MDX content, the `lastTokEnd` and `lastTokStart` values seem to contain location objects instead of numeric positions, while `lastTokEndLoc` and `lastTokStartLoc` contain numeric values instead of location objects.

This is causing downstream issues when trying to access position information from parsed tokens, as the types don't match what's expected.

### Reproduction

```js
// Parse some MDX content
const parser = new Parser(options, input);
parser.next();

// After calling next(), the token positions are swapped:
console.log(parser.lastTokEnd); // Expected: number, Actual: location object
console.log(parser.lastTokStart); // Expected: number, Actual: location object
console.log(parser.lastTokEndLoc); // Expected: location object, Actual: number
console.log(parser.lastTokStartLoc); // Expected: location object, Actual: number
```

### Expected behavior

- `lastTokEnd` and `lastTokStart` should be numeric position values
- `lastTokEndLoc` and `lastTokStartLoc` should be location objects with line/column information

The naming convention suggests that properties ending in `Loc` should contain location objects, while properties without that suffix should contain simple numeric positions.

### Additional context

This seems to have been introduced in a recent change to the parser's `next()` method. The issue affects any code that relies on these token position properties for error reporting or source mapping.

---
Repository: /testbed
