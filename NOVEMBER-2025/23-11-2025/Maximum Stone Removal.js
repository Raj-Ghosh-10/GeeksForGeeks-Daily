class Solution {
    maxRemove(stones) {
        const parent = new Map();

        const find = (x) => {
            if (!parent.has(x)) parent.set(x, x);
            if (parent.get(x) !== x) parent.set(x, find(parent.get(x)));
            return parent.get(x);
        };

        const union = (x, y) => {
            const px = find(x);
            const py = find(y);
            if (px !== py) parent.set(px, py);
        };

        for (const [x, y] of stones) {
            // prefix 'r' for row, 'c' for column to avoid collisions
            union(`r${x}`, `c${y}`);
        }

        const components = new Set();
        for (const [x, y] of stones) {
            components.add(find(`r${x}`));
        }

        return stones.length - components.size;
    }
}