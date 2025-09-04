/*
class Node {
  public:
    int data;
    Node* next;

    Node(int x){
        data = x;
        next = NULL;
    }
};
*/
class Solution {
  public:
  
    Node *reverseKGroup(Node *head, int k) {
        if (!head || k==1) return head;
        Node* temp = head, *prv = NULL, *nxt = NULL;
        for(int i=0;i<k && temp;i++) {
            nxt = temp->next;
            temp->next = prv;
            prv = temp;
            temp = nxt;
        }
        head->next = reverseKGroup(temp, k);
        return prv;
    }
};