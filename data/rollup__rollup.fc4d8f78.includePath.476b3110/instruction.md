# Bug Report

### Describe the bug

I'm experiencing an issue with JSX member expressions where accessing nested properties doesn't work as expected. When using JSX components with member expressions like `Component.SubComponent`, the property path doesn't seem to be properly resolved.

### Reproduction

```jsx
// Define a component with nested members
const MyLib = {
  Button: () => <button>Click me</button>,
  Input: () => <input type="text" />
}

// Try to use the nested component
function App() {
  return (
    <div>
      <MyLib.Button />
    </div>
  )
}
```

When bundling this code, the nested component reference (`MyLib.Button`) doesn't get included correctly in the output. It seems like the property chain is not being followed through properly.

### Expected behavior

The JSX member expression should correctly resolve the nested property path and include the referenced component in the bundle. The component should be accessible and functional in the output.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
