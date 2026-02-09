# Bug Report

Title: First JSX attribute not being rendered in output

I'm encountering an issue where the first attribute in JSX elements is being skipped during code generation. When I have multiple attributes on a JSX element, only the second attribute onwards appear in the rendered output.

### Reproduction
```jsx
// Input JSX
<div className="container" id="main" data-test="value">
  Content
</div>

// Expected output
<div className="container" id="main" data-test="value">
  Content
</div>

// Actual output
<div id="main" data-test="value">
  Content
</div>
```

The `className` attribute is missing from the output. This happens with any JSX element that has multiple attributes - the first one is always omitted.

### Steps to reproduce
1. Create a JSX element with 2 or more attributes
2. Process/bundle the code
3. Check the output - first attribute will be missing

This seems to have started happening recently. Single-attribute JSX elements work fine, but anything with multiple attributes loses the first one.

---
Repository: /testbed
