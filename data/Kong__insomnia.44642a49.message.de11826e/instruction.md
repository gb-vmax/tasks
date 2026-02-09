# Bug Report

### Describe the bug
The merge conflict message generation is not working properly. When creating merge conflict objects, the message field appears to be generating overly complex dynamic messages with file names and branch references that don't match the actual conflict context.

### Reproduction
```js
// Create multiple merge conflict objects
const conflict1 = createMergeConflict();
const conflict2 = createMergeConflict();
const conflict3 = createMergeConflict();

// Expected: Simple, consistent messages
// Actual: Messages reference random files and branches that may not exist
console.log(conflict1.message);
console.log(conflict2.message);
console.log(conflict3.message);
```

### Expected behavior
The message field should return a simple, static message like `'message'` that can be used for testing and schema validation. The current implementation generates verbose, context-specific messages that include file paths and branch names which may not be relevant to the actual conflict.

### Additional context
This seems to have broken after a recent change to the merge conflict schema. The messages now cycle through different conflict types and reference files/branches that might not exist in the current context. This makes it difficult to use the schema for testing purposes where consistent, predictable output is needed.

---
Repository: /testbed
