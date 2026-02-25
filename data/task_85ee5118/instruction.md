You are a Kubernetes operator managing deployment manifests in the directory <code>/home/user/k8s-manifests/</code>. Your task is to reorganize the manifests and set up symbolic links to streamline deployment updates.

1. Inside <code>/home/user/k8s-manifests/</code>, you have three YAML manifest files: <code>frontend-deployment.yaml</code>, <code>backend-deployment.yaml</code>, and <code>database-deployment.yaml</code>. There is also a subdirectory called <code>current/</code>, which is initially empty.
2. Move all three manifest files into a new subdirectory named <code>releases/v1/</code> (full path: <code>/home/user/k8s-manifests/releases/v1/</code>). Create the directory structure as needed.
3. Then, in <code>/home/user/k8s-manifests/current/</code>, create symbolic links named exactly <code>frontend.yaml</code>, <code>backend.yaml</code>, and <code>database.yaml</code> that point to the corresponding files in <code>/home/user/k8s-manifests/releases/v1/</code>.
4. Verify the symbolic links are correctly created by producing a log file at <code>/home/user/k8s-manifests/link-status.log</code>. The log file must contain one line for each link in <code>/home/user/k8s-manifests/current/</code> in the following format:
<pre>
[link name]: [absolute target path] -> [target exists: yes/no]
</pre>
For example:
<pre>
frontend.yaml: /home/user/k8s-manifests/releases/v1/frontend-deployment.yaml -> yes
</pre>
Make sure the symbolic links and the log file are accurate and reflect the current file structure.
