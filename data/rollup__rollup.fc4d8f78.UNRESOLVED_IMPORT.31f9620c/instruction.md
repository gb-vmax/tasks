# Bug Report

### Describe the bug

The warning message for unresolved imports is displaying the importer and dependency in the wrong order. When Rollup encounters an unresolved dependency, the warning output shows which files are importing the unresolved module, but the labels are swapped - it's showing the importers in bold where the dependency name should be, and the actual dependency name where the importer list should be.

### Reproduction

Create a project with an unresolved import:

```js
// index.js
import something from 'unresolved-package';
```

Run the build and observe the warning output. You'll see something like:

```
'index.js' (imported by unresolved-package)
```

### Expected behavior

The warning should display:

```
unresolved-package (imported by 'index.js')
```

The dependency that cannot be resolved should be shown in bold, followed by the list of files that are trying to import it.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
