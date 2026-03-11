I'm setting up a shared workspace for a Kubernetes operator team. We have multiple operators who need to collaborate on YAML manifests, and I need to lock down the directory structure properly so that only the right users can read, write, or execute files in each area.

I have a directory at `/home/user/k8s-operator` that already contains some manifest files. I need you to do the following:

**1. Create the subdirectory structure**

Inside `/home/user/k8s-operator`, create these three subdirectories if they don't already exist:
- `crds/` — for CustomResourceDefinition manifests
- `rbac/` — for Role/ClusterRole/Binding manifests
- `deploy/` — for Deployment and Service manifests

**2. Move the existing manifests into the correct subdirectories**

The existing files in `/home/user/k8s-operator` should be moved as follows:
- `cache-crd.yaml` → `crds/cache-crd.yaml`
- `index-crd.yaml` → `crds/index-crd.yaml`
- `operator-role.yaml` → `rbac/operator-role.yaml`
- `operator-rolebinding.yaml` → `rbac/operator-rolebinding.yaml`
- `operator-deploy.yaml` → `deploy/operator-deploy.yaml`
- `operator-svc.yaml` → `deploy/operator-svc.yaml`

**3. Set permissions on the subdirectories and their contents**

Apply the following permissions using `chmod`:

- `crds/` directory itself: `755`
- All `.yaml` files inside `crds/`: `644`
- `rbac/` directory itself: `750`
- All `.yaml` files inside `rbac/`: `640`
- `deploy/` directory itself: `750`
- All `.yaml` files inside `deploy/`: `640`

**4. Write a permissions manifest**

Create a file at `/home/user/k8s-operator/permissions.txt` that records the permissions of every file and directory under `/home/user/k8s-operator` (including the subdirectories and all `.yaml` files, but NOT `permissions.txt` itself).

The file must contain exactly the following lines in exactly this order (no extra whitespace, no trailing spaces):

```
drwxr-xr-x /home/user/k8s-operator/crds
-rw-r--r-- /home/user/k8s-operator/crds/cache-crd.yaml
-rw-r--r-- /home/user/k8s-operator/crds/index-crd.yaml
drwxr-x--- /home/user/k8s-operator/deploy
-rw-r----- /home/user/k8s-operator/deploy/operator-deploy.yaml
-rw-r----- /home/user/k8s-operator/deploy/operator-svc.yaml
drwxr-x--- /home/user/k8s-operator/rbac
-rw-r----- /home/user/k8s-operator/rbac/operator-role.yaml
-rw-r----- /home/user/k8s-operator/rbac/operator-rolebinding.yaml
```

Each line is the symbolic permission string (10 characters), a single space, and then the absolute path. Entries must be sorted alphabetically by path. The file should have exactly 9 lines with a newline at the end.

To generate the permission string for each entry, you can use `stat --format="%A %n"` on each path, then sort the results and write them to the file.
