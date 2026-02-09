# Bug Report

### Describe the bug

I'm encountering incorrect JSX transformation output when using the automatic JSX runtime with spread attributes. The generated code has the wrong structure - it seems like the logic for handling spread attributes and regular attributes is inverted.

### Reproduction

```jsx
// Input JSX
<div {...props} className="test" />

// Expected output (simplified):
// Object.assign({}, props, { className: "test" })

// Actual output appears to be wrapping things incorrectly
```

When I have JSX elements with:
1. A spread attribute followed by regular attributes
2. Regular attributes followed by a spread attribute

The transformation doesn't produce valid JavaScript. The object wrapping logic seems backwards.

### Steps to reproduce:
1. Configure rollup with JSX mode set to 'automatic'
2. Write a JSX element that has spread attributes mixed with regular attributes
3. Build the project
4. Check the generated output - the Object.assign calls and object literal wrapping are incorrect

### Expected behavior

The automatic JSX runtime should properly handle spread attributes by:
- Wrapping regular attributes in object literals when needed
- Using Object.assign correctly when there are spread attributes
- Generating valid JavaScript that matches the JSX semantics

### System Info
- Using rollup with JSX plugin
- JSX mode: automatic
- This seems to have started happening recently, possibly after a recent update

---
Repository: /testbed
