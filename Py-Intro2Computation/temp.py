# 读取机房的行列数M和N
M, N = map(int, input().split())

# 读取座位矩阵：seat_matrix[i][j]表示第i行第j列的学生编号
seat_matrix = []
for _ in range(M):
    row = list(map(int, input().split()))
    seat_matrix.append(row)

# 读取每个学生的做题情况：solutions[id]存储编号id的做题情况（元组形式，方便比较）
total_students = M * N
solutions = {}
for student_id in range(total_students):
    # 处理空行情况（题目提示可能存在空提交）
    line = input().strip()
    # 将一行的0/1转为整数元组（空行则为空空元组）
    sol = tuple(map(int, line.split())) if line else ()
    solutions[student_id] = sol

# 第一步：统计“做题情况与周围（上下左右）任一同学相同”的学生人数
same_set = set()  # 用集合存符合条件的学生编号，避免重复
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 上下左右四个方向

for i in range(M):
    for j in range(N):
        current_id = seat_matrix[i][j]
        current_sol = solutions[current_id]
        # 检查四个方向的邻居
        for di, dj in directions:
            ni = i + di  # 邻居的行
            nj = j + dj  # 邻居的列
            # 判断邻居是否在合法范围内
            if 0 <= ni < M and 0 <= nj < N:
                neighbor_id = seat_matrix[ni][nj]
                neighbor_sol = solutions[neighbor_id]
                # 做题情况完全相同则计入集合
                if current_sol == neighbor_sol:
                    same_set.add(current_id)
                    break  # 找到一个邻居即可，无需继续检查

same_count = len(same_set)

# 第二步：统计优秀人数
# 1. 按做题情况分组，统计每组人数
group_dict = {}
for student_id in range(total_students):
    sol = solutions[student_id]
    if sol not in group_dict:
        group_dict[sol] = 0
    group_dict[sol] += 1

# 2. 计算每组的得分（做对题数），并找到最高得分
max_score = -1
group_scores = {}
for sol in group_dict:
    score = sum(sol)  # 做题情况中1的数量（做对题数）
    group_scores[sol] = score
    if score > max_score:
        max_score = score

# 3. 统计得分最高的所有组的总人数
sum_top_groups = 0
for sol in group_dict:
    if group_scores[sol] == max_score:
        sum_top_groups += group_dict[sol]

# 4. 计算优秀人数（不超过总人数的40%）
upper_limit = total_students * 0.4
excellent_count = sum_top_groups if sum_top_groups <= upper_limit else 0

# 输出结果
print(same_count, excellent_count)