# Bug Report

### Describe the bug

The `Interpolate` component is not replacing placeholders correctly. When I try to interpolate values into a string template with placeholders like `{name}`, the placeholders remain in the output instead of being replaced with the actual values.

### Reproduction

```jsx
import {Interpolate} from '@docusaurus/Interpolate';

// This should replace {name} with "John"
<Interpolate 
  values={{name: 'John', age: 25}}
>
  {'Hello {name}, you are {age} years old'}
</Interpolate>

// Expected output: "Hello John, you are 25 years old"
// Actual output: "Hello {name}, you are {age} years old"
```

The placeholders are not being substituted with the provided values. It seems like the interpolation logic is not matching the placeholders properly.

### Expected behavior

The component should replace `{name}` and `{age}` with their corresponding values from the `values` prop, producing "Hello John, you are 25 years old".

### System Info

- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
