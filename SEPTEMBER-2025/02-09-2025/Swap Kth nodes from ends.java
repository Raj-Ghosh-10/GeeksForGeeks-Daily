class Solution {
    public int length (Node head) {
        int n = 0;
        while (head != null) {
            n++;
            head = head.next;
        }
        return n;
    }
    public Node swapKth(Node head, int k) {
        // code here
        if (head == null || head.next == null)
            return head;
        
        int len = length(head);
        if (k > len)
            return head;
        
        Node p = head, q = head;
        int idx = 1;
        while (idx++ < k)
            p = p.next;
        
        idx = 1;
        while (idx++ < len - k + 1)
            q = q.next;
        
        int t = p.data;
        p.data = q.data;
        q.data = t;
        
        return head;
    }
}