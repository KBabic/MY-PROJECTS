# moj nacin:

def spy_game(nums):
    
        for i in range(0,len(nums)-1):
            if nums[i] == 0:
                for n in range(i+1,len(nums)-1):
                    if nums[n] == 0:
                        for x in range(i+2,len(nums)-1):
                            if nums[x] == 7:
                                return True
        return False