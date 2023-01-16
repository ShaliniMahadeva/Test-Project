from datetime import datetime


def duration(time_tuple):
    """duration.
    
    calculate time taken in seconds

    Args:
        time_tuple (_type_): Tuple consisting of start & end time
    
    Returns: 
            float (_type_): Time taken in seconds
    """
    st = datetime.strptime(str(time_tuple[0]),"%H%M")
    ed = datetime.strptime(str(time_tuple[1]),"%H%M")
    du = ed - st
    if du.total_seconds() < 0:
        raise ValueError(" Invalid time entered ")
    return du.total_seconds()

def validate_efficiency(Jobs):
    """validate_efficiency

    Args:
        Jobs (_type_): Array of Jobs
    """
    
    inf_list = []
    for indx,job in enumerate(Jobs):
        du_in_sec = duration(job)
        profit = job[2]
        inf_list.append((indx, du_in_sec, profit))

    sorted_prof = sorted(inf_list, key=lambda x: x[2])
    sorted_time = sorted(inf_list, key=lambda x: x[1])
    pop_val = [tim for tim in sorted_time[::-1] if sorted_prof[-1][0] == tim[0]]
    Jobs.pop(pop_val[0][0])
    return Jobs


if __name__ == "__main__":
    Jobs = []
    Number_of_jobs = int(input("Enter the number of Jobs "))
    if Number_of_jobs > 100:
        raise ValueError(" Number of jobs exceeded ")
    print("Enter job start time, end time, and earnings ")
    for job in range(Number_of_jobs):
        start_time = input()
        end_time = input()
        profit = input()
        Jobs.append((start_time, end_time, profit))
    
    sorted_jobs = validate_efficiency(Jobs)
    prof_sum = [int(val[2]) for val in sorted_jobs]
    print(prof_sum)
    print("The number of tasks and earnings available for others ")
    print("Task: ",len(sorted_jobs))
    print("Earnings: ", sum(prof_sum))
    
    
 
        
        
    
    
