# Bug Report

### Describe the bug

The `Interpolate` component is not working correctly - it's showing the placeholder text instead of the actual interpolated values. When I try to use placeholders like `{name}` or `{count}` in my text, they just appear as literal text in the output instead of being replaced with the values I provide.

### Reproduction

```jsx
import {Interpolate} from '@docusaurus/Interpolate';

// This should replace {username} with "John"
<Interpolate
  values={{username: 'John'}}
>
  Hello {username}!
</Interpolate>

// Output: "Hello {username}!" 
// Expected: "Hello John!"
```

Another example:
```jsx
<Interpolate
  values={{count: 5, item: 'apples'}}
>
  You have {count} {item}
</Interpolate>

// Output: "You have {count} {item}"
// Expected: "You have 5 apples"
```

### Expected behavior

The placeholders in curly braces should be replaced with the corresponding values from the `values` prop. Instead, the placeholders are showing up as-is in the rendered output.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
