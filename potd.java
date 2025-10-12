/*
class Node {
    int data;
    Node left;
    Node right;
    Node(int data) {
        this.data = data;
        left = null;
        right = null;
    }
}
*/

class Solution {
    private int raj = 0;
    public int distCandy(Node root) {
        dfs(root);
        return raj;
    }
    private int dfs(Node node) {
        if (node == null){
            return 0;
        } 
        int left = dfs(node.left);
        int right = dfs(node.right);
        raj += Math.abs(left) + Math.abs(right);
        return node.data + left + right - 1;
    }
}