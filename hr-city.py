# HackerRank City
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    MOD = 1000000007
    N = int(input_data[0])
    A = [int(x) for x in input_data[1:N+1]]
    
    # State for the tree at step 0:
    # A single node.
    # V: number of vertices
    # S: sum of all pairwise distances in the tree
    # D: sum of distances from the "corner" node to all nodes in the tree
    # L: maximum distance between the opposite "corners" (or diameter / path length between corners)
    # Let's inspect the corner definition:
    # At step 0, there is 1 node.
    # At each step, 4 copies of the previous graph are placed at the 4 corners of an 'H' structure.
    # The 'H' structure has 2 new nodes: wait, how is H formed?
    # Problem statement:
    # "create 3 duplicates of the current tree (total 4 copies), and create 2 new nodes to connect all 4 copies in the following H shape"
    # Looking at the image or the description:
    # 2 new nodes are created? Wait, the text says:
    # "create 2 new nodes to connect all 4 copies in the following H shape"
    # "as well as 5 new edges connecting everything together"
    # In an H shape:
    # Two central nodes u and v connected by an edge.
    # u is connected to two copies.
    # v is connected to two copies.
    # That gives:
    # Edge between u and v (length c)
    # Edge from u to copy 1 (length c)
    # Edge from u to copy 2 (length c)
    # Edge from v to copy 3 (length c)
    # Edge from v to copy 4 (length c)
    # Total new nodes: 2
    # Total new edges: 5
    # Total copies: 4
    # All 5 new edges have length A[i].
    # Which node of the copy is connected to the new nodes?
    # Notice the symmetry. Each copy was formed symmetrically.
    # In step 1: we start with 1 node.
    # 4 copies of 1 node (nodes 1, 2, 3, 4).
    # 2 new nodes (say 5 and 6).
    # Edges: (1, 5), (2, 5), (5, 6), (3, 6), (4, 6), all with weight A[0].
    # What are the "corners" of the new tree that connect to future new nodes?
    # By symmetry, the tree has 4 equivalent "corners" (outer-most connection points).
    # Specifically, each copy's "outer corner" becomes the new tree's corner!
    # Wait, in the tree of step k, does each copy connect at its own "corner"?
    # Look at the diagram:
    # If copy 1 is connected at its corner, then the remaining 3 corners of copy 1?
    # Wait! In step 0, 1 node is the corner.
    # In step 1, the new tree has 6 nodes:
    # 1, 2 connected to 5. 3, 4 connected to 6. 5-6 is an edge.
    # For step 2, we need 4 copies of this 6-node tree.
    # Which node of the 6-node tree connects to the new H?
    # Looking at Sample 1:
    # N = 2, A = [2, 1]
    # Sample 0 has N = 1, A = [1], output 29.
    # Let's check Sample 0:
    # Nodes: 1, 2, 3, 4, 5, 6.
    # Edges of weight 1: (1, 5), (2, 5), (5, 6), (6, 3), (6, 4).
    # Distances:
    # d(5, 6) = 1
    # d(1, 5) = 1, d(2, 5) = 1, d(3, 6) = 1, d(4, 6) = 1
    # Distances from 5:
    # to 6: 1; to 1: 1; to 2: 1; to 3: 2; to 4: 2. Sum = 7.
    # By symmetry, from 6: sum = 7.
    # From 1:
    # to 5: 1; to 2: 2; to 6: 2; to 3: 3; to 4: 3. Sum = 11.
    # From 2: sum = 11.
    # From 3: sum = 11.
    # From 4: sum = 11.
    # Total sum of all pairs: (4 * 11 + 2 * 7) / 2 = (44 + 14) / 2 = 58 / 2 = 29!
    # Matches sample 0 output!
    #
    # Now, for step 2:
    # Which node of the 6-node tree is connected to the new H?
    # Notice in the diagram for step 2 (Sample 1):
    # The 4 copies are connected to the new nodes via which node?
    # In the diagram, the node of each copy that attaches to the new H is...
    # Wait, the diagram nikcity2.png:
    # The four subtrees are identical.
    # In the 6-node tree, which node connects to the outside?
    # Node 1, 2, 3, or 4?
    # Looking at the tree, nodes 1, 2, 3, 4 were the 4 "corners" of the 6-node tree!
    # One of them connects to the new H.
    # By symmetry, nodes 1, 2, 3, 4 are completely symmetric!
    # If node 1 connects to the new center, then the "corners" of the new tree must be the other corners,
    # or the tree is self-similar and has 4 corners at each step!
    # In step 1, 4 corners were nodes 1, 2, 3, 4.
    # In step 2, each of the 4 copies has 4 corners. One corner connects to the new central node.
    # The remaining corners (or specifically, one from each copy) become the 4 corners of the new tree!
    # Wait, does each copy have a "designated" corner that connects to the center, while another corner becomes the outer corner?
    # Wait, are all 4 corners of the copy identical?
    # Let's check in step 1:
    # Nodes 1, 2 are connected to 5. Nodes 3, 4 are connected to 6.
    # Distance between 1 and 2 is 2.
    # Distance between 1 and 3 is 3.
    # Distance between 1 and 4 is 3.
    # So 1 is NOT symmetric to 2, 3, 4 in terms of distances between each other:
    # For node 1: one corner (2) is at distance 2, two corners (3, 4) are at distance 3.
    # So which corner connects to the new node?
    # Look at the diagram nikcity2.png:
    # In nikcity2.png, node 1 (a corner) is connected to the new node.
    # Wait, in the diagram, how is the copy oriented?
    # The copy connects at ONE of its corners.
    # Does it matter which corner connects?
    # By symmetry of the 6-node tree:
    # 1 and 2 are symmetric. 3 and 4 are symmetric.
    # And {1, 2} is symmetric to {3, 4} via reflection swapping 5 and 6.
    # So ALL 4 corners 1, 2, 3, 4 are AUTOMORPHICALLY EQUIVALENT!
    # That means it doesn't matter WHICH of the 4 corners connects to the new node!
    # But wait, what about the corners of the NEW tree?
    # In the new tree, which nodes will be the corners for the NEXT step?
    # In nikcity2.png, look at the outer-most nodes that would connect if we went to step 3.
    # Each copy has 4 corners. 1 corner connects to the new edge.
    # There are 3 corners left in each of the 4 copies.
    # Which of those becomes the "corner" of the new tree?
    # Wait! In nikcity2.png, look at the H shape of step 2:
    # It has 4 branches. At the end of each branch is a copy of step 1.
    # In step 1, the corner that is furthest away from the connection point?
    # Or does the fractal structure specify which corner?
    # Let's look at the picture nik2.png:
    # In nik2.png:
    # There are 4 copies: Top-Left, Bottom-Left, Top-Right, Bottom-Right.
    # In Top-Left copy, which node is connected?
    # It shows: the bottom-right of the Top-Left copy is connected to the top-left of the center!
    # And the top-left of the Top-Left copy is the new top-left corner!
    # Ah! Top-left corner of the whole tree is the top-left corner of the Top-Left copy!
    # And the connection point to the center is the bottom-right corner of the Top-Left copy!
    # In the Top-Left copy, what is the relation between its top-left corner and its bottom-right corner?
    # In step 1:
    # Top-Left: node 1
    # Bottom-Left: node 2
    # Top-Right: node 3
    # Bottom-Right: node 4
    # Node 5 is the left center, node 6 is the right center.
    # Node 1 is connected to 5, node 2 to 5, node 3 to 6, node 4 to 6.
    # So:
    # Top-Left is node 1.
    # Bottom-Left is node 2.
    # Top-Right is node 3.
    # Bottom-Right is node 4.
    # Now, Top-Left copy is attached at its Bottom-Right corner!
    # Bottom-Right of step 1 is node 4!
    # And the top-left of the new tree will be the top-left corner of Top-Left copy, which is node 1!
    # So the connection point is node 4 (the opposite corner!), and the new corner is node 1!
    # Wait, distance between node 1 (top-left) and node 4 (bottom-right) in step 1 is:
    # 1 -> 5 -> 6 -> 4 = 1 + 1 + 1 = 3 (or A[0] * 3).
    # That is the DIAMETER between opposite corners!
    # Wait, what about Top-Right copy?
    # It connects at its Bottom-Left corner (node 2), and its Top-Right corner (node 3) becomes the new corner!
    # The distance between Bottom-Left (node 2) and Top-Right (node 3) is also:
    # 2 -> 5 -> 6 -> 3 = 3 * A[0]!
    # What about Bottom-Left copy?
    # Connects at its Top-Right corner (node 3), its Bottom-Left corner (node 2) is the new corner!
    # Distance between 3 and 2 is 3 * A[0].
    # Bottom-Right copy connects at its Top-Left corner (node 1), new corner is node 4.
    # Distance between 1 and 4 is 3 * A[0].
    # IN EVERY COPY:
    # The connection point to the new center is the OPPOSITE corner of the new tree's corner!
    # That means the corner that attaches is the corner diagonally opposite to the new corner!
    # Is the corner diagonally opposite unique?
    # Yes! In step 1:
    # Opposite of 1 is 4.
    # Opposite of 2 is 3.
    # Opposite of 3 is 2.
    # Opposite of 4 is 1.
    # And the path from the corner to its opposite corner is the longest path between corners!
    # Let L be the distance between a corner and its opposite corner.
    # In step 0:
    # The graph is a single node.
    # Corner is this node.
    # Opposite corner is also this node.
    # L_0 = 0.
    # In step 1:
    # The path from the new top-left corner to the new bottom-right corner:
    # New top-left corner is the top-left corner of Top-Left copy.
    # From top-left corner of TL copy to its connection point (bottom-right corner of TL copy): distance L_0.
    # From connection point to center node u: length c.
    # From u to center node v: length c.
    # From v to connection point of BR copy (top-left corner of BR copy): length c.
    # From connection point of BR copy to BR corner of BR copy: distance L_0.
    # So L_1 = L_0 + c + c + c + L_0 = 2 * L_0 + 3 * c!
    # For step 1: L_1 = 2 * 0 + 3 * 1 = 3.
    # Check: distance from 1 to 4 is 3. Correct!
    # In general: L_{k} = 2 * L_{k-1} + 3 * c.
    
    # Now, what about the sum of distances from the connection point / corner?
    # Notice that by symmetry:
    # In any copy, the 4 corners are completely symmetric with respect to the whole copy!
    # Why? Because each copy itself was built symmetrically from 4 corners.
    # Every corner has the EXACT SAME sum of distances to all other nodes in the copy!
    # Let D be the sum of distances from any corner to all nodes in the tree.
    # For step 0:
    # V_0 = 1
    # D_0 = 0
    # S_0 = 0
    # L_0 = 0
    
    # Let's check step 1:
    # c = A[0]
    # In step 1, each copy has size V, sum of distances S, corner-sum D, corner-to-corner L.
    # Let's derive V', L', D', S' for step k with edge weight c:
    #
    # 1. Number of vertices:
    # V' = 4 * V + 2
    #
    # 2. Corner-to-corner distance L':
    # L' = 2 * L + 3 * c
    #
    # 3. Sum of distances from a CORNER of the new tree to all vertices in the new tree (D'):
    # Let the corner be C (e.g. top-left corner of the new tree, which is top-left corner of TL copy).
    # Vertices of the new tree consist of:
    # - TL copy:
    #   Sum of distances from C to nodes in TL copy is D.
    # - The two central nodes u and v:
    #   Distance from C to u:
    #   C is the corner, the connection point of TL copy is C_opp (opposite corner).
    #   Distance from C to C_opp is L.
    #   Then edge to u has length c.
    #   So distance from C to u is L + c.
    #   Distance from C to v is (L + c) + c = L + 2c.
    # - BL copy (attached to u):
    #   Distance from C to the attachment point of BL copy is (L + c) + c = L + 2c.
    #   Every node in BL copy has distance from its attachment point.
    #   The attachment point is a corner of BL copy!
    #   So the sum of distances from the attachment point to all nodes in BL copy is D!
    #   Therefore, sum of distances from C to all nodes in BL copy is:
    #   D + V * (distance from C to attachment point) = D + V * (L + 2c).
    # - TR copy (attached to v):
    #   Distance from C to attachment point of TR copy is:
    #   dist(C, u) + dist(u, v) + dist(v, TR_att) = (L + c) + c + c = L + 3c.
    #   Sum of distances to TR copy = D + V * (L + 3c).
    # - BR copy (attached to v):
    #   Distance from C to attachment point of BR copy is also L + 3c.
    #   Sum of distances to BR copy = D + V * (L + 3c).
    #
    # Putting it all together for D':
    # D' = (nodes in TL copy) + (node u) + (node v) + (nodes in BL) + (nodes in TR) + (nodes in BR)
    #    = D
    #      + (L + c) + (L + 2c)
    #      + [D + V * (L + 2c)]
    #      + [D + V * (L + 3c)]
    #      + [D + V * (L + 3c)]
    #    = 4 * D + (2*L + 3c) + V * (3*L + 8c)
    #
    # Let's verify D' for step 1 (V=1, D=0, L=0, c=1):
    # D' = 4 * 0 + (0 + 3) + 1 * (0 + 8) = 11.
    # In sample 0, the sum of distances from node 1 (a corner) was indeed 11! It matches!
    #
    # 4. Total sum of pairwise distances in the new tree (S'):
    # S' is the sum over all pairs {x, y} of dist(x, y).
    # Pairs can be categorized as:
    # A. Both x, y in the same copy (4 copies):
    #    4 * S
    #
    # B. One node is u or v, other node is in a copy:
    #    Let's find sum of distances from u to all nodes in all 4 copies, and from v to all copies.
    #    By symmetry between u and v:
    #    For u:
    #    - To TL copy: attachment point has sum D, distance from u to attachment point is c.
    #      Sum = D + V * c.
    #    - To BL copy: attachment point has sum D, distance from u to attachment point is c.
    #      Sum = D + V * c.
    #    - To TR copy: attachment point has sum D, distance from u to attachment point is c (u-v) + c (v-TR) = 2c.
    #      Sum = D + V * 2c.
    #    - To BR copy: Sum = D + V * 2c.
    #    Total for u to all 4 copies:
    #    4 * D + V * (c + c + 2c + 2c) = 4 * D + 6 * V * c.
    #    By symmetry, sum from v to all 4 copies is also 4 * D + 6 * V * c.
    #    So sum of distances between {u, v} and nodes in the 4 copies:
    #    2 * (4 * D + 6 * V * c) = 8 * D + 12 * V * c.
    #
    # C. Between u and v:
    #    dist(u, v) = c.
    #
    # D. Pairs between different copies:
    #    There are 6 pairs of copies:
    #    1) TL and BL:
    #       Attachment points are both connected to u.
    #       Distance between attachment point of TL and attachment point of BL is c + c = 2c.
    #       For any x in TL and y in BL:
    #       dist(x, y) = dist(x, att_TL) + 2c + dist(y, att_BL).
    #       Sum over all x in TL, y in BL:
    #       sum_x sum_y (dist(x, att_TL) + dist(y, att_BL) + 2c)
    #       = V * D + V * D + V * V * 2c
    #       = 2 * V * D + 2 * c * V^2.
    #
    #    2) TR and BR:
    #       Same as TL and BL! Distance between attachment points is 2c.
    #       Sum = 2 * V * D + 2 * c * V^2.
    #
    #    3) TL and TR:
    #       Path between attachment points: att_TL - u - v - att_TR, distance is 3c.
    #       Sum = 2 * V * D + 3 * c * V^2.
    #
    #    4) TL and BR:
    #       Path between attachment points: 3c.
    #       Sum = 2 * V * D + 3 * c * V^2.
    #
    #    5) BL and TR:
    #       Path between attachment points: 3c.
    #       Sum = 2 * V * D + 3 * c * V^2.
    #
    #    6) BL and BR:
    #       Path between attachment points: 3c.
    #       Sum = 2 * V * D + 3 * c * V^2.
    #
    #    Sum over all 6 pairs of copies:
    #    Total = 6 * (2 * V * D) + c * V^2 * (2 + 2 + 3 + 3 + 3 + 3)
    #          = 12 * V * D + 16 * c * V^2.
    #
    # Adding all parts together for S':
    # S' = 4 * S                              (within copies)
    #      + c                                (between u and v)
    #      + 8 * D + 12 * V * c               (between {u, v} and copies)
    #      + 12 * V * D + 16 * c * V^2        (between different copies)
    #
    # Let's test S' for step 1 (V=1, S=0, D=0, L=0, c=1):
    # S' = 0 + 1 + 0 + 12 + 0 + 16 = 29.
    # Matches Sample 0 output (29)!
    #
    # Let's test step 2 for Sample 1:
    # Input:
    # 2
    # 2 1
    # Step 1: c = 2.
    # V = 1, S = 0, D = 0, L = 0
    # After step 1:
    # V_1 = 4 * 1 + 2 = 6
    # L_1 = 2 * 0 + 3 * 2 = 6
    # D_1 = 4 * 0 + (0 + 6) + 1 * (0 + 16) = 22
    # S_1 = 4 * 0 + 2 + (8 * 0 + 12 * 1 * 2) + (12 * 1 * 0 + 16 * 2 * 1) = 2 + 24 + 32 = 58
    #
    # Now step 2: c = 1, using V=6, L=6, D=22, S=58:
    # V_2 = 4 * 6 + 2 = 26
    # L_2 = 2 * 6 + 3 * 1 = 15
    # D_2 = 4 * 22 + (2 * 6 + 3) + 6 * (3 * 6 + 8) = 88 + 15 + 6 * 26 = 88 + 15 + 156 = 259
    # S_2 = 4 * S + c + 8 * D + 12 * V * c + 12 * V * D + 16 * c * V^2
    #     = 4 * 58 + 1 + 8 * 22 + 12 * 6 * 1 + 12 * 6 * 22 + 16 * 1 * 36
    #     = 232 + 1 + 176 + 72 + 1584 + 576
    #     = 2641.
    # Matches Sample 1 output (2641)!

    V = 1
    S = 0
    D = 0
    L = 0
    
    for c in A:
        c %= MOD
        
        # New values
        new_S = (4 * S + c + 8 * D + 12 * V * c + 12 * V * D + 16 * c * (V * V)) % MOD
        new_D = (4 * D + (2 * L + 3 * c) + V * (3 * L + 8 * c)) % MOD
        new_L = (2 * L + 3 * c) % MOD
        new_V = (4 * V + 2) % MOD
        
        S, D, L, V = new_S, new_D, new_L, new_V

    print(S)

if __name__ == '__main__':
    solve()