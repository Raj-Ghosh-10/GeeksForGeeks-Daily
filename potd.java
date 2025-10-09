/*
class Node {
    int data;
    Node left, right;
    Node(int val){
        data = val;
        left = right = null;
    }
}
*/

class Solution {
    public ArrayList<Integer> postOrder(Node root) {
        ArrayList<Integer> raj = new ArrayList<>();
        traverse(raj,root);
        return raj;
    }
    public static void traverse(ArrayList<Integer> raj,Node root){
        if(root == null) return;
        
        traverse(raj,root.left);
        traverse(raj,root.right);
        raj.add(root.data);
    }
}