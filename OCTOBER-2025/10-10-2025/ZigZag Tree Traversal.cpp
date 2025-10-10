/*
class Node {
    int data;
    Node *left;
    Node *right;

    Node(int val) {
        data = val;
        left = right = NULL;
    }
};
*/
class Solution {
  public:
    vector<int> zigZagTraversal(Node* root) {
        // code here
        vector<int>ans;
        queue<Node*>q;
        q.push(root);
        
        int lftToRgt=1;
        
        while(!q.empty()){
            int sz=q.size();
            vector<int>tmp;
            for(int t=0; t<sz; t++){
                Node* node=q.front();
                q.pop();
                tmp.push_back(node->data);
                if(node->left){
                    q.push(node->left);
                }
                if(node->right){
                    q.push(node->right);
                }
            }
            if(lftToRgt==0){
                reverse(tmp.begin(), tmp.end());
                ans.insert(ans.end(), tmp.begin(), tmp.end());
            }else{
                ans.insert(ans.end(), tmp.begin(), tmp.end());
            }
            lftToRgt=1-lftToRgt;
        }
        
        return ans;
    }
};