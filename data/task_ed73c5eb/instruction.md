You are a Kubernetes operator managing manifest files. In the directory <code>/home/user/k8s-manifests/</code>, there are three YAML files: <code>deployment.yaml</code>, <code>service.yaml</code>, and <code>configmap.yaml</code>. Each file may contain multiple resource definitions, but for this task, focus only on lines that begin with <code>kind:</code>. 

Your job:

1. Search all three YAML files for lines starting with <code>kind:</code> (ignoring case sensitivity). For example, lines can be like <code>kind: Deployment</code>, <code>kind: Service</code>, etc.
2. Normalize the output so the extracted kind values are all uppercased (e.g., <code>Deployment</code> becomes <code>DEPLOYMENT</code>).
3. Count the frequency of each unique resource kind found across all three files.
4. Produce a summary frequency report and save it to <code>/home/user/k8s-manifests/kind_frequency.log</code>.

The output log file must have the following format, sorted alphabetically by the resource kind (one kind per line):

<code>
&lt;KIND&gt; &lt;COUNT&gt;
</code>

For example (but not limited to):

<code>
CONFIGMAP 1
DEPLOYMENT 2
SERVICE 3
</code>

Make sure:
- Each kind name is in full uppercase letters.
- The count reflects the total number of times that kind occurs in all three files combined.
- The summary file must not include any extra lines or spaces; each line contains only the kind name and the count, separated by a single space.
- If there are no kinds found, the log file should be empty.

When finished, print the full contents of <code>/home/user/k8s-manifests/kind_frequency.log</code> to the console as the final step for verification. Use only standard Linux text processing tools in your solution.
