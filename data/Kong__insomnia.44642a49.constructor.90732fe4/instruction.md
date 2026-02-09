# Bug Report

### Describe the bug

When running tests with the JavaScript reporter, passing tests are being reported as failures and failing tests are being reported as passes. The test results are completely inverted - everything shows up in the wrong category.

### Reproduction

Run any test suite that has both passing and failing tests. For example:

```js
describe('Test Suite', () => {
  it('should pass', () => {
    expect(1 + 1).to.equal(2);
  });
  
  it('should fail', () => {
    expect(1 + 1).to.equal(3);
  });
});
```

After running, the test that should pass will be listed in the failures array, and the test that should fail will be listed in the passes array.

### Expected behavior

Passing tests should be in the `passes` array and failing tests should be in the `failures` array. The test results should accurately reflect which tests passed and which failed.

### System Info

- insomnia-testing version: latest
- Node version: 18.x

This is causing major confusion in our CI pipeline as we can't trust the test results anymore. Any help would be appreciated!

---
Repository: /testbed
