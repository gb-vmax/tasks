# Bug Report

### Describe the bug

I'm experiencing an issue with generated code snippets where property access syntax is malformed. When accessing object properties, the generated code includes incorrect bracket notation that results in invalid JavaScript syntax.

### Reproduction

```js
// When generating code for property access:
const obj = { userName: 'test', 'user-name': 'test2' };

// For valid property names, the generated code looks like:
obj.userName]  // Invalid! Extra closing bracket

// For property names requiring bracket notation:
obj[user-name]  // Invalid! Missing quotes around the property name
```

The generated snippets produce syntax errors when trying to use them in actual code.

### Expected behavior

Property access should generate valid JavaScript:
- For valid identifiers: `obj.userName` (no extra bracket)
- For properties requiring bracket notation: `obj["user-name"]` (with proper quotes)

### System Info
- Version: Latest
- Node: 18.x

This is breaking code generation functionality and making the generated snippets unusable. Any help would be appreciated!

---
Repository: /testbed
