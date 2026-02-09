# Bug Report

### Describe the bug

The AST buffer conversion is broken and throwing errors when trying to parse valid JavaScript code. After a recent change, the parser fails to return properly converted AST nodes and instead treats all successful conversions as errors.

### Reproduction

```js
import { convertProgram } from './utils/bufferToAst';

// Create a simple AST buffer from valid JavaScript
const buffer = createAstBuffer('const x = 1;');

// This should return a valid ProgramNode but throws an error instead
const ast = convertProgram(buffer);
```

When parsing any valid JavaScript code, the conversion fails and returns an error even though the code is syntactically correct. This makes it impossible to use the parser for its intended purpose.

### Expected behavior

The `convertProgram` function should return a valid `ProgramNode` when given a buffer containing valid JavaScript code. It should only return errors when the input actually contains parse errors or panic conditions.

### Additional context

This seems to have started happening recently. The parser was working fine before but now every valid program is being treated as an error case. Not sure what changed but it's blocking all parsing operations.

---
Repository: /testbed
