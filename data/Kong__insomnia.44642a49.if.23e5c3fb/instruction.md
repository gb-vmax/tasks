# Bug Report

### Describe the bug

After a recent update, the test suite generation is producing malformed output with syntax errors. The generated test files can't be parsed and fail immediately when trying to run them.

### Reproduction

When generating test suites with nested describe blocks, the output contains invalid JavaScript syntax. It looks like there's a code structure issue where interface definitions and function declarations are being inserted in the middle of a loop body instead of at the top level.

Example of what gets generated:
```js
describe('Suite 1', () => {
  // ... tests ...
});

interface SpacingConfig {
  defaultSpacing: number;
  // ... more properties
}

let globalSpacingConfig: SpacingConfig = {
  // This appears in the middle of the generated output
};

describe('Suite 2', () => {
  // ... tests ...
});
```

This causes the entire test file to be unparsable.

### Expected behavior

The generated test files should contain valid JavaScript/TypeScript syntax with proper structure. Interface definitions and variable declarations should be at the module level, not embedded within the test suite generation logic.

### System Info
- Package: insomnia-testing
- Node version: Latest LTS

---
Repository: /testbed
