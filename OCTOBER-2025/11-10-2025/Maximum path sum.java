/*
class Node{
    int data;
    Node left, right;
    Node(int d){
        data=d;
        left=right=null;
    }
}
*/

class Solution {
    int raj;
    int findMaxSum(Node root) {
        raj = Integer.MIN_VALUE;
        maxPath(root);
        return raj;
    }
    int maxPath(Node node) {
        if (node == null){
            return 0;
        } 
        int left = Math.max(0, maxPath(node.left));
        int right = Math.max(0, maxPath(node.right));
        raj = Math.max(raj, left + right + node.data);
        return node.data + Math.max(left, right);
    }
}