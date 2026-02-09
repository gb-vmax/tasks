# Bug Report

### Describe the bug

When generating test code with the `generate()` function, the output now includes unexpected global setup/teardown hooks (`beforeAll` and `afterAll`) that call `insomnia.initializeTestEnvironment()` and `insomnia.cleanupTestEnvironment()`. These methods don't exist in the insomnia API, causing runtime errors when the generated tests are executed.

### Reproduction

```js
const suites = [
  {
    name: 'API Tests',
    tests: [
      {
        name: 'should return 200',
        code: 'expect(response.status).to.equal(200);'
      }
    ]
  }
];

const generatedCode = generate(suites);
console.log(generatedCode);
```

The generated output includes:
```js
// Global setup
beforeAll(() => {
  insomnia.initializeTestEnvironment();
});

// Global teardown
afterAll(() => {
  insomnia.cleanupTestEnvironment();
});
```

When running the generated tests, I get errors like:
```
TypeError: insomnia.initializeTestEnvironment is not a function
```

### Expected behavior

The generated test code should only include hooks and methods that actually exist in the insomnia testing API. These global setup/teardown hooks should either not be generated, or they should call valid methods.

### Additional context

This appears to have started happening recently. Previously, the generated code would work without these initialization calls. The `beforeEach` hook for clearing active requests still works fine, but these new global hooks are breaking the test execution.

---
Repository: /testbed
