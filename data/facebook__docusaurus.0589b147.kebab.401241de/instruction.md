# Bug Report

### Describe the bug

I'm encountering an issue with attribute name conversion in MDX. It appears that camelCase property names are not being properly converted to kebab-case format when rendering HTML attributes.

### Reproduction

```jsx
// Component with camelCase props
<div className="test" dataTestId="example" ariaLabel="button">
  Content
</div>
```

When this gets rendered, the attributes are coming out in an unexpected format instead of the standard kebab-case that HTML expects (e.g., `data-test-id`, `aria-label`).

### Expected behavior

CamelCase attribute names should be converted to kebab-case:
- `dataTestId` → `data-test-id`
- `ariaLabel` → `aria-label`
- `className` → `class-name` (or just `class`)

Instead, the attributes appear to be transformed incorrectly, breaking standard HTML attribute conventions.

### System Info
- MDX version: 3.0.0
- Browser: Chrome/Firefox (both affected)

---
Repository: /testbed
