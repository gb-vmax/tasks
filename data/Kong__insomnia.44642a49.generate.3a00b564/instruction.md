# Bug Report

### Describe the bug

The `beforeEach` hook that clears the active request is not being called correctly when using the test generator. After a recent change, the hook appears to be missing or not executing, which causes tests to fail when they rely on a clean request state.

### Reproduction

```js
const suites = [
  {
    name: 'My Test Suite',
    tests: [
      {
        name: 'First test',
        code: 'expect(insomnia.getActiveRequest()).to.be.null;'
      },
      {
        name: 'Second test',
        code: 'insomnia.setActiveRequest({ id: "test" }); expect(insomnia.getActiveRequest()).to.not.be.null;'
      },
      {
        name: 'Third test',
        code: 'expect(insomnia.getActiveRequest()).to.be.null;'
      }
    ]
  }
];

const generatedCode = generate(suites);
```

### Expected behavior

The `beforeEach` hook should clear the active request before each test runs. This means:
1. First test should pass (no active request initially)
2. Second test should pass (sets and checks active request)
3. Third test should pass (active request cleared by beforeEach)

### Actual behavior

The third test fails because the active request from the second test is not being cleared. It seems like the `beforeEach` hook is not properly set up in the generated test code.

### System Info
- insomnia-testing version: latest
- Node version: 18.x

---
Repository: /testbed
