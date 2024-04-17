def greedy_assignment(jobs, workers):
    # 각 사람이 각 일을 할 때 드는 비용을 계산
    costs = [[0] * len(jobs) for _ in range(len(workers))]
    for i, worker in enumerate(workers):
        for j, job in enumerate(jobs):
            costs[i][j] = worker[j]  # i번째 사람이 j번째 일을 할 때 드는 비용
    
    # 일할 수 있는 사람들을 인덱스로 저장
    available_workers = list(range(len(workers)))
    total_cost = 0
    
    # 모든 일에 대해 반복
    for job_index in range(len(jobs)):
        min_cost = float('inf')
        selected_worker = None
        
        # 각 사람들 중에서 가장 저렴하게 일을 하는 사람을 선택
        for worker_index in available_workers:
            cost = costs[worker_index][job_index]
            if cost < min_cost:
                min_cost = cost
                selected_worker = worker_index
        
        # 선택된 사람이 일을 수행하고 해당 일을 할 수 없게 함
        total_cost += min_cost
        available_workers.remove(selected_worker)
    
    return total_cost

# 테스트를 위한 간단한 입력
jobs = [
    [3, 2, 7],
    [4, 5, 6],
    [1, 2, 1]
]
workers = [
    [2, 5, 1],
    [3, 4, 2],
    [7, 3, 2]
]

print("최소 비용:", greedy_assignment(jobs, workers))