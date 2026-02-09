# Bug Report

### Describe the bug

I'm experiencing an issue with accessibility testing where the first element in an array is being skipped during validation. When passing multiple React elements to the axe testing utility, only elements starting from index 1 are being checked for accessibility violations, while the element at index 0 is completely ignored.

### Reproduction

```jsx
const elements = [
  <Button>First Button</Button>,
  <Button>Second Button</Button>,
  <Button>Third Button</Button>
];

// When testing these elements, the first button is never checked
axe(elements);
```

In this scenario, only "Second Button" and "Third Button" are validated for accessibility, while "First Button" is silently skipped.

### Expected behavior

All elements in the array should be tested for accessibility violations, including the first element at index 0. Every component passed to the axe testing utility should be validated.

### Additional context

This seems to have started recently. Previously all elements were being properly validated. This is particularly problematic because it can lead to accessibility issues going undetected in the first component of any test suite.

---
Repository: /testbed
