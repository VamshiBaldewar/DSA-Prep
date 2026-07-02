/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int diameterOfBinaryTree(TreeNode root) {
        int[] sol = new int[1];
        height(root,sol);
        return sol[0];
         
       
    }
    private int height(TreeNode root,int[] sol){
        if(root == null){
            return 0;
        }
        int left = height(root.left,sol);
        int right = height(root.right,sol);
        sol[0] = Math.max(sol[0], left + right);
        
        return  1 + Math.max(left,right);

    }
   
       

    
}