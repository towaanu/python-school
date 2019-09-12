# A: n*m, B: m*p
#: Complexity : O(nmp)
def mult_matrices(m_a, m_b):

    m_res = []

    width_b = len(m_b[0])

    for row_idx_a in range(len(m_a)):
        len_row_a = len(m_a[row_idx_a])
        m_res.append([])

        for col_idx_b in range(width_b):
            current_sum = 0            
            for col_idx_a in range(len_row_a):
                    val_a = m_a[row_idx_a][col_idx_a]
                    val_b = m_b[col_idx_a][col_idx_b]
                    current_sum += val_a * val_b

            m_res[row_idx_a].append(current_sum)
    
    return m_res
            
        
def display_matrix(m):
    matrix_str = ""
    for row in m:
        matrix_str += "\n"
        for col in row:
            matrix_str += f" {col}"

    return matrix_str[1:]

if __name__ == '__main__':
    print("Hello matrix :D")

    mat_a = [
        [1, 2],
        [3, 4]
    ]

    mat_b = [
        [1, 2, 5, 7],
        [3, 1, 6, 8]
    ]
    
    res = mult_matrices(mat_a, mat_b)
    print(f"RES : \n {display_matrix(res)}")