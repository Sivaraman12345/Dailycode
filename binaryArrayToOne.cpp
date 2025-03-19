class Solution {
    public:
        int minOperations(vector<int>& nums) {
            int n=nums.size();
            int ctr=0;
            for (int i=0;i<=n-3;i++){
                if (nums[i]==0){
                    nums[i]^=1;
                    nums[i+1]^=1;
                    nums[i+2]^=1;
                    ctr++;
                }
            }
            return (nums[n-1]==1&&nums[n-2]==1)?ctr:-1;
        }
    };
int list[5] = {1,0,0,1,0};
int main(){
    Solution obj;
    cout<<obj.minOperations(list);
    return 0;
}