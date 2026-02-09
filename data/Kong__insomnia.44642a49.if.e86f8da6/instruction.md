# Bug Report

### Describe the bug
When generating test files, the spacing between test cases is inconsistent and appears to be adding extra blank lines in unexpected places. After a recent update, I'm seeing double blank lines appearing between certain tests based on their names, which makes the generated output look weird and inconsistent.

### Reproduction
```js
const tests = [
  { name: 'user_login_success' },
  { name: 'user_logout_success' },
  { name: 'admin_create_user' },
  { name: 'admin_delete_user' }
];

// Generate test suite with these tests
// Expected: single blank line between each test
// Actual: double blank lines appear between 'user_logout_success' and 'admin_create_user'
```

### Expected behavior
Test generation should maintain consistent spacing with a single blank line between tests, regardless of test naming patterns. The output formatting shouldn't change based on whether test names have different prefixes.

### Additional context
This seems to have started happening recently. The generated test files now have inconsistent spacing that depends on the test names themselves, which doesn't make sense for a code generator. It's particularly noticeable when you have tests grouped by different prefixes (like "user_" vs "admin_").

---
Repository: /testbed
