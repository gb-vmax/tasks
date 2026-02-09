# Bug Report

### Describe the bug

I'm encountering a syntax error when trying to generate test files. It appears that the code generation is producing invalid JavaScript output with duplicate code blocks and misplaced interface definitions.

### Reproduction

```js
const suites = [
  {
    name: 'Test Suite',
    suites: [
      { name: 'Nested Suite 1', tests: [] },
      { name: 'Nested Suite 2', tests: [] }
    ],
    tests: []
  }
];

// Try to generate test code
const output = generate(suites);
console.log(output);
```

When running this, the generated output contains malformed JavaScript with interface definitions appearing in the middle of a for loop and duplicate code blocks.

### Expected behavior

The `generate()` function should produce valid, syntactically correct JavaScript test code. The output should be properly structured with describe blocks and any spacing configuration applied correctly.

### Additional context

This seems to have broken recently. The generated code has interface definitions and function declarations inserted in the wrong places, making the output unparsable. The code structure looks corrupted with duplicate loops and misplaced closing braces.

---
Repository: /testbed
