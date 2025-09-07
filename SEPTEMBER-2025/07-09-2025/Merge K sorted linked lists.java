/*
class Node {
    int data;
    Node next;

    Node(int x) {
        data = x;
        next = null;
    }
}
*/

class Solution {
    Node mergeKLists(Node[] arr) {
        // code here
        
    int k = arr.length;

    PriorityQueue<Node> pq = new PriorityQueue<>((a, b) -> a.data - b.data);

    for (int i = 0; i < k; i++) {
        if (arr[i] != null) pq.add(arr[i]);
    }

    Node dummy = new Node(0);
    Node tail = dummy;

    while (!pq.isEmpty()) {
        Node min = pq.poll();
        tail.next = min;
        tail = tail.next;

        if (min.next != null) pq.add(min.next);
    }

    return dummy.next;

    }
}